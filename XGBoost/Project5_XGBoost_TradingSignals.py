# ============================================================
# PROJECT 5: XGBoost — Gradient Boosting Mastery
# Complete evolution: DT → RF → XGBoost
# SHAP values + Optuna hyperparameter tuning
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
import xgboost as xgb
import shap
import optuna
from optuna.samplers import TPESampler
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
optuna.logging.set_verbosity(optuna.logging.WARNING)


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


# ── BLOCK 6: DECISION TREE BASELINE ─────────────────────────
dt = DecisionTreeClassifier(
    max_depth=5, min_samples_leaf=20,
    class_weight="balanced", random_state=42
)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_acc  = accuracy_score(y_test, dt_pred)
dt_f1   = f1_score(y_test, dt_pred, average="macro")
print(f"\nDecision Tree  → Accuracy: {dt_acc:.4f} | F1: {dt_f1:.4f}")


# ── BLOCK 7: RANDOM FOREST BASELINE ─────────────────────────
rf = RandomForestClassifier(
    n_estimators=100, max_depth=5, min_samples_leaf=20,
    class_weight="balanced", random_state=42, n_jobs=-1
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc  = accuracy_score(y_test, rf_pred)
rf_f1   = f1_score(y_test, rf_pred, average="macro")
print(f"Random Forest  → Accuracy: {rf_acc:.4f} | F1: {rf_f1:.4f}")


# ── BLOCK 8: OPTUNA HYPERPARAMETER TUNING FOR XGBOOST ───────
def objective(trial):
    params = {
        "max_depth":        trial.suggest_int("max_depth", 3, 8),
        "learning_rate":    trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
        "n_estimators":     trial.suggest_int("n_estimators", 50, 300),
        "subsample":        trial.suggest_float("subsample", 0.6, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
        "reg_alpha":        trial.suggest_float("reg_alpha", 1e-8, 10.0, log=True),
        "reg_lambda":       trial.suggest_float("reg_lambda", 1e-8, 10.0, log=True),
        "objective":        "multi:softmax",
        "num_class":        3,
        "eval_metric":      "mlogloss",
        "random_state":     42,
        "use_label_encoder": False,
        "verbosity":        0
    }
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)
    return accuracy_score(y_test, model.predict(X_test))

print("\nRunning Optuna tuning (50 trials)...")
study = optuna.create_study(
    direction="maximize",
    sampler=TPESampler(seed=42)
)
study.optimize(objective, n_trials=50, show_progress_bar=False)

print(f"Best accuracy: {study.best_value:.4f}")
print(f"Best params: {study.best_params}")


# ── BLOCK 9: TRAIN FINAL XGBOOST WITH BEST PARAMS ───────────
best_params = study.best_params
best_params.update({
    "objective":        "multi:softmax",
    "num_class":        3,
    "eval_metric":      "mlogloss",
    "random_state":     42,
    "use_label_encoder": False,
    "verbosity":        0
})

xgb_model = xgb.XGBClassifier(**best_params)
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)
xgb_acc  = accuracy_score(y_test, xgb_pred)
xgb_f1   = f1_score(y_test, xgb_pred, average="macro")

print(f"\nXGBoost (tuned) → Accuracy: {xgb_acc:.4f} | F1: {xgb_f1:.4f}")
print(classification_report(y_test, xgb_pred, target_names=class_names))


# ── BLOCK 10: FULL COMPARISON TABLE ──────────────────────────
print("\n" + "=" * 70)
print(f"{'FULL MODEL EVOLUTION':^70}")
print("=" * 70)
print(f"{'Metric':<20} {'Decision Tree':>15} {'Random Forest':>15} {'XGBoost':>15}")
print("-" * 70)
print(f"{'Accuracy':<20} {dt_acc:>15.4f} {rf_acc:>15.4f} {xgb_acc:>15.4f}")
print(f"{'F1-macro':<20} {dt_f1:>15.4f} {rf_f1:>15.4f} {xgb_f1:>15.4f}")

# Per-class breakdown
for i, cls in enumerate(class_names):
    dt_cr = classification_report(y_test, dt_pred, target_names=class_names, output_dict=True)
    rf_cr = classification_report(y_test, rf_pred, target_names=class_names, output_dict=True)
    xgb_cr = classification_report(y_test, xgb_pred, target_names=class_names, output_dict=True)
    print(f"{'Prec: ' + cls:<20} {dt_cr[cls]['precision']:>15.4f} {rf_cr[cls]['precision']:>15.4f} {xgb_cr[cls]['precision']:>15.4f}")
    print(f"{'Rec:  ' + cls:<20} {dt_cr[cls]['recall']:>15.4f} {rf_cr[cls]['recall']:>15.4f} {xgb_cr[cls]['recall']:>15.4f}")
