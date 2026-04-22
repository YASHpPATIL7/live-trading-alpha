# Project 2 — Logistic Regression: Loan Default Prediction

> Binary classification: Will this borrower default? (Yes/No)
> Dataset: Kaggle "Give Me Some Credit" — 150K borrowers.

## Why This Matters for Quant Finance

Banks and AMCs manage credit risk daily. HDFC AMC's debt mutual funds need default scoring. Understanding logistic regression for credit risk = understanding the foundation of fixed income analytics.

## Results

| Metric | Value |
|--------|-------|
| AUC-ROC | ~0.85 |
| Avg Precision | ~0.45 |
| Default Rate | ~7% (imbalanced) |

AUC = 0.85 means the model correctly ranks 85% of defaulter/non-defaulter pairs.

## Key Design Decisions
- **Class imbalance handling:** Upsampled minority class to ~25% (defaults are rare in real life)
- **L2 regularization:** Prevents overfitting to noise in high-dimensional credit data
- **Precision/Recall > Accuracy:** When defaults are 7%, predicting "no default" always gives 93% accuracy — useless. PR curve is the honest metric.

## Features
`debt_to_income` · `late_payments` · `revolving_utilization` · `age_bracket` · `num_dependents`

## Quick Run
```bash
# Download cs-training.csv from Kaggle first
pip install scikit-learn plotly kaleido
python Project2_LogisticRegression_LoanDefault.py
```

## Outputs
- `confusion_matrix.png` — TP/FP/FN/TN heatmap
- `roc_curve.png` — ROC with AUC score
- `precision_recall_curve.png` — PR curve (honest metric for imbalanced data)
- `feature_coefficients.png` — Which features drive default risk
- [`PROJECT2_WORKFLOW.md`](PROJECT2_WORKFLOW.md) — AI-augmented workflow
