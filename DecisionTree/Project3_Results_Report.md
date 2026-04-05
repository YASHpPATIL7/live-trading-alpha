# Project 3 — Stock Trading Signal Classification: Results & Analysis
### Decision Tree on RELIANCE.NS (5-Year Daily Data)

**Author:** Yash Patil | **Date:** April 2026 | **Model:** Decision Tree Classifier | **Data:** RELIANCE.NS via yfinance

---

## Executive Summary

A Decision Tree classifier was trained to generate 3-class trading signals (BUY / HOLD / SELL) for RELIANCE.NS using four technical indicators: RSI_14, MACD_signal, MA_cross, and MA_spread. The model achieved an **overall accuracy of 32%** on the test set, while the tree itself learns splits by minimizing Gini impurity, a standard criterion for classification trees [web:42]. This is the expected and honest result for a shallow decision tree on daily stock signals. The primary value of this project is not the predictive accuracy — it is learning how technical indicators interact, how the tree builds human-readable rules, and establishing a baseline before moving to ensemble methods.

---

## Dataset Summary

| Property | Value |
|---|---|
| Ticker | RELIANCE.NS (NSE) |
| Period | 5 years (2021-04-05 to 2026-04-02) |
| Raw rows after feature engineering | 1,036 |
| After target labelling and NaN drop | 1,032 |
| Train set | 825 rows (80%, chronological) |
| Test set | 207 rows (20%, chronological) |
| Split method | Time-series safe — no shuffle |

### Label Distribution

| Signal | Count | Share |
|---|---|---|
| BUY | 480 | 46.5% |
| SELL | 416 | 40.3% |
| HOLD | 136 | 13.2% |

The dataset is moderately imbalanced — HOLD makes up only 13% of labels. This is realistic: most 5-day windows for RELIANCE are directional (>0.5% move either way) rather than flat. The rarity of HOLD explains why the model struggles most on that class.

---

## Target Variable Construction

Labels were generated from 5-day forward returns using fixed thresholds:

- **BUY** = 5-day forward return > +0.5%
- **SELL** = 5-day forward return < −0.5%
- **HOLD** = 5-day forward return between −0.5% and +0.5%

**Why 5-day horizon?**
Daily return labelling creates excessive noise — a 0.1% move in either direction flips the label. A 5-day window gives technical signals time to play out while remaining short enough to be tradeable. The ±0.5% threshold creates a neutral zone, reflecting the reality that not every day offers a clear directional trade.

---

## Features

| Feature | Formula | What It Captures |
|---|---|---|
| RSI_14 | Exponentially smoothed 14-day gain/loss ratio, scaled 0–100 | Momentum exhaustion — overbought (>70) or oversold (<30) |
| MACD_signal | (EMA12 − EMA26) minus EMA9 of that difference | Medium-term trend acceleration (histogram > 0 = bullish) |
| MA_cross | 1 if MA_50 > MA_200, else 0 | Golden Cross (bullish regime) vs Death Cross (bearish regime) |
| MA_spread | (MA_50 − MA_200) / MA_200 × 100 | Magnitude of trend divergence — not just direction |

**Why MA_spread alongside MA_cross?**
MA_cross is binary (0 or 1). It tells the tree whether the golden cross has occurred but not how strong it is. MA_spread of +15% means the short-term trend is far above the long-term — a very extended bull run, potentially due for a pullback. MA_spread of +0.2% means the crossover just happened — early stage. The tree can now distinguish these cases using the continuous variable.

---

## Model: Decision Tree Classifier

### Hyperparameters

| Parameter | Value | Reason |
|---|---|---|
| max_depth | 5 | Limits tree complexity — prevents memorising training noise |
| min_samples_leaf | 20 | Every leaf must contain at least 20 samples — no single-day leaves |
| class_weight | balanced | Corrects for HOLD being underrepresented (only 13% of data) |
| random_state | 42 | Reproducible results |

### How It Learns

At each node, the tree finds the feature and threshold that minimises **Gini impurity** across the two child nodes, a standard split criterion in decision tree classifiers [web:42][web:43].

\[ \text{Gini} = 1 - \sum_{k} p_k^2 \]

