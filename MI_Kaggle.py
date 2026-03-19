# ============================================================
# BLOCK 1: IMPORTS
# ============================================================
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_regression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold

# yfinance     → pulls real NSE stock data from Yahoo Finance
# pandas       → DataFrame operations (your main data table tool)
# numpy        → math operations (log, arrays)
# mutual_info  → scores each feature by how much it predicts the target
# StandardScaler → rescales features to same range (needed for KMeans + PCA)
# KMeans       → unsupervised clustering (finds market regimes)
# PCA          → compresses correlated features into fewer columns
# KFold        → splits data into folds for leakage-free target encoding


# ============================================================
# BLOCK 2: FETCH DATA
# ============================================================
tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
raw = yf.download(tickers, period="2y", auto_adjust=True, progress=False)

# yf.download pulls 2 years of daily OHLCV data for all 3 stocks at once
# auto_adjust=True → prices are adjusted for splits and dividends automatically
# raw is a multi-level DataFrame: raw["Close"]["RELIANCE.NS"] = close prices for Reliance
# raw["Volume"]["TCS.NS"] = volume for TCS, etc.

close = raw["Close"]    # DataFrame: rows = dates, columns = stock tickers
volume = raw["Volume"]  # same structure


# ============================================================
# BLOCK 3: BUILD FEATURES PER STOCK IN A LOOP
# ============================================================
features_list = []  # empty list, we'll append one df per stock, then merge

for ticker in tickers:

    # Build a clean 2-column starting DataFrame for this stock
    df = pd.DataFrame({
        "Close": close[ticker],
        "Volume": volume[ticker]
    })
    df.dropna(inplace=True)
    # dropna removes rows where Close or Volume is NaN
    # This happens on market holidays where one stock might have data and another doesn't

    # --- MOVING AVERAGES ---
    df["MA_50"] = df["Close"].rolling(50).mean()
    df["MA_200"] = df["Close"].rolling(200).mean()
    # rolling(50) = slide a window of 50 rows across the data
    # .mean() = take the average of those 50 rows
    # MA_50 on Day 60 = average of Close from Day 11 to Day 60
    # First 49 rows of MA_50 will be NaN → normal, not enough history yet
    # MA_50 > MA_200 = short-term trend stronger than long-term = bullish (Golden Cross)
    # MA_50 < MA_200 = short-term weaker = bearish (Death Cross)

    df["MA_cross"] = (df["MA_50"] > df["MA_200"]).astype(int)
    # Boolean comparison: True if Golden Cross, False if Death Cross
    # .astype(int) converts True → 1, False → 0
    # ML models need numbers, not True/False

    # --- VOLUME RATIO ---
    df["Volume_avg_20"] = df["Volume"].rolling(20).mean()
    df["Volume_ratio"] = df["Volume"] / df["Volume_avg_20"]
    # Volume_ratio = today's volume ÷ average volume over last 20 days
    # Volume_ratio = 1.0 → perfectly average day
    # Volume_ratio = 3.0 → 3x normal volume → something big is happening
    # Volume_ratio = 0.4 → very quiet day, low conviction in price move

    # --- RSI (Relative Strength Index, 14-period) ---
    delta = df["Close"].diff()
    # diff() = subtract previous row from current row
    # delta[i] = Close[i] - Close[i-1] = daily price change
    # Positive delta = price went up, Negative = price went down

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    # gain: keep only positive changes, replace negatives with 0
    # loss: keep only negative changes, flip sign to positive, replace positives with 0
    # Example: delta = [+20, -15, +8, -5]
    #   gain = [20, 0, 8, 0]
    #   loss = [0, 15, 0, 5]

    avg_gain = gain.ewm(com=13, adjust=False).mean()
    avg_loss = loss.ewm(com=13, adjust=False).mean()
    # ewm = Exponential Weighted Mean (Wilder's smoothing)
    # com=13 means: alpha = 1 / (1 + 13) = 1/14 → 14-period smoothing
    # Recent days get more weight than older days
    # This is Wilder's original RSI method (not simple rolling average)

    rs = avg_gain / avg_loss
    # RS = how much the stock gains on up days vs loses on down days
    # RS = 3.0 means gains are 3x bigger than losses → strong momentum

    df["RSI_14"] = 100 - (100 / (1 + rs))
    # The RSI formula converts RS into a 0-100 scale
    # RSI = 100 → stock only went up, never down (theoretical max)
    # RSI = 50 → gains and losses are equal → neutral
    # RSI = 0  → stock only went down, never up (theoretical min)
    # RSI < 30 → oversold: stock fell too hard too fast, may bounce
    # RSI > 70 → overbought: stock rallied too hard, may pull back

    # --- MOMENTUM (RETURNS) ---
    df["Return_1d"] = df["Close"].pct_change(1)
    df["Return_5d"] = df["Close"].pct_change(5)
    df["Return_20d"] = df["Close"].pct_change(20)
    # pct_change(n) = (Close[today] - Close[n days ago]) / Close[n days ago]
    # Return_1d = yesterday-to-today return (daily momentum)
    # Return_5d = last week's return (weekly momentum)
    # Return_20d = last month's return (monthly momentum)
    # Why all three? Momentum can persist at different timeframes simultaneously

    # --- PRICE DISTANCE FROM MA ---
    df["Price_vs_MA50_pct"] = (df["Close"] - df["MA_50"]) / df["MA_50"] * 100
    df["Price_vs_MA200_pct"] = (df["Close"] - df["MA_200"]) / df["MA_200"] * 100
    # % above or below the moving average
    # Price_vs_MA50_pct = +8.0 → price is 8% above MA_50 → strong short-term trend
    # Price_vs_MA50_pct = -5.0 → price is 5% below MA_50 → weak, below trend
    # This is a CONTINUOUS version of MA_cross (more info than just 0/1)
    # Tree models (XGBoost) use this much better than the binary MA_cross

    df["Ticker"] = ticker.replace(".NS", "")
    # Store clean ticker name in each row (RELIANCE, TCS, INFY)
    # Needed later for target encoding and groupby operations
    features_list.append(df)


