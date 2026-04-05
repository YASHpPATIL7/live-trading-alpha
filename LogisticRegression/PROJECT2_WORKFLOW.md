# Project 2 — Logistic Regression: Loan Default Prediction
## AI-Augmented Workflow Document

**Author:** Yash Patil
**Date:** April 2026
**Dataset:** Kaggle — Give Me Some Credit
**Stack:** Python · scikit-learn · Plotly · VS Code · GitHub

---

## 1. Project Objective

Predict whether a borrower will default on a loan within 2 years.
Binary classification: 1 = defaulted, 0 = no default.
Output actionable metrics (AUC, Precision, Recall, F1) that a credit risk
team would actually use — not just accuracy.

---

## 2. Dataset

| Property | Value |
|---|---|
| Source | Kaggle: Give Me Some Credit |
| File | cs-training.csv |
| Raw rows | ~150,000 borrowers |
| Target | SeriousDlqin2yrs (1 = defaulted within 2 years) |
| Default rate | ~6.7% (heavily imbalanced) |

---

## 3. Features Used

| Feature | Description | Why it matters |
|---|---|---|
| DTI | Debt-to-Income ratio | Core creditworthiness metric — high DTI = stretched borrower |
| Age | Borrower age in years | Older borrowers historically have lower default rates |
| Late_30_59 | Times 30-59 days past due | Recent stress signal — recent = more predictive |
| Late_60_89 | Times 60-89 days past due | Serious delinquency warning |
| Late_90 | Times 90+ days past due | Most severe delinquency — strongest default predictor |
| Revolving_util | Credit card utilisation rate | >90% = maxed out = distressed |
| Monthly_income | Monthly income in USD | Low income = limited buffer for shocks |
| Open_credit_lines | Number of open credit accounts | Too many = credit-seeking behaviour |

---

## 4. Data Preprocessing

### Outlier Capping (99th percentile)
Revolving_util, DTI, and Monthly_income had extreme outliers
(some borrowers with DTI = 3000, util = 40000).
Clipped at 99th percentile to prevent linear model from being
dominated by single outlier values.

### Class Imbalance — Upsampling
Default rate is ~6.7%. Without correction:
  - Model predicts "No Default" for everyone
  - Gets 93.3% accuracy but catches ZERO defaults
  - Useless for credit risk

Fix: Upsample minority class (defaults) to ~25% of dataset.
Used sklearn resample with replacement on training data only.
Test set kept at natural ratio (never oversample test data).

---

## 5. Model: Logistic Regression

Logistic Regression is the industry standard for credit scoring.
Used globally in FICO scores, bank scorecard models, and Basel III models.
Outputs a probability (0-1) rather than a hard 0/1 label.

Formula:
  P(default) = 1 / (1 + e^(-z))
  where z = w1*DTI + w2*Age + w3*Late_30_59 + ... + b

Threshold default: 0.5 (predicted probability > 0.5 = flag as default)
class_weight="balanced" adds further penalty for missing actual defaults.

---

## 6. Output Metrics — Why Each One Matters

| Metric | Formula | Why it matters in credit risk |
|---|---|---|
| AUC-ROC | Area under ROC curve | Measures ranking quality — can model separate defaults from non-defaults? |
| Precision | TP / (TP + FP) | Of all flagged defaults, how many were real? (cost of false alarms) |
| Recall | TP / (TP + FN) | Of all actual defaults, how many did we catch? (cost of missed defaults) |
| F1 Score | 2 * P*R / (P+R) | Harmonic mean — balance of precision and recall |

In credit risk, Recall matters more than Precision.
Missing a real defaulter (FN) costs the bank the loan principal.
False alarm (FP) only costs the customer a rejected application.

---

## 7. Charts Produced

### confusion_matrix.png
What it shows: 2x2 grid of predicted vs actual labels.
  TN (top-left):  correctly cleared as no default
  FP (top-right): flagged as default but actually fine
  FN (bottom-left): missed defaults — the dangerous number
  TP (bottom-right): correctly caught defaults

What to look for: FN should be as low as possible in a credit model.

### roc_curve.png
What it shows: True Positive Rate vs False Positive Rate at every threshold.
The red dashed line = random classifier (AUC = 0.50).
A perfect model would be a right angle in the top-left corner (AUC = 1.0).
Our model's curve bowing toward the top-left = better than random.

AUC interpretation:
  0.50 = no better than coin flip
  0.70 = acceptable
  0.80 = good
  0.90+ = excellent (rare for credit data)

### precision_recall_curve.png
What it shows: Precision vs Recall as the classification threshold changes.
The red dashed baseline = what a random classifier achieves.
A good model has a curve far above the baseline.

Why this matters more than ROC for imbalanced data:
ROC can look good even when the model performs poorly on the minority class.
Precision-Recall curve focuses only on the positive class (defaults).
It is the honest metric for imbalanced classification.

### feature_coefficients.png
What it shows: Logistic regression coefficient for each feature.
Red bars = positive coefficient = increases default probability.
Blue bars = negative coefficient = decreases default probability.

Expected: Late_90, Late_60_89 should have largest red bars.
Age should have largest blue bar (older = lower risk).

---

## 8. AI-Augmented Workflow

| Stage | Human | AI |
|---|---|---|
| Dataset selection | Chose Kaggle Give Me Some Credit | Explained column names, confirmed DTI interpretation |
| Imbalance handling | Identified class imbalance from default rate | Recommended upsampling only training data, never test |
| Feature selection | Specified DTI, age, late payments | Added Revolving_util, Monthly_income for stronger signal |
| Metric selection | Knew AUC and confusion matrix | Explained why recall > precision for credit risk |
| Code | Ran and verified output | Wrote complete syntax-verified script |

---

## 9. Limitations and Next Steps

1. Logistic Regression assumes linear decision boundary — misses interaction effects
2. DTI alone is weak — needs income stability, job type, loan amount
3. No time-series structure — loan defaults have vintage effects (origination year matters)
4. Next: XGBoost on same dataset — expect AUC improvement to 0.85+
5. Add threshold optimisation — find the threshold that maximises F1 or minimises FN

---

## 10. File Structure

    live-trading-alpha/
    |-- Project2_LogisticRegression_LoanDefault.py
    |-- cs-training.csv                   <- download from Kaggle
    |-- confusion_matrix.png
    |-- roc_curve.png
    |-- precision_recall_curve.png
    |-- feature_coefficients.png
    |-- PROJECT2_WORKFLOW.md              <- this document

---

_Project 2 of the NSE ML series. Credit risk baseline established._
