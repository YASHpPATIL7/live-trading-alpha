# ============================================================
# PROJECT 7: K-Means Clustering — NSE Sector Analysis
# Group 50 NSE stocks by fundamentals: PE, PB, ROE, D/E, Revenue Growth
# K-Means with Elbow method (K=5), PCA for 2D visualization
# ============================================================

# ── BLOCK 1: IMPORTS ────────────────────────────────────────
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")


# ── BLOCK 2: DEFINE 50 NIFTY STOCKS ─────────────────────────
# Top NSE Nifty 50 constituents (Yahoo Finance ticker format)
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


# ── BLOCK 3: FETCH FUNDAMENTALS ─────────────────────────────
print("Fetching fundamental data for 50 NSE stocks...")
data = []
failed = []

for ticker in NIFTY_50:
    try:
        info = yf.Ticker(ticker).info
        short_name = ticker.replace(".NS", "")
        row = {
            "Ticker": short_name,
            "PE": info.get("trailingPE", np.nan),
            "PB": info.get("priceToBook", np.nan),
            "ROE": info.get("returnOnEquity", np.nan),
            "DebtToEquity": info.get("debtToEquity", np.nan),
            "RevenueGrowth": info.get("revenueGrowth", np.nan)
        }
        # Convert ROE and Revenue Growth to percentage
        if row["ROE"] is not None and not np.isnan(row["ROE"]):
            row["ROE"] = row["ROE"] * 100
        if row["RevenueGrowth"] is not None and not np.isnan(row["RevenueGrowth"]):
            row["RevenueGrowth"] = row["RevenueGrowth"] * 100

        data.append(row)
        print(f"  ✓ {short_name}")
    except Exception as e:
        failed.append(ticker)
        print(f"  ✗ {ticker}: {e}")

df = pd.DataFrame(data)
print(f"\nFetched: {len(df)} stocks | Failed: {len(failed)}")
if failed:
    print(f"Failed tickers: {failed}")


# ── BLOCK 4: CLEAN DATA ─────────────────────────────────────
features = ["PE", "PB", "ROE", "DebtToEquity", "RevenueGrowth"]
print(f"\nMissing values before cleaning:")
print(df[features].isna().sum())

# Drop rows with too many missing values, fill remaining with median
df_clean = df.dropna(subset=features, thresh=3).copy()  # keep if at least 3 of 5 available
for col in features:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

# Cap outliers at 1st and 99th percentile
for col in features:
    q01 = df_clean[col].quantile(0.01)
    q99 = df_clean[col].quantile(0.99)
    df_clean[col] = df_clean[col].clip(q01, q99)

print(f"After cleaning: {len(df_clean)} stocks")
print(df_clean[features].describe().round(2))


# ── BLOCK 5: STANDARDISE ────────────────────────────────────
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_clean[features].values)
print(f"\nScaled feature matrix: {X_scaled.shape}")


# ── BLOCK 6: ELBOW METHOD — FIND OPTIMAL K ──────────────────
K_range = range(2, 11)
inertias = []
silhouettes = []

for k in K_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))
    print(f"  K={k}: Inertia={km.inertia_:.1f} | Silhouette={silhouette_score(X_scaled, labels):.4f}")

print(f"\nBest silhouette at K={list(K_range)[np.argmax(silhouettes)]}")


# ── BLOCK 7: FIT FINAL K-MEANS (K=5) ────────────────────────
K_FINAL = 5
kmeans = KMeans(n_clusters=K_FINAL, n_init=10, random_state=42)
df_clean["Cluster"] = kmeans.fit_predict(X_scaled)

print(f"\nCluster distribution (K={K_FINAL}):")
print(df_clean["Cluster"].value_counts().sort_index())

# Cluster profiles
print("\nCluster Profiles (mean of each feature):")
profiles = df_clean.groupby("Cluster")[features].mean().round(2)
print(profiles)


# ── BLOCK 8: PCA FOR 2D VISUALIZATION ───────────────────────
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)
df_clean["PC1"] = X_pca[:, 0]
df_clean["PC2"] = X_pca[:, 1]

explained = pca.explained_variance_ratio_
print(f"\nPCA Explained Variance: PC1={explained[0]:.2%} PC2={explained[1]:.2%} Total={sum(explained):.2%}")


# ── BLOCK 9: ASSIGN CLUSTER NAMES ───────────────────────────
# Name clusters based on their profile characteristics
profile_names = {}
for cluster_id in range(K_FINAL):
    row = profiles.loc[cluster_id]
    if row["PE"] > profiles["PE"].median() and row["ROE"] > profiles["ROE"].median():
        profile_names[cluster_id] = "Growth Premium"
    elif row["DebtToEquity"] > profiles["DebtToEquity"].median():
        profile_names[cluster_id] = "High Leverage"
    elif row["PE"] < profiles["PE"].median() and row["PB"] < profiles["PB"].median():
        profile_names[cluster_id] = "Deep Value"
    elif row["ROE"] > profiles["ROE"].median():
        profile_names[cluster_id] = "Quality"
    else:
        profile_names[cluster_id] = "Moderate"

