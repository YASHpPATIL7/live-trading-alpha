# ============================================================
# PROJECT 1: Linear Regression — RELIANCE NSE Price Prediction
# ============================================================

# ── BLOCK 1: IMPORTS ────────────────────────────────────────
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")


# ── BLOCK 2: FETCH DATA ─────────────────────────────────────
raw = yf.download("RELIANCE.NS", period="5y", auto_adjust=True, progress=False)
df = pd.DataFrame({
    "Close":  raw["Close"].squeeze(),
    "Volume": raw["Volume"].squeeze()
}).dropna()
print(f"Rows: {len(df)} | {df.index[0].date()} to {df.index[-1].date()}")


# ── BLOCK 3: FEATURE ENGINEERING ────────────────────────────
df["MA_50"]         = df["Close"].rolling(50).mean()
df["MA_200"]        = df["Close"].rolling(200).mean()
df["Volume_avg_20"] = df["Volume"].rolling(20).mean()
df["Volume_ratio"]  = df["Volume"] / df["Volume_avg_20"]
df["Daily_return"]  = df["Close"].pct_change(1)
df["Target_price"]  = df["Close"].shift(-1)
df["Target_return"] = df["Close"].pct_change(1).shift(-1)
df.dropna(inplace=True)
print(f"After engineering: {len(df)} rows")


# ── BLOCK 4: TRAIN/TEST SPLIT ────────────────────────────────
features   = ["MA_50", "MA_200", "Volume_ratio", "Daily_return"]
X          = df[features].values
y_return   = df["Target_return"].values
y_price    = df["Target_price"].values

split      = int(len(df) * 0.8)
X_train    = X[:split]
X_test     = X[split:]
yret_train = y_return[:split]
yret_test  = y_return[split:]
yprc_train = y_price[:split]
yprc_test  = y_price[split:]
dates_test = df.index[split:]

scaler     = StandardScaler()
X_train_s  = scaler.fit_transform(X_train)
X_test_s   = scaler.transform(X_test)


# ── BLOCK 5: LINEAR REGRESSION ──────────────────────────────
lr_ret = LinearRegression()
lr_ret.fit(X_train_s, yret_train)
lr_pred_ret = lr_ret.predict(X_test_s)
lr_r2   = r2_score(yret_test, lr_pred_ret)
lr_rmse = np.sqrt(mean_squared_error(yret_test, lr_pred_ret))

lr_prc = LinearRegression()
lr_prc.fit(X_train_s, yprc_train)
lr_pred_prc = lr_prc.predict(X_test_s)

print(f"\nLinear Regression  --> R2: {lr_r2:.4f}   RMSE: {lr_rmse:.6f}")


# ── BLOCK 6: RIDGE REGRESSION ───────────────────────────────
best_alpha = 1.0
best_cv    = -999

for alpha in [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
    tscv   = TimeSeriesSplit(n_splits=5)
    scores = []
    for tr, val in tscv.split(X_train_s):
        r = Ridge(alpha=alpha)
        r.fit(X_train_s[tr], yret_train[tr])
        scores.append(r2_score(yret_train[val], r.predict(X_train_s[val])))
    if np.mean(scores) > best_cv:
        best_cv    = np.mean(scores)
        best_alpha = alpha

ridge_ret = Ridge(alpha=best_alpha)
ridge_ret.fit(X_train_s, yret_train)
ridge_pred_ret = ridge_ret.predict(X_test_s)
ridge_r2   = r2_score(yret_test, ridge_pred_ret)
ridge_rmse = np.sqrt(mean_squared_error(yret_test, ridge_pred_ret))

ridge_prc = Ridge(alpha=best_alpha)
ridge_prc.fit(X_train_s, yprc_train)
ridge_pred_prc = ridge_prc.predict(X_test_s)

resid_lr    = yret_test - lr_pred_ret
resid_ridge = yret_test - ridge_pred_ret

print(f"Ridge (alpha={best_alpha}) --> R2: {ridge_r2:.4f}   RMSE: {ridge_rmse:.6f}")


# ── BLOCK 7: RESULTS TABLE ──────────────────────────────────
print("\n" + "=" * 55)
print(f"{'Metric':<20} {'Linear Reg':>15} {'Ridge':>15}")
print("-" * 55)
print(f"{'R2 Score':<20} {lr_r2:>15.4f} {ridge_r2:>15.4f}")
print(f"{'RMSE':<20} {lr_rmse:>15.6f} {ridge_rmse:>15.6f}")
print(f"{'Best Alpha':<20} {'N/A':>15} {str(best_alpha):>15}")
print(f"{'Train rows':<20} {split:>15} {split:>15}")
print(f"{'Test rows':<20} {len(X_test):>15} {len(X_test):>15}")
print("=" * 55)

print("\nCoefficients (Linear Regression):")
for f, c in zip(features, lr_ret.coef_):
    print(f"  {f:<22} {c:>+.6f}")


# ── BLOCK 8: PLOT 1 — Actual vs Predicted Price ─────────────
fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=dates_test,
    y=yprc_test,
    name="Actual Close",
    line=dict(color="#1f77b4", width=1.5)
))

