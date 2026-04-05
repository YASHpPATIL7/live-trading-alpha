# Project 7 — K-Means Clustering: NSE Sector Analysis

Group 50 NSE Nifty stocks into fundamental clusters using K-Means. Unsupervised learning.

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python Project7_KMeans_NSE_Sectors.py
```

## Key Results
| Property | Value |
|---|---|
| Stocks | 50 Nifty constituents |
| Features | PE, PB, ROE, D/E, Revenue Growth |
| K (clusters) | 5 |
| Method | Elbow + Silhouette validation |

Clusters: Growth Premium · Deep Value · Quality · High Leverage · Moderate

## Outputs
- `kmeans_elbow.png` — Elbow method curve
- `kmeans_pca_scatter.png` — PCA 2D scatter with stock labels
- `kmeans_cluster_profiles.png` — Cluster profile heatmap
- `kmeans_silhouette.png` — Silhouette score vs K
- `nse_cluster_assignments.csv` — Full cluster assignments
- `PROJECT7_WORKFLOW.md` — Full AI-augmented workflow document
