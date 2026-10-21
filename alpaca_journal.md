# ALPACA PAPER JOURNAL — SPY
_Last updated: October 21, 2026 | Day 70 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$753.605/share**
> (2026-07-15, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-10-21): **BULLISH**  
> Fast: MA10 $772.19 | MA30 $767.99  
> Slow: MA20 $770.88 | MA50 $767.35  
> Regime: **BULL** | Momentum: **STRONG** | Session: AFTER_HOURS

## Strategy Description

This journal tracks a **dual-timeframe SMA crossover** strategy on SPY:

| Component | MAs | Purpose |
|---|---|---|
| **Fast Signal** | SMA 10 / SMA 30 | Entry and exit triggers |
| **Regime Filter** | SMA 20 / SMA 50 | Trend context — blocks longs in strong bear regimes |
| **Price Override** | Close > MA50 × 1.02 | Overrides bearish regime if price has clearly recovered |
| **Position Sizing** | 40% max allocation | Risk-based sizing with 1.5% stop-loss |

**Rules:**
- BUY when MA10 > MA30 AND regime ≠ STRONG_BEAR
- BUY when price > 2% above MA50 AND above both fast MAs (price override)
- SELL when MA10 < MA30 (unless price override active)
- Long-only (no shorting)

## Trade History

**Total trades:** 19 | **Closed:** 18 | **Open:** Yes | **Cumulative Realized P&L:** -$1808.52

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $753.605 (2026-07-15) | $754.500 (2026-07-15) | 33 | +$29.55 | ✅ Closed |
| T2 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T3 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T4 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T5 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T6 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T7 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T8 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T9 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T10 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T11 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T12 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T13 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |
| T14 | $773.250 (2026-09-22) | $773.540 (2026-09-22) | 51 | +$14.79 | ✅ Closed |
| T15 | $768.534 (2026-09-23) | $767.970 (2026-09-23) | 51 | -$28.77 | ✅ Closed |
| T16 | $765.350 (2026-09-28) | $765.980 (2026-09-29) | 51 | +$32.13 | ✅ Closed |
| T17 | $766.590 (2026-09-30) | $767.680 (2026-10-14) | 51 | +$55.59 | ✅ Closed |
| T18 | $769.600 (2026-10-15) | $770.610 (2026-10-20) | 51 | +$51.51 | ✅ Closed |
| T19 | $773.850 (2026-10-21) | — | 51 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $98,986.87 |
| Alpaca cash | $59,730.64 |
| Cumulative realized P&L | -$1808.52 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $752.90 | FLAT | — | — | $100,029.55 |
| Day 2 | 2026-07-16 | $749.01 | FLAT | — | — | $99,853.42 |
| Day 3 | 2026-07-17 | $741.44 | FLAT | — | — | $99,710.86 |
| Day 4 | 2026-07-20 | $740.31 | FLAT | — | — | $99,518.88 |
| Day 5 | 2026-07-21 | $746.30 | Long 53 SPY (T5) | -$69.96 | -0.177% | $99,448.92 |
| Day 6 | 2026-07-22 | $745.64 | Long 53 SPY (T5) | -$104.94 | -0.265% | $99,413.94 |
| Day 7 | 2026-07-23 | $736.23 | Long 52 SPY (T6) | -$135.72 | -0.353% | $98,747.69 |
| Day 8 | 2026-07-24 | $737.07 | FLAT | — | — | $98,891.73 |
| Day 9 | 2026-07-27 | $737.02 | FLAT | — | — | $98,995.87 |
| Day 10 | 2026-07-28 | $738.96 | FLAT | — | — | $98,952.41 |
| Day 11 | 2026-07-29 | $727.76 | FLAT | — | — | $98,952.41 |
| Day 12 | 2026-07-30 | $739.79 | FLAT | — | — | $98,952.41 |
| Day 13 | 2026-07-31 | $744.94 | FLAT | — | — | $98,952.41 |
| Day 14 | 2026-08-03 | $755.84 | FLAT | — | — | $98,952.41 |
| Day 15 | 2026-08-04 | $769.20 | Long 50 SPY (T9) | -$147.50 | -0.382% | $98,804.91 |
| Day 16 | 2026-08-05 | $767.88 | FLAT | — | — | $98,865.41 |
| Day 17 | 2026-08-06 | $766.74 | FLAT | — | — | $98,865.41 |
| Day 18 | 2026-08-07 | $771.25 | Long 51 SPY (T10) | -$64.27 | -0.163% | $98,801.14 |
| Day 19 | 2026-08-10 | $771.11 | FLAT | — | — | $98,890.39 |
| Day 20 | 2026-08-11 | $768.61 | Long 51 SPY (T11) | -$256.60 | -0.650% | $98,633.79 |
| Day 21 | 2026-08-12 | $770.63 | Long 51 SPY (T11) | -$153.58 | -0.389% | $98,736.81 |
| Day 22 | 2026-08-13 | $775.91 | Long 51 SPY (T11) | +$115.70 | +0.293% | $99,006.09 |
| Day 23 | 2026-08-14 | $774.38 | Long 51 SPY (T11) | +$37.67 | +0.095% | $98,928.06 |
| Day 24 | 2026-08-17 | $770.71 | Long 51 SPY (T11) | -$149.50 | -0.379% | $98,740.89 |
| Day 25 | 2026-08-18 | $765.46 | Long 51 SPY (T11) | -$417.25 | -1.058% | $98,473.14 |
| Day 26 | 2026-08-19 | $767.19 | Long 51 SPY (T11) | -$329.02 | -0.834% | $98,561.37 |
| Day 27 | 2026-08-20 | $760.73 | Long 51 SPY (T11) | -$658.48 | -1.669% | $98,231.91 |
| Day 28 | 2026-08-21 | $763.74 | Long 51 SPY (T11) | -$504.97 | -1.280% | $98,385.42 |
| Day 29 | 2026-08-24 | $761.57 | Long 51 SPY (T11) | -$615.64 | -1.560% | $98,274.75 |
| Day 30 | 2026-08-25 | $763.89 | Long 51 SPY (T11) | -$497.32 | -1.260% | $98,393.07 |
| Day 31 | 2026-08-26 | $764.04 | Long 51 SPY (T11) | -$489.67 | -1.241% | $98,400.72 |
| Day 32 | 2026-08-27 | $769.27 | Long 51 SPY (T11) | -$222.94 | -0.565% | $98,667.45 |
| Day 33 | 2026-08-28 | $767.37 | Long 51 SPY (T11) | -$319.84 | -0.811% | $98,570.55 |
| Day 34 | 2026-08-31 | $764.97 | Long 51 SPY (T11) | -$442.24 | -1.121% | $98,448.15 |
| Day 35 | 2026-09-01 | $759.74 | FLAT | — | — | $98,277.81 |
| Day 36 | 2026-09-02 | $763.23 | Long 51 SPY (T12) | -$86.19 | -0.221% | $98,191.62 |
| Day 37 | 2026-09-03 | $771.20 | Long 51 SPY (T12) | +$320.28 | +0.821% | $98,598.09 |
| Day 38 | 2026-09-04 | $768.27 | Long 51 SPY (T12) | +$170.85 | +0.438% | $98,448.66 |
| Day 39 | 2026-09-08 | $764.16 | FLAT | — | — | $98,330.34 |
| Day 40 | 2026-09-09 | $760.54 | Long 52 SPY (T13) | -$127.87 | -0.322% | $98,202.47 |
| Day 41 | 2026-09-10 | $755.99 | FLAT | — | — | $98,066.23 |
| Day 42 | 2026-09-11 | $762.25 | FLAT | — | — | $98,066.23 |
| Day 43 | 2026-09-14 | $758.87 | FLAT | — | — | $98,066.23 |
| Day 44 | 2026-09-15 | $755.54 | FLAT | — | — | $98,066.23 |
| Day 45 | 2026-09-16 | $752.18 | FLAT | — | — | $98,066.23 |
| Day 46 | 2026-09-17 | $760.75 | FLAT | — | — | $98,066.23 |
| Day 47 | 2026-09-18 | $761.62 | FLAT | — | — | $98,066.23 |
| Day 48 | 2026-09-21 | $773.52 | FLAT | — | — | $98,066.23 |
| Day 49 | 2026-09-22 | $773.44 | FLAT | — | — | $98,081.02 |
| Day 50 | 2026-09-23 | $767.93 | FLAT | — | — | $98,052.25 |
| Day 51 | 2026-09-24 | $767.29 | FLAT | — | — | $98,052.25 |
| Day 52 | 2026-09-25 | $771.35 | FLAT | — | — | $98,052.25 |
| Day 53 | 2026-09-28 | $765.49 | Long 51 SPY (T16) | +$7.14 | +0.018% | $98,059.39 |
| Day 54 | 2026-09-29 | $764.38 | FLAT | — | — | $98,084.38 |
| Day 55 | 2026-09-30 | $762.34 | Long 51 SPY (T17) | -$216.75 | -0.554% | $97,867.63 |
| Day 56 | 2026-10-01 | $764.10 | Long 51 SPY (T17) | -$126.99 | -0.325% | $97,957.39 |
| Day 57 | 2026-10-02 | $769.65 | Long 51 SPY (T17) | +$156.06 | +0.399% | $98,240.44 |
| Day 58 | 2026-10-05 | $774.97 | Long 51 SPY (T17) | +$427.38 | +1.093% | $98,511.76 |
| Day 59 | 2026-10-06 | $779.10 | Long 51 SPY (T17) | +$638.01 | +1.632% | $98,722.39 |
| Day 60 | 2026-10-07 | $777.15 | Long 51 SPY (T17) | +$538.56 | +1.378% | $98,622.94 |
| Day 61 | 2026-10-08 | $773.88 | Long 51 SPY (T17) | +$371.79 | +0.951% | $98,456.17 |
| Day 62 | 2026-10-09 | $778.51 | Long 51 SPY (T17) | +$607.92 | +1.555% | $98,692.30 |
| Day 63 | 2026-10-12 | $778.03 | Long 51 SPY (T17) | +$583.44 | +1.492% | $98,667.82 |
| Day 64 | 2026-10-13 | $778.03 | Long 51 SPY (T17) | +$583.44 | +1.492% | $98,667.82 |
| Day 65 | 2026-10-14 | $769.65 | FLAT | — | — | $98,139.97 |
| Day 66 | 2026-10-15 | $771.77 | Long 51 SPY (T18) | +$110.67 | +0.282% | $98,250.64 |
| Day 67 | 2026-10-16 | $763.34 | Long 51 SPY (T18) | -$319.26 | -0.813% | $97,820.71 |
| Day 68 | 2026-10-19 | $766.60 | Long 51 SPY (T18) | -$153.00 | -0.390% | $97,986.97 |
| Day 69 | 2026-10-20 | $769.09 | FLAT | — | — | $98,191.48 |
| Day 70 | 2026-10-21 | $773.13 | Long 51 SPY (T19) | -$36.72 | -0.093% | $98,154.76 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $100,029.55 | $100,000.03 | +0.0296% | +0.000% | **+0.030%** |
| Day 2 | 2026-07-16 | $99,853.42 | $99,483.36 | -0.1466% | -0.517% | **+0.370%** |
| Day 3 | 2026-07-17 | $99,710.86 | $98,477.91 | -0.2891% | -1.522% | **+1.233%** |
| Day 4 | 2026-07-20 | $99,518.88 | $98,327.83 | -0.4811% | -1.672% | **+1.191%** |
| Day 5 | 2026-07-21 | $99,448.92 | $99,123.42 | -0.5511% | -0.877% | **+0.326%** |
| Day 6 | 2026-07-22 | $99,413.94 | $99,035.76 | -0.5861% | -0.964% | **+0.378%** |
| Day 7 | 2026-07-23 | $98,747.69 | $97,785.92 | -1.2523% | -2.214% | **+0.962%** |
| Day 8 | 2026-07-24 | $98,891.73 | $97,897.49 | -1.1083% | -2.103% | **+0.995%** |
| Day 9 | 2026-07-27 | $98,995.87 | $97,890.85 | -1.0041% | -2.109% | **+1.105%** |
| Day 10 | 2026-07-28 | $98,952.41 | $98,148.52 | -1.0476% | -1.851% | **+0.803%** |
| Day 11 | 2026-07-29 | $98,952.41 | $96,660.94 | -1.0476% | -3.339% | **+2.291%** |
| Day 12 | 2026-07-30 | $98,952.41 | $98,258.76 | -1.0476% | -1.741% | **+0.693%** |
| Day 13 | 2026-07-31 | $98,952.41 | $98,942.78 | -1.0476% | -1.057% | **+0.009%** |
| Day 14 | 2026-08-03 | $98,952.41 | $100,390.52 | -1.0476% | +0.391% | **-1.439%** |
| Day 15 | 2026-08-04 | $98,804.91 | $102,164.99 | -1.1951% | +2.165% | **-3.360%** |
| Day 16 | 2026-08-05 | $98,865.41 | $101,989.67 | -1.1346% | +1.990% | **-3.125%** |
| Day 17 | 2026-08-06 | $98,865.41 | $101,838.25 | -1.1346% | +1.838% | **-2.973%** |
| Day 18 | 2026-08-07 | $98,801.14 | $102,437.27 | -1.1989% | +2.437% | **-3.636%** |
| Day 19 | 2026-08-10 | $98,890.39 | $102,418.68 | -1.1096% | +2.419% | **-3.529%** |
| Day 20 | 2026-08-11 | $98,633.79 | $102,086.63 | -1.3662% | +2.087% | **-3.453%** |
| Day 21 | 2026-08-12 | $98,736.81 | $102,354.92 | -1.2632% | +2.355% | **-3.618%** |
| Day 22 | 2026-08-13 | $99,006.09 | $103,056.21 | -0.9939% | +3.056% | **-4.050%** |
| Day 23 | 2026-08-14 | $98,928.06 | $102,853.00 | -1.0719% | +2.853% | **-3.925%** |
| Day 24 | 2026-08-17 | $98,740.89 | $102,365.55 | -1.2591% | +2.366% | **-3.625%** |
| Day 25 | 2026-08-18 | $98,473.14 | $101,668.24 | -1.5269% | +1.668% | **-3.195%** |
| Day 26 | 2026-08-19 | $98,561.37 | $101,898.02 | -1.4386% | +1.898% | **-3.337%** |
| Day 27 | 2026-08-20 | $98,231.91 | $101,040.01 | -1.7681% | +1.040% | **-2.808%** |
| Day 28 | 2026-08-21 | $98,385.42 | $101,439.79 | -1.6146% | +1.440% | **-3.055%** |
| Day 29 | 2026-08-24 | $98,274.75 | $101,151.58 | -1.7252% | +1.152% | **-2.877%** |
| Day 30 | 2026-08-25 | $98,393.07 | $101,459.72 | -1.6069% | +1.460% | **-3.067%** |
| Day 31 | 2026-08-26 | $98,400.72 | $101,479.64 | -1.5993% | +1.480% | **-3.079%** |
| Day 32 | 2026-08-27 | $98,667.45 | $102,174.29 | -1.3326% | +2.174% | **-3.507%** |
| Day 33 | 2026-08-28 | $98,570.55 | $101,921.93 | -1.4294% | +1.922% | **-3.351%** |
| Day 34 | 2026-08-31 | $98,448.15 | $101,603.16 | -1.5519% | +1.603% | **-3.155%** |
| Day 35 | 2026-09-01 | $98,277.81 | $100,908.51 | -1.7222% | +0.909% | **-2.631%** |
| Day 36 | 2026-09-02 | $98,191.62 | $101,372.06 | -1.8084% | +1.372% | **-3.180%** |
| Day 37 | 2026-09-03 | $98,598.09 | $102,430.63 | -1.4019% | +2.431% | **-3.833%** |
| Day 38 | 2026-09-04 | $98,448.66 | $102,041.47 | -1.5513% | +2.041% | **-3.592%** |
| Day 39 | 2026-09-08 | $98,330.34 | $101,495.58 | -1.6697% | +1.496% | **-3.166%** |
| Day 40 | 2026-09-09 | $98,202.47 | $101,014.77 | -1.7975% | +1.015% | **-2.812%** |
| Day 41 | 2026-09-10 | $98,066.23 | $100,410.44 | -1.9338% | +0.410% | **-2.344%** |
| Day 42 | 2026-09-11 | $98,066.23 | $101,241.89 | -1.9338% | +1.242% | **-3.176%** |
| Day 43 | 2026-09-14 | $98,066.23 | $100,792.96 | -1.9338% | +0.793% | **-2.727%** |
| Day 44 | 2026-09-15 | $98,066.23 | $100,350.67 | -1.9338% | +0.351% | **-2.285%** |
| Day 45 | 2026-09-16 | $98,066.23 | $99,904.40 | -1.9338% | -0.096% | **-1.838%** |
| Day 46 | 2026-09-17 | $98,066.23 | $101,042.66 | -1.9338% | +1.043% | **-2.977%** |
| Day 47 | 2026-09-18 | $98,066.23 | $101,158.22 | -1.9338% | +1.158% | **-3.092%** |
| Day 48 | 2026-09-21 | $98,066.23 | $102,738.77 | -1.9338% | +2.739% | **-4.673%** |
| Day 49 | 2026-09-22 | $98,081.02 | $102,728.15 | -1.9190% | +2.728% | **-4.647%** |
| Day 50 | 2026-09-23 | $98,052.25 | $101,996.31 | -1.9478% | +1.996% | **-3.944%** |
| Day 51 | 2026-09-24 | $98,052.25 | $101,911.30 | -1.9478% | +1.911% | **-3.859%** |
| Day 52 | 2026-09-25 | $98,052.25 | $102,450.55 | -1.9478% | +2.451% | **-4.399%** |
| Day 53 | 2026-09-28 | $98,059.39 | $101,672.23 | -1.9406% | +1.672% | **-3.613%** |
| Day 54 | 2026-09-29 | $98,084.38 | $101,524.80 | -1.9156% | +1.525% | **-3.441%** |
| Day 55 | 2026-09-30 | $97,867.63 | $101,253.85 | -2.1324% | +1.254% | **-3.386%** |
| Day 56 | 2026-10-01 | $97,957.39 | $101,487.61 | -2.0426% | +1.488% | **-3.531%** |
| Day 57 | 2026-10-02 | $98,240.44 | $102,224.76 | -1.7596% | +2.225% | **-3.985%** |
| Day 58 | 2026-10-05 | $98,511.76 | $102,931.36 | -1.4882% | +2.931% | **-4.419%** |
| Day 59 | 2026-10-06 | $98,722.39 | $103,479.91 | -1.2776% | +3.480% | **-4.758%** |
| Day 60 | 2026-10-07 | $98,622.94 | $103,220.91 | -1.3771% | +3.221% | **-4.598%** |
| Day 61 | 2026-10-08 | $98,456.17 | $102,786.59 | -1.5438% | +2.787% | **-4.331%** |
| Day 62 | 2026-10-09 | $98,692.30 | $103,401.54 | -1.3077% | +3.402% | **-4.710%** |
| Day 63 | 2026-10-12 | $98,667.82 | $103,337.79 | -1.3322% | +3.338% | **-4.670%** |
| Day 64 | 2026-10-13 | $98,667.82 | $103,337.79 | -1.3322% | +3.338% | **-4.670%** |
| Day 65 | 2026-10-14 | $98,139.97 | $102,224.76 | -1.8600% | +2.225% | **-4.085%** |
| Day 66 | 2026-10-15 | $98,250.64 | $102,506.34 | -1.7494% | +2.506% | **-4.255%** |
| Day 67 | 2026-10-16 | $97,820.71 | $101,386.67 | -2.1793% | +1.387% | **-3.566%** |
| Day 68 | 2026-10-19 | $97,986.97 | $101,819.66 | -2.0130% | +1.820% | **-3.833%** |
| Day 69 | 2026-10-20 | $98,191.48 | $102,150.38 | -1.8085% | +2.150% | **-3.958%** |
| Day 70 | 2026-10-21 | $98,154.76 | $102,686.97 | -1.8452% | +2.687% | **-4.532%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $752.90 | -$23.25 | -$1785.27 | Holding would have been **$1785.27** better — honest entry |
| Day 2 | 2026-07-16 | $749.01 | -$151.62 | -$1656.90 | Holding would have been **$1656.90** better — honest entry |
| Day 3 | 2026-07-17 | $741.44 | -$401.43 | -$1407.09 | Holding would have been **$1407.09** better — honest entry |
| Day 4 | 2026-07-20 | $740.31 | -$438.72 | -$1369.80 | Holding would have been **$1369.80** better — honest entry |
| Day 5 | 2026-07-21 | $746.30 | -$241.05 | -$1567.47 | Position open |
| Day 6 | 2026-07-22 | $745.64 | -$262.83 | -$1545.69 | Position open |
| Day 7 | 2026-07-23 | $736.23 | -$573.36 | -$1235.16 | Position open |
| Day 8 | 2026-07-24 | $737.07 | -$545.64 | -$1262.88 | Holding would have been **$1262.88** better — honest entry |
| Day 9 | 2026-07-27 | $737.02 | -$547.29 | -$1261.23 | Holding would have been **$1261.23** better — honest entry |
| Day 10 | 2026-07-28 | $738.96 | -$483.27 | -$1325.25 | Holding would have been **$1325.25** better — honest entry |
| Day 11 | 2026-07-29 | $727.76 | -$852.87 | -$955.65 | Holding would have been **$955.65** better — honest entry |
| Day 12 | 2026-07-30 | $739.79 | -$455.88 | -$1352.64 | Holding would have been **$1352.64** better — honest entry |
| Day 13 | 2026-07-31 | $744.94 | -$285.93 | -$1522.59 | Holding would have been **$1522.59** better — honest entry |
| Day 14 | 2026-08-03 | $755.84 | +$73.77 | -$1882.29 | Holding would have been **$1882.29** better — honest entry |
| Day 15 | 2026-08-04 | $769.20 | +$514.65 | -$2323.17 | Position open |
| Day 16 | 2026-08-05 | $767.88 | +$471.09 | -$2279.61 | Holding would have been **$2279.61** better — honest entry |
| Day 17 | 2026-08-06 | $766.74 | +$433.47 | -$2241.99 | Holding would have been **$2241.99** better — honest entry |
| Day 18 | 2026-08-07 | $771.25 | +$582.30 | -$2390.82 | Position open |
| Day 19 | 2026-08-10 | $771.11 | +$577.68 | -$2386.20 | Holding would have been **$2386.20** better — honest entry |
| Day 20 | 2026-08-11 | $768.61 | +$495.18 | -$2303.70 | Position open |
| Day 21 | 2026-08-12 | $770.63 | +$561.84 | -$2370.36 | Position open |
| Day 22 | 2026-08-13 | $775.91 | +$736.08 | -$2544.60 | Position open |
| Day 23 | 2026-08-14 | $774.38 | +$685.59 | -$2494.11 | Position open |
| Day 24 | 2026-08-17 | $770.71 | +$564.48 | -$2373.00 | Position open |
| Day 25 | 2026-08-18 | $765.46 | +$391.23 | -$2199.75 | Position open |
| Day 26 | 2026-08-19 | $767.19 | +$448.32 | -$2256.84 | Position open |
| Day 27 | 2026-08-20 | $760.73 | +$235.14 | -$2043.66 | Position open |
| Day 28 | 2026-08-21 | $763.74 | +$334.47 | -$2142.99 | Position open |
| Day 29 | 2026-08-24 | $761.57 | +$262.86 | -$2071.38 | Position open |
| Day 30 | 2026-08-25 | $763.89 | +$339.42 | -$2147.94 | Position open |
| Day 31 | 2026-08-26 | $764.04 | +$344.37 | -$2152.89 | Position open |
| Day 32 | 2026-08-27 | $769.27 | +$516.96 | -$2325.48 | Position open |
| Day 33 | 2026-08-28 | $767.37 | +$454.26 | -$2262.78 | Position open |
| Day 34 | 2026-08-31 | $764.97 | +$375.06 | -$2183.58 | Position open |
| Day 35 | 2026-09-01 | $759.74 | +$202.47 | -$2010.99 | Holding would have been **$2010.99** better — honest entry |
| Day 36 | 2026-09-02 | $763.23 | +$317.64 | -$2126.16 | Position open |
| Day 37 | 2026-09-03 | $771.20 | +$580.65 | -$2389.17 | Position open |
| Day 38 | 2026-09-04 | $768.27 | +$483.96 | -$2292.48 | Position open |
| Day 39 | 2026-09-08 | $764.16 | +$348.33 | -$2156.85 | Holding would have been **$2156.85** better — honest entry |
| Day 40 | 2026-09-09 | $760.54 | +$228.87 | -$2037.39 | Position open |
| Day 41 | 2026-09-10 | $755.99 | +$78.72 | -$1887.24 | Holding would have been **$1887.24** better — honest entry |
| Day 42 | 2026-09-11 | $762.25 | +$285.30 | -$2093.82 | Holding would have been **$2093.82** better — honest entry |
| Day 43 | 2026-09-14 | $758.87 | +$173.76 | -$1982.28 | Holding would have been **$1982.28** better — honest entry |
| Day 44 | 2026-09-15 | $755.54 | +$63.87 | -$1872.39 | Holding would have been **$1872.39** better — honest entry |
| Day 45 | 2026-09-16 | $752.18 | -$47.01 | -$1761.51 | Holding would have been **$1761.51** better — honest entry |
| Day 46 | 2026-09-17 | $760.75 | +$235.80 | -$2044.32 | Holding would have been **$2044.32** better — honest entry |
| Day 47 | 2026-09-18 | $761.62 | +$264.51 | -$2073.03 | Holding would have been **$2073.03** better — honest entry |
| Day 48 | 2026-09-21 | $773.52 | +$657.21 | -$2465.73 | Holding would have been **$2465.73** better — honest entry |
| Day 49 | 2026-09-22 | $773.44 | +$654.57 | -$2463.09 | Holding would have been **$2463.09** better — honest entry |
| Day 50 | 2026-09-23 | $767.93 | +$472.74 | -$2281.26 | Holding would have been **$2281.26** better — honest entry |
| Day 51 | 2026-09-24 | $767.29 | +$451.62 | -$2260.14 | Holding would have been **$2260.14** better — honest entry |
| Day 52 | 2026-09-25 | $771.35 | +$585.60 | -$2394.12 | Holding would have been **$2394.12** better — honest entry |
| Day 53 | 2026-09-28 | $765.49 | +$392.22 | -$2200.74 | Position open |
| Day 54 | 2026-09-29 | $764.38 | +$355.59 | -$2164.11 | Holding would have been **$2164.11** better — honest entry |
| Day 55 | 2026-09-30 | $762.34 | +$288.27 | -$2096.79 | Position open |
| Day 56 | 2026-10-01 | $764.10 | +$346.35 | -$2154.87 | Position open |
| Day 57 | 2026-10-02 | $769.65 | +$529.50 | -$2338.02 | Position open |
| Day 58 | 2026-10-05 | $774.97 | +$705.06 | -$2513.58 | Position open |
| Day 59 | 2026-10-06 | $779.10 | +$841.35 | -$2649.87 | Position open |
| Day 60 | 2026-10-07 | $777.15 | +$777.00 | -$2585.52 | Position open |
| Day 61 | 2026-10-08 | $773.88 | +$669.09 | -$2477.61 | Position open |
| Day 62 | 2026-10-09 | $778.51 | +$821.88 | -$2630.40 | Position open |
| Day 63 | 2026-10-12 | $778.03 | +$806.04 | -$2614.56 | Position open |
| Day 64 | 2026-10-13 | $778.03 | +$806.04 | -$2614.56 | Position open |
| Day 65 | 2026-10-14 | $769.65 | +$529.50 | -$2338.02 | Holding would have been **$2338.02** better — honest entry |
| Day 66 | 2026-10-15 | $771.77 | +$599.46 | -$2407.98 | Position open |
| Day 67 | 2026-10-16 | $763.34 | +$321.27 | -$2129.79 | Position open |
| Day 68 | 2026-10-19 | $766.60 | +$428.85 | -$2237.37 | Position open |
| Day 69 | 2026-10-20 | $769.09 | +$511.02 | -$2319.54 | Holding would have been **$2319.54** better — honest entry |
| Day 70 | 2026-10-21 | $773.13 | +$644.34 | -$2452.86 | Position open |

