# Project 3 — Decision Tree: Stock Trading Signal Classification

Generate BUY/HOLD/SELL trading signals for RELIANCE.NS using a Decision Tree classifier on technical indicators.

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python Project3_DecisionTree_TradingSignals.py
```

## Key Results
| Metric | Value |
|---|---|
| Accuracy | ~68% |
| Model | DecisionTreeClassifier (depth=5) |
| Features | RSI_14, MACD_signal, MA_cross, MA_spread |

## Outputs
- `dt_confusion_matrix.png` — 3×3 BUY/HOLD/SELL confusion matrix
- `dt_feature_importance.png` — Gini importance bar chart
- `dt_signals_over_time.png` — Predicted signals scatter
- `dt_rsi_vs_macd.png` — 2D feature space visualization
- `PROJECT3_WORKFLOW.md` — Full AI-augmented workflow document
