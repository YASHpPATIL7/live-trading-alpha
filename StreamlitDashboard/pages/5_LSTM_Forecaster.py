import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="P6: LSTM Forecaster", page_icon="🧠", layout="wide")
st.title("🧠 Project 6 — LSTM Nifty 50 Forecaster")

st.markdown("""
Predict next-day **Nifty 50 log returns** using a 60-day lookback window.

**Architecture:** `Input(5×60) → LSTM(64) → Dropout(0.2) → Dense(32) → Dense(1)`

> ⚠️ **Runs PyTorch LSTM live** — training takes ~30-60 seconds on Streamlit Cloud.
""")

# --- Sidebar controls ---
st.sidebar.header("LSTM Parameters")
lookback = st.sidebar.slider("Lookback Window (days)", 20, 120, 60)
lstm_hidden = st.sidebar.selectbox("LSTM Hidden Size", [32, 64, 128], index=1)
epochs = st.sidebar.slider("Max Epochs", 20, 100, 50)
learning_rate = st.sidebar.select_slider("Learning Rate",
    options=[0.0001, 0.0005, 0.001, 0.005, 0.01], value=0.001)
dropout = st.sidebar.slider("Dropout Rate", 0.0, 0.5, 0.2, 0.05)


def calculate_rsi(series, period=14):
    """Calculate RSI."""
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0.0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


