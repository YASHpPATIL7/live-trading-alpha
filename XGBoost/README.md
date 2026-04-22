# Project 5 — XGBoost: Gradient Boosting Mastery

> Complete model evolution: DT (68%) → RF (74%) → **XGBoost (78%)**.
> SHAP for interpretability. Optuna for hyperparameter tuning.
> **Part 3 of the Model Evolution trilogy** (P3 → P4 → P5).

## The Final Fix: Bias Reduction via Boosting

Random Forest reduced variance. XGBoost goes further — it reduces **bias** by learning from mistakes:

1. **Sequential Learning:** Each new tree corrects the previous tree's errors
2. **Gradient Optimization:** Minimizes loss via gradient descent on tree space
3. **L1/L2 Regularization:** `reg_alpha` + `reg_lambda` prevent overfitting
4. **Optuna Auto-Tuning:** 50 Bayesian trials optimize 7 hyperparameters simultaneously

## Results — Full Model Evolution

| Model | Accuracy | F1-Macro | Key Improvement |
|-------|----------|----------|-----------------|
| Decision Tree (P3) | ~68% | ~0.55 | Baseline (high variance) |
| Random Forest (P4) | ~74% | ~0.62 | Bagging reduces variance |
| **XGBoost (P5)** | **~78%** | **~0.68** | **Boosting reduces bias** |

## SHAP Explainability

SHAP values answer "WHY did the model predict BUY for this day?"

Every prediction is decomposed into per-feature contributions:
- RSI_14 = +0.15 (pushed toward BUY)
- MACD_signal = +0.08 (bullish momentum)
- MA_spread = -0.03 (slight bearish divergence)

This is **critical for compliance** — you can explain every trade to a portfolio manager.

## Optuna Hyperparameter Tuning

50 Bayesian (TPE) trials auto-optimized:
- `max_depth` · `learning_rate` · `n_estimators` · `subsample`
- `colsample_bytree` · `reg_alpha` (L1) · `reg_lambda` (L2)

## Quick Run
```bash
pip install yfinance scikit-learn xgboost shap optuna plotly kaleido matplotlib
python Project5_XGBoost_TradingSignals.py
```

## Outputs
- `xgb_confusion_matrix.png` — XGBoost confusion matrix
- `xgb_shap_beeswarm.png` — SHAP value distribution per feature
- `xgb_shap_bar.png` — Feature importance via mean |SHAP|
- `xgb_optuna_history.png` — 50-trial optimization trajectory
- `xgb_full_comparison.png` — DT vs RF vs XGB comparison chart
- [`PROJECT5_WORKFLOW.md`](PROJECT5_WORKFLOW.md) — AI-augmented workflow
