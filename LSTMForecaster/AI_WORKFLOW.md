# AI-Augmented Workflow Documentation
## Project 6: LSTM Nifty 50 Forecaster

### Problem Statement
Predict next-day Nifty 50 log returns using a 60-day lookback window with LSTM.

### Why LSTM? (Andrew Ng C5 W1 Connection)
Standard RNNs suffer from **vanishing gradients** — they can't learn dependencies beyond ~10-20 timesteps. Financial markets exhibit patterns across 20-60 day windows (monthly cycles, quarterly earnings effects, options expiry patterns). An LSTM's **cell state conveyor belt** preserves information across all 60 timesteps:

- **Forget gate** learns: "discard the price pattern from 50 days ago if there's been a regime change"
- **Update gate** learns: "this sudden volume spike + RSI divergence is important, store it"
- **Output gate** learns: "for today's prediction, expose the recent momentum signal"

### Architecture
```
Input (batch_size, 60, 5) 
    ↓
LSTM Layer (hidden_size=64, 1 layer)
    ↓ [last timestep hidden state]
Dropout (p=0.2)
    ↓
Dense (64 → 32) + ReLU
    ↓
Dense (32 → 1)
    ↓
Output: predicted next-day log return
```

### Features (5 inputs)
| Feature | Why |
|---------|-----|
| Close | Raw price level — trend information |
| Volume | Liquidity signal — confirms price moves |
| MA_50 | 50-day moving average — trend direction |
| RSI_14 | Momentum oscillator — overbought/oversold |
| Log_Return | Daily return — recent momentum |

### Critical Design Decision: No Data Leakage
```python
# ✅ CORRECT: Fit scaler on training data ONLY
scaler.fit_transform(train_data)
scaler.transform(test_data)     # Transform only!

# ❌ WRONG: Would leak future information
scaler.fit_transform(all_data)  # NEVER do this
```

### AI Tools Used
| Tool | Purpose | How I Verified |
|------|---------|----------------|
| GitHub Copilot | Boilerplate for DataLoader setup | Verified batch dimensions with print(tensor.shape) |
| Claude | Architecture review — confirmed Input→LSTM→Dense is standard | Cross-checked with PyTorch LSTM tutorial |
| ChatGPT | RSI calculation formula verification | Validated against investopedia definition |

### What I Learned
1. `batch_first=True` changes LSTM input from (seq, batch, features) to (batch, seq, features)
2. Directional accuracy matters more than RMSE for trading — you profit from direction, not magnitude
3. Early stopping prevents overfitting to training regime's specific patterns
4. Financial time series are NON-STATIONARY — predicting log returns (stationary) is better than predicting price (non-stationary)

### Key Metrics
- **Directional Accuracy**: The percentage of days where the model correctly predicts UP or DOWN
- **Strategy Sharpe**: Annualized Sharpe ratio if you trade the predicted direction
- **Buy & Hold Sharpe**: Benchmark — just holding Nifty 50

### Failure Modes
1. **Regime changes**: Model trained on bull market fails in crash (COVID 2020)
2. **Non-stationarity**: Statistical properties change over time
3. **Overfitting**: Model memorizes training patterns instead of learning generalizable signals
4. **Data leakage**: If scaler sees future data, metrics are inflated and meaningless
