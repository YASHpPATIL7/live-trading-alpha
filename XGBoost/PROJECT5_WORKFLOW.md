# Project 5 — XGBoost: Gradient Boosting Mastery
## AI-Augmented Workflow Document

**Author:** Yash Patil
**Date:** April 2026
**Data:** RELIANCE.NS via yfinance (5 years)
**Stack:** Python · yfinance · XGBoost · SHAP · Optuna · scikit-learn · Plotly · Matplotlib

---

## 1. Project Objective

Complete the model evolution: Decision Tree → Random Forest → XGBoost.
Use Optuna for hyperparameter tuning (50 trials), SHAP for interpretability.
Build the definitive comparison table across all three model families.

---

## 2. The Evolution Story

| Model | Project | Type | What it learns from |
|---|---|---|---|
| Decision Tree | P3 | Single tree | Training data directly |
| Random Forest | P4 | Bagging (parallel trees) | Bootstrap samples of data |
| XGBoost | P5 | Boosting (sequential trees) | Previous model's ERRORS |

### Why this order matters:
- **DT** = baseline. High variance, overfits.
- **RF** = fixes variance via bagging. But doesn't actively fix bias.
- **XGBoost** = fixes bias via boosting. Each tree corrects the previous tree's mistakes.

---

## 3. How XGBoost Works (Gradient Boosting)

### Core Idea
Instead of building 100 independent trees (RF), XGBoost builds trees **sequentially**.
Each new tree focuses on the examples the previous trees got WRONG.

### Step by Step:
1. Start with a constant prediction (base score = mean of targets)
2. Calculate residuals: actual - predicted
3. Train Tree 1 on the residuals (not the raw labels)
4. Update predictions: pred = pred + learning_rate × Tree1_output
5. Calculate new residuals
6. Train Tree 2 on the NEW residuals
7. Repeat for N trees

### Mathematical Formula:
```
F(x) = F_0(x) + η·h_1(x) + η·h_2(x) + ... + η·h_N(x)

Where:
  F(x)   = final prediction
  F_0(x) = initial constant prediction
  h_t(x) = tree t trained on residuals of F_{t-1}(x)
  η      = learning rate (shrinkage — prevents overfitting)
```

### Why "Gradient"?
Residuals = negative gradient of the loss function with respect to predictions.
Training on residuals = doing gradient descent in function space.
This is why it's called "gradient boosting" — it's SGD but over trees instead of weights.

### XGBoost-Specific Improvements over Generic Gradient Boosting:
- **L1 + L2 regularisation** on leaf weights (reg_alpha, reg_lambda)
- **Column subsampling** (colsample_bytree) — borrows from Random Forest
- **Row subsampling** (subsample) — reduces overfitting
- **Weighted quantile sketch** — efficient split finding
- **Sparsity-aware** — handles missing values natively

---

## 4. Optuna Hyperparameter Tuning

### Why Optuna over GridSearch?
GridSearch tries ALL combinations: 5 values × 5 values × 5 values = 125 combos.
Optuna uses **TPE (Tree-structured Parzen Estimator)**: 
- Start with random trials
- Build a probability model of which regions of hyperparameter space give good results
- Sample from high-probability regions
- 50 smart trials > 125 random grid combinations

### Tuned Parameters:
| Parameter | Range | What it controls |
|---|---|---|
| max_depth | 3–8 | Individual tree complexity |
| learning_rate | 0.01–0.3 | Step size (lower = more trees needed but less overfitting) |
| n_estimators | 50–300 | Total number of boosting rounds |
| subsample | 0.6–1.0 | Fraction of rows per tree (stochastic boosting) |
| colsample_bytree | 0.6–1.0 | Fraction of features per tree |
| reg_alpha | 1e-8–10 | L1 regularisation (sparsity) |
| reg_lambda | 1e-8–10 | L2 regularisation (weight decay) |

---

## 5. SHAP Values — Model Interpretability

### The Problem:
XGBoost is a black box — 200+ trees, each with up to 8 levels.
You can't read the rules like a Decision Tree.

