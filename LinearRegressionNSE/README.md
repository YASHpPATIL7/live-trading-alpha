# Project 1 — Linear Regression: RELIANCE NSE Price Prediction

Predict next-day returns for RELIANCE.NS using Linear Regression and Ridge Regression.

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python LinearRegressionNSE_final.py
```

## Key Results
| Metric | Linear Regression | Ridge (α=1000) |
|---|---|---|
| R² | 0.0072 | 0.0048 |
| RMSE | 0.0118 | 0.0118 |

R² = 0.007 is normal for daily stock return prediction — see workflow doc for explanation.

## Outputs
- `actual_vs_predicted.png` — Price tracking chart
- `residual_analysis.png` — 2×2 residual analysis grid
- `predicted_vs_actual_scatter.png` — Return prediction scatter
- `PROJECT1_WORKFLOW.md` — Full AI-augmented workflow document
