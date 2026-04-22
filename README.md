# 📈 Live Trading Alpha

**90-day live paper trading system** + **7-project ML portfolio** for quantitative finance.

Systematic trading engine running on Alpaca ($100K paper), with ML models from linear regression to LSTM neural networks — all trained on Indian (NSE) and US market data.

[![Live Trading](https://img.shields.io/badge/Alpaca-LIVE_PAPER_TRADING-00C805?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyYTEwIDEwIDAgMSAwIDAgMjAgMTAgMTAgMCAwIDAgMC0yMHoiLz48L3N2Zz4=)](https://alpaca.markets)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-LSTM-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org)

---

## 🧠 ML Project Portfolio

7 projects demonstrating progressive ML mastery — from linear models to deep learning:

| # | Project | Model | Data | Key Metric | Theory |
|---|---------|-------|------|------------|--------|
| 1 | [Price Prediction](LinearRegressionNSE/) | Linear + Ridge Regression | RELIANCE.NS 5yr | R² = 0.007 | Andrew Ng C1 W1-3 |
| 2 | [Credit Risk](LogisticRegression/) | Logistic Regression | Kaggle 150K loans | AUC = 0.85 | Andrew Ng C1 W3 |
| 3 | [Trading Signals](DecisionTree/) | Decision Tree (depth=5) | RELIANCE.NS technicals | Acc ~68% | Andrew Ng C2 W3 |
| 4 | [Ensemble](RandomForest/) | Random Forest (100 trees) | Same as P3 | Acc ~74% | Andrew Ng C2 W3 |
| 5 | [Gradient Boosting](XGBoost/) | XGBoost + SHAP + Optuna | Same as P3 | Acc ~78% | Andrew Ng C2 W3 |
| 6 | [LSTM Forecaster](LSTMForecaster/) | LSTM Neural Network | Nifty 50 10yr | Dir Acc 52.3% | Andrew Ng C5 W1 |
| 7 | [Sector Clustering](KMeans/) | K-Means + PCA | 50 Nifty stocks | 5 clusters | Andrew Ng C3 W1 |

### Model Evolution Story (P3 → P4 → P5)

The same trading signal problem solved three ways — each model fixes the previous one's weakness:

```
Decision Tree (68%)  ──→  Random Forest (74%)  ──→  XGBoost (78%)
       ↑                         ↑                        ↑
  Single tree              100 parallel trees       Sequential correction
  HIGH VARIANCE            Bagging reduces it       Boosting reduces BIAS
  Overfits to noise        OOB validation           SHAP explains WHY
                                                    Optuna auto-tunes
```

> **Interview pitch:** "I deliberately built all three on identical data to demonstrate why ensemble methods outperform single learners. SHAP values revealed RSI_14 as the dominant feature — consistent with momentum factor literature."

---

## 🔴 Live Trading Engine

**🟢 ACTIVE** — Alpaca paper trading ($100K) since March 10, 2026

| Component | Detail |
|-----------|--------|
| **Strategy** | Dual-timeframe SMA crossover (MA20/MA50) with price-override |
| **Signal Logic** | Golden Cross = BULLISH, Death Cross = BEARISH |
| **Regime Filter** | Bull/Bear regime detection via MA spread |
| **Execution** | Automated daily via cron (9:31 PM IST = 9:31 AM EST) |
| **Journal** | Auto-generated P&L journal from Alpaca fill data |
| **Benchmark** | SPY buy-and-hold comparison with alpha tracking |

### Signal Pipeline
```
Market Data (yfinance)
    ↓
Feature Engineering (MA10, MA20, MA30, MA50)
    ↓
Signal Generation (crossover + price override)
    ↓
Regime Classification (BULL/BEAR/NEUTRAL)
    ↓
Order Execution (Alpaca API — session-aware routing)
    ↓
Journal Update (P&L, benchmark, alpha)
```

---

## 📊 Dashboard

Interactive Streamlit dashboard with all 7 models running live:

```bash
cd StreamlitDashboard
pip install -r requirements.txt
streamlit run app.py
```

**Pages:** Home · Linear Regression · Credit Risk · Trading Signals · Clustering · LSTM Forecaster

Also deployed on **Google Cloud Run** via Docker.

---

## 🏗️ Project Structure

```
live-trading-alpha/
├── LinearRegressionNSE/    # P1: Ridge vs Linear on RELIANCE returns
├── LogisticRegression/     # P2: Loan default binary classifier
├── DecisionTree/           # P3: BUY/HOLD/SELL signal tree
├── RandomForest/           # P4: Ensemble improvement (+6% acc)
├── XGBoost/                # P5: Boosting + SHAP + Optuna tuning
├── LSTMForecaster/         # P6: LSTM next-day Nifty return
├── KMeans/                 # P7: Unsupervised stock clustering
├── StreamlitDashboard/     # Multi-page Streamlit app
│   ├── app.py              # Home page
│   ├── pages/              # Project-specific pages
│   ├── Dockerfile          # GCP Cloud Run deployment
│   └── requirements.txt
├── AlpacaDaily.py          # Live trading signal engine
├── Alpaca_Journal.py       # Auto-generated P&L journal
├── Alpaca_Journal_NewGroq.py # AI-enhanced journal narratives
├── Feature-Engineering_NSE.py # NSE feature pipeline
├── alpaca_journal.md       # Current trading journal
└── signal_state.json       # Latest signal state
```

---

## ⚡ Quick Start

```bash
git clone https://github.com/YASHpPATIL7/live-trading-alpha.git
cd live-trading-alpha
pip install -r requirements.txt

# Run any project
python LinearRegressionNSE/LinearRegressionNSE_final.py
python XGBoost/Project5_XGBoost_TradingSignals.py
python LSTMForecaster/lstm_forecaster.py

# Run dashboard
cd StreamlitDashboard && streamlit run app.py

# Live trading (requires Alpaca keys)
cp .env.example .env    # Add your Alpaca paper keys
python AlpacaDaily.py
```

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **ML/DL** | scikit-learn · XGBoost · PyTorch · SHAP · Optuna |
| **Data** | yfinance · pandas · numpy |
| **Viz** | Plotly · Matplotlib · Streamlit |
| **Trading** | Alpaca API (paper) |
| **Deploy** | Docker · Google Cloud Run |
| **Theory** | Andrew Ng ML/DL Specialization (C1-C5) |

---

## 📈 Design Decisions

Each project documents AI-augmented workflow: what tools were used (Copilot, Claude, ChatGPT), what was manually verified, and what the model's failure modes are. See `PROJECT*_WORKFLOW.md` files.

**Key engineering choices:**
- **No data leakage:** All scalers fitted on training data only. Time-series splits are chronological.
- **Honest metrics:** R²=0.007 for returns prediction is **correct** — stock returns are nearly random. We report truthfully.
- **Walk-forward validation:** No shuffle. No random splits. Financial data is temporal.

---

*Built by Yash Patil — April 2026*
*7-project ML portfolio: Supervised + Unsupervised + Deep Learning + Live Paper Trading*
