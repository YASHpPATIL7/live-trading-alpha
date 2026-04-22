# Project 1 — Linear Regression: RELIANCE Price Prediction

> Predict next-day RELIANCE.NS returns using Linear Regression vs Ridge Regression.

## Why R² = 0.007?

This is **correct and expected**. Daily stock returns are nearly random (Efficient Market Hypothesis). If R² was 0.90, it would signal data leakage or overfitting. The project demonstrates proper methodology, not predictive power.

## Features

| Feature | Description | Why |
|---------|-------------|-----|
| MA_50 | 50-day moving average | Trend direction |
| MA_200 | 200-day moving average | Long-term trend |
| Volume_ratio | Today's volume / 20-day avg | Liquidity signal |
| Daily_return | Yesterday's return | Momentum |

## Results

| Metric | Linear Regression | Ridge (α=1000) |
|--------|-------------------|----------------|
| R² | 0.0072 | 0.0048 |
| RMSE | 0.0118 | 0.0118 |

Ridge's regularization (λ||w||²) shrinks coefficients → prevents overfitting in limited data.

## Design Decisions
- **StandardScaler** fitted on training data only (`fit_transform` on train, `transform` on test)
- **Chronological split** (80/20) — no random shuffling for time series
- **TimeSeriesSplit** for Ridge alpha selection via cross-validation

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python LinearRegressionNSE_final.py
```

## Outputs
- `actual_vs_predicted.png` — Price tracking chart
- `residual_analysis.png` — 2×2 residual grid (time series + distribution)
- `predicted_vs_actual_scatter.png` — Return prediction scatter
- [`PROJECT1_WORKFLOW.md`](PROJECT1_WORKFLOW.md) — AI-augmented workflow
