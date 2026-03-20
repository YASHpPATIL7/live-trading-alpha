# live-trading-alpha

90-day live paper trading: Multi-factor ML strategy | XGBoost signal engine 
| Alpaca API | NSE + US equities | Sharpe 1.5+ target

---

# 📈 Live Trading Alpha

Systematic trading framework built from scratch — live paper trading on Alpaca
with a feature engineering pipeline targeting institutional-grade signal quality.

## Current Status
🟢 **Alpaca Paper Trading: ACTIVE** ($100k allocated)
🟢 **Week 1** — Core infrastructure complete
🟡 **XGBoost model** — Feature matrix built, training next session
🔴 **FinBERT sentiment** — Planned Week 3
🔴 **HMM Regime Detection** — Planned Week 4

---

## What's Built (Session 1)

### Live Trading Engine
- Session-aware order routing — market orders (regular), limit orders (extended hours)
- Pre-market / regular / after-hours / closed detection via EST timezone guard
- SMA Golden Cross / Death Cross signal (MA20 vs MA50)
- Automated daily execution via cron (9:31 PM IST = 9:31 AM EST)
- P&L journal sourced from Alpaca FILL activities (not yfinance — actual fills)

### Feature Engineering Pipeline (NSE + US)
- 14 engineered features per stock per day
- RSI (Wilder's smoothing), Volume Ratio, Momentum (1d/5d/20d returns)
- Interaction features: RSI × Volume, MA spread, Return acceleration
- KMeans market regime clustering (4 regimes: Panic / Bull / Complacency / Bear)
- PCA dimensionality reduction (9 correlated features → 3 clean components)
- Target encoding with KFold (leakage-free categorical encoding)
- Mutual Information feature selection (linear + non-linear signal detection)

### Infrastructure
- .env secrets management (keys never in source)
- Startup auth validation (fail fast on dead credentials)
- Cron automation with caffeinate (prevents Mac sleep at market open)
- Structured error logging — no bare except blocks

---

## Strategy Roadmap

| Component | Status | Target Week |
|---|---|---|
| SMA Crossover baseline | ✅ Live | Week 1 |
| Feature engineering pipeline | ✅ Complete | Week 1 |
| XGBoost signal model | 🔄 In progress | Week 2 |
| Backtesting framework | 📋 Planned | Week 2 |
| FinBERT sentiment overlay | 📋 Planned | Week 3 |
| HMM regime detection | 📋 Planned | Week 4 |
| Position sizing (Kelly/vol-target) | 📋 Planned | Week 3 |
| Live trading journal dashboard | 📋 Planned | Week 4 |

---

## Target Metrics
- **Sharpe Ratio:** >1.5
- **Max Drawdown:** <15%
- **Win Rate:** >55%
- **Trades/month:** 40–60

---

## Tech Stack
- Python 3.9, pandas, numpy, scikit-learn
- XGBoost (signal model — next session)
- HuggingFace Transformers / FinBERT (planned)
- Alpaca Markets API (paper trading)
- yfinance (signal generation only — not P&L)
- MLflow, Docker (planned)

---

## Architecture Decision Log

| Decision | Reason |
|---|---|
| Alpaca API = P&L source of truth | yfinance close ≠ actual fill price (after-hours gap) |
| Limit orders in extended hours | Market orders rejected outside regular session |
| KFold target encoding | Prevents data leakage on ticker categorical feature |
| Log transform on volume | Right-skewed distribution breaks KMeans distance metric |
| PCA on 9 correlated features | Reduces noise, removes multicollinearity before XGBoost |

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/live-trading-alpha
cd live-trading-alpha
pip install -r requirements.txt

cp .env.example .env
# Add your Alpaca paper keys to .env

python AlpacaDaily.py       # run signal + place order
python Alpaca_Journal.py    # pull fills + build P&L journal
python feature_engineering.py  # build ML feature matrix