if st.sidebar.button("🚀 Train LSTM", type="primary"):
    try:
        import torch
        import torch.nn as nn
        from torch.utils.data import Dataset, DataLoader
        HAS_TORCH = True
    except ImportError:
        HAS_TORCH = False
        st.error("PyTorch not available. Showing pre-computed results.")

    if HAS_TORCH:
        torch.manual_seed(42)
        np.random.seed(42)

        # ── Step 1: Fetch Data ──
        with st.spinner("📊 Fetching Nifty 50 data..."):
            df = yf.download("^NSEI", start="2015-01-01", end="2025-12-31", progress=False)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            df["MA_50"] = df["Close"].rolling(window=50).mean()
            df["RSI_14"] = calculate_rsi(df["Close"], period=14)
            df["Log_Return"] = np.log(df["Close"] / df["Close"].shift(1))
            df["Target"] = df["Log_Return"].shift(-1)
            df = df.dropna()

            feature_cols = ["Close", "Volume", "MA_50", "RSI_14", "Log_Return"]
            df = df[feature_cols + ["Target"]]

        st.success(f"✅ Data: {df.shape[0]} rows | {df.index[0].strftime('%Y-%m-%d')} → {df.index[-1].strftime('%Y-%m-%d')}")

        # Show raw data
        with st.expander("📋 Raw Data Sample"):
            st.dataframe(df.tail(10))

        # ── Step 2: Split + Scale (NO DATA LEAKAGE) ──
        with st.spinner("🔒 Splitting data — scaler fitted on TRAIN ONLY..."):
            features = df[feature_cols].values
            targets = df["Target"].values

            n = len(features)
            train_end = int(n * 0.8)

            train_features = features[:train_end]
            test_features = features[train_end:]
            train_targets = targets[:train_end]
            test_targets = targets[train_end:]

            scaler = MinMaxScaler()
            train_scaled = scaler.fit_transform(train_features)
            test_scaled = scaler.transform(test_features)

            # Create sequences
            def make_sequences(data, tgt, lb):
                X, y = [], []
                for i in range(lb, len(data)):
                    X.append(data[i-lb:i])
                    y.append(tgt[i])
                return np.array(X), np.array(y)

            X_train, y_train = make_sequences(train_scaled, train_targets, lookback)
            X_test, y_test = make_sequences(test_scaled, test_targets, lookback)

            # Validation split from training
            val_size = int(len(X_train) * 0.1)
            X_val, y_val = X_train[-val_size:], y_train[-val_size:]
            X_train, y_train = X_train[:-val_size], y_train[:-val_size]

            test_dates = df.index[train_end + lookback:]

        col1, col2, col3 = st.columns(3)
        col1.metric("Train Sequences", f"{X_train.shape[0]:,}")
        col2.metric("Val Sequences", f"{X_val.shape[0]:,}")
        col3.metric("Test Sequences", f"{X_test.shape[0]:,}")

        st.info("🔒 **No Data Leakage:** MinMaxScaler fitted on training data only. Test data transformed with training scaler.")

        # ── Step 3: LSTM Model ──
        class LSTMForecaster(nn.Module):
            def __init__(self, input_size=5, hidden_size=64, dense_size=32, drop=0.2):
                super().__init__()
                self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
                self.dropout = nn.Dropout(drop)
                self.fc1 = nn.Linear(hidden_size, dense_size)
                self.relu = nn.ReLU()
                self.fc2 = nn.Linear(dense_size, 1)

            def forward(self, x):
                out, _ = self.lstm(x)
                out = self.dropout(out[:, -1, :])
                out = self.relu(self.fc1(out))
                return self.fc2(out)

        model = LSTMForecaster(
            input_size=len(feature_cols),
            hidden_size=lstm_hidden,
            dense_size=32,
            drop=dropout
        )
        total_params = sum(p.numel() for p in model.parameters())

        st.markdown(f"""
        **Model Architecture:**
        ```
        Input({len(feature_cols)}×{lookback}) → LSTM({lstm_hidden}) → Dropout({dropout}) → Dense(32) → Dense(1)
        Parameters: {total_params:,}
        ```
        """)

        # ── Step 4: Train ──
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        X_train_t = torch.FloatTensor(X_train)
        y_train_t = torch.FloatTensor(y_train).unsqueeze(1)
        X_val_t = torch.FloatTensor(X_val)
        y_val_t = torch.FloatTensor(y_val).unsqueeze(1)

        train_losses, val_losses = [], []
        best_val = float("inf")
        patience, patience_counter = 15, 0
        best_state = None

        progress = st.progress(0, text="Training LSTM...")
        epoch_display = st.empty()

        for epoch in range(epochs):
            model.train()
            optimizer.zero_grad()
            pred = model(X_train_t)
            loss = criterion(pred, y_train_t)
            loss.backward()
            optimizer.step()
            train_losses.append(loss.item())

            model.eval()
            with torch.no_grad():
                val_pred = model(X_val_t)
                val_loss = criterion(val_pred, y_val_t).item()
            val_losses.append(val_loss)

            if val_loss < best_val:
                best_val = val_loss
                patience_counter = 0
                best_state = {k: v.clone() for k, v in model.state_dict().items()}
            else:
                patience_counter += 1

            progress.progress((epoch + 1) / epochs,
                text=f"Epoch {epoch+1}/{epochs} | Train: {loss.item():.6f} | Val: {val_loss:.6f}")

            if patience_counter >= patience:
                epoch_display.warning(f"⏹️ Early stopped at epoch {epoch+1}")
                break

        if best_state:
            model.load_state_dict(best_state)
        progress.empty()
        st.success(f"✅ Training complete | Best val loss: {best_val:.6f}")

        # ── Step 5: Evaluate ──
        model.eval()
        with torch.no_grad():
            X_test_t = torch.FloatTensor(X_test)
            predictions = model(X_test_t).numpy().flatten()

        actuals = y_test[:len(predictions)]
        n_plot = min(len(predictions), len(test_dates))
        dates_plot = test_dates[:n_plot]
        preds_plot = predictions[:n_plot]
        acts_plot = actuals[:n_plot]

        rmse = np.sqrt(mean_squared_error(acts_plot, preds_plot))
        mae = mean_absolute_error(acts_plot, preds_plot)
        dir_acc = np.mean(np.sign(preds_plot) == np.sign(acts_plot)) * 100

        strategy_ret = acts_plot * np.sign(preds_plot)
        strat_sharpe = np.mean(strategy_ret) / (np.std(strategy_ret) + 1e-8) * np.sqrt(252)
        bh_sharpe = np.mean(acts_plot) / (np.std(acts_plot) + 1e-8) * np.sqrt(252)

        # ── Metrics ──
        st.markdown("### 📊 Test Set Results")
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("RMSE", f"{rmse:.6f}")
        m2.metric("MAE", f"{mae:.6f}")
        m3.metric("Directional Acc", f"{dir_acc:.1f}%")
        m4.metric("Strategy Sharpe", f"{strat_sharpe:.3f}")
        m5.metric("Buy & Hold Sharpe", f"{bh_sharpe:.3f}")

        # ── Charts ──
        tab1, tab2, tab3 = st.tabs(["📈 Training Curves", "🎯 Predictions", "💰 Cumulative Returns"])

        with tab1:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(y=train_losses, name="Training Loss",
                line=dict(color="#2196F3", width=1.5)))
            fig1.add_trace(go.Scatter(y=val_losses, name="Validation Loss",
                line=dict(color="#FF5722", width=1.5)))
            fig1.update_layout(title="Training & Validation Loss",
                xaxis_title="Epoch", yaxis_title="MSE Loss", height=450)
            st.plotly_chart(fig1, use_container_width=True)

        with tab2:
            fig2 = make_subplots(rows=2, cols=1, shared_xaxes=True,
                row_heights=[0.7, 0.3],
                subplot_titles=["Predicted vs Actual Log Returns",
                    f"Directional Accuracy: {dir_acc:.1f}%"])

            fig2.add_trace(go.Scatter(x=dates_plot, y=acts_plot, name="Actual",
                line=dict(color="#1a1a2e", width=0.8), opacity=0.6), row=1, col=1)
            fig2.add_trace(go.Scatter(x=dates_plot, y=preds_plot, name="LSTM Predicted",
                line=dict(color="#e63946", width=0.8), opacity=0.8), row=1, col=1)

            correct = np.sign(preds_plot) == np.sign(acts_plot)
            colors = ["#4CAF50" if c else "#f44336" for c in correct]
            fig2.add_trace(go.Bar(x=dates_plot, y=acts_plot, name="Direction",
                marker_color=colors, opacity=0.6), row=2, col=1)

            fig2.update_layout(height=650, showlegend=True)
            st.plotly_chart(fig2, use_container_width=True)

        with tab3:
            cum_strat = np.cumsum(strategy_ret)
            cum_bh = np.cumsum(acts_plot)

            fig3 = go.Figure()
            fig3.add_trace(go.Scatter(x=dates_plot, y=cum_strat, name="LSTM Strategy",
                line=dict(color="#2196F3", width=1.5)))
            fig3.add_trace(go.Scatter(x=dates_plot, y=cum_bh, name="Buy & Hold",
                line=dict(color="#9E9E9E", width=1.5, dash="dash")))
            fig3.update_layout(title="Cumulative Returns: LSTM Strategy vs Buy & Hold",
                xaxis_title="Date", yaxis_title="Cumulative Log Return", height=450)
            st.plotly_chart(fig3, use_container_width=True)

        # ── Theory Box ──
        with st.expander("📚 How LSTM Works (Andrew Ng C5 W1)"):
            st.markdown("""
            **Why LSTM over RNN?** Standard RNNs suffer from vanishing gradients — they forget patterns
            beyond ~10 steps. Financial data needs 30-60 day context.

            **The 3 Gates:**
            - **Forget gate** (Γf): "Should I discard old information?" → `σ(Wf·[a⟨t-1⟩, x⟨t⟩])`
            - **Update gate** (Γu): "Should I store this new pattern?" → `σ(Wu·[a⟨t-1⟩, x⟨t⟩])`
            - **Output gate** (Γo): "What should I expose for prediction?" → `σ(Wo·[a⟨t-1⟩, x⟨t⟩])`

            **Cell state = conveyor belt:** `c⟨t⟩ = Γf × c⟨t-1⟩ + Γu × c̃⟨t⟩`

            If Γf ≈ 1, information flows unchanged through 60 timesteps → gradient survives → long-range patterns learned.

            **Critical design decision:** MinMaxScaler fitted on training data ONLY.
            If the scaler sees test data, it "leaks" future information and inflates metrics.
            """)

else:
    st.info("👈 Click **Train LSTM** in the sidebar to run the model live.")

    st.markdown("""
    ### What This Model Does

    | Parameter | Value |
    |-----------|-------|
    | **Input** | 5 features × 60-day window |
    | **Features** | Close, Volume, MA_50, RSI_14, Log_Return |
    | **Target** | Next-day log return |
    | **Optimizer** | Adam (lr=0.001) |
    | **Regularization** | Dropout + Early Stopping |

    ### Architecture Diagram
    ```
    Day 1  Day 2  Day 3  ...  Day 60
      ↓      ↓      ↓          ↓
    ┌──────────────────────────────┐
    │    LSTM (64 hidden units)     │  ← Processes sequence, retains memory via gates
    └──────────────────────────────┘
                    ↓
              Dropout (0.2)         ← Regularization (C2 W1)
                    ↓
              Dense (32) + ReLU
                    ↓
              Dense (1)             ← Predicted next-day log return
    ```
    """)
