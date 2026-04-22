# Project 4 — Random Forest: Ensemble Improvement

> Same trading signal problem as P3 — now with Random Forest (100 trees).
> **Part 2 of the Model Evolution trilogy** (P3 → P4 → P5).

## The Fix: Variance Reduction via Bagging

Decision Tree overfit (68%). Random Forest fixes this by:

1. **Bootstrap Aggregating (Bagging):** Each tree sees a random 63% of training data
2. **Feature Randomization:** Each split considers random subset of features
3. **Majority Vote:** 100 trees vote → noise cancels out → variance drops

## Results

| Metric | Decision Tree (P3) | Random Forest (P4) |
|--------|--------------------|--------------------|
| Accuracy | ~68% | **~74% (+6%)** |
| OOB Score | N/A | ~0.70 |
| Variance | HIGH | LOW (thanks to bagging) |

## Why +6% Matters

In algorithmic trading, **6% directional improvement compounds**. Over 252 trading days, a 74% directional model captures significantly more alpha than a 68% model.

## Out-of-Bag (OOB) Validation

Each tree never sees ~37% of the data (the bootstrap "out-of-bag" samples). RF uses these for internal validation — no separate dev set needed. OOB score ≈ 0.70 confirms generalization.

## Quick Run
```bash
pip install yfinance scikit-learn plotly kaleido
python Project4_RandomForest_TradingSignals.py
```

## Outputs
- `rf_confusion_matrix.png` — RF confusion matrix
- `rf_feature_importance_comparison.png` — DT vs RF feature importance
- `rf_oob_error_curve.png` — OOB error vs number of trees
- `rf_dt_vs_rf_accuracy.png` — Side-by-side accuracy comparison
- [`PROJECT4_WORKFLOW.md`](PROJECT4_WORKFLOW.md) — AI-augmented workflow
