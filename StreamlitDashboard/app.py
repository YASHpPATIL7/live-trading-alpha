import streamlit as st

st.set_page_config(
    page_title="Live Trading Alpha — ML Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
# 📈 Live Trading Alpha — ML Dashboard

**7-Project Machine Learning Portfolio** for quantitative finance.

---

### 🧠 Model Evolution

| # | Project | Model | Key Metric |
|---|---|---|---|
| 1 | Price Prediction | Linear Regression + Ridge | R² = 0.007 |
| 2 | Credit Risk | Logistic Regression | AUC ≈ 0.85 |
| 3 | Trading Signals | Decision Tree | Accuracy ~68% |
| 4 | Ensemble Improvement | Random Forest (100 trees) | Accuracy ~74% |
| 5 | Gradient Boosting | XGBoost + SHAP + Optuna | Accuracy ~78% |
| 6 | Time Series | LSTM *(coming soon)* | — |
| 7 | Sector Clustering | K-Means + PCA | 5 clusters |

---

### ⚡ Quick Navigation

Use the **sidebar** to navigate between project pages.

Each page runs the model **live** and displays interactive charts.

---

**Tech Stack:** Python · scikit-learn · XGBoost · SHAP · Optuna · Plotly · Streamlit · yfinance

*Built by Yash Patil — April 2026*
""")
