import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import plotly.graph_objects as go

st.set_page_config(page_title="P7: Clustering", page_icon="🎯", layout="wide")
st.title("🎯 Project 7 — K-Means Clustering: NSE Sector Analysis")

st.markdown("""
Group NSE Nifty stocks by fundamental metrics using K-Means.
Features: PE, PB, ROE, D/E, Revenue Growth. PCA for 2D visualization.
""")

NIFTY_50 = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "ITC.NS", "SBIN.NS", "BHARTIARTL.NS", "KOTAKBANK.NS",
    "LT.NS", "AXISBANK.NS", "ASIANPAINT.NS", "MARUTI.NS", "HCLTECH.NS",
    "SUNPHARMA.NS", "TITAN.NS", "BAJFINANCE.NS", "ULTRACEMCO.NS", "NTPC.NS",
    "WIPRO.NS", "NESTLEIND.NS", "POWERGRID.NS", "TATAMOTORS.NS", "M&M.NS",
    "JSWSTEEL.NS", "TATASTEEL.NS", "ADANIPORTS.NS", "INDUSINDBK.NS", "TECHM.NS",
    "COALINDIA.NS", "HINDALCO.NS", "GRASIM.NS", "DIVISLAB.NS", "DRREDDY.NS",
    "CIPLA.NS", "BAJAJ-AUTO.NS", "EICHERMOT.NS", "BPCL.NS", "ONGC.NS",
    "HEROMOTOCO.NS", "BRITANNIA.NS", "APOLLOHOSP.NS", "TATACONSUM.NS", "UPL.NS",
    "SBILIFE.NS", "HDFCLIFE.NS", "SHREECEM.NS", "BAJAJFINSV.NS", "ADANIENT.NS"
]

# --- Sidebar ---
st.sidebar.header("Parameters")
k_clusters = st.sidebar.slider("Number of Clusters (K)", 2, 10, 5)

if st.sidebar.button("🚀 Run Clustering", type="primary"):
    progress = st.progress(0, text="Fetching fundamental data...")
    data = []

    for i, ticker in enumerate(NIFTY_50):
        try:
            info = yf.Ticker(ticker).info
            short_name = ticker.replace(".NS", "")
            roe = info.get("returnOnEquity", np.nan)
            rg  = info.get("revenueGrowth", np.nan)
            row = {
                "Ticker": short_name,
                "PE": info.get("trailingPE", np.nan),
                "PB": info.get("priceToBook", np.nan),
                "ROE": roe * 100 if roe and not np.isnan(roe) else np.nan,
                "DebtToEquity": info.get("debtToEquity", np.nan),
                "RevenueGrowth": rg * 100 if rg and not np.isnan(rg) else np.nan
            }
            data.append(row)
        except:
            pass
        progress.progress((i + 1) / len(NIFTY_50), text=f"Fetching {ticker}...")

    df = pd.DataFrame(data)
    features = ["PE", "PB", "ROE", "DebtToEquity", "RevenueGrowth"]

    # Clean
    df_clean = df.dropna(subset=features, thresh=3).copy()
    for col in features:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        q01, q99 = df_clean[col].quantile(0.01), df_clean[col].quantile(0.99)
        df_clean[col] = df_clean[col].clip(q01, q99)

    progress.progress(1.0, text="Clustering...")

    # Scale + Cluster
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_clean[features].values)

    kmeans = KMeans(n_clusters=k_clusters, n_init=10, random_state=42)
    df_clean["Cluster"] = kmeans.fit_predict(X_scaled)

    # PCA
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    df_clean["PC1"] = X_pca[:, 0]
    df_clean["PC2"] = X_pca[:, 1]
    explained = pca.explained_variance_ratio_

    sil = silhouette_score(X_scaled, df_clean["Cluster"])

    # --- Metrics ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Stocks Analysed", len(df_clean))
    col2.metric("Silhouette Score", f"{sil:.4f}")
    col3.metric("PCA Variance Explained", f"{sum(explained)*100:.1f}%")

    # --- Elbow + Silhouette ---
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 PCA Scatter", "📐 Elbow Method", "📊 Cluster Profiles", "📋 Stock List"])

    with tab1:
        cluster_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                          "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
        fig_pca = go.Figure()
        for cid in sorted(df_clean["Cluster"].unique()):
            mask = df_clean["Cluster"] == cid
            subset = df_clean[mask]
            fig_pca.add_trace(go.Scatter(
                x=subset["PC1"], y=subset["PC2"],
                mode="markers+text", name=f"Cluster {cid}",
                text=subset["Ticker"], textposition="top center",
                textfont=dict(size=8),
                marker=dict(color=cluster_colors[cid], size=12,
                            line=dict(width=1, color="white"))
            ))
        fig_pca.update_layout(
            title=f"NSE Stocks — K-Means Clusters (K={k_clusters}) via PCA",
            xaxis_title=f"PC1 ({explained[0]:.1%})",
            yaxis_title=f"PC2 ({explained[1]:.1%})",
            height=600
        )
        st.plotly_chart(fig_pca, use_container_width=True)

    with tab2:
        inertias, sils = [], []
        for k in range(2, 11):
            km = KMeans(n_clusters=k, n_init=10, random_state=42)
            labels = km.fit_predict(X_scaled)
            inertias.append(km.inertia_)
            sils.append(silhouette_score(X_scaled, labels))

        fig_elbow = go.Figure()
        fig_elbow.add_trace(go.Scatter(x=list(range(2,11)), y=inertias,
            mode="lines+markers", name="Inertia"))
        fig_elbow.add_vline(x=k_clusters, line_dash="dash", line_color="red")
        fig_elbow.update_layout(title="Elbow Method", xaxis_title="K", yaxis_title="Inertia", height=400)
        st.plotly_chart(fig_elbow, use_container_width=True)

        fig_sil = go.Figure()
        fig_sil.add_trace(go.Scatter(x=list(range(2,11)), y=sils,
            mode="lines+markers", name="Silhouette", line=dict(color="#2ca02c")))
        fig_sil.add_vline(x=k_clusters, line_dash="dash", line_color="red")
        fig_sil.update_layout(title="Silhouette Score", xaxis_title="K", yaxis_title="Score", height=400)
        st.plotly_chart(fig_sil, use_container_width=True)

    with tab3:
        profiles = df_clean.groupby("Cluster")[features].mean()
        profiles_z = (profiles - profiles.mean()) / profiles.std()
        fig_heat = go.Figure(data=go.Heatmap(
            z=profiles_z.values,
            x=features,
            y=[f"Cluster {i}" for i in range(k_clusters)],
            colorscale="RdYlBu_r",
            text=profiles.values.round(1),
            texttemplate="%{text}",
            textfont=dict(size=12),
            colorbar=dict(title="Z-Score")
        ))
        fig_heat.update_layout(title="Cluster Profiles (z-scored)", height=400)
        st.plotly_chart(fig_heat, use_container_width=True)

    with tab4:
        st.dataframe(
            df_clean[["Ticker", "Cluster"] + features].sort_values("Cluster"),
            hide_index=True, use_container_width=True
        )

    progress.empty()
else:
    st.info("👈 Click **Run Clustering** in the sidebar to start.")
