# Project 3 — Decision Tree: Stock Trading Signal Classification

> Generate BUY/HOLD/SELL signals for RELIANCE.NS using technical indicators.
> This is **Part 1 of the Model Evolution trilogy** (P3 → P4 → P5).

## The Problem

Given today's technicals (RSI, MACD, MA crossover), what should you do?
- **BUY:** 5-day forward return > +0.5%
- **SELL:** 5-day forward return < -0.5%
- **HOLD:** Everything in between

## Results

| Metric | Value |
|--------|-------|
| Accuracy | ~68% |
| Max Depth | 5 |
| Top Feature | RSI_14 (Gini importance) |

## Why Decision Trees?
- **Interpretable:** You can read the exact rules (`if RSI > 70 AND MACD < 0 → SELL`)
- **Weakness → HIGH VARIANCE:** Small data changes → completely different tree
- **This is why P4 (Random Forest) exists** — it fixes variance via ensemble averaging

## Features
| Feature | Description |
|---------|-------------|
| RSI_14 | Relative Strength Index (momentum oscillator) |
| MACD_signal | MACD histogram (trend strength) |
| MA_cross | Binary: is MA_50 > MA_200? (Golden Cross) |
| MA_spread | % distance between MA_50 and MA_200 |

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python Project3_DecisionTree_TradingSignals.py
```

## Outputs
- `dt_confusion_matrix.png` — 3×3 BUY/HOLD/SELL confusion matrix
- `dt_feature_importance.png` — Gini importance bar chart
- `dt_signals_over_time.png` — Predicted signals scatter
- `dt_rsi_vs_macd.png` — 2D feature space visualization
- [`PROJECT3_WORKFLOW.md`](PROJECT3_WORKFLOW.md) — AI-augmented workflow