# ============================================================
# BLOCK 4: MERGE ALL STOCKS + FIX DUPLICATE INDEX BUG
# ============================================================
df = pd.concat(features_list).dropna()
# pd.concat stacks the 3 DataFrames vertically into one big table
# Problem: all 3 stocks share the SAME DatetimeIndex (same trading dates)
# RELIANCE row for 2025-01-02 and TCS row for 2025-01-02 both have index = 2025-01-02
# This causes y[X.index] to return 3 matches per date = 3x row count = BUG

df = df.reset_index()
# reset_index() replaces the duplicate DatetimeIndex with unique integers: 0, 1, 2, 3...
# Now every row has a completely unique label → no more phantom row multiplication
# The old Date column moves into a regular column (not the index) — that's fine

print(f"Total rows after cleaning: {len(df)}")
print(df.tail(3))


# ============================================================
# BLOCK 5: CREATE TARGET VARIABLE
# ============================================================
df["Target"] = df.groupby("Ticker")["Close"].pct_change(1).shift(-1)
# groupby("Ticker") → apply separately per stock, never mix RELIANCE with TCS rows
# pct_change(1) → daily return for each row
# shift(-1) → shift the return column UP by 1 row
#   Before shift: Row[i] has today's return (today vs yesterday)
#   After shift:  Row[i] has TOMORROW's return
# Why? We want to predict what happens NEXT. So today's features should map to tomorrow's return.
# The very last row of each stock gets NaN as Target (no tomorrow data)

df.dropna(subset=["Target"], inplace=True)
# Only drop rows where Target is NaN (last row of each stock)
# Keep all other rows even if some features are NaN (handled stock by stock later)

print(f"Rows after adding target: {len(df)}")


# ============================================================
# BLOCK 6: MUTUAL INFORMATION — BASE FEATURES
# ============================================================
base_features = [
    "MA_50", "MA_200", "MA_cross",
    "Volume_ratio", "RSI_14",
    "Price_vs_MA50_pct", "Price_vs_MA200_pct",
    "Return_1d", "Return_5d", "Return_20d"
]