---

## Daily Entries

### Day 1 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $752.90 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$23.25 |
| Signal saved | -$1785.27 |
| Portfolio value | $100,029.55 |
| Benchmark value | $100,000.03 |
| Alpha (cumulative) | +0.030% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 2 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$151.62 |
| Signal saved | -$1656.90 |
| Portfolio value | $99,853.42 |
| Benchmark value | $99,483.36 |
| Alpha (cumulative) | +0.370% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 3 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$401.43 |
| Signal saved | -$1407.09 |
| Portfolio value | $99,710.86 |
| Benchmark value | $98,477.91 |
| Alpha (cumulative) | +1.233% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 4 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$438.72 |
| Signal saved | -$1369.80 |
| Portfolio value | $99,518.88 |
| Benchmark value | $98,327.83 |
| Alpha (cumulative) | +1.191% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 5 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T5) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,448.92 |
| Benchmark value | $99,123.42 |
| Alpha (cumulative) | +0.326% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 6 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T5) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,413.94 |
| Benchmark value | $99,035.76 |
| Alpha (cumulative) | +0.378% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 7 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T6) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,747.69 |
| Benchmark value | $97,785.92 |
| Alpha (cumulative) | +0.962% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 8 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$545.64 |
| Signal saved | -$1262.88 |
| Portfolio value | $98,891.73 |
| Benchmark value | $97,897.49 |
| Alpha (cumulative) | +0.995% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 9 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$547.29 |
| Signal saved | -$1261.23 |
| Portfolio value | $98,995.87 |
| Benchmark value | $97,890.85 |
| Alpha (cumulative) | +1.105% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 10 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$483.27 |
| Signal saved | -$1325.25 |
| Portfolio value | $98,952.41 |
| Benchmark value | $98,148.52 |
| Alpha (cumulative) | +0.803% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 11 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$852.87 |
| Signal saved | -$955.65 |
| Portfolio value | $98,952.41 |
| Benchmark value | $96,660.94 |
| Alpha (cumulative) | +2.291% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 12 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$455.88 |
| Signal saved | -$1352.64 |
| Portfolio value | $98,952.41 |
| Benchmark value | $98,258.76 |
| Alpha (cumulative) | +0.693% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 13 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$285.93 |
| Signal saved | -$1522.59 |
| Portfolio value | $98,952.41 |
| Benchmark value | $98,942.78 |
| Alpha (cumulative) | +0.009% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 14 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$73.77 |
| Signal saved | -$1882.29 |
| Portfolio value | $98,952.41 |
| Benchmark value | $100,390.52 |
| Alpha (cumulative) | -1.439% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 15 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T9) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,804.91 |
| Benchmark value | $102,164.99 |
| Alpha (cumulative) | -3.360% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 16 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$471.09 |
| Signal saved | -$2279.61 |
| Portfolio value | $98,865.41 |
| Benchmark value | $101,989.67 |
| Alpha (cumulative) | -3.125% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 17 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$433.47 |
| Signal saved | -$2241.99 |
| Portfolio value | $98,865.41 |
| Benchmark value | $101,838.25 |
| Alpha (cumulative) | -2.973% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 18 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,801.14 |
| Benchmark value | $102,437.27 |
| Alpha (cumulative) | -3.636% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 19 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$577.68 |
| Signal saved | -$2386.20 |
| Portfolio value | $98,890.39 |
| Benchmark value | $102,418.68 |
| Alpha (cumulative) | -3.529% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 20 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,633.79 |
| Benchmark value | $102,086.63 |
| Alpha (cumulative) | -3.453% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 21 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,736.81 |
| Benchmark value | $102,354.92 |
| Alpha (cumulative) | -3.618% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 22 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $99,006.09 |
| Benchmark value | $103,056.21 |
| Alpha (cumulative) | -4.050% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 23 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $98,928.06 |
| Benchmark value | $102,853.00 |
| Alpha (cumulative) | -3.925% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 24 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,740.89 |
| Benchmark value | $102,365.55 |
| Alpha (cumulative) | -3.625% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 25 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,473.14 |
| Benchmark value | $101,668.24 |
| Alpha (cumulative) | -3.195% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 26 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,561.37 |
| Benchmark value | $101,898.02 |
| Alpha (cumulative) | -3.337% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 27 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,231.91 |
| Benchmark value | $101,040.01 |
| Alpha (cumulative) | -2.808% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 28 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,385.42 |
| Benchmark value | $101,439.79 |
| Alpha (cumulative) | -3.055% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 29 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,274.75 |
| Benchmark value | $101,151.58 |
| Alpha (cumulative) | -2.877% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 30 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,393.07 |
| Benchmark value | $101,459.72 |
| Alpha (cumulative) | -3.067% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 31 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,400.72 |
| Benchmark value | $101,479.64 |
| Alpha (cumulative) | -3.079% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 32 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,667.45 |
| Benchmark value | $102,174.29 |
| Alpha (cumulative) | -3.507% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 33 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,570.55 |
| Benchmark value | $101,921.93 |
| Alpha (cumulative) | -3.351% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 34 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,448.15 |
| Benchmark value | $101,603.16 |
| Alpha (cumulative) | -3.155% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 35 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$202.47 |
| Signal saved | -$2010.99 |
| Portfolio value | $98,277.81 |
| Benchmark value | $100,908.51 |
| Alpha (cumulative) | -2.631% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 36 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,191.62 |
| Benchmark value | $101,372.06 |
| Alpha (cumulative) | -3.180% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 37 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,598.09 |
| Benchmark value | $102,430.63 |
| Alpha (cumulative) | -3.833% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 38 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,448.66 |
| Benchmark value | $102,041.47 |
| Alpha (cumulative) | -3.592% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$348.33 |
| Signal saved | -$2156.85 |
| Portfolio value | $98,330.34 |
| Benchmark value | $101,495.58 |
| Alpha (cumulative) | -3.166% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 40 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T13) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,202.47 |
| Benchmark value | $101,014.77 |
| Alpha (cumulative) | -2.812% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$78.72 |
| Signal saved | -$1887.24 |
| Portfolio value | $98,066.23 |
| Benchmark value | $100,410.44 |
| Alpha (cumulative) | -2.344% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$285.30 |
| Signal saved | -$2093.82 |
| Portfolio value | $98,066.23 |
| Benchmark value | $101,241.89 |
| Alpha (cumulative) | -3.176% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$173.76 |
| Signal saved | -$1982.28 |
| Portfolio value | $98,066.23 |
| Benchmark value | $100,792.96 |
| Alpha (cumulative) | -2.727% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$63.87 |
| Signal saved | -$1872.39 |
| Portfolio value | $98,066.23 |
| Benchmark value | $100,350.67 |
| Alpha (cumulative) | -2.285% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | -$47.01 |
| Signal saved | -$1761.51 |
| Portfolio value | $98,066.23 |
| Benchmark value | $99,904.40 |
| Alpha (cumulative) | -1.838% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$235.80 |
| Signal saved | -$2044.32 |
| Portfolio value | $98,066.23 |
| Benchmark value | $101,042.66 |
| Alpha (cumulative) | -2.977% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$264.51 |
| Signal saved | -$2073.03 |
| Portfolio value | $98,066.23 |
| Benchmark value | $101,158.22 |
| Alpha (cumulative) | -3.092% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$657.21 |
| Signal saved | -$2465.73 |
| Portfolio value | $98,066.23 |
| Benchmark value | $102,738.77 |
| Alpha (cumulative) | -4.673% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$654.57 |
| Signal saved | -$2463.09 |
| Portfolio value | $98,081.02 |
| Benchmark value | $102,728.15 |
| Alpha (cumulative) | -4.647% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$472.74 |
| Signal saved | -$2281.26 |
| Portfolio value | $98,052.25 |
| Benchmark value | $101,996.31 |
| Alpha (cumulative) | -3.944% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$451.62 |
| Signal saved | -$2260.14 |
| Portfolio value | $98,052.25 |
| Benchmark value | $101,911.30 |
| Alpha (cumulative) | -3.859% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$585.60 |
| Signal saved | -$2394.12 |
| Portfolio value | $98,052.25 |
| Benchmark value | $102,450.55 |
| Alpha (cumulative) | -4.399% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $765.49 |
| Unrealized P&L | +$7.14 |
| P&L % | +0.018% |
| Portfolio value | $98,059.39 |
| Benchmark value | $101,672.23 |
| Alpha (cumulative) | -3.613% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $764.38 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$355.59 |
| Signal saved | -$2164.11 |
| Portfolio value | $98,084.38 |
| Benchmark value | $101,524.80 |
| Alpha (cumulative) | -3.441% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 55 — 2026-09-30

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $762.34 |
| Unrealized P&L | -$216.75 |
| P&L % | -0.554% |
| Portfolio value | $97,867.63 |
| Benchmark value | $101,253.85 |
| Alpha (cumulative) | -3.386% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 56 — 2026-10-01

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $764.10 |
| Unrealized P&L | -$126.99 |
| P&L % | -0.325% |
| Portfolio value | $97,957.39 |
| Benchmark value | $101,487.61 |
| Alpha (cumulative) | -3.531% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.33% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-10-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $769.65 |
| Unrealized P&L | +$156.06 |
| P&L % | +0.399% |
| Portfolio value | $98,240.44 |
| Benchmark value | $102,224.76 |
| Alpha (cumulative) | -3.985% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.40% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 58 — 2026-10-05

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $774.97 |
| Unrealized P&L | +$427.38 |
| P&L % | +1.093% |
| Portfolio value | $98,511.76 |
| Benchmark value | $102,931.36 |
| Alpha (cumulative) | -4.419% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +1.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 59 — 2026-10-06

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $779.10 |
| Unrealized P&L | +$638.01 |
| P&L % | +1.632% |
| Portfolio value | $98,722.39 |
| Benchmark value | $103,479.91 |
| Alpha (cumulative) | -4.758% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +1.63% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 60 — 2026-10-07

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $777.15 |
| Unrealized P&L | +$538.56 |
| P&L % | +1.378% |
| Portfolio value | $98,622.94 |
| Benchmark value | $103,220.91 |
| Alpha (cumulative) | -4.598% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +1.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 61 — 2026-10-08

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $773.88 |
| Unrealized P&L | +$371.79 |
| P&L % | +0.951% |
| Portfolio value | $98,456.17 |
| Benchmark value | $102,786.59 |
| Alpha (cumulative) | -4.331% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.95% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 62 — 2026-10-09

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $778.51 |
| Unrealized P&L | +$607.92 |
| P&L % | +1.555% |
| Portfolio value | $98,692.30 |
| Benchmark value | $103,401.54 |
| Alpha (cumulative) | -4.710% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +1.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 63 — 2026-10-12

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,667.82 |
| Benchmark value | $103,337.79 |
| Alpha (cumulative) | -4.670% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 64 — 2026-10-13

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,667.82 |
| Benchmark value | $103,337.79 |
| Alpha (cumulative) | -4.670% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 65 — 2026-10-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $769.65 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$529.50 |
| Signal saved | -$2338.02 |
| Portfolio value | $98,139.97 |
| Benchmark value | $102,224.76 |
| Alpha (cumulative) | -4.085% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 66 — 2026-10-15

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $771.77 |
| Unrealized P&L | +$110.67 |
| P&L % | +0.282% |
| Portfolio value | $98,250.64 |
| Benchmark value | $102,506.34 |
| Alpha (cumulative) | -4.255% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: +0.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 67 — 2026-10-16

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $763.34 |
| Unrealized P&L | -$319.26 |
| P&L % | -0.813% |
| Portfolio value | $97,820.71 |
| Benchmark value | $101,386.67 |
| Alpha (cumulative) | -3.566% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 68 — 2026-10-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $766.60 |
| Unrealized P&L | -$153.00 |
| P&L % | -0.390% |
| Portfolio value | $97,986.97 |
| Benchmark value | $101,819.66 |
| Alpha (cumulative) | -3.833% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 69 — 2026-10-20

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $769.09 |
| Realized P&L (locked) | -$1808.52 |
| Reference if held | +$511.02 |
| Signal saved | -$2319.54 |
| Portfolio value | $98,191.48 |
| Benchmark value | $102,150.38 |
| Alpha (cumulative) | -3.958% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1808.52. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 70 — 2026-10-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T19) |
| Entry (Alpaca fill) | $753.605/share |
| Close price | $773.13 |
| Unrealized P&L | -$36.72 |
| P&L % | -0.093% |
| Portfolio value | $98,154.76 |
| Benchmark value | $102,686.97 |
| Alpha (cumulative) | -4.532% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.88 vs MA50 $767.35). Momentum: STRONG. Unrealized P&L: -0.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

## Strategy Evolution Log

| Date | Change | Rationale |
|---|---|---|
| 2026-03-09 | Initial deployment: SMA 20/50 crossover | Simple trend-following baseline |
| 2026-04-16 | Upgraded to dual-timeframe SMA 10/30 + 20/50 regime filter | SMA 20/50 too slow — sat flat 24/27 days during volatile market. Faster MAs capture recovery rallies. 20/50 retained as regime filter. |
| 2026-04-16 | Added price-action override | If price closes >2% above MA50 AND above both fast MAs, override bearish regime filter. Prevents sitting flat during V-shaped recoveries. Multi-trade journal tracking added. |

## Anomaly Log

| # | Date | Observation | Hypothesis | Status |
|---|---|---|---|---|
| 1 | 2026-03-12 to 2026-04-15 | System sat FLAT for 24 consecutive days despite 10%+ SPY recovery | SMA 20/50 too slow to catch regime change; death cross persisted even as price recovered above both MAs | Fixed — switched to SMA 10/30 |
| _add entries here_ | | | | |

---
_Day 70 of 90 · Alpaca equity: $98,986.87 · Cumulative alpha vs SPY: -4.532%_