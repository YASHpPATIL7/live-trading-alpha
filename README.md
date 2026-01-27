# live-trading-alpha
90-day live paper trading: Multi-factor ML strategy | XGBoost + FinBERT + HMM regime detection | Alpaca API | Sharpe 1.5+ target

# 📈 Live Trading Alpha

Systematic trading strategy with 90-day live paper trading results.

## Strategy
- **Factors:** Momentum, Value, Quality, Low-Volatility
- **ML Overlay:** XGBoost for signal combination
- **Sentiment:** FinBERT analysis on news/earnings
- **Regime Detection:** Hidden Markov Model (bull/bear/sideways)
- **Execution:** Alpaca API (paper trading)

## Target Metrics
- Sharpe Ratio: >1.5
- Max Drawdown: <15%
- Win Rate: >55%
- Trades/month: 40-60

## Tech Stack
- Python 3.11, XGBoost, PyTorch
- HuggingFace Transformers (FinBERT)
- Backtrader, Alpaca API
- MLflow, Docker

## Status
🟢 **Alpaca Paper Trading: ACTIVE** ($200k allocated)  
🔴 **Week 1** - Data pipeline setup

---
Live trading journal: [Coming Week 4]
