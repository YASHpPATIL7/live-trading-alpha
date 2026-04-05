import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="P3-P5: Trading Signals", page_icon="📊", layout="wide")
st.title("📊 Trading Signals — DT → RF → XGBoost Evolution")

st.markdown("""
3-class trading signals (BUY/HOLD/SELL) for RELIANCE.NS.
Compare Decision Tree, Random Forest, and XGBoost on the **same data**.
""")

# --- Sidebar ---
st.sidebar.header("Parameters")
ticker = st.sidebar.text_input("Ticker", "RELIANCE.NS")
buy_thresh = st.sidebar.number_input("BUY threshold (%)", value=0.5, step=0.1) / 100
sell_thresh = -buy_thresh

# Optional XGBoost
try:
    import xgboost as xgb
    HAS_XGB = True
except ImportError:
    HAS_XGB = False

try:
    import shap
    HAS_SHAP = True
except ImportError:
    HAS_SHAP = False

if st.sidebar.button("🚀 Run All Models", type="primary"):
    with st.spinner("Fetching data and training DT → RF → XGB..."):
        # Fetch data
        raw = yf.download(ticker, period="5y", auto_adjust=True, progress=False)
        df = pd.DataFrame({
            "Close": raw["Close"].squeeze(),
            "Volume": raw["Volume"].squeeze()
        }).dropna()

        # Feature engineering
        delta    = df["Close"].diff()
        gain     = delta.where(delta > 0, 0.0)
        loss     = -delta.where(delta < 0, 0.0)
        avg_gain = gain.ewm(com=13, adjust=False).mean()
        avg_loss = loss.ewm(com=13, adjust=False).mean()
        rs       = avg_gain / avg_loss
        df["RSI_14"] = 100 - (100 / (1 + rs))

        ema_12 = df["Close"].ewm(span=12, adjust=False).mean()
        ema_26 = df["Close"].ewm(span=26, adjust=False).mean()
        df["MACD_signal"] = (ema_12 - ema_26) - (ema_12 - ema_26).ewm(span=9, adjust=False).mean()

        df["MA_50"]     = df["Close"].rolling(50).mean()
        df["MA_200"]    = df["Close"].rolling(200).mean()
        df["MA_cross"]  = (df["MA_50"] > df["MA_200"]).astype(int)
        df["MA_spread"] = (df["MA_50"] - df["MA_200"]) / df["MA_200"] * 100

        df["Fwd_return_5d"] = df["Close"].pct_change(5).shift(-5)
        df.dropna(inplace=True)

        # Labels
        def label(r):
            if r > buy_thresh: return "BUY"
            elif r < sell_thresh: return "SELL"
            else: return "HOLD"

        df["Signal"] = df["Fwd_return_5d"].apply(label)
        le = LabelEncoder()
        df["Signal_enc"] = le.fit_transform(df["Signal"])
        class_names = list(le.classes_)

        features = ["RSI_14", "MACD_signal", "MA_cross", "MA_spread"]
        X = df[features].values
        y = df["Signal_enc"].values
        split = int(len(df) * 0.8)
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]
        dates_test = df.index[split:]

        # --- Train all models ---
        results = {}

        # Decision Tree
        dt = DecisionTreeClassifier(max_depth=5, min_samples_leaf=20,
            class_weight="balanced", random_state=42)
        dt.fit(X_train, y_train)
        dt_pred = dt.predict(X_test)
        results["Decision Tree"] = {
            "acc": accuracy_score(y_test, dt_pred),
            "f1": f1_score(y_test, dt_pred, average="macro"),
            "pred": dt_pred,
            "cm": confusion_matrix(y_test, dt_pred)
        }

        # Random Forest
        rf = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=20,
            class_weight="balanced", random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)
        rf_pred = rf.predict(X_test)
        results["Random Forest"] = {
            "acc": accuracy_score(y_test, rf_pred),
            "f1": f1_score(y_test, rf_pred, average="macro"),
            "pred": rf_pred,
            "cm": confusion_matrix(y_test, rf_pred)
        }

        # XGBoost (if available)
        if HAS_XGB:
            xgb_model = xgb.XGBClassifier(
                max_depth=5, learning_rate=0.1, n_estimators=100,
                objective="multi:softmax", num_class=3,
                use_label_encoder=False, verbosity=0, random_state=42
            )
            xgb_model.fit(X_train, y_train)
            xgb_pred = xgb_model.predict(X_test)
            results["XGBoost"] = {
                "acc": accuracy_score(y_test, xgb_pred),
                "f1": f1_score(y_test, xgb_pred, average="macro"),
                "pred": xgb_pred,
                "cm": confusion_matrix(y_test, xgb_pred)
            }

        # --- Metrics ---
        st.subheader("📊 Model Comparison")
        cols = st.columns(len(results))
        colors_map = {"Decision Tree": "#ff7f0e", "Random Forest": "#1f77b4", "XGBoost": "#2ca02c"}
        for i, (name, res) in enumerate(results.items()):
            with cols[i]:
                st.metric(f"{name} Accuracy", f"{res['acc']*100:.1f}%")
                st.metric(f"{name} F1-macro", f"{res['f1']:.4f}")

        # --- Comparison bar chart ---
        models = list(results.keys())
        accs = [results[m]["acc"] * 100 for m in models]
        f1s  = [results[m]["f1"] * 100 for m in models]
        clrs = [colors_map.get(m, "#999") for m in models]

        fig_comp = make_subplots(rows=1, cols=2,
            subplot_titles=["Accuracy (%)", "F1-Macro (%)"])
        fig_comp.add_trace(go.Bar(x=models, y=accs,
            text=[f"{a:.1f}%" for a in accs], textposition="outside",
            marker_color=clrs, showlegend=False), row=1, col=1)
        fig_comp.add_trace(go.Bar(x=models, y=f1s,
            text=[f"{f:.1f}%" for f in f1s], textposition="outside",
            marker_color=clrs, showlegend=False), row=1, col=2)
        fig_comp.update_yaxes(range=[0, 100])
        fig_comp.update_layout(title="Model Evolution: DT → RF → XGBoost", height=450)
        st.plotly_chart(fig_comp, use_container_width=True)

        # --- Confusion matrices ---
        st.subheader("🔲 Confusion Matrices")
        cm_cols = st.columns(len(results))
        for i, (name, res) in enumerate(results.items()):
            with cm_cols[i]:
                cm = res["cm"]
                fig_cm = go.Figure(data=go.Heatmap(
                    z=cm, x=["P:" + c for c in class_names],
                    y=["A:" + c for c in class_names],
                    colorscale="Blues", text=cm, texttemplate="%{text}",
                    textfont=dict(size=14), showscale=False
                ))
                fig_cm.update_layout(title=name, height=350, width=350)
                st.plotly_chart(fig_cm, use_container_width=True)

        # --- Signals over time ---
        st.subheader("📈 Predicted Signals Over Time (Best Model)")
        best_model = max(results.items(), key=lambda x: x[1]["acc"])
        decoded = le.inverse_transform(best_model[1]["pred"])
        signal_colors = {"BUY": "#2ca02c", "HOLD": "#ff7f0e", "SELL": "#d62728"}
        fig_sig = go.Figure()
        for sig, color in signal_colors.items():
            mask = decoded == sig
            fig_sig.add_trace(go.Scatter(
                x=dates_test[mask], y=[sig] * mask.sum(),
                mode="markers", name=sig,
                marker=dict(color=color, size=6, opacity=0.7)
            ))
        fig_sig.update_layout(title=f"Predicted Signals — {best_model[0]}", height=350)
        st.plotly_chart(fig_sig, use_container_width=True)

        # --- SHAP (if available) ---
        if HAS_XGB and HAS_SHAP and "XGBoost" in results:
            st.subheader("🔍 SHAP Feature Importance (XGBoost)")
            explainer = shap.TreeExplainer(xgb_model)
            shap_values = explainer.shap_values(X_test)

            # Manual SHAP bar chart
            if isinstance(shap_values, list):
                mean_shap = np.mean([np.abs(sv).mean(axis=0) for sv in shap_values], axis=0)
            else:
                mean_shap = np.abs(shap_values).mean(axis=0)
            shap_df = pd.DataFrame({"Feature": features, "Mean |SHAP|": mean_shap})
            shap_df = shap_df.sort_values("Mean |SHAP|", ascending=True)
            fig_shap = go.Figure(go.Bar(
                x=shap_df["Mean |SHAP|"], y=shap_df["Feature"],
                orientation="h", marker_color="#2ca02c"
            ))
            fig_shap.update_layout(title="Mean |SHAP| per Feature", height=350)
            st.plotly_chart(fig_shap, use_container_width=True)
else:
    st.info("👈 Click **Run All Models** in the sidebar to start.")
    if not HAS_XGB:
        st.warning("⚠️ `xgboost` not installed. XGBoost comparison will be skipped.")
