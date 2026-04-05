# ============================================================
# PROJECT 4: Random Forest — Ensemble Improvement
# Same problem as P3. RF 100 trees. Compare: DT → RF accuracy.
# ============================================================

# ── BLOCK 1: IMPORTS ────────────────────────────────────────
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (classification_report, confusion_matrix,
                              accuracy_score, f1_score)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")


# ── BLOCK 2: FETCH DATA ─────────────────────────────────────
raw = yf.download("RELIANCE.NS", period="5y", auto_adjust=True, progress=False)
df  = pd.DataFrame({
    "Close":  raw["Close"].squeeze(),
    "Volume": raw["Volume"].squeeze()
}).dropna()
print(f"Rows: {len(df)} | {df.index[0].date()} to {df.index[-1].date()}")


# ── BLOCK 3: FEATURE ENGINEERING ────────────────────────────
# RSI 14 (Wilder's smoothing)
delta    = df["Close"].diff()
gain     = delta.where(delta > 0, 0.0)
loss     = -delta.where(delta < 0, 0.0)
avg_gain = gain.ewm(com=13, adjust=False).mean()
avg_loss = loss.ewm(com=13, adjust=False).mean()
rs       = avg_gain / avg_loss
df["RSI_14"] = 100 - (100 / (1 + rs))

# MACD histogram
ema_12        = df["Close"].ewm(span=12, adjust=False).mean()
ema_26        = df["Close"].ewm(span=26, adjust=False).mean()
macd_line     = ema_12 - ema_26
signal_line   = macd_line.ewm(span=9, adjust=False).mean()
df["MACD_signal"] = macd_line - signal_line

# MA crossover
df["MA_50"]     = df["Close"].rolling(50).mean()
df["MA_200"]    = df["Close"].rolling(200).mean()
df["MA_cross"]  = (df["MA_50"] > df["MA_200"]).astype(int)
df["MA_spread"] = (df["MA_50"] - df["MA_200"]) / df["MA_200"] * 100

# Forward return for labelling
df["Fwd_return_5d"] = df["Close"].pct_change(5).shift(-5)
df.dropna(inplace=True)
print(f"After engineering: {len(df)} rows")


# ── BLOCK 4: CREATE 3-CLASS LABELS ──────────────────────────
BUY_THRESH  =  0.005
SELL_THRESH = -0.005

def label(r):
    if r > BUY_THRESH:  return "BUY"
    elif r < SELL_THRESH: return "SELL"
    else: return "HOLD"

df["Signal"] = df["Fwd_return_5d"].apply(label)
print("Label distribution:")
print(df["Signal"].value_counts())

le = LabelEncoder()
df["Signal_enc"] = le.fit_transform(df["Signal"])
class_names = list(le.classes_)


# ── BLOCK 5: TRAIN/TEST SPLIT (CHRONOLOGICAL) ───────────────
features = ["RSI_14", "MACD_signal", "MA_cross", "MA_spread"]
X        = df[features].values
y        = df["Signal_enc"].values

split     = int(len(df) * 0.8)
X_train   = X[:split];  X_test  = X[split:]
y_train   = y[:split];  y_test  = y[split:]
dates_test = df.index[split:]

print(f"Train: {X_train.shape} | Test: {X_test.shape}")


# ── BLOCK 6: DECISION TREE (BASELINE — same as P3) ──────────
dt = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=20,
    class_weight="balanced",
    random_state=42
)
dt.fit(X_train, y_train)
dt_pred  = dt.predict(X_test)
dt_acc   = accuracy_score(y_test, dt_pred)
dt_f1    = f1_score(y_test, dt_pred, average="macro")
dt_imp   = dt.feature_importances_

print(f"\n--- Decision Tree (P3 Baseline) ---")
print(f"Accuracy: {dt_acc:.4f} | F1-macro: {dt_f1:.4f}")
print(classification_report(y_test, dt_pred, target_names=class_names))


# ── BLOCK 7: RANDOM FOREST (100 TREES) ──────────────────────
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_leaf=20,
    class_weight="balanced",
    oob_score=True,          # enable out-of-bag error tracking
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
rf_pred  = rf.predict(X_test)
rf_acc   = accuracy_score(y_test, rf_pred)
rf_f1    = f1_score(y_test, rf_pred, average="macro")
rf_imp   = rf.feature_importances_
rf_oob   = rf.oob_score_

print(f"\n--- Random Forest (100 trees) ---")
print(f"Accuracy: {rf_acc:.4f} | F1-macro: {rf_f1:.4f} | OOB Score: {rf_oob:.4f}")
print(classification_report(y_test, rf_pred, target_names=class_names))


# ── BLOCK 8: OOB ERROR vs N_ESTIMATORS ──────────────────────
# Shows how adding more trees reduces error — the ensemble effect
oob_errors = []
n_tree_range = list(range(10, 201, 10))

for n in n_tree_range:
    rf_temp = RandomForestClassifier(
        n_estimators=n,
        max_depth=5,
        min_samples_leaf=20,
        class_weight="balanced",
        oob_score=True,
        random_state=42,
        n_jobs=-1
    )
    rf_temp.fit(X_train, y_train)
    oob_errors.append(1 - rf_temp.oob_score_)

