
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, classification_report,
    roc_auc_score, roc_curve, precision_recall_curve, average_precision_score)
from sklearn.utils import resample
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

# BLOCK 2: LOAD DATA
df = pd.read_csv("cs-training.csv", index_col=0)
print("Raw shape:", df.shape)
print("Columns:", list(df.columns))
print("Default rate:", round(df["SeriousDlqin2yrs"].mean(), 4))

# BLOCK 3: RENAME — using exact Kaggle column names
df = df.rename(columns={
    "SeriousDlqin2yrs":                      "Target",
    "RevolvingUtilizationOfUnsecuredLines":   "Revolving_util",
    "age":                                    "Age",
    "NumberOfTime30-59DaysPastDueNotWorse":   "Late_30_59",
    "DebtRatio":                              "DTI",
    "MonthlyIncome":                          "Monthly_income",
    "NumberOfOpenCreditLinesAndLoans":        "Open_credit_lines",
    "NumberOfTimes90DaysLate":                "Late_90",
    "NumberRealEstateLoansOrLines":           "RE_loans",
    "NumberOfTime60-89DaysPastDueNotWorse":   "Late_60_89",
    "NumberOfDependents":                     "Dependents"
})
print("Renamed columns:", list(df.columns))

# BLOCK 4: CLEAN
features = ["DTI", "Age", "Late_30_59", "Late_60_89", "Late_90",
            "Revolving_util", "Monthly_income", "Open_credit_lines"]
df = df[features + ["Target"]].copy()
for col in ["Revolving_util", "DTI", "Monthly_income"]:
    df[col] = df[col].clip(upper=df[col].quantile(0.99))
df.dropna(inplace=True)
print("After cleaning:", df.shape)

# BLOCK 5: BALANCE CLASSES
df_maj    = df[df["Target"] == 0]
df_min    = df[df["Target"] == 1]
df_min_up = resample(df_min, replace=True,
                     n_samples=len(df_maj) // 3, random_state=42)
df_bal    = pd.concat([df_maj, df_min_up]).sample(frac=1, random_state=42).reset_index(drop=True)
print("Balanced shape:", df_bal.shape, "| Default rate:", round(df_bal["Target"].mean(), 4))

# BLOCK 6: SPLIT + SCALE
X         = df_bal[features].values
y         = df_bal["Target"].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
scaler    = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)
print("Train:", X_train.shape, "| Test:", X_test.shape)

# BLOCK 7: LOGISTIC REGRESSION
lr = LogisticRegression(C=1.0, max_iter=1000, class_weight="balanced", random_state=42)
lr.fit(X_train_s, y_train)
y_pred   = lr.predict(X_test_s)
y_prob   = lr.predict_proba(X_test_s)[:, 1]
auc      = roc_auc_score(y_test, y_prob)
avg_prec = average_precision_score(y_test, y_prob)
cm       = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print("\nAUC-ROC:", round(auc, 4))
print("Avg Precision:", round(avg_prec, 4))
print(classification_report(y_test, y_pred, target_names=["No Default", "Default"]))

# BLOCK 8: CONFUSION MATRIX PLOT
fig1 = go.Figure(data=go.Heatmap(
    z=cm,
    x=["Pred: No Default", "Pred: Default"],
    y=["Actual: No Default", "Actual: Default"],
    colorscale="Blues", text=cm,
    texttemplate="%{text}", textfont=dict(size=18), showscale=True
))
fig1.update_layout(
    title="Confusion Matrix — Logistic Regression Loan Default",
    xaxis_title="Predicted Label",
    yaxis_title="Actual Label"
)
fig1.write_image("confusion_matrix.png")
fig1.show()
print("Saved: confusion_matrix.png")

# BLOCK 9: ROC CURVE
fpr, tpr, _ = roc_curve(y_test, y_prob)
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines",
    name="LR AUC=" + str(round(auc, 4)),
    line=dict(color="#1f77b4", width=2),
    fill="tozeroy", fillcolor="rgba(31,119,180,0.1)"))
fig2.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines",
    name="Random AUC=0.50",
    line=dict(color="red", width=1.5, dash="dash")))
fig2.update_layout(
    title="ROC Curve — Loan Default (AUC=" + str(round(auc, 4)) + ")",
    xaxis_title="False Positive Rate",
    yaxis_title="True Positive Rate",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)
fig2.write_image("roc_curve.png")
fig2.show()
print("Saved: roc_curve.png")

# BLOCK 10: PRECISION-RECALL CURVE
precision_vals, recall_vals, _ = precision_recall_curve(y_test, y_prob)
baseline = float(y_test.sum()) / len(y_test)
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=recall_vals, y=precision_vals, mode="lines",
    name="LR AvgPrec=" + str(round(avg_prec, 4)),
    line=dict(color="#2ca02c", width=2),
    fill="tozeroy", fillcolor="rgba(44,160,44,0.1)"))
fig3.add_trace(go.Scatter(x=[0, 1], y=[baseline, baseline], mode="lines",
    name="Baseline=" + str(round(baseline, 4)),
    line=dict(color="red", width=1.5, dash="dash")))
fig3.update_layout(
    title="Precision-Recall Curve — Loan Default",
    xaxis_title="Recall",
    yaxis_title="Precision",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)
fig3.write_image("precision_recall_curve.png")
fig3.show()
print("Saved: precision_recall_curve.png")

# BLOCK 11: FEATURE COEFFICIENTS
coef_df = pd.DataFrame({"Feature": features, "Coefficient": lr.coef_[0]})
coef_df = coef_df.sort_values("Coefficient", ascending=True)
colors  = ["#d62728" if c > 0 else "#1f77b4" for c in coef_df["Coefficient"]]
fig4 = go.Figure(go.Bar(
    x=coef_df["Coefficient"], y=coef_df["Feature"],
    orientation="h", marker_color=colors
))
fig4.update_layout(
    title="Feature Coefficients — LR (red = raises default risk)",
    xaxis_title="Coefficient",
    yaxis_title="Feature"
)
fig4.write_image("feature_coefficients.png")
fig4.show()
print("Saved: feature_coefficients.png")

print("\n=== PROJECT 2 COMPLETE ===")
print("AUC-ROC:      ", round(auc, 4))
print("Avg Precision:", round(avg_prec, 4))
print("TP (defaults caught):", tp)
print("FP (false alarms):   ", fp)
print("FN (missed defaults):", fn)
print("TN (correct clears): ", tn)
