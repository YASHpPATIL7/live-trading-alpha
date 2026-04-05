
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (classification_report, confusion_matrix,
                              ConfusionMatrixDisplay)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")

# BLOCK 2: FETCH DATA
raw = yf.download("RELIANCE.NS", period="5y", auto_adjust=True, progress=False)
df  = pd.DataFrame({
    "Close":  raw["Close"].squeeze(),
    "Volume": raw["Volume"].squeeze()
}).dropna()
print("Rows:", len(df), "|", str(df.index[0].date()), "to", str(df.index[-1].date()))

# BLOCK 3: FEATURE ENGINEERING
# RSI 14
delta    = df["Close"].diff()
gain     = delta.where(delta > 0, 0.0)
loss     = -delta.where(delta < 0, 0.0)
avg_gain = gain.ewm(com=13, adjust=False).mean()
avg_loss = loss.ewm(com=13, adjust=False).mean()
rs       = avg_gain / avg_loss
df["RSI_14"] = 100 - (100 / (1 + rs))

# MACD
ema_12        = df["Close"].ewm(span=12, adjust=False).mean()
ema_26        = df["Close"].ewm(span=26, adjust=False).mean()
macd_line     = ema_12 - ema_26
signal_line   = macd_line.ewm(span=9, adjust=False).mean()
df["MACD_signal"] = macd_line - signal_line   # histogram > 0 = bullish

# MA crossover
df["MA_50"]       = df["Close"].rolling(50).mean()
df["MA_200"]      = df["Close"].rolling(200).mean()
df["MA_cross"]    = (df["MA_50"] > df["MA_200"]).astype(int)
df["MA_spread"]   = (df["MA_50"] - df["MA_200"]) / df["MA_200"] * 100

# Forward return for labelling
df["Fwd_return_5d"] = df["Close"].pct_change(5).shift(-5)
df.dropna(inplace=True)

# BLOCK 4: CREATE 3-CLASS LABELS
# BUY  = forward 5d return > +0.5%
# SELL = forward 5d return < -0.5%
# HOLD = everything in between

BUY_THRESH  =  0.005
SELL_THRESH = -0.005

def label(r):
    if r > BUY_THRESH:
        return "BUY"
    elif r < SELL_THRESH:
        return "SELL"
    else:
        return "HOLD"

df["Signal"] = df["Fwd_return_5d"].apply(label)
print("Label distribution:")
print(df["Signal"].value_counts())

le = LabelEncoder()
df["Signal_enc"] = le.fit_transform(df["Signal"])   # BUY=0 HOLD=1 SELL=2

# BLOCK 5: TRAIN/TEST SPLIT
features = ["RSI_14", "MACD_signal", "MA_cross", "MA_spread"]
X        = df[features].values
y        = df["Signal_enc"].values

split     = int(len(df) * 0.8)
X_train   = X[:split];  X_test  = X[split:]
y_train   = y[:split];  y_test  = y[split:]
dates_test = df.index[split:]

print("Train:", X_train.shape, "| Test:", X_test.shape)

# BLOCK 6: DECISION TREE
dt = DecisionTreeClassifier(
    max_depth=5,
    min_samples_leaf=20,
    class_weight="balanced",
    random_state=42
)
dt.fit(X_train, y_train)
y_pred      = dt.predict(X_test)
class_names = list(le.classes_)   # ["BUY", "HOLD", "SELL"]

print("\nDecision Tree Rules (top 3 levels):")
tree_text = export_text(dt, feature_names=features, max_depth=3)
print(tree_text)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

# BLOCK 7: FEATURE IMPORTANCE
importances = dt.feature_importances_
imp_df      = pd.DataFrame({"Feature": features, "Importance": importances})
imp_df      = imp_df.sort_values("Importance", ascending=True)

# BLOCK 8: PLOT 1 — CONFUSION MATRIX
cm = confusion_matrix(y_test, y_pred)
fig1 = go.Figure(data=go.Heatmap(
    z=cm,
    x=["Pred: " + c for c in class_names],
    y=["Actual: " + c for c in class_names],
    colorscale="Blues",
    text=cm,
    texttemplate="%{text}",
    textfont=dict(size=16),
    showscale=True
))
fig1.update_layout(
    title="Confusion Matrix — Decision Tree Trading Signals (BUY/HOLD/SELL)",
    xaxis_title="Predicted Signal",
    yaxis_title="Actual Signal"
)
fig1.write_image("dt_confusion_matrix.png")
fig1.show()
print("Saved: dt_confusion_matrix.png")

# BLOCK 9: PLOT 2 — FEATURE IMPORTANCE
fig2 = go.Figure(go.Bar(
    x=imp_df["Importance"],
    y=imp_df["Feature"],
    orientation="h",
    marker_color="#1f77b4"
))
fig2.update_layout(
    title="Feature Importance — Decision Tree Trading Signals",
    xaxis_title="Gini Importance",
    yaxis_title="Feature"
)
fig2.write_image("dt_feature_importance.png")
fig2.show()
print("Saved: dt_feature_importance.png")

# BLOCK 10: PLOT 3 — SIGNAL DISTRIBUTION OVER TIME
colors_map = {"BUY": "#2ca02c", "HOLD": "#ff7f0e", "SELL": "#d62728"}
decoded    = le.inverse_transform(y_pred)
pred_df    = pd.DataFrame({"Date": dates_test, "Signal": decoded})

fig3 = go.Figure()
for sig, color in colors_map.items():
    mask = pred_df["Signal"] == sig
    fig3.add_trace(go.Scatter(
        x=pred_df.loc[mask, "Date"],
        y=[sig] * mask.sum(),
        mode="markers",
        name=sig,
        marker=dict(color=color, size=6, opacity=0.7)
    ))
fig3.update_layout(
    title="Predicted Trading Signals Over Time — RELIANCE (Test Set)",
    xaxis_title="Date",
    yaxis_title="Signal",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)
fig3.write_image("dt_signals_over_time.png")
fig3.show()
print("Saved: dt_signals_over_time.png")

# BLOCK 11: PLOT 4 — RSI vs MACD coloured by signal
actual_signals = le.inverse_transform(y_test)
fig4 = go.Figure()
for sig, color in colors_map.items():
    mask = actual_signals == sig
    fig4.add_trace(go.Scatter(
        x=X_test[mask, 0],    # RSI_14
        y=X_test[mask, 1],    # MACD_signal
        mode="markers",
        name=sig,
        marker=dict(color=color, size=5, opacity=0.6)
    ))
fig4.update_layout(
    title="RSI vs MACD Coloured by Actual Signal — RELIANCE (Test Set)",
    xaxis_title="RSI 14",
    yaxis_title="MACD Histogram",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)
fig4.write_image("dt_rsi_vs_macd.png")
fig4.show()
print("Saved: dt_rsi_vs_macd.png")

print("\n=== PROJECT 3 COMPLETE ===")
print("Features used:", features)
print("Max depth: 5 | Min samples leaf: 20")
print("Top feature:", features[importances.argmax()])
