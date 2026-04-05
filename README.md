# 📈 Live Trading Alpha

Systematic trading framework + ML project portfolio — from linear regression to gradient boosting to clustering.

**Live Paper Trading:** Alpaca API ($100k) | **ML Projects:** 7 complete models | **Dashboard:** Streamlit

---

## 🧠 ML Project Portfolio

| # | Project | Model | Key Metric | Folder |
|---|---|---|---|---|
| 1 | [Price Prediction](LinearRegressionNSE/) | Linear Regression + Ridge | R² = 0.007 | `LinearRegressionNSE/` |
| 2 | [Credit Risk](LogisticRegression/) | Logistic Regression | AUC = 0.85 | `LogisticRegression/` |
| 3 | [Trading Signals](DecisionTree/) | Decision Tree | Accuracy ~68% | `DecisionTree/` |
| 4 | [Ensemble Improvement](RandomForest/) | Random Forest (100 trees) | Accuracy ~74% | `RandomForest/` |
| 5 | [Gradient Boosting](XGBoost/) | XGBoost + SHAP + Optuna | Accuracy ~78% | `XGBoost/` |
| 6 | LSTM (coming soon) | LSTM Neural Network | — | — |
| 7 | [Sector Clustering](KMeans/) | K-Means + PCA | 5 clusters | `KMeans/` |

### Model Evolution (P3 → P4 → P5)
```
Decision Tree (68%) → Random Forest (74%) → XGBoost (78%)
       ↑                     ↑                    ↑
   Single tree          Bagging (variance)    Boosting (bias)
   High variance        100 parallel trees    Sequential correction
   Interpretable        OOB validation        SHAP + Optuna
```

Each project includes:
- ✅ Complete Python script with block-by-block code
- ✅ Plotly charts saved as PNGs
- ✅ AI-Augmented Workflow document (`PROJECT*_WORKFLOW.md`)
- ✅ README with quick-run instructions

---

## 📊 Streamlit Dashboard

Interactive dashboard integrating all projects:

```bash
cd StreamlitDashboard
pip install -r requirements.txt
streamlit run app.py
```

Pages: Home · Linear Regression · Credit Risk · Trading Signals · Clustering

---

## 🔴 Live Trading Engine

🟢 **Alpaca Paper Trading: ACTIVE** ($100k allocated)

- Session-aware order routing (market/limit by session type)
- SMA Golden Cross / Death Cross signal (MA20 vs MA50)
- Automated daily execution via cron (9:31 PM IST = 9:31 AM EST)
- P&L journal from actual Alpaca FILL activities

---

## Tech Stack

Python 3.9 · pandas · numpy · scikit-learn · XGBoost · SHAP · Optuna · Plotly · Streamlit · yfinance · Alpaca API

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/live-trading-alpha
cd live-trading-alpha
pip install -r requirements.txt

cp .env.example .env
# Add your Alpaca paper keys to .env
```

---

_7-project ML portfolio demonstrating supervised + unsupervised + ensemble learning on NSE/credit data._
