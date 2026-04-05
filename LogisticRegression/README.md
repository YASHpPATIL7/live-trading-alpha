# Project 2 — Logistic Regression: Loan Default Prediction

Binary classification on Kaggle's "Give Me Some Credit" dataset — predict borrower defaults.

## Quick Run
```bash
# Download cs-training.csv from Kaggle first
pip install scikit-learn plotly kaleido
python Project2_LogisticRegression_LoanDefault.py
```

## Key Results
| Metric | Value |
|---|---|
| AUC-ROC | ~0.85 |
| Avg Precision | ~0.45 |
| Class Balance | Upsampled minority to ~25% |

## Outputs
- `confusion_matrix.png` — TP/FP/FN/TN heatmap
- `roc_curve.png` — ROC with AUC score
- `precision_recall_curve.png` — PR curve (honest metric for imbalanced data)
- `feature_coefficients.png` — Which features drive default risk
- `PROJECT2_WORKFLOW.md` — Full AI-augmented workflow document