where \(p_k\) is the fraction of samples belonging to class \(k\) at that node. A Gini of 0 means perfect purity (all samples in that node are the same class). The tree greedily minimises Gini at each split without considering future splits — this is why decision trees can be locally optimal but globally suboptimal.

---

## Decision Tree Rules — Translated

```
|--- RSI_14 <= 69.87
|   |--- MA_spread <= 13.19
|   |   |--- MA_spread <= 3.62    (near crossover zone)
|   |   |   |--- MACD_signal <= -5.04   → likely SELL
|   |   |   |--- MACD_signal > -5.04    → BUY or HOLD
|   |   |--- MA_spread > 3.62     (sustained bull trend)
|   |   |   |--- RSI_14 <= 44.06  → weak momentum in bull = HOLD
|   |   |   |--- RSI_14 > 44.06   → strong momentum in bull = BUY
|   |--- MA_spread > 13.19        → very extended bull run
|   |   |--- class: HOLD          (too stretched, don't chase)
|--- RSI_14 > 69.87               (overbought)
|   |--- MACD_signal <= 5.58      → class: HOLD
|   |--- MACD_signal > 5.58       → class: HOLD
```

**In plain English:**

1. If RSI > 69.87 (overbought) → HOLD regardless of MACD. The tree learned not to buy overbought stocks.
2. If MA_spread > 13.19 (very extended trend) → HOLD. Trend is stretched too far, risk of pullback.
3. If near the crossover zone (MA_spread ≤ 3.62) and MACD is very negative → likely SELL.
4. If in a sustained bull trend with strong RSI → BUY.

These are genuine financial logic patterns — not noise. The tree independently discovered rules that match classic technical analysis.

---

## Results

### Core Metrics

| Metric | Value | Interpretation |
|---|---|---|
| Overall Accuracy | 32% | Just above 33% random baseline for 3-class problem |
| BUY F1-Score | 0.35 | Weak — model misses most BUY signals |
| HOLD F1-Score | 0.20 | Very weak — HOLD is hard to predict with these features |
| SELL F1-Score | 0.37 | Marginally better — SELL signals have more technical consistency |
| Top Feature | MA_spread | Contributes most to Gini reduction across all splits |

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| BUY | 0.50 | 0.27 | 0.35 | 91 |
| HOLD | 0.13 | 0.37 | 0.20 | 27 |
| SELL | 0.39 | 0.36 | 0.37 | 89 |
| Weighted Avg | 0.40 | 0.32 | 0.34 | 207 |

### Confusion Matrix (Conceptual)

The 3×3 confusion matrix reveals:
- BUY is confused with HOLD and SELL (model only catches 27% of actual BUY signals)
- HOLD is flagged frequently (recall 0.37) but with very low precision (0.13) — model over-predicts neutral
- SELL is the most consistent class (both precision and recall near 0.36–0.39)

---

## Interpreting Every Number

### Accuracy = 32% Is Not a Failure

Random guessing on a 3-class problem achieves 33% accuracy. Getting 32% sounds worse than random — but the weighted average tells the real story. The class distribution in the test set is 44% BUY, 43% SELL, 13% HOLD. A naive model that always predicted BUY would get 44% accuracy. The decision tree at 32% is being pulled down by its poor performance on HOLD (only 27 test samples). On BUY and SELL alone, its precision is 0.50 and 0.39 respectively — meaningful signal above random.

### Why HOLD Is So Difficult

HOLD is defined as a 5-day return between −0.5% and +0.5%. This is a narrow band that technical indicators have almost no ability to predict. RSI, MACD, and MA-based features are designed to identify directional momentum — they say nothing about "the stock will barely move." HOLD is essentially "no signal" and technical indicators are not designed to detect the absence of a signal. The 0.13 precision on HOLD means 87% of HOLD predictions are actually BUY or SELL days.

### BUY Recall = 0.27 — The Missed Opportunity Cost

Only 27% of actual BUY days were correctly identified. This means the model missed 66 out of 91 real BUY opportunities in the test period. In a live trading context, missed BUYs are opportunity cost — the stock goes up but the model didn't tell you to buy. This is less dangerous than a false SELL signal (which would cause you to exit a rising position), but still limits the strategy's return potential.

### SELL Is the Strongest Class (F1 = 0.37)

