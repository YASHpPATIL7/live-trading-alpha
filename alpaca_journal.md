# ALPACA PAPER JOURNAL — SPY
_Last updated: October 23, 2026 | Day 72 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$753.610/share**
> (2026-07-15, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-10-23): **BULLISH**  
> Fast: MA10 $771.19 | MA30 $768.26  
> Slow: MA20 $770.72 | MA50 $767.22  
> Regime: **BULL** | Momentum: **WEAK** | Session: REGULAR

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

**Total trades:** 19 | **Closed:** 19 | **Open:** No | **Cumulative Realized P&L:** -$2429.69

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $753.610 (2026-07-15) | $754.500 (2026-07-15) | 8 | +$7.12 | ✅ Closed |
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
| T19 | $773.850 (2026-10-21) | $762.110 (2026-10-22) | 51 | -$598.74 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $98,596.51 |
| Alpaca cash | $59,806.42 |
| Cumulative realized P&L | -$2429.69 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $752.90 | FLAT | — | — | $100,007.12 |
| Day 2 | 2026-07-16 | $749.01 | FLAT | — | — | $99,830.99 |
| Day 3 | 2026-07-17 | $741.44 | FLAT | — | — | $99,688.43 |
| Day 4 | 2026-07-20 | $740.31 | FLAT | — | — | $99,496.45 |
| Day 5 | 2026-07-21 | $746.30 | Long 53 SPY (T5) | -$69.96 | -0.177% | $99,426.49 |
| Day 6 | 2026-07-22 | $745.64 | Long 53 SPY (T5) | -$104.94 | -0.265% | $99,391.51 |
| Day 7 | 2026-07-23 | $736.23 | Long 52 SPY (T6) | -$135.72 | -0.353% | $98,725.26 |
| Day 8 | 2026-07-24 | $737.07 | FLAT | — | — | $98,869.30 |
| Day 9 | 2026-07-27 | $737.02 | FLAT | — | — | $98,973.44 |
| Day 10 | 2026-07-28 | $738.96 | FLAT | — | — | $98,929.98 |
| Day 11 | 2026-07-29 | $727.76 | FLAT | — | — | $98,929.98 |
| Day 12 | 2026-07-30 | $739.79 | FLAT | — | — | $98,929.98 |
| Day 13 | 2026-07-31 | $744.94 | FLAT | — | — | $98,929.98 |
| Day 14 | 2026-08-03 | $755.84 | FLAT | — | — | $98,929.98 |
| Day 15 | 2026-08-04 | $769.20 | Long 50 SPY (T9) | -$147.50 | -0.382% | $98,782.48 |
| Day 16 | 2026-08-05 | $767.88 | FLAT | — | — | $98,842.98 |
| Day 17 | 2026-08-06 | $766.74 | FLAT | — | — | $98,842.98 |
| Day 18 | 2026-08-07 | $771.25 | Long 51 SPY (T10) | -$64.27 | -0.163% | $98,778.71 |
| Day 19 | 2026-08-10 | $771.11 | FLAT | — | — | $98,867.96 |
| Day 20 | 2026-08-11 | $768.61 | Long 51 SPY (T11) | -$256.60 | -0.650% | $98,611.36 |
| Day 21 | 2026-08-12 | $770.63 | Long 51 SPY (T11) | -$153.58 | -0.389% | $98,714.38 |
| Day 22 | 2026-08-13 | $775.91 | Long 51 SPY (T11) | +$115.70 | +0.293% | $98,983.66 |
| Day 23 | 2026-08-14 | $774.38 | Long 51 SPY (T11) | +$37.67 | +0.095% | $98,905.63 |
| Day 24 | 2026-08-17 | $770.71 | Long 51 SPY (T11) | -$149.50 | -0.379% | $98,718.46 |
| Day 25 | 2026-08-18 | $765.46 | Long 51 SPY (T11) | -$417.25 | -1.058% | $98,450.71 |
| Day 26 | 2026-08-19 | $767.19 | Long 51 SPY (T11) | -$329.02 | -0.834% | $98,538.94 |
| Day 27 | 2026-08-20 | $760.73 | Long 51 SPY (T11) | -$658.48 | -1.669% | $98,209.48 |
| Day 28 | 2026-08-21 | $763.74 | Long 51 SPY (T11) | -$504.97 | -1.280% | $98,362.99 |
| Day 29 | 2026-08-24 | $761.57 | Long 51 SPY (T11) | -$615.64 | -1.560% | $98,252.32 |
| Day 30 | 2026-08-25 | $763.89 | Long 51 SPY (T11) | -$497.32 | -1.260% | $98,370.64 |
| Day 31 | 2026-08-26 | $764.04 | Long 51 SPY (T11) | -$489.67 | -1.241% | $98,378.29 |
| Day 32 | 2026-08-27 | $769.27 | Long 51 SPY (T11) | -$222.94 | -0.565% | $98,645.02 |
| Day 33 | 2026-08-28 | $767.37 | Long 51 SPY (T11) | -$319.84 | -0.811% | $98,548.12 |
| Day 34 | 2026-08-31 | $764.97 | Long 51 SPY (T11) | -$442.24 | -1.121% | $98,425.72 |
| Day 35 | 2026-09-01 | $759.74 | FLAT | — | — | $98,255.38 |
| Day 36 | 2026-09-02 | $763.23 | Long 51 SPY (T12) | -$86.19 | -0.221% | $98,169.19 |
| Day 37 | 2026-09-03 | $771.20 | Long 51 SPY (T12) | +$320.28 | +0.821% | $98,575.66 |
| Day 38 | 2026-09-04 | $768.27 | Long 51 SPY (T12) | +$170.85 | +0.438% | $98,426.23 |
| Day 39 | 2026-09-08 | $764.16 | FLAT | — | — | $98,307.91 |
| Day 40 | 2026-09-09 | $760.54 | Long 52 SPY (T13) | -$127.87 | -0.322% | $98,180.04 |
| Day 41 | 2026-09-10 | $755.99 | FLAT | — | — | $98,043.80 |
| Day 42 | 2026-09-11 | $762.25 | FLAT | — | — | $98,043.80 |
| Day 43 | 2026-09-14 | $758.87 | FLAT | — | — | $98,043.80 |
| Day 44 | 2026-09-15 | $755.54 | FLAT | — | — | $98,043.80 |
| Day 45 | 2026-09-16 | $752.18 | FLAT | — | — | $98,043.80 |
| Day 46 | 2026-09-17 | $760.75 | FLAT | — | — | $98,043.80 |
| Day 47 | 2026-09-18 | $761.62 | FLAT | — | — | $98,043.80 |
| Day 48 | 2026-09-21 | $773.52 | FLAT | — | — | $98,043.80 |
| Day 49 | 2026-09-22 | $773.44 | FLAT | — | — | $98,058.59 |
| Day 50 | 2026-09-23 | $767.93 | FLAT | — | — | $98,029.82 |
| Day 51 | 2026-09-24 | $767.29 | FLAT | — | — | $98,029.82 |
| Day 52 | 2026-09-25 | $771.35 | FLAT | — | — | $98,029.82 |
| Day 53 | 2026-09-28 | $765.49 | Long 51 SPY (T16) | +$7.14 | +0.018% | $98,036.96 |
| Day 54 | 2026-09-29 | $764.38 | FLAT | — | — | $98,061.95 |
| Day 55 | 2026-09-30 | $762.34 | Long 51 SPY (T17) | -$216.75 | -0.554% | $97,845.20 |
| Day 56 | 2026-10-01 | $764.10 | Long 51 SPY (T17) | -$126.99 | -0.325% | $97,934.96 |
| Day 57 | 2026-10-02 | $769.65 | Long 51 SPY (T17) | +$156.06 | +0.399% | $98,218.01 |
| Day 58 | 2026-10-05 | $774.97 | Long 51 SPY (T17) | +$427.38 | +1.093% | $98,489.33 |
| Day 59 | 2026-10-06 | $779.10 | Long 51 SPY (T17) | +$638.01 | +1.632% | $98,699.96 |
| Day 60 | 2026-10-07 | $777.15 | Long 51 SPY (T17) | +$538.56 | +1.378% | $98,600.51 |
| Day 61 | 2026-10-08 | $773.88 | Long 51 SPY (T17) | +$371.79 | +0.951% | $98,433.74 |
| Day 62 | 2026-10-09 | $778.51 | Long 51 SPY (T17) | +$607.92 | +1.555% | $98,669.87 |
| Day 63 | 2026-10-12 | $778.03 | Long 51 SPY (T17) | +$583.44 | +1.492% | $98,645.39 |
| Day 64 | 2026-10-13 | $778.03 | Long 51 SPY (T17) | +$583.44 | +1.492% | $98,645.39 |
| Day 65 | 2026-10-14 | $769.65 | FLAT | — | — | $98,117.54 |
| Day 66 | 2026-10-15 | $771.77 | Long 51 SPY (T18) | +$110.67 | +0.282% | $98,228.21 |
| Day 67 | 2026-10-16 | $763.34 | Long 51 SPY (T18) | -$319.26 | -0.813% | $97,798.28 |
| Day 68 | 2026-10-19 | $766.60 | Long 51 SPY (T18) | -$153.00 | -0.390% | $97,964.54 |
| Day 69 | 2026-10-20 | $769.09 | FLAT | — | — | $98,169.05 |
| Day 70 | 2026-10-21 | $773.13 | Long 51 SPY (T19) | -$36.72 | -0.093% | $98,132.33 |
| Day 71 | 2026-10-22 | $764.03 | FLAT | — | — | $97,570.31 |
| Day 72 | 2026-10-23 | $760.70 | FLAT | — | — | $97,570.31 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $100,007.12 | $100,000.03 | +0.0071% | +0.000% | **+0.007%** |
| Day 2 | 2026-07-16 | $99,830.99 | $99,483.36 | -0.1690% | -0.517% | **+0.348%** |
| Day 3 | 2026-07-17 | $99,688.43 | $98,477.91 | -0.3116% | -1.522% | **+1.210%** |
| Day 4 | 2026-07-20 | $99,496.45 | $98,327.83 | -0.5036% | -1.672% | **+1.168%** |
| Day 5 | 2026-07-21 | $99,426.49 | $99,123.42 | -0.5735% | -0.877% | **+0.304%** |
| Day 6 | 2026-07-22 | $99,391.51 | $99,035.76 | -0.6085% | -0.964% | **+0.355%** |
| Day 7 | 2026-07-23 | $98,725.26 | $97,785.92 | -1.2747% | -2.214% | **+0.939%** |
| Day 8 | 2026-07-24 | $98,869.30 | $97,897.49 | -1.1307% | -2.103% | **+0.972%** |
| Day 9 | 2026-07-27 | $98,973.44 | $97,890.85 | -1.0266% | -2.109% | **+1.082%** |
| Day 10 | 2026-07-28 | $98,929.98 | $98,148.52 | -1.0700% | -1.851% | **+0.781%** |
| Day 11 | 2026-07-29 | $98,929.98 | $96,660.94 | -1.0700% | -3.339% | **+2.269%** |
| Day 12 | 2026-07-30 | $98,929.98 | $98,258.76 | -1.0700% | -1.741% | **+0.671%** |
| Day 13 | 2026-07-31 | $98,929.98 | $98,942.78 | -1.0700% | -1.057% | **-0.013%** |
| Day 14 | 2026-08-03 | $98,929.98 | $100,390.52 | -1.0700% | +0.391% | **-1.461%** |
| Day 15 | 2026-08-04 | $98,782.48 | $102,164.99 | -1.2175% | +2.165% | **-3.383%** |
| Day 16 | 2026-08-05 | $98,842.98 | $101,989.67 | -1.1570% | +1.990% | **-3.147%** |
| Day 17 | 2026-08-06 | $98,842.98 | $101,838.25 | -1.1570% | +1.838% | **-2.995%** |
| Day 18 | 2026-08-07 | $98,778.71 | $102,437.27 | -1.2213% | +2.437% | **-3.658%** |
| Day 19 | 2026-08-10 | $98,867.96 | $102,418.68 | -1.1320% | +2.419% | **-3.551%** |
| Day 20 | 2026-08-11 | $98,611.36 | $102,086.63 | -1.3886% | +2.087% | **-3.476%** |
| Day 21 | 2026-08-12 | $98,714.38 | $102,354.92 | -1.2856% | +2.355% | **-3.641%** |
| Day 22 | 2026-08-13 | $98,983.66 | $103,056.21 | -1.0163% | +3.056% | **-4.072%** |
| Day 23 | 2026-08-14 | $98,905.63 | $102,853.00 | -1.0944% | +2.853% | **-3.947%** |
| Day 24 | 2026-08-17 | $98,718.46 | $102,365.55 | -1.2815% | +2.366% | **-3.648%** |
| Day 25 | 2026-08-18 | $98,450.71 | $101,668.24 | -1.5493% | +1.668% | **-3.217%** |
| Day 26 | 2026-08-19 | $98,538.94 | $101,898.02 | -1.4611% | +1.898% | **-3.359%** |
| Day 27 | 2026-08-20 | $98,209.48 | $101,040.01 | -1.7905% | +1.040% | **-2.830%** |
| Day 28 | 2026-08-21 | $98,362.99 | $101,439.79 | -1.6370% | +1.440% | **-3.077%** |
| Day 29 | 2026-08-24 | $98,252.32 | $101,151.58 | -1.7477% | +1.152% | **-2.900%** |
| Day 30 | 2026-08-25 | $98,370.64 | $101,459.72 | -1.6294% | +1.460% | **-3.089%** |
| Day 31 | 2026-08-26 | $98,378.29 | $101,479.64 | -1.6217% | +1.480% | **-3.102%** |
| Day 32 | 2026-08-27 | $98,645.02 | $102,174.29 | -1.3550% | +2.174% | **-3.529%** |
| Day 33 | 2026-08-28 | $98,548.12 | $101,921.93 | -1.4519% | +1.922% | **-3.374%** |
| Day 34 | 2026-08-31 | $98,425.72 | $101,603.16 | -1.5743% | +1.603% | **-3.177%** |
| Day 35 | 2026-09-01 | $98,255.38 | $100,908.51 | -1.7446% | +0.909% | **-2.654%** |
| Day 36 | 2026-09-02 | $98,169.19 | $101,372.06 | -1.8308% | +1.372% | **-3.203%** |
| Day 37 | 2026-09-03 | $98,575.66 | $102,430.63 | -1.4243% | +2.431% | **-3.855%** |
| Day 38 | 2026-09-04 | $98,426.23 | $102,041.47 | -1.5738% | +2.041% | **-3.615%** |
| Day 39 | 2026-09-08 | $98,307.91 | $101,495.58 | -1.6921% | +1.496% | **-3.188%** |
| Day 40 | 2026-09-09 | $98,180.04 | $101,014.77 | -1.8200% | +1.015% | **-2.835%** |
| Day 41 | 2026-09-10 | $98,043.80 | $100,410.44 | -1.9562% | +0.410% | **-2.366%** |
| Day 42 | 2026-09-11 | $98,043.80 | $101,241.89 | -1.9562% | +1.242% | **-3.198%** |
| Day 43 | 2026-09-14 | $98,043.80 | $100,792.96 | -1.9562% | +0.793% | **-2.749%** |
| Day 44 | 2026-09-15 | $98,043.80 | $100,350.67 | -1.9562% | +0.351% | **-2.307%** |
| Day 45 | 2026-09-16 | $98,043.80 | $99,904.40 | -1.9562% | -0.096% | **-1.860%** |
| Day 46 | 2026-09-17 | $98,043.80 | $101,042.66 | -1.9562% | +1.043% | **-2.999%** |
| Day 47 | 2026-09-18 | $98,043.80 | $101,158.22 | -1.9562% | +1.158% | **-3.114%** |
| Day 48 | 2026-09-21 | $98,043.80 | $102,738.77 | -1.9562% | +2.739% | **-4.695%** |
| Day 49 | 2026-09-22 | $98,058.59 | $102,728.15 | -1.9414% | +2.728% | **-4.669%** |
| Day 50 | 2026-09-23 | $98,029.82 | $101,996.31 | -1.9702% | +1.996% | **-3.966%** |
| Day 51 | 2026-09-24 | $98,029.82 | $101,911.30 | -1.9702% | +1.911% | **-3.881%** |
| Day 52 | 2026-09-25 | $98,029.82 | $102,450.55 | -1.9702% | +2.451% | **-4.421%** |
| Day 53 | 2026-09-28 | $98,036.96 | $101,672.23 | -1.9630% | +1.672% | **-3.635%** |
| Day 54 | 2026-09-29 | $98,061.95 | $101,524.80 | -1.9381% | +1.525% | **-3.463%** |
| Day 55 | 2026-09-30 | $97,845.20 | $101,253.85 | -2.1548% | +1.254% | **-3.409%** |
| Day 56 | 2026-10-01 | $97,934.96 | $101,487.61 | -2.0650% | +1.488% | **-3.553%** |
| Day 57 | 2026-10-02 | $98,218.01 | $102,224.76 | -1.7820% | +2.225% | **-4.007%** |
| Day 58 | 2026-10-05 | $98,489.33 | $102,931.36 | -1.5107% | +2.931% | **-4.442%** |
| Day 59 | 2026-10-06 | $98,699.96 | $103,479.91 | -1.3000% | +3.480% | **-4.780%** |
| Day 60 | 2026-10-07 | $98,600.51 | $103,220.91 | -1.3995% | +3.221% | **-4.620%** |
| Day 61 | 2026-10-08 | $98,433.74 | $102,786.59 | -1.5663% | +2.787% | **-4.353%** |
| Day 62 | 2026-10-09 | $98,669.87 | $103,401.54 | -1.3301% | +3.402% | **-4.732%** |
| Day 63 | 2026-10-12 | $98,645.39 | $103,337.79 | -1.3546% | +3.338% | **-4.693%** |
| Day 64 | 2026-10-13 | $98,645.39 | $103,337.79 | -1.3546% | +3.338% | **-4.693%** |
| Day 65 | 2026-10-14 | $98,117.54 | $102,224.76 | -1.8825% | +2.225% | **-4.108%** |
| Day 66 | 2026-10-15 | $98,228.21 | $102,506.34 | -1.7718% | +2.506% | **-4.278%** |
| Day 67 | 2026-10-16 | $97,798.28 | $101,386.67 | -2.2017% | +1.387% | **-3.589%** |
| Day 68 | 2026-10-19 | $97,964.54 | $101,819.66 | -2.0355% | +1.820% | **-3.856%** |
| Day 69 | 2026-10-20 | $98,169.05 | $102,150.38 | -1.8309% | +2.150% | **-3.981%** |
| Day 70 | 2026-10-21 | $98,132.33 | $102,686.97 | -1.8677% | +2.687% | **-4.555%** |
| Day 71 | 2026-10-22 | $97,570.31 | $101,478.31 | -2.4297% | +1.478% | **-3.908%** |
| Day 72 | 2026-10-23 | $97,570.31 | $101,036.02 | -2.4297% | +1.036% | **-3.466%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $752.90 | -$5.68 | -$2424.01 | Holding would have been **$2424.01** better — honest entry |
| Day 2 | 2026-07-16 | $749.01 | -$36.80 | -$2392.89 | Holding would have been **$2392.89** better — honest entry |
| Day 3 | 2026-07-17 | $741.44 | -$97.36 | -$2332.33 | Holding would have been **$2332.33** better — honest entry |
| Day 4 | 2026-07-20 | $740.31 | -$106.40 | -$2323.29 | Holding would have been **$2323.29** better — honest entry |
| Day 5 | 2026-07-21 | $746.30 | -$58.48 | -$2371.21 | Position open |
| Day 6 | 2026-07-22 | $745.64 | -$63.76 | -$2365.93 | Position open |
| Day 7 | 2026-07-23 | $736.23 | -$139.04 | -$2290.65 | Position open |
| Day 8 | 2026-07-24 | $737.07 | -$132.32 | -$2297.37 | Holding would have been **$2297.37** better — honest entry |
| Day 9 | 2026-07-27 | $737.02 | -$132.72 | -$2296.97 | Holding would have been **$2296.97** better — honest entry |
| Day 10 | 2026-07-28 | $738.96 | -$117.20 | -$2312.49 | Holding would have been **$2312.49** better — honest entry |
| Day 11 | 2026-07-29 | $727.76 | -$206.80 | -$2222.89 | Holding would have been **$2222.89** better — honest entry |
| Day 12 | 2026-07-30 | $739.79 | -$110.56 | -$2319.13 | Holding would have been **$2319.13** better — honest entry |
| Day 13 | 2026-07-31 | $744.94 | -$69.36 | -$2360.33 | Holding would have been **$2360.33** better — honest entry |
| Day 14 | 2026-08-03 | $755.84 | +$17.84 | -$2447.53 | Holding would have been **$2447.53** better — honest entry |
| Day 15 | 2026-08-04 | $769.20 | +$124.72 | -$2554.41 | Position open |
| Day 16 | 2026-08-05 | $767.88 | +$114.16 | -$2543.85 | Holding would have been **$2543.85** better — honest entry |
| Day 17 | 2026-08-06 | $766.74 | +$105.04 | -$2534.73 | Holding would have been **$2534.73** better — honest entry |
| Day 18 | 2026-08-07 | $771.25 | +$141.12 | -$2570.81 | Position open |
| Day 19 | 2026-08-10 | $771.11 | +$140.00 | -$2569.69 | Holding would have been **$2569.69** better — honest entry |
| Day 20 | 2026-08-11 | $768.61 | +$120.00 | -$2549.69 | Position open |
| Day 21 | 2026-08-12 | $770.63 | +$136.16 | -$2565.85 | Position open |
| Day 22 | 2026-08-13 | $775.91 | +$178.40 | -$2608.09 | Position open |
| Day 23 | 2026-08-14 | $774.38 | +$166.16 | -$2595.85 | Position open |
| Day 24 | 2026-08-17 | $770.71 | +$136.80 | -$2566.49 | Position open |
| Day 25 | 2026-08-18 | $765.46 | +$94.80 | -$2524.49 | Position open |
| Day 26 | 2026-08-19 | $767.19 | +$108.64 | -$2538.33 | Position open |
| Day 27 | 2026-08-20 | $760.73 | +$56.96 | -$2486.65 | Position open |
| Day 28 | 2026-08-21 | $763.74 | +$81.04 | -$2510.73 | Position open |
| Day 29 | 2026-08-24 | $761.57 | +$63.68 | -$2493.37 | Position open |
| Day 30 | 2026-08-25 | $763.89 | +$82.24 | -$2511.93 | Position open |
| Day 31 | 2026-08-26 | $764.04 | +$83.44 | -$2513.13 | Position open |
| Day 32 | 2026-08-27 | $769.27 | +$125.28 | -$2554.97 | Position open |
| Day 33 | 2026-08-28 | $767.37 | +$110.08 | -$2539.77 | Position open |
| Day 34 | 2026-08-31 | $764.97 | +$90.88 | -$2520.57 | Position open |
| Day 35 | 2026-09-01 | $759.74 | +$49.04 | -$2478.73 | Holding would have been **$2478.73** better — honest entry |
| Day 36 | 2026-09-02 | $763.23 | +$76.96 | -$2506.65 | Position open |
| Day 37 | 2026-09-03 | $771.20 | +$140.72 | -$2570.41 | Position open |
| Day 38 | 2026-09-04 | $768.27 | +$117.28 | -$2546.97 | Position open |
| Day 39 | 2026-09-08 | $764.16 | +$84.40 | -$2514.09 | Holding would have been **$2514.09** better — honest entry |
| Day 40 | 2026-09-09 | $760.54 | +$55.44 | -$2485.13 | Position open |
| Day 41 | 2026-09-10 | $755.99 | +$19.04 | -$2448.73 | Holding would have been **$2448.73** better — honest entry |
| Day 42 | 2026-09-11 | $762.25 | +$69.12 | -$2498.81 | Holding would have been **$2498.81** better — honest entry |
| Day 43 | 2026-09-14 | $758.87 | +$42.08 | -$2471.77 | Holding would have been **$2471.77** better — honest entry |
| Day 44 | 2026-09-15 | $755.54 | +$15.44 | -$2445.13 | Holding would have been **$2445.13** better — honest entry |
| Day 45 | 2026-09-16 | $752.18 | -$11.44 | -$2418.25 | Holding would have been **$2418.25** better — honest entry |
| Day 46 | 2026-09-17 | $760.75 | +$57.12 | -$2486.81 | Holding would have been **$2486.81** better — honest entry |
| Day 47 | 2026-09-18 | $761.62 | +$64.08 | -$2493.77 | Holding would have been **$2493.77** better — honest entry |
| Day 48 | 2026-09-21 | $773.52 | +$159.28 | -$2588.97 | Holding would have been **$2588.97** better — honest entry |
| Day 49 | 2026-09-22 | $773.44 | +$158.64 | -$2588.33 | Holding would have been **$2588.33** better — honest entry |
| Day 50 | 2026-09-23 | $767.93 | +$114.56 | -$2544.25 | Holding would have been **$2544.25** better — honest entry |
| Day 51 | 2026-09-24 | $767.29 | +$109.44 | -$2539.13 | Holding would have been **$2539.13** better — honest entry |
| Day 52 | 2026-09-25 | $771.35 | +$141.92 | -$2571.61 | Holding would have been **$2571.61** better — honest entry |
| Day 53 | 2026-09-28 | $765.49 | +$95.04 | -$2524.73 | Position open |
| Day 54 | 2026-09-29 | $764.38 | +$86.16 | -$2515.85 | Holding would have been **$2515.85** better — honest entry |
| Day 55 | 2026-09-30 | $762.34 | +$69.84 | -$2499.53 | Position open |
| Day 56 | 2026-10-01 | $764.10 | +$83.92 | -$2513.61 | Position open |
| Day 57 | 2026-10-02 | $769.65 | +$128.32 | -$2558.01 | Position open |
| Day 58 | 2026-10-05 | $774.97 | +$170.88 | -$2600.57 | Position open |
| Day 59 | 2026-10-06 | $779.10 | +$203.92 | -$2633.61 | Position open |
| Day 60 | 2026-10-07 | $777.15 | +$188.32 | -$2618.01 | Position open |
| Day 61 | 2026-10-08 | $773.88 | +$162.16 | -$2591.85 | Position open |
| Day 62 | 2026-10-09 | $778.51 | +$199.20 | -$2628.89 | Position open |
| Day 63 | 2026-10-12 | $778.03 | +$195.36 | -$2625.05 | Position open |
| Day 64 | 2026-10-13 | $778.03 | +$195.36 | -$2625.05 | Position open |
| Day 65 | 2026-10-14 | $769.65 | +$128.32 | -$2558.01 | Holding would have been **$2558.01** better — honest entry |
| Day 66 | 2026-10-15 | $771.77 | +$145.28 | -$2574.97 | Position open |
| Day 67 | 2026-10-16 | $763.34 | +$77.84 | -$2507.53 | Position open |
| Day 68 | 2026-10-19 | $766.60 | +$103.92 | -$2533.61 | Position open |
| Day 69 | 2026-10-20 | $769.09 | +$123.84 | -$2553.53 | Holding would have been **$2553.53** better — honest entry |
| Day 70 | 2026-10-21 | $773.13 | +$156.16 | -$2585.85 | Position open |
| Day 71 | 2026-10-22 | $764.03 | +$83.36 | -$2513.05 | Holding would have been **$2513.05** better — honest entry |
| Day 72 | 2026-10-23 | $760.70 | +$56.72 | -$2486.41 | Holding would have been **$2486.41** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $752.90 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$5.68 |
| Signal saved | -$2424.01 |
| Portfolio value | $100,007.12 |
| Benchmark value | $100,000.03 |
| Alpha (cumulative) | +0.007% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 2 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$36.80 |
| Signal saved | -$2392.89 |
| Portfolio value | $99,830.99 |
| Benchmark value | $99,483.36 |
| Alpha (cumulative) | +0.348% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 3 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$97.36 |
| Signal saved | -$2332.33 |
| Portfolio value | $99,688.43 |
| Benchmark value | $98,477.91 |
| Alpha (cumulative) | +1.210% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 4 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$106.40 |
| Signal saved | -$2323.29 |
| Portfolio value | $99,496.45 |
| Benchmark value | $98,327.83 |
| Alpha (cumulative) | +1.168% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 5 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T5) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,426.49 |
| Benchmark value | $99,123.42 |
| Alpha (cumulative) | +0.304% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 6 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T5) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,391.51 |
| Benchmark value | $99,035.76 |
| Alpha (cumulative) | +0.355% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 7 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T6) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,725.26 |
| Benchmark value | $97,785.92 |
| Alpha (cumulative) | +0.939% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 8 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$132.32 |
| Signal saved | -$2297.37 |
| Portfolio value | $98,869.30 |
| Benchmark value | $97,897.49 |
| Alpha (cumulative) | +0.972% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 9 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$132.72 |
| Signal saved | -$2296.97 |
| Portfolio value | $98,973.44 |
| Benchmark value | $97,890.85 |
| Alpha (cumulative) | +1.082% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 10 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$117.20 |
| Signal saved | -$2312.49 |
| Portfolio value | $98,929.98 |
| Benchmark value | $98,148.52 |
| Alpha (cumulative) | +0.781% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 11 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$206.80 |
| Signal saved | -$2222.89 |
| Portfolio value | $98,929.98 |
| Benchmark value | $96,660.94 |
| Alpha (cumulative) | +2.269% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 12 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$110.56 |
| Signal saved | -$2319.13 |
| Portfolio value | $98,929.98 |
| Benchmark value | $98,258.76 |
| Alpha (cumulative) | +0.671% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 13 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$69.36 |
| Signal saved | -$2360.33 |
| Portfolio value | $98,929.98 |
| Benchmark value | $98,942.78 |
| Alpha (cumulative) | -0.013% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 14 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$17.84 |
| Signal saved | -$2447.53 |
| Portfolio value | $98,929.98 |
| Benchmark value | $100,390.52 |
| Alpha (cumulative) | -1.461% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 15 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T9) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,782.48 |
| Benchmark value | $102,164.99 |
| Alpha (cumulative) | -3.383% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 16 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$114.16 |
| Signal saved | -$2543.85 |
| Portfolio value | $98,842.98 |
| Benchmark value | $101,989.67 |
| Alpha (cumulative) | -3.147% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 17 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$105.04 |
| Signal saved | -$2534.73 |
| Portfolio value | $98,842.98 |
| Benchmark value | $101,838.25 |
| Alpha (cumulative) | -2.995% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 18 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,778.71 |
| Benchmark value | $102,437.27 |
| Alpha (cumulative) | -3.658% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 19 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$140.00 |
| Signal saved | -$2569.69 |
| Portfolio value | $98,867.96 |
| Benchmark value | $102,418.68 |
| Alpha (cumulative) | -3.551% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 20 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,611.36 |
| Benchmark value | $102,086.63 |
| Alpha (cumulative) | -3.476% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 21 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,714.38 |
| Benchmark value | $102,354.92 |
| Alpha (cumulative) | -3.641% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 22 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $98,983.66 |
| Benchmark value | $103,056.21 |
| Alpha (cumulative) | -4.072% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 23 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $98,905.63 |
| Benchmark value | $102,853.00 |
| Alpha (cumulative) | -3.947% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 24 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,718.46 |
| Benchmark value | $102,365.55 |
| Alpha (cumulative) | -3.648% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 25 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,450.71 |
| Benchmark value | $101,668.24 |
| Alpha (cumulative) | -3.217% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 26 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,538.94 |
| Benchmark value | $101,898.02 |
| Alpha (cumulative) | -3.359% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 27 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,209.48 |
| Benchmark value | $101,040.01 |
| Alpha (cumulative) | -2.830% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 28 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,362.99 |
| Benchmark value | $101,439.79 |
| Alpha (cumulative) | -3.077% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 29 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,252.32 |
| Benchmark value | $101,151.58 |
| Alpha (cumulative) | -2.900% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 30 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,370.64 |
| Benchmark value | $101,459.72 |
| Alpha (cumulative) | -3.089% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 31 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,378.29 |
| Benchmark value | $101,479.64 |
| Alpha (cumulative) | -3.102% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 32 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,645.02 |
| Benchmark value | $102,174.29 |
| Alpha (cumulative) | -3.529% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 33 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,548.12 |
| Benchmark value | $101,921.93 |
| Alpha (cumulative) | -3.374% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 34 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,425.72 |
| Benchmark value | $101,603.16 |
| Alpha (cumulative) | -3.177% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 35 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$49.04 |
| Signal saved | -$2478.73 |
| Portfolio value | $98,255.38 |
| Benchmark value | $100,908.51 |
| Alpha (cumulative) | -2.654% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 36 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,169.19 |
| Benchmark value | $101,372.06 |
| Alpha (cumulative) | -3.203% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 37 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,575.66 |
| Benchmark value | $102,430.63 |
| Alpha (cumulative) | -3.855% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 38 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,426.23 |
| Benchmark value | $102,041.47 |
| Alpha (cumulative) | -3.615% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$84.40 |
| Signal saved | -$2514.09 |
| Portfolio value | $98,307.91 |
| Benchmark value | $101,495.58 |
| Alpha (cumulative) | -3.188% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 40 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T13) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,180.04 |
| Benchmark value | $101,014.77 |
| Alpha (cumulative) | -2.835% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$19.04 |
| Signal saved | -$2448.73 |
| Portfolio value | $98,043.80 |
| Benchmark value | $100,410.44 |
| Alpha (cumulative) | -2.366% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$69.12 |
| Signal saved | -$2498.81 |
| Portfolio value | $98,043.80 |
| Benchmark value | $101,241.89 |
| Alpha (cumulative) | -3.198% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$42.08 |
| Signal saved | -$2471.77 |
| Portfolio value | $98,043.80 |
| Benchmark value | $100,792.96 |
| Alpha (cumulative) | -2.749% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$15.44 |
| Signal saved | -$2445.13 |
| Portfolio value | $98,043.80 |
| Benchmark value | $100,350.67 |
| Alpha (cumulative) | -2.307% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | -$11.44 |
| Signal saved | -$2418.25 |
| Portfolio value | $98,043.80 |
| Benchmark value | $99,904.40 |
| Alpha (cumulative) | -1.860% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$57.12 |
| Signal saved | -$2486.81 |
| Portfolio value | $98,043.80 |
| Benchmark value | $101,042.66 |
| Alpha (cumulative) | -2.999% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$64.08 |
| Signal saved | -$2493.77 |
| Portfolio value | $98,043.80 |
| Benchmark value | $101,158.22 |
| Alpha (cumulative) | -3.114% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$159.28 |
| Signal saved | -$2588.97 |
| Portfolio value | $98,043.80 |
| Benchmark value | $102,738.77 |
| Alpha (cumulative) | -4.695% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$158.64 |
| Signal saved | -$2588.33 |
| Portfolio value | $98,058.59 |
| Benchmark value | $102,728.15 |
| Alpha (cumulative) | -4.669% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$114.56 |
| Signal saved | -$2544.25 |
| Portfolio value | $98,029.82 |
| Benchmark value | $101,996.31 |
| Alpha (cumulative) | -3.966% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$109.44 |
| Signal saved | -$2539.13 |
| Portfolio value | $98,029.82 |
| Benchmark value | $101,911.30 |
| Alpha (cumulative) | -3.881% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$141.92 |
| Signal saved | -$2571.61 |
| Portfolio value | $98,029.82 |
| Benchmark value | $102,450.55 |
| Alpha (cumulative) | -4.421% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $765.49 |
| Unrealized P&L | +$7.14 |
| P&L % | +0.018% |
| Portfolio value | $98,036.96 |
| Benchmark value | $101,672.23 |
| Alpha (cumulative) | -3.635% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.38 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$86.16 |
| Signal saved | -$2515.85 |
| Portfolio value | $98,061.95 |
| Benchmark value | $101,524.80 |
| Alpha (cumulative) | -3.463% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 55 — 2026-09-30

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $762.34 |
| Unrealized P&L | -$216.75 |
| P&L % | -0.554% |
| Portfolio value | $97,845.20 |
| Benchmark value | $101,253.85 |
| Alpha (cumulative) | -3.409% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 56 — 2026-10-01

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.10 |
| Unrealized P&L | -$126.99 |
| P&L % | -0.325% |
| Portfolio value | $97,934.96 |
| Benchmark value | $101,487.61 |
| Alpha (cumulative) | -3.553% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.33% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-10-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.65 |
| Unrealized P&L | +$156.06 |
| P&L % | +0.399% |
| Portfolio value | $98,218.01 |
| Benchmark value | $102,224.76 |
| Alpha (cumulative) | -4.007% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.40% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 58 — 2026-10-05

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $774.97 |
| Unrealized P&L | +$427.38 |
| P&L % | +1.093% |
| Portfolio value | $98,489.33 |
| Benchmark value | $102,931.36 |
| Alpha (cumulative) | -4.442% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +1.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 59 — 2026-10-06

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $779.10 |
| Unrealized P&L | +$638.01 |
| P&L % | +1.632% |
| Portfolio value | $98,699.96 |
| Benchmark value | $103,479.91 |
| Alpha (cumulative) | -4.780% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +1.63% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 60 — 2026-10-07

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $777.15 |
| Unrealized P&L | +$538.56 |
| P&L % | +1.378% |
| Portfolio value | $98,600.51 |
| Benchmark value | $103,220.91 |
| Alpha (cumulative) | -4.620% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +1.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 61 — 2026-10-08

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $773.88 |
| Unrealized P&L | +$371.79 |
| P&L % | +0.951% |
| Portfolio value | $98,433.74 |
| Benchmark value | $102,786.59 |
| Alpha (cumulative) | -4.353% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.95% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 62 — 2026-10-09

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $778.51 |
| Unrealized P&L | +$607.92 |
| P&L % | +1.555% |
| Portfolio value | $98,669.87 |
| Benchmark value | $103,401.54 |
| Alpha (cumulative) | -4.732% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +1.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 63 — 2026-10-12

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,645.39 |
| Benchmark value | $103,337.79 |
| Alpha (cumulative) | -4.693% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 64 — 2026-10-13

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,645.39 |
| Benchmark value | $103,337.79 |
| Alpha (cumulative) | -4.693% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 65 — 2026-10-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.65 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$128.32 |
| Signal saved | -$2558.01 |
| Portfolio value | $98,117.54 |
| Benchmark value | $102,224.76 |
| Alpha (cumulative) | -4.108% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 66 — 2026-10-15

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.77 |
| Unrealized P&L | +$110.67 |
| P&L % | +0.282% |
| Portfolio value | $98,228.21 |
| Benchmark value | $102,506.34 |
| Alpha (cumulative) | -4.278% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: +0.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 67 — 2026-10-16

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $763.34 |
| Unrealized P&L | -$319.26 |
| P&L % | -0.813% |
| Portfolio value | $97,798.28 |
| Benchmark value | $101,386.67 |
| Alpha (cumulative) | -3.589% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 68 — 2026-10-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $766.60 |
| Unrealized P&L | -$153.00 |
| P&L % | -0.390% |
| Portfolio value | $97,964.54 |
| Benchmark value | $101,819.66 |
| Alpha (cumulative) | -3.856% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 69 — 2026-10-20

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.09 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$123.84 |
| Signal saved | -$2553.53 |
| Portfolio value | $98,169.05 |
| Benchmark value | $102,150.38 |
| Alpha (cumulative) | -3.981% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 70 — 2026-10-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T19) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $773.13 |
| Unrealized P&L | -$36.72 |
| P&L % | -0.093% |
| Portfolio value | $98,132.33 |
| Benchmark value | $102,686.97 |
| Alpha (cumulative) | -4.555% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Momentum: WEAK. Unrealized P&L: -0.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 71 — 2026-10-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.03 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$83.36 |
| Signal saved | -$2513.05 |
| Portfolio value | $97,570.31 |
| Benchmark value | $101,478.31 |
| Alpha (cumulative) | -3.908% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 72 — 2026-10-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $760.70 |
| Realized P&L (locked) | -$2429.69 |
| Reference if held | +$56.72 |
| Signal saved | -$2486.41 |
| Portfolio value | $97,570.31 |
| Benchmark value | $101,036.02 |
| Alpha (cumulative) | -3.466% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2429.69. Regime: BULL (MA20 $770.72 vs MA50 $767.22). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
_Day 72 of 90 · Alpaca equity: $98,596.51 · Cumulative alpha vs SPY: -3.466%_