# Project 7 — K-Means Clustering: NSE Sector Analysis
## AI-Augmented Workflow Document

**Author:** Yash Patil
**Date:** April 2026
**Data:** 50 NSE Nifty stocks via yfinance fundamentals
**Stack:** Python · yfinance · scikit-learn · Plotly · VS Code · GitHub

---

## 1. Project Objective

Group 50 NSE Nifty stocks into clusters based on fundamental metrics.
This is **unsupervised learning** — no labels, no "right answer."
The algorithm discovers natural groupings (Growth, Value, Quality, etc.)
that can inform portfolio construction and sector rotation strategies.

---

## 2. Data

| Property | Value |
|---|---|
| Universe | Nifty 50 constituents |
| Source | yfinance `.info` dictionary per stock |
| Features | PE, PB, ROE, D/E, Revenue Growth |
| Preprocessing | Median imputation, 1/99% outlier capping, StandardScaler |

### Why these 5 features?
| Feature | What it captures | Investment significance |
|---|---|---|
| PE (Price/Earnings) | How much you pay per ₹1 of earnings | Low PE = cheap, High PE = growth expectation |
| PB (Price/Book) | Price relative to net asset value | Low PB = undervalued on assets, High PB = intangibles |
| ROE (Return on Equity) | Profitability: profit / shareholder equity | High ROE = efficient capital use |
| D/E (Debt/Equity) | Leverage: total debt / equity | High D/E = risky, amplified returns |
| Revenue Growth | Year-over-year revenue change | High growth = expanding business |

Together they capture: **valuation + profitability + risk + momentum**.

---

## 3. K-Means Algorithm

### How it works:
1. Choose K (number of clusters)
2. Randomly initialise K centroids in feature space
3. Assign each stock to the nearest centroid (Euclidean distance)
4. Recompute centroids as mean of assigned stocks
5. Repeat steps 3-4 until convergence (assignments stop changing)

### Key properties:
- **Distance-based**: uses Euclidean distance → features MUST be standardised
- **Deterministic given seed**: same random_state = same clusters every time
- **K must be specified**: use Elbow method + Silhouette score to choose
- **Spherical clusters**: assumes clusters are roughly spherical in feature space

### Why StandardScaler is CRITICAL:
PE ranges from 5 to 100. D/E ranges from 0 to 3.
Without scaling, PE would dominate the distance calculation
because its numerical range is ~30× larger than D/E.
StandardScaler normalises each feature to mean=0, std=1.

---

## 4. Choosing K — Elbow Method + Silhouette Score

### Elbow Method
Plot Inertia (within-cluster sum of squares) vs K.
Inertia always decreases as K increases (more clusters = each cluster is smaller).
The "elbow" = point where adding more clusters gives diminishing returns.

### Silhouette Score
For each stock i:
  s(i) = (b(i) - a(i)) / max(a(i), b(i))

Where:
  a(i) = mean distance to other stocks in the same cluster (cohesion)
  b(i) = mean distance to stocks in the nearest other cluster (separation)

Range: -1 to +1
  +1 = perfectly assigned (far from other clusters, close to own cluster)
   0 = on cluster boundary
  -1 = probably in wrong cluster

We chose K=5 as a baseline — Elbow typically shows diminishing returns around K=4-6.

---

## 5. PCA for Visualization

5 features → 5 dimensions → impossible to plot directly.
PCA (Principal Component Analysis) projects data onto the 2 directions of maximum variance.

### How PCA works:
1. Compute covariance matrix of standardised features
2. Find eigenvectors (principal components) and eigenvalues
3. PC1 = direction of maximum variance, PC2 = orthogonal to PC1, maximum remaining variance
4. Project all data onto PC1 and PC2

### Information loss:
If PC1 + PC2 explain 70% of variance: the 2D plot captures most of the structure.
If they explain only 40%: the plot misses important dimensions, clusters may overlap visually
even if they're well separated in the full 5D space.

---

## 6. Cluster Interpretation

Clusters are named based on their mean feature values relative to medians:

| Cluster Type | Characteristics | Investment Implication |
|---|---|---|
| Growth Premium | High PE, High ROE | Expensive but high-quality, momentum stocks |
| Deep Value | Low PE, Low PB | Cheap on fundamentals, potential turnaround plays |
| Quality | High ROE, moderate PE | Efficient businesses at fair price |
| High Leverage | High D/E | Capital-intensive sectors (infra, banks, metals) |
| Moderate | Average across all metrics | Market-average stocks, diversification core |

---

## 7. Charts Produced

### kmeans_elbow.png
Inertia vs K (2 to 10). Red dashed line at K=5.
Look for the "elbow" — where the curve bends from steep to flat.
This tells you: adding more clusters beyond this point doesn't meaningfully improve grouping.

### kmeans_pca_scatter.png
2D scatter of all 50 stocks projected via PCA, coloured by cluster.
Stock tickers annotated on each point.
Key question: do the clusters form visually separable groups?
If clusters overlap: either K is wrong or the features don't separate stocks well.

### kmeans_cluster_profiles.png
Heatmap: rows = clusters, columns = features, values = mean of each feature in each cluster.
Z-score normalised for visual comparison.
Red = above average, Blue = below average.
This is the most important chart for INTERPRETING what each cluster represents.

### kmeans_silhouette.png
Silhouette score vs K. Higher = better cluster quality.
Often peaks at a different K than the Elbow — use both signals together.

---

## 8. AI-Augmented Workflow

| Stage | Human | AI |
|---|---|---|
| Stock universe | Specified Nifty 50 | Fetched Yahoo Finance tickers with .NS suffix |
| Feature selection | Chose PE, PB, ROE, D/E, Revenue Growth | Explained why StandardScaler is mandatory for K-Means |
| K selection | Understood Elbow concept | Built Elbow + Silhouette loop, explained diminishing returns |
| Visualization | Wanted 2D scatter | Implemented PCA projection, explained variance explained |
| Interpretation | Named clusters after inspection | Automated naming logic based on median comparisons |
| Data quality | Assumed clean data | Added median imputation, outlier capping, missing value handling |

---

## 9. Limitations and Next Steps

1. yfinance fundamentals are point-in-time — no historical fundamental data available
2. K=5 is a starting point — Silhouette may suggest a different optimal K
3. K-Means assumes spherical clusters — DBSCAN or Gaussian Mixture would handle irregular shapes
4. No sector labels used — could validate clusters against actual GICS sectors
5. Missing stocks — some tickers may fail to fetch from yfinance
6. Next: Streamlit Dashboard integrating all projects into one interactive app

---

## 10. File Structure

    live-trading-alpha/KMeans/
    |-- Project7_KMeans_NSE_Sectors.py
    |-- kmeans_elbow.png
    |-- kmeans_pca_scatter.png
    |-- kmeans_cluster_profiles.png
    |-- kmeans_silhouette.png
    |-- nse_cluster_assignments.csv
    |-- PROJECT7_WORKFLOW.md              <- this document

---

_Project 7 of the NSE ML series. Unsupervised learning applied to NSE fundamental analysis._
