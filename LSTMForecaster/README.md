# Project 6: LSTM Nifty 50 Forecaster 📈

> Next-day Nifty 50 log return prediction using LSTM with a 60-day lookback window.

## Architecture

```
Input(5×60) → LSTM(64) → Dropout(0.2) → Dense(32) → ReLU → Dense(1)
```

| Component | Detail |
|-----------|--------|
| **Input** | 5 features × 60 day window |
| **Features** | Close, Volume, MA_50, RSI_14, Log_Return |
| **Target** | Next-day log return |
| **Optimizer** | Adam (lr=0.001, β₁=0.9, β₂=0.999) |
| **Loss** | MSE |
| **Regularization** | Dropout(0.2) + Early Stopping (patience=15) |
| **Data** | Nifty 50 daily (2015-2025) via yfinance |

## Key Design: No Data Leakage ⚠️

```python
# MinMaxScaler fitted ONLY on training data
scaler.fit_transform(train_data)    # Learn min/max from train
scaler.transform(test_data)         # Apply same transform (no fitting!)
```

## Run

```bash
cd 06_lstm_nifty_forecaster
python lstm_forecaster.py
```

## Outputs

| File | Description |
|------|-------------|
| `outputs/training_loss_curves.png` | Train vs Validation MSE per epoch |
| `outputs/predicted_vs_actual.png` | Predicted vs actual log returns + directional accuracy |
| `outputs/cumulative_returns.png` | LSTM strategy vs Buy & Hold cumulative returns |
| `outputs/metrics.json` | RMSE, MAE, Directional Accuracy, Strategy Sharpe |
| `models/lstm_nifty_forecaster.pth` | Saved model + scaler params |

## Metrics

- **RMSE** — Prediction error magnitude
- **Directional Accuracy** — % of days with correct UP/DOWN prediction (most important for trading)
- **Strategy Sharpe** — Annualized Sharpe if trading predicted direction
- **Buy & Hold Sharpe** — Benchmark comparison

## Theory (Andrew Ng C5 W1)

The LSTM's cell state acts as a **conveyor belt** that preserves information across 60 timesteps:

```
c⟨t⟩ = Γf × c⟨t-1⟩ + Γu × c̃⟨t⟩
```

- **Forget gate (Γf)**: Discard old patterns after regime change
- **Update gate (Γu)**: Store new volume spikes / momentum shifts
- **Output gate (Γo)**: Expose relevant signal for today's prediction

This solves the **vanishing gradient problem** that makes basic RNNs fail on financial time series.