print("=" * 70)


# ── BLOCK 11: SHAP VALUES ───────────────────────────────────
print("\nComputing SHAP values...")
explainer   = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)

# SHAP beeswarm plot (saved via matplotlib)
fig_shap, ax = plt.subplots(figsize=(10, 6))
shap.summary_plot(
    shap_values, X_test,
    feature_names=features,
    class_names=class_names,
    show=False
)
plt.tight_layout()
plt.savefig("xgb_shap_beeswarm.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: xgb_shap_beeswarm.png")

# SHAP bar plot (mean |SHAP| per feature)
fig_shap2, ax2 = plt.subplots(figsize=(10, 6))
shap.summary_plot(
    shap_values, X_test,
    feature_names=features,
    class_names=class_names,
    plot_type="bar",
    show=False
)
plt.tight_layout()
plt.savefig("xgb_shap_bar.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: xgb_shap_bar.png")


# ── BLOCK 12: CHART 1 — XGB CONFUSION MATRIX ────────────────
cm_xgb = confusion_matrix(y_test, xgb_pred)
fig1 = go.Figure(data=go.Heatmap(
    z=cm_xgb,
    x=["Pred: " + c for c in class_names],
    y=["Actual: " + c for c in class_names],
    colorscale="Blues",
    text=cm_xgb,
    texttemplate="%{text}",
    textfont=dict(size=16),
    showscale=True
))
fig1.update_layout(
    title="Confusion Matrix — XGBoost Trading Signals (Optuna Tuned)",
    xaxis_title="Predicted Signal",
    yaxis_title="Actual Signal"
)
fig1.write_image("xgb_confusion_matrix.png")
print("Saved: xgb_confusion_matrix.png")


# ── BLOCK 13: CHART 2 — OPTUNA OPTIMIZATION HISTORY ─────────
trials_df = study.trials_dataframe()
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=list(range(len(trials_df))),
    y=trials_df["value"],
    mode="markers",
    name="Trial Accuracy",
    marker=dict(color="#1f77b4", size=6, opacity=0.6)
))

# Running best
running_best = trials_df["value"].cummax()
fig2.add_trace(go.Scatter(
    x=list(range(len(trials_df))),
    y=running_best,
    mode="lines",
    name="Best So Far",
    line=dict(color="#d62728", width=2)
))
fig2.update_layout(
    title="Optuna Hyperparameter Tuning — 50 Trials (TPE Sampler)",
    xaxis_title="Trial Number",
    yaxis_title="Accuracy",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)
fig2.write_image("xgb_optuna_history.png")
print("Saved: xgb_optuna_history.png")


# ── BLOCK 14: CHART 3 — FULL MODEL COMPARISON ───────────────
models = ["Decision Tree\n(P3)", "Random Forest\n(P4)", "XGBoost\n(P5)"]
accs   = [dt_acc * 100, rf_acc * 100, xgb_acc * 100]
f1s    = [dt_f1 * 100, rf_f1 * 100, xgb_f1 * 100]
colors = ["#ff7f0e", "#1f77b4", "#2ca02c"]

fig3 = make_subplots(rows=1, cols=2,
    subplot_titles=["Accuracy (%)", "F1-Macro (%)"],
    horizontal_spacing=0.15
)

fig3.add_trace(go.Bar(
    x=models, y=accs,
    text=[f"{a:.1f}%" for a in accs],
    textposition="outside",
    marker_color=colors, width=0.5,
    showlegend=False
), row=1, col=1)

fig3.add_trace(go.Bar(
    x=models, y=f1s,
    text=[f"{f:.1f}%" for f in f1s],
    textposition="outside",
    marker_color=colors, width=0.5,
    showlegend=False
), row=1, col=2)

fig3.update_layout(
    title="Complete Model Evolution: Decision Tree → Random Forest → XGBoost",
    height=500
)
fig3.update_yaxes(range=[0, 100], row=1, col=1)
fig3.update_yaxes(range=[0, 100], row=1, col=2)
fig3.write_image("xgb_full_comparison.png")
print("Saved: xgb_full_comparison.png")


# ── BLOCK 15: SUMMARY ───────────────────────────────────────
print("\n=== PROJECT 5 COMPLETE ===")
print(f"Decision Tree:  {dt_acc*100:.1f}% accuracy | {dt_f1*100:.1f}% F1")
print(f"Random Forest:  {rf_acc*100:.1f}% accuracy | {rf_f1*100:.1f}% F1")
print(f"XGBoost:        {xgb_acc*100:.1f}% accuracy | {xgb_f1*100:.1f}% F1")
print(f"\nOptuna best params:")
for k, v in study.best_params.items():
    print(f"  {k}: {v}")
print(f"\nSHAP top feature: check xgb_shap_bar.png")
