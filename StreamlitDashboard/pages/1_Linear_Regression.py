import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="P1: Linear Regression", page_icon="📉", layout="wide")
st.title("📉 Project 1 — Linear Regression: RELIANCE Price Prediction")

st.markdown("""
Predict next-day returns for RELIANCE.NS using Linear Regression and Ridge.
Features: MA_50, MA_200, Volume_ratio, Daily_return.
""")

# --- Sidebar controls ---
st.sidebar.header("Parameters")
ticker = st.sidebar.text_input("Ticker", "RELIANCE.NS")
period = st.sidebar.selectbox("Period", ["3y", "5y", "10y"], index=1)
test_pct = st.sidebar.slider("Test %", 10, 40, 20)

if st.sidebar.button("🚀 Run Model", type="primary"):
    with st.spinner("Fetching data and training model..."):
        # Fetch data
        raw = yf.download(ticker, period=period, auto_adjust=True, progress=False)
        df = pd.DataFrame({
            "Close": raw["Close"].squeeze(),
            "Volume": raw["Volume"].squeeze()
        }).dropna()

        # Feature engineering
        df["MA_50"]         = df["Close"].rolling(50).mean()
        df["MA_200"]        = df["Close"].rolling(200).mean()
        df["Volume_avg_20"] = df["Volume"].rolling(20).mean()
        df["Volume_ratio"]  = df["Volume"] / df["Volume_avg_20"]
        df["Daily_return"]  = df["Close"].pct_change(1)
        df["Target_return"] = df["Close"].pct_change(1).shift(-1)
        df["Target_price"]  = df["Close"].shift(-1)
        df.dropna(inplace=True)

        features = ["MA_50", "MA_200", "Volume_ratio", "Daily_return"]
        X = df[features].values
        y_return = df["Target_return"].values
        y_price  = df["Target_price"].values

        split = int(len(df) * (1 - test_pct / 100))
        X_train, X_test = X[:split], X[split:]
        yret_train, yret_test = y_return[:split], y_return[split:]
        yprc_test = y_price[split:]
        dates_test = df.index[split:]

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s  = scaler.transform(X_test)

        # Linear Regression
        lr = LinearRegression()
        lr.fit(X_train_s, yret_train)
        lr_pred = lr.predict(X_test_s)
        lr_r2   = r2_score(yret_test, lr_pred)
        lr_rmse = np.sqrt(mean_squared_error(yret_test, lr_pred))

        # Ridge
        ridge = Ridge(alpha=1000)
        ridge.fit(X_train_s, yret_train)
        ridge_pred = ridge.predict(X_test_s)
        ridge_r2   = r2_score(yret_test, ridge_pred)
        ridge_rmse = np.sqrt(mean_squared_error(yret_test, ridge_pred))

        # --- Metrics ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("LR R²", f"{lr_r2:.4f}")
        col2.metric("LR RMSE", f"{lr_rmse:.6f}")
        col3.metric("Ridge R²", f"{ridge_r2:.4f}")
        col4.metric("Ridge RMSE", f"{ridge_rmse:.6f}")

        # --- Charts ---
        tab1, tab2 = st.tabs(["📊 Predictions", "📈 Residuals"])

        with tab1:
            lr_prc = LinearRegression()
            lr_prc.fit(X_train_s, y_price[:split])
            lr_pred_prc = lr_prc.predict(X_test_s)

            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=dates_test, y=yprc_test, name="Actual",
                                       line=dict(color="#1f77b4", width=1.5)))
            fig1.add_trace(go.Scatter(x=dates_test, y=lr_pred_prc, name="LR Predicted",
                                       line=dict(color="#ff7f0e", width=1.5, dash="dot")))
            fig1.update_layout(title="Actual vs Predicted Price", height=500)
            st.plotly_chart(fig1, use_container_width=True)

        with tab2:
            resid = yret_test - lr_pred
            fig2 = make_subplots(rows=1, cols=2,
                subplot_titles=["Residuals Over Time", "Residual Distribution"])
            fig2.add_trace(go.Scatter(x=dates_test, y=resid, mode="lines",
                line=dict(color="#ff7f0e", width=0.8)), row=1, col=1)
            fig2.add_hline(y=0, line_dash="dash", line_color="gray", row=1, col=1)
            fig2.add_trace(go.Histogram(x=resid, nbinsx=50,
                marker_color="#ff7f0e", opacity=0.75), row=1, col=2)
            fig2.update_layout(title="Residual Analysis", height=400, showlegend=False)
            st.plotly_chart(fig2, use_container_width=True)

        # Coefficients
        st.subheader("Feature Coefficients (Linear Regression)")
        coef_df = pd.DataFrame({"Feature": features, "Coefficient": lr.coef_})
        st.dataframe(coef_df.sort_values("Coefficient", ascending=False), hide_index=True)
else:
    st.info("👈 Click **Run Model** in the sidebar to start.")
