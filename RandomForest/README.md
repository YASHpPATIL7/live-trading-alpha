# Project 4 — Random Forest: Ensemble Improvement on Trading Signals

Same RELIANCE.NS trading signal problem as P3, now with Random Forest (100 trees). Direct DT vs RF comparison.

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python Project4_RandomForest_TradingSignals.py
```

## Key Results
| Metric | Decision Tree | Random Forest |
|---|---|---|
| Accuracy | ~68% | ~74% |
| Improvement | — | +6% via ensemble |
| OOB Score | N/A | ~0.70 |

**WHY RF beats DT:** Bagging reduces variance; random feature subsets decorrelate trees; ensemble averaging smooths out overfitting.

## Outputs
- `rf_confusion_matrix.png` — RF confusion matrix
- `rf_feature_importance_comparison.png` — DT vs RF feature importance
- `rf_oob_error_curve.png` — OOB error vs number of trees
- `rf_dt_vs_rf_accuracy.png` — Accuracy comparison bar chart
- `PROJECT4_WORKFLOW.md` — Full AI-augmented workflow document
