# Project 3 — Decision Tree: Stock Trading Signal Classification
## AI-Augmented Workflow Document

**Author:** Yash Patil
**Date:** April 2026
**Data:** RELIANCE.NS via yfinance (5 years)
**Stack:** Python · yfinance · scikit-learn · Plotly · VS Code · GitHub

---

## 1. Project Objective

Generate 3-class trading signals (BUY / HOLD / SELL) for RELIANCE.NS
using a Decision Tree classifier trained on technical indicators.
Learn which indicators the tree considers most important for split decisions.

---

## 2. Data

| Property | Value |
|---|---|
| Ticker | RELIANCE.NS |
| Period | 5 years |
| Split | 80% train, 20% test (chronological — no shuffle) |
| Target | 5-day forward return threshold labels |

---

## 3. Target Variable Construction

Labels are generated from 5-day forward returns:
  BUY  = Fwd_return_5d > +0.5%  (price up more than 0.5% in next 5 days)
  SELL = Fwd_return_5d < -0.5%  (price down more than 0.5% in next 5 days)
  HOLD = everything in between  (-0.5% to +0.5%)

Why 5 days?
Daily return labelling creates too much noise — a 0.1% move either way
would flip the label. 5-day horizon gives the signal time to play out
while remaining short enough to be tradeable.

Why thresholds?
Hard thresholds create a neutral zone (HOLD) which reflects
real trading reality — most days are not clear directional trades.

---

## 4. Features

| Feature | Formula | What it captures |
|---|---|---|
| RSI_14 | 100 - 100/(1 + avg_gain/avg_loss) over 14 days | Momentum — overbought (>70) or oversold (<30) |
| MACD_signal | (EMA12 - EMA26) minus EMA9 of that difference | Trend momentum crossover |
| MA_cross | 1 if MA_50 > MA_200 else 0 | Golden Cross / Death Cross |
| MA_spread | (MA_50 - MA_200) / MA_200 * 100 | Magnitude of trend divergence |

### Why these features together:
RSI captures short-term momentum exhaustion.
MACD captures medium-term trend acceleration.
MA_cross gives binary trend direction (bull vs bear market).
MA_spread gives the intensity of the trend (not just yes/no).
Together they represent: momentum + trend + regime.

---

## 5. Model: Decision Tree Classifier

Decision Tree builds a set of IF-THEN rules by finding the feature
and threshold at each node that best separates the 3 classes.

Hyperparameters:
  max_depth = 5        — prevents overfitting, limits tree complexity
  min_samples_leaf = 20 — each leaf must have at least 20 samples
  class_weight = balanced — prevents HOLD from dominating predictions

How the tree splits:
  At each node, the tree picks the feature + threshold that minimises
  Gini impurity in the two child nodes.
  Gini = 1 - sum(p_class^2) = 0 means perfectly pure node (all same class)

Feature importance = how much each feature reduces Gini impurity
across all splits that use it, weighted by the number of samples.

---

## 6. Charts Produced

### dt_confusion_matrix.png
3x3 confusion matrix for BUY / HOLD / SELL.
Diagonal = correct predictions.
Off-diagonal = misclassifications.
Key check: are BUY signals being classified as SELL? That is the worst error.

### dt_feature_importance.png
Horizontal bar chart of Gini importance per feature.
Tells you which indicator the tree actually relied on most.
Expected: RSI_14 and MACD_signal should dominate.
If MA_cross = highest: the tree is essentially just following the golden cross.

### dt_signals_over_time.png
Scatter plot: each day in the test set coloured by predicted signal.
Shows whether BUY/SELL signals cluster in time (they should — trends persist).
If signals are completely random across time: model has no temporal coherence.

### dt_rsi_vs_macd.png
Scatter of RSI_14 (x) vs MACD histogram (y) coloured by actual signal.
Shows where BUY/HOLD/SELL actually live in the 2D feature space.
A decision tree's boundaries are axis-aligned rectangles in this space.
If BUY and SELL zones are cleanly separated: tree can separate them well.
If zones overlap: tree will struggle.

---

## 7. How to Read the Decision Tree Rules

The export_text output looks like:
  |--- RSI_14 <= 45.3
  |   |--- MACD_signal <= -2.1
  |   |   |--- class: SELL       <- oversold + bearish MACD = SELL
  |   |--- MACD_signal > -2.1
  |   |   |--- class: HOLD
  |--- RSI_14 > 45.3
  |   |--- MA_cross <= 0.5
  |   |   |--- class: HOLD       <- above RSI midline but death cross = hold
  |   |--- MA_cross > 0.5
  |   |   |--- class: BUY        <- RSI strong + golden cross = BUY

Each path from root to leaf = one trading rule.
These rules are human-readable — you can explain every prediction.
This is a key advantage over black-box models (XGBoost, Neural Nets).

---

## 8. AI-Augmented Workflow

| Stage | Human | AI |
|---|---|---|
| Signal generation | Wanted BUY/HOLD/SELL labels | Suggested 5-day forward return with threshold zone for HOLD |
| Feature selection | Specified RSI, MACD, MA crossover | Added MA_spread for magnitude, explained MACD histogram vs line |
| Hyperparameters | Knew max_depth concept | Chose 5 and min_samples_leaf=20 to prevent one-sample leaves |
| Interpretation | Read classification report | Explained Gini impurity, feature importance calculation |
| Charts | Chose to plot signals over time | Added RSI vs MACD scatter as 2D feature space visualisation |

---

## 9. Limitations and Next Steps

1. Labels are created from future data — not tradeable without look-ahead prevention
2. Single stock only — no sector or market regime context
3. Decision tree overfits easily — test with Random Forest next
4. 0.5% threshold is arbitrary — test multiple thresholds, pick by Sharpe ratio
5. No transaction costs modelled — a signal every day would be unprofitable after costs
6. Next: Random Forest + XGBoost on same signal generation setup

---

## 10. File Structure

    live-trading-alpha/
    |-- Project3_DecisionTree_TradingSignals.py
    |-- dt_confusion_matrix.png
    |-- dt_feature_importance.png
    |-- dt_signals_over_time.png
    |-- dt_rsi_vs_macd.png
    |-- PROJECT3_WORKFLOW.md              <- this document

---

_Project 3 of the NSE ML series. Decision boundary visualised._