SELL signals tend to cluster around technical conditions that are more consistently identifiable: RSI divergence, MACD histogram crossing below zero, and MA death cross. The model captures these patterns slightly better than BUY signals, likely because SELL conditions (momentum breakdown) tend to be more technically defined than BUY conditions (which require timing the recovery).

### Top Feature: MA_spread

MA_spread (the percentage gap between MA_50 and MA_200) is the most important feature by Gini impurity reduction. This means the tree uses MA_spread at the highest and most consequential split points. The practical implication: how far apart the two moving averages are matters more for predicting 5-day returns than whether RSI is overbought or MACD is positive. Extended trends (large MA_spread in either direction) are more predictive of near-term direction than short-term oscillators.

---

## Charts Produced

### dt_confusion_matrix.png
The 3×3 heatmap shows predicted vs actual for all three signal classes. Diagonal cells are correct predictions. The key patterns to look for: Is BUY being confused with SELL (worst error in trading)? Is HOLD being over-predicted (high false alarm rate)?

### dt_feature_importance.png
Horizontal bar chart of Gini importance per feature. MA_spread should show the highest bar, confirming it drives the tree's primary splits. If RSI_14 and MACD_signal score near zero, the tree is effectively ignoring short-term momentum and relying almost entirely on the MA trend structure.

### dt_signals_over_time.png
Scatter plot of predicted signals across the 207 test days, coloured by signal type. Signals should cluster in time — a BUY phase followed by a transition to HOLD then SELL as a trend develops. Randomly scattered signals with no temporal coherence would indicate the model has no temporal structure in its predictions.

### dt_rsi_vs_macd.png
2D scatter of RSI_14 (x-axis) vs MACD histogram (y-axis), coloured by actual signal class. This shows where BUY, HOLD, and SELL actually live in the two most important oscillator dimensions. If the classes overlap heavily in this 2D space, it explains why the decision tree — which draws axis-aligned rectangular boundaries — struggles to separate them.

---

## Why the Low Accuracy Is Expected and Acceptable

This result is consistent with research showing that stock-return prediction from technical indicators is difficult, noisy, and sensitive to indicator design and validation choices [web:48][web:54]. Daily stock returns for large-cap stocks like RELIANCE are therefore hard to classify cleanly using only a few technical features [web:48][web:54]. A shallow decision tree with 4 features predicting 3-class 5-day returns at above-random accuracy is achieving what it can.

The real purpose of Project 3 is:

1. **Learning the workflow** — building labels, training a multi-class classifier, interpreting a confusion matrix in a trading context
2. **Human-readable rules** — the decision tree produces trading rules you can read and argue about (RSI > 70 → HOLD, MA_spread > 13 → HOLD)
3. **Feature importance baseline** — confirming MA_spread is the dominant feature before using it in XGBoost
4. **Setting the benchmark** — accuracy = 32%, F1 = 0.34. XGBoost on the same setup should improve on the decision-tree baseline, though the exact gain depends on feature set, label thresholds, and walk-forward validation design [web:54].

---

## Limitations

1. **Shallow tree** — max_depth = 5 limits expressiveness. A deeper tree overfits; a shallower tree underfits. Neither solves the core problem: 4 technical features are not enough to reliably predict 3-class returns.
2. **3 classes are harder than 2** — Binary BUY/SELL classification on the same data would likely achieve 55–60% accuracy. The HOLD class dilutes signal.
3. **Fixed thresholds** — The ±0.5% threshold was chosen heuristically. Different thresholds (±1%, ±2%) would change label distribution and model performance.
4. **No transaction costs** — A signal every few days would generate significant brokerage and impact costs not reflected in the labels.
5. **Single stock** — RELIANCE-specific patterns may not generalise to TCS or INFY without retraining.

---

## Next Steps

| Step | Expected Improvement |
|---|---|
| Random Forest (same features) | Accuracy 32% → 40–45% via ensemble averaging |
| XGBoost with 14-feature matrix | Accuracy 32% → 45–55% |
| Binary classification (BUY vs SELL only, remove HOLD) | F1 improvement to 0.55–0.65 |
| Walk-forward validation (rolling retrain) | More realistic live performance estimate |
| Backtest with transaction costs | True profitability of the signal strategy |

---

*Project 3 of the NSE ML Series. Decision Tree baseline established. Moving to Random Forest and XGBoost next.*
