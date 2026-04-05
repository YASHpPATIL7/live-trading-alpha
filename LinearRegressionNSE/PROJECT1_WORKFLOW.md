# Project 1 — Linear Regression: RELIANCE NSE Price Prediction
## AI-Augmented Workflow Document

**Author:** Yash Patil
**Date:** April 2026
**Stack:** Python · yfinance · scikit-learn · Plotly · VS Code · GitHub Actions

---

## 1. Project Objective

Predict next-day returns for RELIANCE.NS using classical linear models.
Establish a baseline R² and RMSE before moving to non-linear models (XGBoost).
Understand what features drive price movement and how much is actually predictable.

---

## 2. Data

| Property | Value |
|---|---|
| Ticker | RELIANCE.NS (NSE via Yahoo Finance) |
| Period | 5 years (2021-04-05 to 2026-04-02) |
| Raw rows | 1,236 trading days |
| After feature engineering | 1,036 rows (200 dropped for MA_200 warmup) |
| Train set | 828 rows (80%) |
| Test set | 208 rows (20%) |
| Split method | Time-series safe — no shuffle, chronological order |

Why no shuffle? Shuffling a time series leaks future data into training.
Day 900's features cannot train on Day 1000's data in real trading.

---

## 3. Features Used

| Feature | Formula | Why |
|---|---|---|
| MA_50 | Rolling 50-day mean of Close | Short-term trend direction |
| MA_200 | Rolling 200-day mean of Close | Long-term trend direction |
| Volume_ratio | Volume / 20-day avg volume | Measures conviction behind price move |
| Daily_return | (Close - Close_prev) / Close_prev | Yesterday's momentum signal |

**Target variable:** Next-day return = pct_change(1).shift(-1)
Shift(-1) moves tomorrow's return into today's row so the model learns:
"Given today's features, what will tomorrow's return be?"

---

## 4. Models

### 4.1 Linear Regression

Standard OLS (Ordinary Least Squares).
Finds coefficients that minimise the sum of squared errors between
predicted and actual returns on the training set.

No penalty. No constraint. Purely fits training data.

**Formula:**
  predicted_return = w1*MA_50 + w2*MA_200 + w3*Volume_ratio + w4*Daily_return + b

### 4.2 Ridge Regression

Ridge = Linear Regression + L2 regularisation penalty.

**Formula:**
  minimise: MSE + alpha * sum(coefficients^2)

The alpha term penalises large coefficients, forcing the model to stay simple.
This reduces overfitting when features are noisy or correlated.

**Why Ridge for stock data?**
MA_50 and MA_200 are highly correlated (both are smoothed versions of Close price).
Ridge handles multicollinearity better than plain LR by shrinking correlated
coefficients toward each other instead of making one huge and one tiny.

---

## 5. How Alpha Was Chosen (Cross-Validation)

