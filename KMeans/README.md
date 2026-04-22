# Project 7 — K-Means Clustering: NSE Sector Analysis

> Group 50 Nifty stocks into fundamental clusters using unsupervised learning.
> No labels needed — the algorithm discovers natural groupings.

## Why Clustering for Portfolio Management?

Diversification means investing **across** different types of stocks. But how do you define "different"? Sector labels (IT, Banking, Pharma) are arbitrary. K-Means finds **data-driven groupings** based on actual fundamentals.

## Results

| Property | Value |
|----------|-------|
| Stocks Analyzed | 50 Nifty constituents |
| Optimal K | 5 (Elbow + Silhouette validation) |
| PCA Variance | ~60% explained by 2 components |

### Discovered Clusters
| Cluster | Profile | Example Stocks |
|---------|---------|----------------|
| Growth Premium | High PE, high ROE | Asian Paints, Titan |
| Deep Value | Low PE, low PB | ONGC, Coal India |
| Quality | High ROE, low leverage | HDFC, Kotak |
| High Leverage | High D/E ratio | JSW Steel, Tata Steel |
| Moderate | Average on all metrics | Wipro, BPCL |

## Method
1. **Fetch** live fundamental data for 50 stocks (PE, PB, ROE, D/E, Revenue Growth)
2. **StandardScaler** — normalize features (PE is ~20, D/E can be ~100)
3. **Elbow Method** — plot inertia vs K, find the "elbow"
4. **Silhouette Score** — validate cluster quality
5. **PCA** — reduce 5D → 2D for visualization

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python Project7_KMeans_NSE_Sectors.py
```

## Outputs
- `kmeans_elbow.png` — Inertia vs K (elbow method)
- `kmeans_pca_scatter.png` — 2D PCA projection with stock labels
- `kmeans_cluster_profiles.png` — Heatmap of cluster centroids
- `kmeans_silhouette.png` — Silhouette score vs K
- `nse_cluster_assignments.csv` — Full stock → cluster mapping
- [`PROJECT7_WORKFLOW.md`](PROJECT7_WORKFLOW.md) — AI-augmented workflow