X_base = df[base_features]
y = df["Target"]

mi_scores = mutual_info_regression(X_base, y, random_state=42)
# mutual_info_regression tests each feature independently against the target
# Score = 0.0 → feature gives ZERO information about tomorrow's return
# Score = 0.05 → weak but real signal (normal for stock data)
# Score = 0.3+ → strong predictor (rare in financial data)
# Unlike correlation, MI catches NON-LINEAR relationships too
# random_state=42 → makes results reproducible (MI uses random sampling internally)

mi_df = pd.Series(mi_scores, index=base_features).sort_values(ascending=False)
print("\n--- MI SCORES (Base Features) ---")
print(mi_df.round(4))
# Top scorers are worth keeping and building on
# Score near 0 = feature is noise, but don't drop yet — it might help in an interaction


# ============================================================
# BLOCK 7: INTERACTION FEATURES
# ============================================================
df["RSI_x_Volume"] = df["RSI_14"] * df["Volume_ratio"]
# Multiplying RSI × Volume creates a "confirmation" signal
# Low RSI (30) × High Volume (3.0) = 90 → panic selling with real participation
# Low RSI (30) × Low Volume (0.5) = 15 → weak drift, not real panic
# High RSI (70) × High Volume (3.0) = 210 → strong rally with conviction
# Volume alone scores 0.0 in MI. RSI alone scores 0.04.
# Their product should score higher than either alone. Test it.

df["MA_spread"] = (df["MA_50"] - df["MA_200"]) / df["MA_200"] * 100
# How stretched is the gap between short-term and long-term trend?
# +5.0 → MA_50 is 5% above MA_200 → strong sustained bull trend
# -8.0 → MA_50 is 8% below MA_200 → deep downtrend
# Near 0 → crossover zone, trend is changing
# Captures more info than MA_cross (which only tells you positive/negative, not magnitude)

df["Log_Volume"] = np.log1p(df["Volume"])
# log1p = log(1 + x), safe for zero values
# Raw volume is right-skewed: most days 1-2M, some days 20M, rare days 100M
# This skew hurts linear models and distances in KMeans/PCA
# Log transform compresses the tail → near-normal distribution → better ML behavior
# np.log1p(1000000) ≈ 13.8, np.log1p(10000000) ≈ 16.1 → compressed but distinguishable

df["Return_accel"] = df["Return_1d"] - (df["Return_5d"] / 5)
# Momentum acceleration: is today's move faster or slower than recent average?
# Return_5d / 5 = average daily return over last 5 days
# If Return_1d > average → momentum is speeding up → continuation likely
# If Return_1d < average → momentum is fading → potential reversal
# This is the rate of change of momentum (second derivative of price, roughly)

df["RSI_zone"] = pd.cut(
    df["RSI_14"],
    bins=[0, 30, 50, 70, 100],
    labels=[0, 1, 2, 3]
).astype(float)
# Bucket RSI into 4 discrete zones instead of using raw 0-100 value
# Zone 0: RSI < 30  → oversold (potential bounce)
# Zone 1: RSI 30-50 → weak/neutral
# Zone 2: RSI 50-70 → strong/neutral
# Zone 3: RSI > 70  → overbought (potential reversal)
# Why? The relationship between RSI and returns is non-linear and threshold-based
# RSI = 29 and RSI = 31 are VERY different signals but close in raw number
# Binning captures this step-change behavior that continuous RSI misses

# Re-run MI with interaction features to compare
extended_features = base_features + ["RSI_x_Volume", "MA_spread", "Log_Volume", "Return_accel"]

# FIX: keep X and y aligned by working from the same DataFrame slice
df_ext = df[extended_features + ["Target"]].dropna()
X_ext = df_ext[extended_features]
y_ext = df_ext["Target"]
# This guarantees X_ext and y_ext have EXACTLY the same rows → no length mismatch error

