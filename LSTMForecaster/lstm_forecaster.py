"""
PROJECT 6: LSTM Nifty 50 Forecaster
====================================
Predicts next-day Nifty 50 log returns using a 60-day lookback window.

Architecture: Input(5×60) → LSTM(64) → Dense(32) → Dense(1)
Features: Close, Volume, MA_50, RSI_14, Daily_Log_Return
Critical: MinMaxScaler fitted ONLY on training data (no data leakage!)

Author: Yash Patil
Date: April 2026
"""

import os
import json
import warnings
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

warnings.filterwarnings('ignore')
np.random.seed(42)
torch.manual_seed(42)

# ═══════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════

CONFIG = {
    'ticker': '^NSEI',              # Nifty 50 Index
    'start_date': '2015-01-01',
    'end_date': '2025-12-31',
    'lookback': 60,                 # 60-day window
    'features': ['Close', 'Volume', 'MA_50', 'RSI_14', 'Log_Return'],
    'train_split': 0.8,            # 80% train, 20% test
    'val_split': 0.1,              # 10% of train for validation
    'lstm_hidden': 64,
    'dense_hidden': 32,
    'dropout': 0.2,
    'batch_size': 32,
    'epochs': 100,
    'learning_rate': 0.001,
    'patience': 15,                 # Early stopping patience
    'output_dir': os.path.join(os.path.dirname(__file__), 'outputs'),
    'model_dir': os.path.join(os.path.dirname(__file__), 'models'),
}


# ═══════════════════════════════════════════════════════════════
# STEP 1: DATA ACQUISITION & FEATURE ENGINEERING
# ═══════════════════════════════════════════════════════════════