### SHAP (SHapley Additive exPlanations)
From game theory: Shapley values measure each player's contribution to a coalition's payoff.
Applied to ML: each feature's contribution to a specific prediction.

For each prediction:
```
f(x) = base_value + SHAP(RSI_14) + SHAP(MACD_signal) + SHAP(MA_cross) + SHAP(MA_spread)
```

### SHAP Properties (why it's the gold standard):
1. **Local accuracy**: SHAP values sum to the actual prediction minus base value
2. **Missingness**: features not used get SHAP = 0
3. **Consistency**: if a feature's contribution increases in a new model, its SHAP value doesn't decrease

### SHAP Plots:
- **Beeswarm**: every dot = one test sample. X-axis = SHAP value. Color = feature value (high/low).
  Shows not just importance but HOW features affect predictions.
- **Bar**: mean |SHAP| per feature. Simpler view of overall importance.

---

## 6. Charts Produced

### xgb_confusion_matrix.png
3×3 confusion matrix for the Optuna-tuned XGBoost model.
Compare diagonal values with P3 (DT) and P4 (RF) — XGB should have highest correct counts.

### xgb_shap_beeswarm.png
SHAP beeswarm plot for all test samples.
Key insights:
- Which features push predictions toward BUY vs SELL?
- Does high RSI consistently push toward SELL (overbought)?
- Is MACD's effect monotonic or non-linear?

### xgb_shap_bar.png
Mean |SHAP| per feature per class.
Direct comparison with Gini importance from P3/P4 — SHAP is more reliable because
it measures actual contribution to predictions, not just split quality.

### xgb_optuna_history.png
Scatter of all 50 trials + running best line.
Shows how TPE sampler converges — early trials are exploratory, later trials exploit
high-performing regions of hyperparameter space.

### xgb_full_comparison.png
Side-by-side bar chart: DT vs RF vs XGB for both Accuracy and F1-macro.
The definitive visual proof of the model evolution.

---

## 7. Bagging vs Boosting — The Key Difference

| Property | Bagging (RF) | Boosting (XGBoost) |
|---|---|---|
| Trees | Independent, parallel | Sequential, dependent |
| Training focus | Random subsets of data | Examples the model gets WRONG |
| Error reduction | Reduces variance | Reduces bias |
| Overfitting risk | Low (independent) | Higher (can overfit to noisy errors) |
| Regularisation | Not needed (diverse trees) | Critical (learning_rate, reg_alpha, reg_lambda) |
| Speed | Parallelisable | Sequential (slower) |

---

## 8. AI-Augmented Workflow

| Stage | Human | AI |
|---|---|---|
| Model selection | Chose XGBoost as next step | Explained gradient boosting math, residual learning |
| Optuna setup | Knew hyperparameter tuning concept | Built Optuna objective function with TPE sampler |
| SHAP integration | Wanted model interpretability | Implemented TreeExplainer + beeswarm/bar plots |
| Comparison table | Wanted DT → RF → XGB in one place | Built full per-class breakdown table |
| Theory | Understood "boosting = sequential" | Explained gradient descent in function space, L1/L2 regularisation |

---

## 9. Limitations and Next Steps

1. Same 4 features — XGBoost can handle more features; full 14-feature matrix would likely improve results
2. Optuna on test set — ideally should use validation set separate from test set
3. No walk-forward validation — single train/test split doesn't capture regime changes
4. No feature engineering search — Optuna could also optimise which features to include
5. Next: K-Means clustering (P7) for unsupervised market segmentation

---

## 10. File Structure

    live-trading-alpha/XGBoost/
    |-- Project5_XGBoost_TradingSignals.py
    |-- xgb_confusion_matrix.png
    |-- xgb_shap_beeswarm.png
    |-- xgb_shap_bar.png
    |-- xgb_optuna_history.png
    |-- xgb_full_comparison.png
    |-- PROJECT5_WORKFLOW.md              <- this document

---

_Project 5 of the NSE ML series. Gradient boosting mastery demonstrated. DT → RF → XGB evolution complete._