mi_ext = mutual_info_regression(X_ext, y_ext, random_state=42)
mi_ext_df = pd.Series(mi_ext, index=extended_features).sort_values(ascending=False)
print("\n--- MI SCORES (With Interaction Features) ---")
print(mi_ext_df.round(4))
# Key question: Does RSI_x_Volume outscore RSI_14 alone?
# If yes → the interaction captured something real
# If no → the combination doesn't help for predicting next-day return


# ============================================================
# BLOCK 8: TARGET ENCODING
# ============================================================
# Replace categorical "RELIANCE" / "TCS" / "INFY" with a number
# The number = mean next-day return of that stock, computed without leakage

df = df.copy()
df["Ticker_encoded"] = 0.0  # placeholder, will be filled by KFold loop

kf = KFold(n_splits=5, shuffle=False)
# KFold splits the data into 5 equal chunks (folds)
# shuffle=False → keep chronological order (NEVER shuffle time series data)
# For each fold: encode using the OTHER 4 folds, apply to this fold
# This prevents the model from seeing tomorrow's info while encoding today's row

for train_idx, val_idx in kf.split(df):
    train_fold = df.iloc[train_idx]  # rows used to compute the encoding
    val_fold = df.iloc[val_idx]      # rows being encoded

    means = train_fold.groupby("Ticker")["Target"].mean()
    # For each ticker, compute mean return using ONLY the training fold rows

    df.iloc[val_idx, df.columns.get_loc("Ticker_encoded")] = \
        val_fold["Ticker"].map(means).fillna(df["Target"].mean())
    # Map each ticker name to its mean return
    # .fillna(global_mean) → safety net if a ticker appears in val but not train

# m-estimate smoothing (important when you scale to 50+ stocks later)
global_mean = df["Target"].mean()
m = 10  # smoothing factor

ticker_stats = df.groupby("Ticker")["Target"].agg(["mean", "count"])
ticker_stats["smoothed_encoding"] = (
    (ticker_stats["count"] * ticker_stats["mean"]) + (m * global_mean)
) / (ticker_stats["count"] + m)
# Formula: (n × category_mean + m × global_mean) / (n + m)
# n = number of rows for this ticker
# When n is large (250+ rows): result ≈ category mean (trust the data)
# When n is small (5 rows): result pulled toward global mean (be conservative)
# m=10 means: treat each ticker as if it has 10 "fake" rows at the global mean

print("\n--- TARGET ENCODING PER TICKER ---")
print(ticker_stats.round(6))


# ============================================================
# BLOCK 9: K-MEANS CLUSTERING — MARKET REGIMES
# ============================================================
cluster_features = ["RSI_14", "Volume_ratio", "Price_vs_MA50_pct", "MA_spread"]
df_cluster = df[cluster_features].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)
# K-Means uses Euclidean distance to group points
# RSI is on 0-100 scale. Volume_ratio is on 0-5 scale.
# Without scaling: RSI dominates clustering just because its numbers are bigger
# StandardScaler: subtract mean, divide by std → every feature has mean=0, std=1
# Now all 4 features contribute equally to the distance calculation

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
# n_clusters=4 → we want 4 different market regimes
# n_init=10 → run KMeans 10 times with different random starting points
# Returns the best clustering out of 10 runs (avoids bad local minima)

df.loc[df_cluster.index, "Market_regime"] = kmeans.fit_predict(X_scaled).astype(float)
# fit_predict learns the 4 cluster centers AND assigns each row to a cluster
# Labels: 0, 1, 2, 3 → just numbers, meaning comes from interpreting the profiles below

regime_profile = df.groupby("Market_regime")[cluster_features].mean().round(2)
print("\n--- MARKET REGIME PROFILES ---")
print(regime_profile)
# Look at each row and label it manually using domain knowledge:
# Low RSI + High Volume + Negative Price_vs_MA → Capitulation (panic selling)
# High RSI + High Volume + Positive Price_vs_MA → Strong bull trend
# High RSI + Low Volume + Slightly positive → Weak drift/complacency
# Low RSI + Low Volume + Slightly negative → Quiet bearish drift
# These regime labels become a feature → "is today a panic day or a bull day?"