def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Relative Strength Index."""
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0.0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def fetch_and_prepare_data(config: dict) -> pd.DataFrame:
    """
    Fetch Nifty 50 data and engineer features.
    Returns DataFrame with: Close, Volume, MA_50, RSI_14, Log_Return, Target
    """
    print(f"📊 Fetching {config['ticker']} data: {config['start_date']} → {config['end_date']}")
    df = yf.download(config['ticker'], start=config['start_date'], end=config['end_date'], progress=False)

    # Handle multi-level columns from yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Feature engineering
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['RSI_14'] = calculate_rsi(df['Close'], period=14)
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))

    # Target: NEXT-DAY log return (what we're predicting)
    df['Target'] = df['Log_Return'].shift(-1)

    # Drop NaN rows (from rolling calcs + target shift)
    df = df.dropna()

    # Keep only required columns
    feature_cols = config['features']
    df = df[feature_cols + ['Target']]

    print(f"   ✅ Data shape: {df.shape}")
    print(f"   📅 Date range: {df.index[0].strftime('%Y-%m-%d')} → {df.index[-1].strftime('%Y-%m-%d')}")
    print(f"   📈 Features: {feature_cols}")

    return df


# ═══════════════════════════════════════════════════════════════
# STEP 2: WINDOWING + NO-LEAK SCALING
# ═══════════════════════════════════════════════════════════════

def create_sequences(data: np.ndarray, targets: np.ndarray, lookback: int):
    """
    Create sliding window sequences.
    Input:  data (N, features), targets (N,)
    Output: X (N-lookback, lookback, features), y (N-lookback,)
    """
    X, y = [], []
    for i in range(lookback, len(data)):
        X.append(data[i - lookback:i])
        y.append(targets[i])
    return np.array(X), np.array(y)


class NiftyDataset(Dataset):
    """PyTorch Dataset for Nifty sequences."""
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.FloatTensor(X)
        self.y = torch.FloatTensor(y).unsqueeze(1)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


def prepare_data_splits(df: pd.DataFrame, config: dict):
    """
    Split data chronologically → scale ONLY on training data → create sequences.

    CRITICAL: MinMaxScaler is fitted on TRAINING data only.
    Dev/test data is transformed using the SAME scaler (no data leakage).
    """
    feature_cols = config['features']
    lookback = config['lookback']

    features = df[feature_cols].values
    targets = df['Target'].values

    # Chronological split (NO shuffle — time series!)
    n = len(features)
    train_end = int(n * config['train_split'])

    train_features = features[:train_end]
    train_targets = targets[:train_end]
    test_features = features[train_end:]
    test_targets = targets[train_end:]

    # ═══════════════════════════════════════════════════
    # CRITICAL: Fit scaler on TRAINING DATA ONLY
    # ═══════════════════════════════════════════════════
    scaler = MinMaxScaler()
    train_features_scaled = scaler.fit_transform(train_features)
    test_features_scaled = scaler.transform(test_features)  # Transform only!

    print(f"\n🔒 Scaler fitted on training data ONLY (no data leakage)")
    print(f"   Train: {len(train_features)} samples")
    print(f"   Test:  {len(test_features)} samples")

    # Create sequences
    X_train, y_train = create_sequences(train_features_scaled, train_targets, lookback)
    X_test, y_test = create_sequences(test_features_scaled, test_targets, lookback)

    # Split training into train/val (for early stopping)
    val_size = int(len(X_train) * config['val_split'])
    X_val = X_train[-val_size:]
    y_val = y_train[-val_size:]
    X_train = X_train[:-val_size]
    y_train = y_train[:-val_size]

    print(f"   Train sequences: {X_train.shape}")
    print(f"   Val sequences:   {X_val.shape}")
    print(f"   Test sequences:  {X_test.shape}")

    # Create DataLoaders
    train_dataset = NiftyDataset(X_train, y_train)
    val_dataset = NiftyDataset(X_val, y_val)
    test_dataset = NiftyDataset(X_test, y_test)

    train_loader = DataLoader(train_dataset, batch_size=config['batch_size'], shuffle=False)
    val_loader = DataLoader(val_dataset, batch_size=config['batch_size'], shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=config['batch_size'], shuffle=False)

    # Store dates for plotting
    test_dates = df.index[train_end + lookback:]

    return train_loader, val_loader, test_loader, scaler, test_dates, y_test


# ═══════════════════════════════════════════════════════════════
# STEP 3: LSTM MODEL
# ═══════════════════════════════════════════════════════════════

class LSTMForecaster(nn.Module):
    """
    LSTM model for Nifty 50 next-day log return prediction.

    Architecture:
        Input(batch, 60, 5) → LSTM(64) → Dropout(0.2) → Dense(32) → ReLU → Dense(1)

    Gate equations (from C5 W1 notes):
        Forget:  Γf = σ(Wf·[a⟨t-1⟩, x⟨t⟩] + bf)
        Update:  Γu = σ(Wu·[a⟨t-1⟩, x⟨t⟩] + bu)
        Output:  Γo = σ(Wo·[a⟨t-1⟩, x⟨t⟩] + bo)
        Cell:    c⟨t⟩ = Γf * c⟨t-1⟩ + Γu * tanh(Wc·[a⟨t-1⟩, x⟨t⟩] + bc)
        Hidden:  a⟨t⟩ = Γo * tanh(c⟨t⟩)
    """

    def __init__(self, input_size: int = 5, hidden_size: int = 64,
                 dense_size: int = 32, dropout: float = 0.2):
        super(LSTMForecaster, self).__init__()

        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=1,
            batch_first=True,       # Input shape: (batch, seq_len, features)
            dropout=0               # Single layer, no inter-layer dropout
        )

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(hidden_size, dense_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(dense_size, 1)

    def forward(self, x):
        """
        Forward pass.
        x shape: (batch_size, 60, 5) → output shape: (batch_size, 1)
        """
        # LSTM processes all 60 timesteps, we take the LAST hidden state
        lstm_out, (h_n, c_n) = self.lstm(x)  # lstm_out: (batch, 60, 64)

        # Take last timestep output: (batch, 64)
        last_hidden = lstm_out[:, -1, :]

        # Dense layers
        out = self.dropout(last_hidden)
        out = self.fc1(out)                   # (batch, 32)
        out = self.relu(out)
        out = self.fc2(out)                   # (batch, 1)

        return out


# ═══════════════════════════════════════════════════════════════
# STEP 4: TRAINING WITH EARLY STOPPING
# ═══════════════════════════════════════════════════════════════

def train_model(model, train_loader, val_loader, config):
    """
    Train LSTM with Adam optimizer and early stopping.

    Adam (from C2 notes):
        v = β₁v + (1-β₁)dW      (momentum)
        s = β₂s + (1-β₂)dW²     (RMSprop)
        W = W - α × v_corr / (√s_corr + ε)
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=config['learning_rate'])

    train_losses = []
    val_losses = []
    best_val_loss = float('inf')
    patience_counter = 0
    best_model_state = None

    print(f"\n🧠 Training LSTM Forecaster")
    print(f"   Device: {device}")
    print(f"   Optimizer: Adam (lr={config['learning_rate']})")
    print(f"   Epochs: {config['epochs']} (patience={config['patience']})")
    print(f"   Architecture: Input(5×60) → LSTM(64) → Dropout(0.2) → Dense(32) → Dense(1)")
    print(f"   {'─'*60}")

    for epoch in range(config['epochs']):
        # ── Training Phase ──
        model.train()
        epoch_train_loss = 0
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)

            optimizer.zero_grad()
            predictions = model(X_batch)
            loss = criterion(predictions, y_batch)
            loss.backward()
            optimizer.step()

            epoch_train_loss += loss.item() * X_batch.size(0)

        epoch_train_loss /= len(train_loader.dataset)
        train_losses.append(epoch_train_loss)

        # ── Validation Phase ──
        model.eval()
        epoch_val_loss = 0
        with torch.no_grad():
            for X_batch, y_batch in val_loader:
                X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                predictions = model(X_batch)
                loss = criterion(predictions, y_batch)
                epoch_val_loss += loss.item() * X_batch.size(0)

        epoch_val_loss /= len(val_loader.dataset)
        val_losses.append(epoch_val_loss)

        # ── Early Stopping Check ──
        if epoch_val_loss < best_val_loss:
            best_val_loss = epoch_val_loss
            patience_counter = 0
            best_model_state = model.state_dict().copy()
        else:
            patience_counter += 1

        if (epoch + 1) % 10 == 0 or patience_counter == 0:
            marker = " ← best" if patience_counter == 0 else ""
            print(f"   Epoch {epoch+1:3d}/{config['epochs']} | "
                  f"Train: {epoch_train_loss:.6f} | Val: {epoch_val_loss:.6f}{marker}")

        if patience_counter >= config['patience']:
            print(f"   ⏹️  Early stopping at epoch {epoch+1} (patience={config['patience']})")
            break

    # Restore best model
    model.load_state_dict(best_model_state)
    print(f"   ✅ Best val loss: {best_val_loss:.6f}")

    return model, train_losses, val_losses