print(f"\nOOB Error range: {max(oob_errors):.4f} (10 trees) → {min(oob_errors):.4f} ({n_tree_range[oob_errors.index(min(oob_errors))]} trees)")


# ── BLOCK 9: COMPARISON TABLE ────────────────────────────────
print("\n" + "=" * 60)
print(f"{'Metric':<25} {'Decision Tree':>15} {'Random Forest':>15}")
print("-" * 60)
print(f"{'Accuracy':<25} {dt_acc:>15.4f} {rf_acc:>15.4f}")
print(f"{'F1-macro':<25} {dt_f1:>15.4f} {rf_f1:>15.4f}")
print(f"{'OOB Score':<25} {'N/A':>15} {rf_oob:>15.4f}")
for i, feat in enumerate(features):
    print(f"{'Imp: ' + feat:<25} {dt_imp[i]:>15.4f} {rf_imp[i]:>15.4f}")
print("=" * 60)
improvement = (rf_acc - dt_acc) / dt_acc * 100
print(f"\nRF improvement over DT: {improvement:+.1f}% accuracy")


# ── BLOCK 10: CHART 1 — RF CONFUSION MATRIX ─────────────────
cm_rf = confusion_matrix(y_test, rf_pred)
fig1 = go.Figure(data=go.Heatmap(
    z=cm_rf,
    x=["Pred: " + c for c in class_names],
    y=["Actual: " + c for c in class_names],
    colorscale="Blues",
    text=cm_rf,
    texttemplate="%{text}",
    textfont=dict(size=16),
    showscale=True
))
fig1.update_layout(
    title="Confusion Matrix — Random Forest Trading Signals (BUY/HOLD/SELL)",
    xaxis_title="Predicted Signal",
    yaxis_title="Actual Signal"
)
fig1.write_image("rf_confusion_matrix.png")
print("Saved: rf_confusion_matrix.png")


# ── BLOCK 11: CHART 2 — FEATURE IMPORTANCE (DT vs RF) ───────
imp_df = pd.DataFrame({
    "Feature": features,
    "Decision Tree": dt_imp,
    "Random Forest": rf_imp
})
imp_df = imp_df.sort_values("Random Forest", ascending=True)

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    y=imp_df["Feature"], x=imp_df["Decision Tree"],
    name="Decision Tree", orientation="h",
    marker_color="#ff7f0e"
))
fig2.add_trace(go.Bar(
    y=imp_df["Feature"], x=imp_df["Random Forest"],
    name="Random Forest", orientation="h",
    marker_color="#1f77b4"
))
fig2.update_layout(
    title="Feature Importance — Decision Tree vs Random Forest",
    xaxis_title="Importance (Gini)",
    yaxis_title="Feature",
    barmode="group",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)
fig2.write_image("rf_feature_importance_comparison.png")
print("Saved: rf_feature_importance_comparison.png")


# ── BLOCK 12: CHART 3 — OOB ERROR vs N_ESTIMATORS ───────────
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=n_tree_range,
    y=oob_errors,
    mode="lines+markers",
    name="OOB Error",
    line=dict(color="#d62728", width=2),
    marker=dict(size=6)
))
fig3.add_hline(
    y=min(oob_errors), line_dash="dash", line_color="gray",
    annotation_text=f"Min OOB Error = {min(oob_errors):.4f}"
)
fig3.update_layout(
    title="Out-of-Bag Error vs Number of Trees — Random Forest",
    xaxis_title="Number of Trees (n_estimators)",
    yaxis_title="OOB Error Rate",
    yaxis=dict(range=[0, max(oob_errors) * 1.2])
)
fig3.write_image("rf_oob_error_curve.png")
print("Saved: rf_oob_error_curve.png")


# ── BLOCK 13: CHART 4 — DT vs RF ACCURACY BAR CHART ─────────
fig4 = go.Figure()
fig4.add_trace(go.Bar(
    x=["Decision Tree", "Random Forest"],
    y=[dt_acc * 100, rf_acc * 100],
    text=[f"{dt_acc*100:.1f}%", f"{rf_acc*100:.1f}%"],
    textposition="outside",
    marker_color=["#ff7f0e", "#1f77b4"],
    width=0.5
))
fig4.update_layout(
    title="Accuracy Comparison — Decision Tree vs Random Forest",
    yaxis_title="Accuracy (%)",
    yaxis=dict(range=[0, 100]),
    showlegend=False
)
fig4.write_image("rf_dt_vs_rf_accuracy.png")
print("Saved: rf_dt_vs_rf_accuracy.png")


# ── BLOCK 14: SUMMARY ───────────────────────────────────────
print("\n=== PROJECT 4 COMPLETE ===")
print(f"Decision Tree Accuracy:  {dt_acc*100:.1f}%")
print(f"Random Forest Accuracy:  {rf_acc*100:.1f}%")
print(f"Improvement:             {improvement:+.1f}%")
print(f"OOB Score (RF):          {rf_oob:.4f}")
print(f"Top feature (RF):        {features[rf_imp.argmax()]}")
print(f"Top feature (DT):        {features[dt_imp.argmax()]}")