fig1.add_trace(go.Scatter(
    x=dates_test,
    y=lr_pred_prc,
    name="LR Predicted",
    line=dict(color="#ff7f0e", width=1.5, dash="dot")
))

fig1.add_trace(go.Scatter(
    x=dates_test,
    y=ridge_pred_prc,
    name="Ridge Predicted (alpha=" + str(best_alpha) + ")",
    line=dict(color="#2ca02c", width=1.5, dash="dash")
))

fig1.update_layout(
    title="Actual vs Predicted — RELIANCE Close Price (Test Set)",
    xaxis_title="Date",
    yaxis_title="Price (INR)",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)

fig1.write_image("actual_vs_predicted.png")
fig1.show()
print("Saved: actual_vs_predicted.png")


# ── BLOCK 9: PLOT 2 — Residual Analysis (2x2) ───────────────
fig2 = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=[
        "LR Residuals Over Time",
        "Ridge Residuals Over Time",
        "LR Residual Distribution",
        "Ridge Residual Distribution"
    ]
)

fig2.add_trace(
    go.Scatter(
        x=dates_test,
        y=resid_lr,
        mode="lines",
        name="LR Residuals",
        line=dict(color="#ff7f0e", width=0.8)
    ),
    row=1, col=1
)

fig2.add_trace(
    go.Scatter(
        x=dates_test,
        y=resid_ridge,
        mode="lines",
        name="Ridge Residuals",
        line=dict(color="#2ca02c", width=0.8)
    ),
    row=1, col=2
)

fig2.add_hline(y=0, line_dash="dash", line_color="gray", row=1, col=1)
fig2.add_hline(y=0, line_dash="dash", line_color="gray", row=1, col=2)

fig2.add_trace(
    go.Histogram(
        x=resid_lr,
        nbinsx=50,
        name="LR Distribution",
        marker_color="#ff7f0e",
        opacity=0.75
    ),
    row=2, col=1
)

fig2.add_trace(
    go.Histogram(
        x=resid_ridge,
        nbinsx=50,
        name="Ridge Distribution",
        marker_color="#2ca02c",
        opacity=0.75
    ),
    row=2, col=2
)

fig2.update_layout(
    title="Residual Analysis — Linear Regression vs Ridge",
    showlegend=False,
    height=700
)

fig2.update_xaxes(title_text="Date",     row=1, col=1)
fig2.update_xaxes(title_text="Date",     row=1, col=2)
fig2.update_xaxes(title_text="Residual", row=2, col=1)
fig2.update_xaxes(title_text="Residual", row=2, col=2)
fig2.update_yaxes(title_text="Residual", row=1, col=1)
fig2.update_yaxes(title_text="Residual", row=1, col=2)
fig2.update_yaxes(title_text="Count",    row=2, col=1)
fig2.update_yaxes(title_text="Count",    row=2, col=2)

fig2.write_image("residual_analysis.png")
fig2.show()
print("Saved: residual_analysis.png")


# ── BLOCK 10: PLOT 3 — Predicted vs Actual Scatter ──────────
minv = float(yret_test.min())
maxv = float(yret_test.max())

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=yret_test,
    y=lr_pred_ret,
    mode="markers",
    name="LR",
    marker=dict(color="#ff7f0e", size=4, opacity=0.5)
))

fig3.add_trace(go.Scatter(
    x=yret_test,
    y=ridge_pred_ret,
    mode="markers",
    name="Ridge",
    marker=dict(color="#2ca02c", size=4, opacity=0.5)
))

fig3.add_trace(go.Scatter(
    x=[minv, maxv],
    y=[minv, maxv],
    mode="lines",
    name="Perfect Fit",
    line=dict(color="red", dash="dash", width=1.5)
))

fig3.update_layout(
    title="Predicted vs Actual Returns — RELIANCE (Test Set)",
    xaxis_title="Actual Return",
    yaxis_title="Predicted Return",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)

fig3.write_image("predicted_vs_actual_scatter.png")
fig3.show()
print("Saved: predicted_vs_actual_scatter.png")

print("\n=== PROJECT 1 COMPLETE ===")
print(f"Linear Regression  --> R2: {lr_r2:.4f}   RMSE: {lr_rmse:.6f}")
print(f"Ridge (alpha={best_alpha}) --> R2: {ridge_r2:.4f}   RMSE: {ridge_rmse:.6f}")