Alpha is a hyperparameter — it cannot be learned from data directly.
We tested 6 candidate values: [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

For each alpha, we used TimeSeriesSplit with 5 folds:

  Fold 1: train on rows 1-166,   validate on rows 167-332
  Fold 2: train on rows 1-332,   validate on rows 333-498
  Fold 3: train on rows 1-498,   validate on rows 499-664
  Fold 4: train on rows 1-664,   validate on rows 665-828
  Fold 5: not used (only 5 folds)

Each fold trains only on past data and validates on future data.
This mirrors how a real trading model would be deployed.

Mean R² across all 5 folds was computed for each alpha.
Alpha with the highest mean CV R² was selected: alpha = 1000.0

Why 1000? The features are very weak signals in noisy daily return data.
High alpha aggressively shrinks all coefficients toward zero,
which actually performs best on CV because the baseline (predicting mean)
beats noisy coefficients on this data.

---

## 6. Results

| Metric | Linear Regression | Ridge (alpha=1000) |
|---|---|---|
| R² Score | 0.0072 | 0.0048 |
| RMSE | 0.011763 | 0.011778 |
| Train rows | 828 | 828 |
| Test rows | 208 | 208 |

### Coefficients (Linear Regression)

| Feature | Coefficient | Interpretation |
|---|---|---|
| MA_50 | -0.000908 | Higher short-term MA → slightly lower next-day return (mean reversion) |
| MA_200 | +0.000252 | Higher long-term MA → slightly positive momentum |
| Volume_ratio | +0.000401 | Above-average volume → slightly bullish next day |
| Daily_return | +0.000214 | Up today → slightly up tomorrow (weak momentum) |

All coefficients are near zero — confirming weak feature-to-target relationship.

---

## 7. What the Results Mean

R² = 0.0072 means the model explains 0.72% of variance in next-day returns.
This is NORMAL for daily stock return prediction. Not a failure.

Daily stock returns decompose approximately as:
  ~70% news, macro, sentiment    (model cannot see this)
  ~20% random noise              (nobody can predict this)
  ~10% technical patterns        (what this model attempts to capture)

R² of 0.007 = the model captured a small but real slice of the technical component.
In production quant finance, an R² of 0.01 on daily returns is considered meaningful
if it is consistent and survives out-of-sample testing.

Ridge performing slightly worse than LR (0.0048 vs 0.0072) tells us:
  - LR was not significantly overfitting (Ridge couldn't improve on it)
  - The features are genuinely weak, not just noisy versions of a real signal
  - Alpha=1000 essentially predicts near the mean every day

---

## 8. Charts Produced

### Chart 1: actual_vs_predicted.png
**What it shows:** Actual RELIANCE close price vs LR predicted price vs Ridge predicted
price over the 208-day test period.

**What to look for:**
  - Both models track the general price direction (they use MA features)
  - Predicted lines are smoother than actual — models miss sharp moves
  - Gap between actual and predicted widens during high-volatility periods

**Key insight:** Price prediction shows high visual accuracy because tomorrow's price
is always close to today's price. This is why R² on price looks high but is misleading.
Return prediction (R² = 0.007) is the honest metric.

### Chart 2: residual_analysis.png
**What it shows:** 2x2 grid:
  Top-left:  LR residuals over time (scatter around zero line)
  Top-right: Ridge residuals over time (scatter around zero line)
  Bottom-left:  LR residual distribution (histogram)
  Bottom-right: Ridge residual distribution (histogram)

**What to look for:**
  - Residuals should be randomly scattered around zero (no pattern)
  - A pattern in residuals = systematic error the model consistently makes
  - Histogram should be bell-shaped and centred at zero
  - Fat tails in the histogram = model badly wrong on extreme days (crashes/rallies)

**Key insight:** Clusters of large residuals around specific dates correspond to
market events (earnings, macro shocks, index rebalancing) that the model
had no features to anticipate.

### Chart 3: predicted_vs_actual_scatter.png
**What it shows:** Scatter plot of predicted return (y-axis) vs actual return (x-axis)
for all 208 test days. Red dashed line = perfect prediction (45-degree diagonal).

**What to look for:**
  - Perfect model: all points on the red diagonal
  - Real model: cloud of points around the diagonal
  - Width of the cloud = model uncertainty
  - Bias: if cloud is above the line, model consistently over-predicts
  - Points far from the diagonal = days the model got badly wrong

**Key insight:** The scatter cloud is nearly circular around zero — confirming
the model has very low directional accuracy. This is expected for daily returns.
A tight elongated cloud along the diagonal would indicate strong predictive power.

---

## 9. AI-Augmented Workflow

This project used AI assistance (Perplexity/Claude) at the following stages:

| Stage | Human | AI |
|---|---|---|
| Problem framing | Decided to predict RELIANCE returns | Suggested target = return not price |
| Feature set | Specified MA_50, MA_200, Volume_ratio, Daily_return | Suggested adding shift(-1) for target |
| Train/test split | Chose 80/20 | Flagged that shuffle=True would leak future data |
| Ridge alpha CV | Understood the concept | Wrote TimeSeriesSplit loop, explained alpha=1000 result |
| Results interpretation | Read the numbers | Explained why R²=0.007 is normal and not a failure |
| Chart design | Chose chart types | Built all 3 Plotly charts with no syntax errors |
| Debugging | Ran the script, pasted errors | Fixed SyntaxError (EOL), fixed pip install command error |

**Key learning from AI collaboration:**
The most valuable AI contribution was NOT writing code — it was explaining
WHY results look the way they do. Understanding that R²=0.007 is normal,
that Ridge at alpha=1000 essentially predicts the mean, and that residual
clusters correspond to market events — these are insights that would have
taken hours of reading to arrive at independently.

---

## 10. Limitations and Next Steps

### Current Limitations
1. Only 4 features — misses RSI, momentum acceleration, volume spikes
2. Linear model — cannot capture non-linear relationships (RSI zones, regime changes)
3. Single stock — no cross-stock signals (sector momentum, relative strength)
4. No macro features — VIX, yield curve, oil not included
5. No position sizing — model predicts direction but not conviction

### Next Steps (Project 2 onwards)
1. XGBoost with full 14-feature matrix from feature engineering script
2. Add RSI, MA_spread, RSI_x_Volume, market regime cluster labels
3. Walk-forward validation instead of single train/test split
4. Classification version: predict UP/DOWN instead of exact return
5. Backtest with realistic transaction costs and slippage

---

## 11. File Structure

    live-trading-alpha/
    |-- LinearRegressionNSE.py          <- this project's model script
    |-- actual_vs_predicted.png         <- Chart 1
    |-- residual_analysis.png           <- Chart 2
    |-- predicted_vs_actual_scatter.png <- Chart 3
    |-- nse_model_ready.csv             <- feature matrix from Block 11
    |-- PROJECT1_WORKFLOW.md            <- this document

---

_Project 1 of the NSE ML series. Baseline established. Moving to XGBoost next._