# ============================================================
# BLOCK 10: PCA — COMPRESS CORRELATED FEATURES
# ============================================================
pca_input = [
    "MA_50", "MA_200", "RSI_14", "Volume_ratio",
    "Price_vs_MA50_pct", "Price_vs_MA200_pct",
    "Return_1d", "Return_5d", "Return_20d"
]

df_pca = df[pca_input].dropna()

scaler2 = StandardScaler()
X_pca_scaled = scaler2.fit_transform(df_pca)
# Scale before PCA (same reason as KMeans — all features must be on same scale)
# PCA finds directions of maximum variance, which is distorted by different scales

pca = PCA(n_components=3)
# PCA finds 3 new "super-features" (principal components)
# PC1 = the single direction that explains the MOST variance across all 9 features
# PC2 = the direction with SECOND most variance, completely uncorrelated with PC1
# PC3 = third most variance, uncorrelated with PC1 and PC2
# Result: 9 correlated features → 3 uncorrelated components (less noise, less redundancy)

components = pca.fit_transform(X_pca_scaled)
df.loc[df_pca.index, "PC1"] = components[:, 0]
df.loc[df_pca.index, "PC2"] = components[:, 1]
df.loc[df_pca.index, "PC3"] = components[:, 2]
# Each row now has a score for each component
# PC1 score = "how much in the direction of the main trend factor is this row?"

print("\n--- PCA EXPLAINED VARIANCE ---")
ev = pd.Series(pca.explained_variance_ratio_, index=["PC1", "PC2", "PC3"]).round(3)
print(ev)
# If PC1 = 0.62 → one number captures 62% of all information across 9 features
# If PC1+PC2 > 0.80 → you can replace 9 features with just 2 numbers (very efficient)

loadings = pd.DataFrame(
    pca.components_.T,
    index=pca_input,
    columns=["PC1", "PC2", "PC3"]
).round(3)
print("\n--- WHAT DRIVES EACH COMPONENT (LOADINGS) ---")
print(loadings)
# Loading = how strongly each original feature contributes to each component
# High absolute value = strong contribution
# If MA_50, MA_200, Price_vs_MA200 all have loading ~0.8 on PC1
#   → PC1 = "trend component" (call it that in your notes)
# If Volume_ratio, Return_1d load on PC2
#   → PC2 = "activity/volatility component"
# This is where finance domain knowledge meets math


# ============================================================
# BLOCK 11: FINAL MODEL-READY MATRIX
# ============================================================
final_features = [
    "RSI_14",              # raw momentum oscillator
    "Volume_ratio",        # raw volume signal
    "Price_vs_MA50_pct",   # short-term trend distance
    "Price_vs_MA200_pct",  # long-term trend distance
    "MA_cross",            # golden/death cross (binary)
    "RSI_x_Volume",        # interaction: panic/euphoria strength
    "MA_spread",           # interaction: trend magnitude
    "Log_Volume",          # transformed volume (de-skewed)
    "Return_accel",        # momentum acceleration
    "RSI_zone",            # non-linear RSI buckets
    "Ticker_encoded",      # target encoded ticker identity
    "Market_regime",       # cluster label (market regime)
    "PC1", "PC2"           # compressed trend + activity components
]

df_model = df[final_features + ["Target"]].dropna()

print(f"\n--- FINAL FEATURE MATRIX ---")
print(f"Shape: {df_model.shape}")
# Should be ~850 rows × 15 columns
# Every row = one trading day for one stock
# Every column = one engineered feature
# Target column = next day's return (what the model will learn to predict)

print(df_model.describe().round(3))
# describe() gives count, mean, std, min, max for every column
# Check: no NaN counts, no infinite values, RSI between 0-100, Volume_ratio > 0

df_model.to_csv("nse_model_ready.csv")
print("\nSaved to nse_model_ready.csv — ready for XGBoost next session")