# ═══════════════════════════════════════════════════════════════
# STEP 5: EVALUATION & METRICS
# ═══════════════════════════════════════════════════════════════

def evaluate_model(model, test_loader, y_test):
    """
    Evaluate model on test set.
    Returns predictions and comprehensive metrics.
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    model.eval()

    all_predictions = []
    with torch.no_grad():
        for X_batch, _ in test_loader:
            X_batch = X_batch.to(device)
            predictions = model(X_batch)
            all_predictions.append(predictions.cpu().numpy())

    predictions = np.concatenate(all_predictions).flatten()
    actuals = y_test[:len(predictions)]

    # Metrics
    rmse = np.sqrt(mean_squared_error(actuals, predictions))
    mae = mean_absolute_error(actuals, predictions)

    # Directional Accuracy (THE key metric for trading)
    pred_direction = np.sign(predictions)
    actual_direction = np.sign(actuals)
    directional_accuracy = np.mean(pred_direction == actual_direction) * 100

    # Sharpe-like metric: if we trade based on predicted direction
    strategy_returns = actuals * pred_direction
    buy_hold_returns = actuals
    strategy_sharpe = np.mean(strategy_returns) / (np.std(strategy_returns) + 1e-8) * np.sqrt(252)
    buyhold_sharpe = np.mean(buy_hold_returns) / (np.std(buy_hold_returns) + 1e-8) * np.sqrt(252)

    metrics = {
        'rmse': float(rmse),
        'mae': float(mae),
        'directional_accuracy': float(directional_accuracy),
        'strategy_sharpe': float(strategy_sharpe),
        'buy_hold_sharpe': float(buyhold_sharpe),
        'test_samples': len(actuals),
    }

    print(f"\n📊 TEST SET RESULTS")
    print(f"   {'─'*45}")
    print(f"   RMSE:                  {rmse:.6f}")
    print(f"   MAE:                   {mae:.6f}")
    print(f"   Directional Accuracy:  {directional_accuracy:.1f}%")
    print(f"   Strategy Sharpe:       {strategy_sharpe:.3f}")
    print(f"   Buy & Hold Sharpe:     {buyhold_sharpe:.3f}")
    print(f"   Alpha over B&H:       {'✅ YES' if strategy_sharpe > buyhold_sharpe else '❌ NO'}")

    return predictions, actuals, metrics


# ═══════════════════════════════════════════════════════════════
# STEP 6: VISUALIZATION
# ═══════════════════════════════════════════════════════════════

def plot_training_curves(train_losses, val_losses, output_dir):
    """Plot training and validation loss curves."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(train_losses, label='Training Loss', color='#2196F3', linewidth=1.5)
    ax.plot(val_losses, label='Validation Loss', color='#FF5722', linewidth=1.5)
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('MSE Loss', fontsize=12)
    ax.set_title('LSTM Training & Validation Loss', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#fafafa')
    fig.tight_layout()
    path = os.path.join(output_dir, 'training_loss_curves.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"   📈 Saved: {path}")
    return path


def plot_predictions_vs_actual(predictions, actuals, test_dates, output_dir):
    """Plot predicted vs actual log returns."""
    n = min(len(predictions), len(test_dates))
    dates = test_dates[:n]
    preds = predictions[:n]
    acts = actuals[:n]

    fig, axes = plt.subplots(2, 1, figsize=(14, 9), gridspec_kw={'height_ratios': [3, 1]})

    # Top: Predicted vs Actual
    ax1 = axes[0]
    ax1.plot(dates, acts, label='Actual Log Return', color='#1a1a2e', alpha=0.6, linewidth=0.8)
    ax1.plot(dates, preds, label='LSTM Predicted', color='#e63946', alpha=0.8, linewidth=0.8)
    ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax1.set_title('LSTM Nifty 50 Forecaster — Predicted vs Actual Log Returns', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Log Return', fontsize=12)
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_facecolor('#fafafa')

    # Bottom: Directional accuracy (green = correct, red = wrong)
    ax2 = axes[1]
    correct = np.sign(preds) == np.sign(acts)
    colors = ['#4CAF50' if c else '#f44336' for c in correct]
    ax2.bar(dates, acts, color=colors, alpha=0.6, width=2)
    ax2.set_title(f'Directional Accuracy: {np.mean(correct)*100:.1f}% (Green = Correct)', fontsize=12)
    ax2.set_ylabel('Actual Return', fontsize=10)
    ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_facecolor('#fafafa')

    fig.tight_layout()
    path = os.path.join(output_dir, 'predicted_vs_actual.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"   📈 Saved: {path}")
    return path


def plot_cumulative_returns(predictions, actuals, test_dates, output_dir):
    """Plot cumulative returns: LSTM strategy vs Buy & Hold."""
    n = min(len(predictions), len(test_dates))
    dates = test_dates[:n]
    preds = predictions[:n]
    acts = actuals[:n]

    strategy_returns = acts * np.sign(preds)
    cum_strategy = np.cumsum(strategy_returns)
    cum_buyhold = np.cumsum(acts)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, cum_strategy, label='LSTM Strategy', color='#2196F3', linewidth=1.5)
    ax.plot(dates, cum_buyhold, label='Buy & Hold', color='#9E9E9E', linewidth=1.5, linestyle='--')
    ax.fill_between(dates, cum_strategy, cum_buyhold,
                     where=cum_strategy > cum_buyhold, alpha=0.2, color='green', label='Alpha')
    ax.fill_between(dates, cum_strategy, cum_buyhold,
                     where=cum_strategy <= cum_buyhold, alpha=0.2, color='red')
    ax.set_title('Cumulative Returns: LSTM Strategy vs Buy & Hold', fontsize=14, fontweight='bold')
    ax.set_ylabel('Cumulative Log Return', fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#fafafa')
    fig.tight_layout()
    path = os.path.join(output_dir, 'cumulative_returns.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"   📈 Saved: {path}")
    return path


# ═══════════════════════════════════════════════════════════════
# MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  PROJECT 6: LSTM NIFTY 50 FORECASTER")
    print("  Architecture: Input(5×60) → LSTM(64) → Dense(32) → Dense(1)")
    print("=" * 60)

    # Ensure output dirs exist
    os.makedirs(CONFIG['output_dir'], exist_ok=True)
    os.makedirs(CONFIG['model_dir'], exist_ok=True)

    # Step 1: Fetch and prepare data
    df = fetch_and_prepare_data(CONFIG)
    df.to_csv(os.path.join(CONFIG['output_dir'], 'nifty_features.csv'))

    # Step 2: Prepare splits with NO data leakage
    train_loader, val_loader, test_loader, scaler, test_dates, y_test = \
        prepare_data_splits(df, CONFIG)

    # Step 3: Build model
    model = LSTMForecaster(
        input_size=len(CONFIG['features']),
        hidden_size=CONFIG['lstm_hidden'],
        dense_size=CONFIG['dense_hidden'],
        dropout=CONFIG['dropout']
    )
    total_params = sum(p.numel() for p in model.parameters())
    print(f"\n🏗️  Model Parameters: {total_params:,}")
    print(model)

    # Step 4: Train
    model, train_losses, val_losses = train_model(model, train_loader, val_loader, CONFIG)

    # Step 5: Evaluate
    predictions, actuals, metrics = evaluate_model(model, test_loader, y_test)

    # Step 6: Visualize
    print(f"\n🎨 Generating visualizations...")
    plot_training_curves(train_losses, val_losses, CONFIG['output_dir'])
    plot_predictions_vs_actual(predictions, actuals, test_dates, CONFIG['output_dir'])
    plot_cumulative_returns(predictions, actuals, test_dates, CONFIG['output_dir'])

    # Save model
    model_path = os.path.join(CONFIG['model_dir'], 'lstm_nifty_forecaster.pth')
    torch.save({
        'model_state_dict': model.state_dict(),
        'config': CONFIG,
        'metrics': metrics,
        'scaler_min': scaler.data_min_.tolist(),
        'scaler_max': scaler.data_max_.tolist(),
    }, model_path)
    print(f"\n💾 Model saved: {model_path}")

    # Save metrics
    metrics_path = os.path.join(CONFIG['output_dir'], 'metrics.json')
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"📊 Metrics saved: {metrics_path}")

    print(f"\n{'='*60}")
    print(f"  ✅ PROJECT 6 COMPLETE")
    print(f"  RMSE: {metrics['rmse']:.6f}")
    print(f"  Directional Accuracy: {metrics['directional_accuracy']:.1f}%")
    print(f"  Strategy Sharpe: {metrics['strategy_sharpe']:.3f}")
    print(f"{'='*60}")

    return model, metrics


if __name__ == '__main__':
    model, metrics = main()
