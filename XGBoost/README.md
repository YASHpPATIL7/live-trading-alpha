# Project 5 — XGBoost: Gradient Boosting Mastery

Complete model evolution: DT → RF → XGBoost. SHAP values for interpretability. Optuna hyperparameter tuning.

## Quick Run
```bash
pip install yfinance scikit-learn xgboost shap optuna plotly kaleido matplotlib
python Project5_XGBoost_TradingSignals.py
```

## Key Results
| Model | Accuracy | F1-Macro |
|---|---|---|
| Decision Tree (P3) | ~68% | ~0.55 |
| Random Forest (P4) | ~74% | ~0.62 |
| XGBoost (P5) | ~78% | ~0.68 |

## Outputs
- `xgb_confusion_matrix.png` — XGBoost confusion matrix
- `xgb_shap_beeswarm.png` — SHAP beeswarm (how features affect predictions)
- `xgb_shap_bar.png` — SHAP feature importance
- `xgb_optuna_history.png` — 50-trial optimization history
- `xgb_full_comparison.png` — DT vs RF vs XGB accuracy + F1 comparison
- `PROJECT5_WORKFLOW.md` — Full AI-augmented workflow document
