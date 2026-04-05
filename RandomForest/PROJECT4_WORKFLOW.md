# Project 4 — Random Forest: Ensemble Improvement on Trading Signals
## AI-Augmented Workflow Document

**Author:** Yash Patil
**Date:** April 2026
**Data:** RELIANCE.NS via yfinance (5 years)
**Stack:** Python · yfinance · scikit-learn · Plotly · VS Code · GitHub

---

## 1. Project Objective

Improve on Project 3's Decision Tree trading signals by using a Random Forest ensemble.
Same dataset, same features, same labels — direct comparison to isolate the effect of
ensemble learning. Target: DT ~68% → RF ~74% accuracy.

---

## 2. Data

| Property | Value |
|---|---|
| Ticker | RELIANCE.NS |
| Period | 5 years |
| Split | 80% train, 20% test (chronological — no shuffle) |
| Target | 5-day forward return threshold labels (BUY/HOLD/SELL) |
| Features | RSI_14, MACD_signal, MA_cross, MA_spread |

Identical to Project 3 — allows direct apples-to-apples comparison.

---

## 3. Why Random Forest?

### The Problem with a Single Decision Tree
A single Decision Tree has **high variance**: train it on slightly different data and you get
a completely different tree. It memorises training noise. This is why P3's DT plateaus
around 68% — it overfits to training patterns that don't generalise.

### How Random Forest Fixes This
Random Forest = **Bagging** (Bootstrap Aggregating) + **Random Feature Selection**

1. **Bagging**: Create 100 bootstrap samples (random subsets with replacement) of the training data.
   Train one tree per sample. Average their predictions → variance drops.

2. **Random Feature Selection**: At each split, each tree only considers a random subset of features
   (default: √4 = 2 features). This **decorrelates** the trees — if RSI_14 is always the best
   first split, every tree would be similar. Random subsets force different trees to find
   different patterns.

3. **Ensemble Averaging**: Final prediction = majority vote across all 100 trees.
   Individual trees overfit to different noise → their errors cancel out when averaged.

**Mathematical intuition:**
- Single tree variance: σ²
- Average of n independent trees: σ²/n
- Average of n correlated trees (ρ = correlation): ρσ² + (1-ρ)σ²/n
- Random feature selection reduces ρ → lower ensemble variance

---

## 4. Hyperparameters

| Parameter | Value | Why |
|---|---|---|
| n_estimators | 100 | Standard starting point — OOB curve shows diminishing returns after ~80 |
| max_depth | 5 | Same as P3 — controls individual tree complexity |
| min_samples_leaf | 20 | Same as P3 — prevents one-sample leaves |
| class_weight | balanced | Same as P3 — prevents HOLD from dominating |
| oob_score | True | Enables out-of-bag error estimation (free validation) |
| random_state | 42 | Reproducibility |
| n_jobs | -1 | Use all CPU cores — trees train independently |

---

## 5. Out-of-Bag (OOB) Score — Free Validation

Each bootstrap sample uses ~63% of training rows (the rest are "out-of-bag").
For each training sample, ~37 trees never saw it during training.
Those trees predict that sample → OOB prediction.

OOB score ≈ cross-validation accuracy, but:
- No need to set aside a validation set
- Computed automatically during training
- Gives an unbiased estimate of generalisation error

OOB error curve shows how error decreases as trees increase:
- 10 trees: high OOB error (high variance, not enough averaging)
- 50 trees: error stabilises
- 100+ trees: diminishing returns (more compute, minimal improvement)

---

## 6. Charts Produced

### rf_confusion_matrix.png
3×3 confusion matrix for Random Forest predictions.
Compare with P3's DT confusion matrix — RF should have higher diagonal values
(more correct predictions) and lower off-diagonal values (fewer misclassifications).

### rf_feature_importance_comparison.png
Grouped bar chart: DT importance vs RF importance for each feature.
Key insight: RF importance is **smoother** and **more distributed** across features.
DT might assign 70% importance to one feature; RF spreads it out because different
trees use different features at the root.

### rf_oob_error_curve.png
OOB error rate vs number of trees (10 to 200).
Shows the ensemble effect visually — error drops steeply at first, then plateaus.
This is the most important chart for understanding WHY ensembles work.

### rf_dt_vs_rf_accuracy.png
Simple bar chart: DT accuracy vs RF accuracy on the same test set.
The visual proof of ensemble improvement.

---

## 7. DT vs RF — Why RF Wins

| Property | Decision Tree | Random Forest |
|---|---|---|
| Model type | Single tree | 100 trees averaged |
| Variance | HIGH — changes with data | LOW — bagging smooths it |
| Bias | Low (can fit complex patterns) | Low (same) |
| Overfitting | Prone | Resistant |
| Feature importance | Noisy (one tree's opinion) | Stable (averaged across 100 trees) |
| Interpretability | High (one set of rules) | Medium (100 sets of rules → black-box-ish) |
| Training speed | Fast | Slower (100× more trees) |

The key tradeoff: RF sacrifices interpretability for accuracy.
In P3, you could read every decision rule. In RF, you get better accuracy
but can't inspect individual rules as easily.

---

## 8. AI-Augmented Workflow

| Stage | Human | AI |
|---|---|---|
| Project design | Wanted to improve P3's accuracy | Suggested same data/features for direct comparison |
| RF hyperparameters | Knew n_estimators=100 | Explained why max_depth stays at 5, added oob_score=True |
| OOB analysis | Understood concept | Built OOB error curve loop across 10→200 trees |
| Comparison charts | Wanted DT vs RF bar chart | Added grouped feature importance comparison |
| Theory | Knew "more trees = better" | Explained bagging, decorrelation, variance reduction formula |

---

## 9. Limitations and Next Steps

1. RF reduces variance but doesn't reduce **bias** — if features are fundamentally weak, more trees won't help
2. RF is a **bagging** method — next step is **boosting** (XGBoost) which reduces bias
3. No hyperparameter tuning — Optuna tuning in P5 will optimise all parameters
4. Feature set is still limited — same 4 indicators, no volume, no sentiment
5. Next: XGBoost → expect accuracy to reach ~78% with SHAP for interpretability

---

## 10. File Structure

    live-trading-alpha/RandomForest/
    |-- Project4_RandomForest_TradingSignals.py
    |-- rf_confusion_matrix.png
    |-- rf_feature_importance_comparison.png
    |-- rf_oob_error_curve.png
    |-- rf_dt_vs_rf_accuracy.png
    |-- PROJECT4_WORKFLOW.md              <- this document

---

_Project 4 of the NSE ML series. Ensemble improvement demonstrated: DT → RF._