df_clean["ClusterName"] = df_clean["Cluster"].map(profile_names)
print("\nCluster Names:")
for k, v in profile_names.items():
    stocks = df_clean[df_clean["Cluster"] == k]["Ticker"].tolist()
    print(f"  Cluster {k} ({v}): {', '.join(stocks)}")


# ── BLOCK 10: CHART 1 — ELBOW CURVE ─────────────────────────
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=list(K_range), y=inertias,
    mode="lines+markers",
    name="Inertia",
    line=dict(color="#1f77b4", width=2),
    marker=dict(size=8)
))
fig1.add_vline(x=K_FINAL, line_dash="dash", line_color="red",
               annotation_text=f"K={K_FINAL} (chosen)")
fig1.update_layout(
    title="Elbow Method — Optimal K for K-Means Clustering",
    xaxis_title="Number of Clusters (K)",
    yaxis_title="Inertia (Within-Cluster Sum of Squares)"
)
fig1.write_image("kmeans_elbow.png")
print("Saved: kmeans_elbow.png")


# ── BLOCK 11: CHART 2 — PCA 2D SCATTER ──────────────────────
cluster_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                  "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]

fig2 = go.Figure()
for cluster_id in sorted(df_clean["Cluster"].unique()):
    mask = df_clean["Cluster"] == cluster_id
    name = profile_names.get(cluster_id, f"Cluster {cluster_id}")
    subset = df_clean[mask]
    fig2.add_trace(go.Scatter(
        x=subset["PC1"], y=subset["PC2"],
        mode="markers+text",
        name=f"C{cluster_id}: {name}",
        text=subset["Ticker"],
        textposition="top center",
        textfont=dict(size=8),
        marker=dict(
            color=cluster_colors[cluster_id],
            size=12,
            line=dict(width=1, color="white")
        )
    ))

fig2.update_layout(
    title=f"NSE Nifty Stocks — K-Means Clusters (K={K_FINAL}) via PCA Projection",
    xaxis_title=f"PC1 ({explained[0]:.1%} variance)",
    yaxis_title=f"PC2 ({explained[1]:.1%} variance)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
    height=700
)
fig2.write_image("kmeans_pca_scatter.png")
print("Saved: kmeans_pca_scatter.png")


# ── BLOCK 12: CHART 3 — CLUSTER PROFILE HEATMAP ─────────────
# Normalise profiles (z-score) for heatmap readability
profiles_z = (profiles - profiles.mean()) / profiles.std()

fig3 = go.Figure(data=go.Heatmap(
    z=profiles_z.values,
    x=features,
    y=[f"C{i}: {profile_names[i]}" for i in range(K_FINAL)],
    colorscale="RdYlBu_r",
    text=profiles.values.round(1),
    texttemplate="%{text}",
    textfont=dict(size=12),
    showscale=True,
    colorbar=dict(title="Z-Score")
))
fig3.update_layout(
    title="Cluster Profiles — Mean Fundamental Metrics per Cluster",
    xaxis_title="Feature",
    yaxis_title="Cluster",
    height=400
)
fig3.write_image("kmeans_cluster_profiles.png")
print("Saved: kmeans_cluster_profiles.png")


# ── BLOCK 13: CHART 4 — SILHOUETTE SCORE vs K ───────────────
fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    x=list(K_range), y=silhouettes,
    mode="lines+markers",
    name="Silhouette Score",
    line=dict(color="#2ca02c", width=2),
    marker=dict(size=8)
))
fig4.add_vline(x=K_FINAL, line_dash="dash", line_color="red",
               annotation_text=f"K={K_FINAL}")
fig4.update_layout(
    title="Silhouette Score vs K — Cluster Quality Metric",
    xaxis_title="Number of Clusters (K)",
    yaxis_title="Silhouette Score (higher = better separation)"
)
fig4.write_image("kmeans_silhouette.png")
print("Saved: kmeans_silhouette.png")


# ── BLOCK 14: SAVE CLUSTER ASSIGNMENTS ──────────────────────
output_cols = ["Ticker", "Cluster", "ClusterName"] + features
df_clean[output_cols].to_csv("nse_cluster_assignments.csv", index=False)
print("Saved: nse_cluster_assignments.csv")


# ── BLOCK 15: SUMMARY ───────────────────────────────────────
print("\n=== PROJECT 7 COMPLETE ===")
print(f"Stocks analysed: {len(df_clean)}")
print(f"Features: {features}")
print(f"K chosen: {K_FINAL}")
print(f"Silhouette score at K={K_FINAL}: {silhouettes[K_FINAL-2]:.4f}")
print(f"PCA explained variance: {sum(explained):.1%}")
print(f"\nCluster summary:")
for k, v in profile_names.items():
    count = (df_clean["Cluster"] == k).sum()
    print(f"  {v}: {count} stocks")
