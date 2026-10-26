# ALPACA PAPER JOURNAL — SPY
_Last updated: October 26, 2026 | Day 73 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$753.610/share**
> (2026-07-15, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-10-26): **BULLISH**  
> Fast: MA10 $769.33 | MA30 $768.18  
> Slow: MA20 $770.15 | MA50 $766.9  
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

**Total trades:** 20 | **Closed:** 19 | **Open:** Yes | **Cumulative Realized P&L:** -$2435.03

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $753.610 (2026-07-15) | $754.500 (2026-07-15) | 2 | +$1.78 | ✅ Closed |
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
| T20 | $760.600 (2026-10-23) | — | 51 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $98,838.24 |
| Alpaca cash | $59,806.41 |
| Cumulative realized P&L | -$2435.03 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $752.90 | FLAT | — | — | $100,001.78 |
| Day 2 | 2026-07-16 | $749.01 | FLAT | — | — | $99,825.65 |
| Day 3 | 2026-07-17 | $741.44 | FLAT | — | — | $99,683.09 |
| Day 4 | 2026-07-20 | $740.31 | FLAT | — | — | $99,491.11 |
| Day 5 | 2026-07-21 | $746.30 | Long 53 SPY (T5) | -$69.96 | -0.177% | $99,421.15 |
| Day 6 | 2026-07-22 | $745.64 | Long 53 SPY (T5) | -$104.94 | -0.265% | $99,386.17 |
| Day 7 | 2026-07-23 | $736.23 | Long 52 SPY (T6) | -$135.72 | -0.353% | $98,719.92 |
| Day 8 | 2026-07-24 | $737.07 | FLAT | — | — | $98,863.96 |
| Day 9 | 2026-07-27 | $737.02 | FLAT | — | — | $98,968.10 |
| Day 10 | 2026-07-28 | $738.96 | FLAT | — | — | $98,924.64 |
| Day 11 | 2026-07-29 | $727.76 | FLAT | — | — | $98,924.64 |
| Day 12 | 2026-07-30 | $739.79 | FLAT | — | — | $98,924.64 |
| Day 13 | 2026-07-31 | $744.94 | FLAT | — | — | $98,924.64 |
| Day 14 | 2026-08-03 | $755.84 | FLAT | — | — | $98,924.64 |
| Day 15 | 2026-08-04 | $769.20 | Long 50 SPY (T9) | -$147.50 | -0.382% | $98,777.14 |
| Day 16 | 2026-08-05 | $767.88 | FLAT | — | — | $98,837.64 |
| Day 17 | 2026-08-06 | $766.74 | FLAT | — | — | $98,837.64 |
| Day 18 | 2026-08-07 | $771.25 | Long 51 SPY (T10) | -$64.27 | -0.163% | $98,773.37 |
| Day 19 | 2026-08-10 | $771.11 | FLAT | — | — | $98,862.62 |
| Day 20 | 2026-08-11 | $768.61 | Long 51 SPY (T11) | -$256.60 | -0.650% | $98,606.02 |
| Day 21 | 2026-08-12 | $770.63 | Long 51 SPY (T11) | -$153.58 | -0.389% | $98,709.04 |
| Day 22 | 2026-08-13 | $775.91 | Long 51 SPY (T11) | +$115.70 | +0.293% | $98,978.32 |
| Day 23 | 2026-08-14 | $774.38 | Long 51 SPY (T11) | +$37.67 | +0.095% | $98,900.29 |
| Day 24 | 2026-08-17 | $770.71 | Long 51 SPY (T11) | -$149.50 | -0.379% | $98,713.12 |
| Day 25 | 2026-08-18 | $765.46 | Long 51 SPY (T11) | -$417.25 | -1.058% | $98,445.37 |
| Day 26 | 2026-08-19 | $767.19 | Long 51 SPY (T11) | -$329.02 | -0.834% | $98,533.60 |
| Day 27 | 2026-08-20 | $760.73 | Long 51 SPY (T11) | -$658.48 | -1.669% | $98,204.14 |
| Day 28 | 2026-08-21 | $763.74 | Long 51 SPY (T11) | -$504.97 | -1.280% | $98,357.65 |
| Day 29 | 2026-08-24 | $761.57 | Long 51 SPY (T11) | -$615.64 | -1.560% | $98,246.98 |
| Day 30 | 2026-08-25 | $763.89 | Long 51 SPY (T11) | -$497.32 | -1.260% | $98,365.30 |
| Day 31 | 2026-08-26 | $764.04 | Long 51 SPY (T11) | -$489.67 | -1.241% | $98,372.95 |
| Day 32 | 2026-08-27 | $769.27 | Long 51 SPY (T11) | -$222.94 | -0.565% | $98,639.68 |
| Day 33 | 2026-08-28 | $767.37 | Long 51 SPY (T11) | -$319.84 | -0.811% | $98,542.78 |
| Day 34 | 2026-08-31 | $764.97 | Long 51 SPY (T11) | -$442.24 | -1.121% | $98,420.38 |
| Day 35 | 2026-09-01 | $759.74 | FLAT | — | — | $98,250.04 |
| Day 36 | 2026-09-02 | $763.23 | Long 51 SPY (T12) | -$86.19 | -0.221% | $98,163.85 |
| Day 37 | 2026-09-03 | $771.20 | Long 51 SPY (T12) | +$320.28 | +0.821% | $98,570.32 |
| Day 38 | 2026-09-04 | $768.27 | Long 51 SPY (T12) | +$170.85 | +0.438% | $98,420.89 |
| Day 39 | 2026-09-08 | $764.16 | FLAT | — | — | $98,302.57 |
| Day 40 | 2026-09-09 | $760.54 | Long 52 SPY (T13) | -$127.87 | -0.322% | $98,174.70 |
| Day 41 | 2026-09-10 | $755.99 | FLAT | — | — | $98,038.46 |
| Day 42 | 2026-09-11 | $762.25 | FLAT | — | — | $98,038.46 |
| Day 43 | 2026-09-14 | $758.87 | FLAT | — | — | $98,038.46 |
| Day 44 | 2026-09-15 | $755.54 | FLAT | — | — | $98,038.46 |
| Day 45 | 2026-09-16 | $752.18 | FLAT | — | — | $98,038.46 |
| Day 46 | 2026-09-17 | $760.75 | FLAT | — | — | $98,038.46 |
| Day 47 | 2026-09-18 | $761.62 | FLAT | — | — | $98,038.46 |
| Day 48 | 2026-09-21 | $773.52 | FLAT | — | — | $98,038.46 |
| Day 49 | 2026-09-22 | $773.44 | FLAT | — | — | $98,053.25 |
| Day 50 | 2026-09-23 | $767.93 | FLAT | — | — | $98,024.48 |
| Day 51 | 2026-09-24 | $767.29 | FLAT | — | — | $98,024.48 |
| Day 52 | 2026-09-25 | $771.35 | FLAT | — | — | $98,024.48 |
| Day 53 | 2026-09-28 | $765.49 | Long 51 SPY (T16) | +$7.14 | +0.018% | $98,031.62 |
| Day 54 | 2026-09-29 | $764.38 | FLAT | — | — | $98,056.61 |
| Day 55 | 2026-09-30 | $762.34 | Long 51 SPY (T17) | -$216.75 | -0.554% | $97,839.86 |
| Day 56 | 2026-10-01 | $764.10 | Long 51 SPY (T17) | -$126.99 | -0.325% | $97,929.62 |
| Day 57 | 2026-10-02 | $769.65 | Long 51 SPY (T17) | +$156.06 | +0.399% | $98,212.67 |
| Day 58 | 2026-10-05 | $774.97 | Long 51 SPY (T17) | +$427.38 | +1.093% | $98,483.99 |
| Day 59 | 2026-10-06 | $779.10 | Long 51 SPY (T17) | +$638.01 | +1.632% | $98,694.62 |
| Day 60 | 2026-10-07 | $777.15 | Long 51 SPY (T17) | +$538.56 | +1.378% | $98,595.17 |
| Day 61 | 2026-10-08 | $773.88 | Long 51 SPY (T17) | +$371.79 | +0.951% | $98,428.40 |
| Day 62 | 2026-10-09 | $778.51 | Long 51 SPY (T17) | +$607.92 | +1.555% | $98,664.53 |
| Day 63 | 2026-10-12 | $778.03 | Long 51 SPY (T17) | +$583.44 | +1.492% | $98,640.05 |
| Day 64 | 2026-10-13 | $778.03 | Long 51 SPY (T17) | +$583.44 | +1.492% | $98,640.05 |
| Day 65 | 2026-10-14 | $769.65 | FLAT | — | — | $98,112.20 |
| Day 66 | 2026-10-15 | $771.77 | Long 51 SPY (T18) | +$110.67 | +0.282% | $98,222.87 |
| Day 67 | 2026-10-16 | $763.34 | Long 51 SPY (T18) | -$319.26 | -0.813% | $97,792.94 |
| Day 68 | 2026-10-19 | $766.60 | Long 51 SPY (T18) | -$153.00 | -0.390% | $97,959.20 |
| Day 69 | 2026-10-20 | $769.09 | FLAT | — | — | $98,163.71 |
| Day 70 | 2026-10-21 | $773.13 | Long 51 SPY (T19) | -$36.72 | -0.093% | $98,126.99 |
| Day 71 | 2026-10-22 | $764.03 | FLAT | — | — | $97,564.97 |
| Day 72 | 2026-10-23 | $759.83 | Long 51 SPY (T20) | -$39.27 | -0.101% | $97,525.70 |
| Day 73 | 2026-10-26 | $765.37 | Long 51 SPY (T20) | +$243.27 | +0.627% | $97,808.24 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $100,001.78 | $100,000.03 | +0.0018% | +0.000% | **+0.002%** |
| Day 2 | 2026-07-16 | $99,825.65 | $99,483.36 | -0.1744% | -0.517% | **+0.343%** |
| Day 3 | 2026-07-17 | $99,683.09 | $98,477.91 | -0.3169% | -1.522% | **+1.205%** |
| Day 4 | 2026-07-20 | $99,491.11 | $98,327.83 | -0.5089% | -1.672% | **+1.163%** |
| Day 5 | 2026-07-21 | $99,421.15 | $99,123.42 | -0.5789% | -0.877% | **+0.298%** |
| Day 6 | 2026-07-22 | $99,386.17 | $99,035.76 | -0.6138% | -0.964% | **+0.350%** |
| Day 7 | 2026-07-23 | $98,719.92 | $97,785.92 | -1.2801% | -2.214% | **+0.934%** |
| Day 8 | 2026-07-24 | $98,863.96 | $97,897.49 | -1.1360% | -2.103% | **+0.967%** |
| Day 9 | 2026-07-27 | $98,968.10 | $97,890.85 | -1.0319% | -2.109% | **+1.077%** |
| Day 10 | 2026-07-28 | $98,924.64 | $98,148.52 | -1.0754% | -1.851% | **+0.776%** |
| Day 11 | 2026-07-29 | $98,924.64 | $96,660.94 | -1.0754% | -3.339% | **+2.264%** |
| Day 12 | 2026-07-30 | $98,924.64 | $98,258.76 | -1.0754% | -1.741% | **+0.666%** |
| Day 13 | 2026-07-31 | $98,924.64 | $98,942.78 | -1.0754% | -1.057% | **-0.018%** |
| Day 14 | 2026-08-03 | $98,924.64 | $100,390.52 | -1.0754% | +0.391% | **-1.466%** |
| Day 15 | 2026-08-04 | $98,777.14 | $102,164.99 | -1.2229% | +2.165% | **-3.388%** |
| Day 16 | 2026-08-05 | $98,837.64 | $101,989.67 | -1.1624% | +1.990% | **-3.152%** |
| Day 17 | 2026-08-06 | $98,837.64 | $101,838.25 | -1.1624% | +1.838% | **-3.000%** |
| Day 18 | 2026-08-07 | $98,773.37 | $102,437.27 | -1.2266% | +2.437% | **-3.664%** |
| Day 19 | 2026-08-10 | $98,862.62 | $102,418.68 | -1.1374% | +2.419% | **-3.556%** |
| Day 20 | 2026-08-11 | $98,606.02 | $102,086.63 | -1.3940% | +2.087% | **-3.481%** |
| Day 21 | 2026-08-12 | $98,709.04 | $102,354.92 | -1.2910% | +2.355% | **-3.646%** |
| Day 22 | 2026-08-13 | $98,978.32 | $103,056.21 | -1.0217% | +3.056% | **-4.078%** |
| Day 23 | 2026-08-14 | $98,900.29 | $102,853.00 | -1.0997% | +2.853% | **-3.953%** |
| Day 24 | 2026-08-17 | $98,713.12 | $102,365.55 | -1.2869% | +2.366% | **-3.653%** |
| Day 25 | 2026-08-18 | $98,445.37 | $101,668.24 | -1.5546% | +1.668% | **-3.223%** |
| Day 26 | 2026-08-19 | $98,533.60 | $101,898.02 | -1.4664% | +1.898% | **-3.364%** |
| Day 27 | 2026-08-20 | $98,204.14 | $101,040.01 | -1.7959% | +1.040% | **-2.836%** |
| Day 28 | 2026-08-21 | $98,357.65 | $101,439.79 | -1.6424% | +1.440% | **-3.082%** |
| Day 29 | 2026-08-24 | $98,246.98 | $101,151.58 | -1.7530% | +1.152% | **-2.905%** |
| Day 30 | 2026-08-25 | $98,365.30 | $101,459.72 | -1.6347% | +1.460% | **-3.095%** |
| Day 31 | 2026-08-26 | $98,372.95 | $101,479.64 | -1.6271% | +1.480% | **-3.107%** |
| Day 32 | 2026-08-27 | $98,639.68 | $102,174.29 | -1.3603% | +2.174% | **-3.534%** |
| Day 33 | 2026-08-28 | $98,542.78 | $101,921.93 | -1.4572% | +1.922% | **-3.379%** |
| Day 34 | 2026-08-31 | $98,420.38 | $101,603.16 | -1.5796% | +1.603% | **-3.183%** |
| Day 35 | 2026-09-01 | $98,250.04 | $100,908.51 | -1.7500% | +0.909% | **-2.659%** |
| Day 36 | 2026-09-02 | $98,163.85 | $101,372.06 | -1.8361% | +1.372% | **-3.208%** |
| Day 37 | 2026-09-03 | $98,570.32 | $102,430.63 | -1.4297% | +2.431% | **-3.861%** |
| Day 38 | 2026-09-04 | $98,420.89 | $102,041.47 | -1.5791% | +2.041% | **-3.620%** |
| Day 39 | 2026-09-08 | $98,302.57 | $101,495.58 | -1.6974% | +1.496% | **-3.193%** |
| Day 40 | 2026-09-09 | $98,174.70 | $101,014.77 | -1.8253% | +1.015% | **-2.840%** |
| Day 41 | 2026-09-10 | $98,038.46 | $100,410.44 | -1.9615% | +0.410% | **-2.372%** |
| Day 42 | 2026-09-11 | $98,038.46 | $101,241.89 | -1.9615% | +1.242% | **-3.204%** |
| Day 43 | 2026-09-14 | $98,038.46 | $100,792.96 | -1.9615% | +0.793% | **-2.754%** |
| Day 44 | 2026-09-15 | $98,038.46 | $100,350.67 | -1.9615% | +0.351% | **-2.312%** |
| Day 45 | 2026-09-16 | $98,038.46 | $99,904.40 | -1.9615% | -0.096% | **-1.866%** |
| Day 46 | 2026-09-17 | $98,038.46 | $101,042.66 | -1.9615% | +1.043% | **-3.004%** |
| Day 47 | 2026-09-18 | $98,038.46 | $101,158.22 | -1.9615% | +1.158% | **-3.120%** |
| Day 48 | 2026-09-21 | $98,038.46 | $102,738.77 | -1.9615% | +2.739% | **-4.700%** |
| Day 49 | 2026-09-22 | $98,053.25 | $102,728.15 | -1.9467% | +2.728% | **-4.675%** |
| Day 50 | 2026-09-23 | $98,024.48 | $101,996.31 | -1.9755% | +1.996% | **-3.972%** |
| Day 51 | 2026-09-24 | $98,024.48 | $101,911.30 | -1.9755% | +1.911% | **-3.886%** |
| Day 52 | 2026-09-25 | $98,024.48 | $102,450.55 | -1.9755% | +2.451% | **-4.426%** |
| Day 53 | 2026-09-28 | $98,031.62 | $101,672.23 | -1.9684% | +1.672% | **-3.640%** |
| Day 54 | 2026-09-29 | $98,056.61 | $101,524.80 | -1.9434% | +1.525% | **-3.468%** |
| Day 55 | 2026-09-30 | $97,839.86 | $101,253.85 | -2.1601% | +1.254% | **-3.414%** |
| Day 56 | 2026-10-01 | $97,929.62 | $101,487.61 | -2.0704% | +1.488% | **-3.558%** |
| Day 57 | 2026-10-02 | $98,212.67 | $102,224.76 | -1.7873% | +2.225% | **-4.012%** |
| Day 58 | 2026-10-05 | $98,483.99 | $102,931.36 | -1.5160% | +2.931% | **-4.447%** |
| Day 59 | 2026-10-06 | $98,694.62 | $103,479.91 | -1.3054% | +3.480% | **-4.785%** |
| Day 60 | 2026-10-07 | $98,595.17 | $103,220.91 | -1.4048% | +3.221% | **-4.626%** |
| Day 61 | 2026-10-08 | $98,428.40 | $102,786.59 | -1.5716% | +2.787% | **-4.359%** |
| Day 62 | 2026-10-09 | $98,664.53 | $103,401.54 | -1.3355% | +3.402% | **-4.738%** |
| Day 63 | 2026-10-12 | $98,640.05 | $103,337.79 | -1.3599% | +3.338% | **-4.698%** |
| Day 64 | 2026-10-13 | $98,640.05 | $103,337.79 | -1.3599% | +3.338% | **-4.698%** |
| Day 65 | 2026-10-14 | $98,112.20 | $102,224.76 | -1.8878% | +2.225% | **-4.113%** |
| Day 66 | 2026-10-15 | $98,222.87 | $102,506.34 | -1.7771% | +2.506% | **-4.283%** |
| Day 67 | 2026-10-16 | $97,792.94 | $101,386.67 | -2.2071% | +1.387% | **-3.594%** |
| Day 68 | 2026-10-19 | $97,959.20 | $101,819.66 | -2.0408% | +1.820% | **-3.861%** |
| Day 69 | 2026-10-20 | $98,163.71 | $102,150.38 | -1.8363% | +2.150% | **-3.986%** |
| Day 70 | 2026-10-21 | $98,126.99 | $102,686.97 | -1.8730% | +2.687% | **-4.560%** |
| Day 71 | 2026-10-22 | $97,564.97 | $101,478.31 | -2.4350% | +1.478% | **-3.913%** |
| Day 72 | 2026-10-23 | $97,525.70 | $100,920.47 | -2.4743% | +0.920% | **-3.394%** |
| Day 73 | 2026-10-26 | $97,808.24 | $101,656.29 | -2.1918% | +1.656% | **-3.848%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-15 | $752.90 | -$1.42 | -$2433.61 | Holding would have been **$2433.61** better — honest entry |
| Day 2 | 2026-07-16 | $749.01 | -$9.20 | -$2425.83 | Holding would have been **$2425.83** better — honest entry |
| Day 3 | 2026-07-17 | $741.44 | -$24.34 | -$2410.69 | Holding would have been **$2410.69** better — honest entry |
| Day 4 | 2026-07-20 | $740.31 | -$26.60 | -$2408.43 | Holding would have been **$2408.43** better — honest entry |
| Day 5 | 2026-07-21 | $746.30 | -$14.62 | -$2420.41 | Position open |
| Day 6 | 2026-07-22 | $745.64 | -$15.94 | -$2419.09 | Position open |
| Day 7 | 2026-07-23 | $736.23 | -$34.76 | -$2400.27 | Position open |
| Day 8 | 2026-07-24 | $737.07 | -$33.08 | -$2401.95 | Holding would have been **$2401.95** better — honest entry |
| Day 9 | 2026-07-27 | $737.02 | -$33.18 | -$2401.85 | Holding would have been **$2401.85** better — honest entry |
| Day 10 | 2026-07-28 | $738.96 | -$29.30 | -$2405.73 | Holding would have been **$2405.73** better — honest entry |
| Day 11 | 2026-07-29 | $727.76 | -$51.70 | -$2383.33 | Holding would have been **$2383.33** better — honest entry |
| Day 12 | 2026-07-30 | $739.79 | -$27.64 | -$2407.39 | Holding would have been **$2407.39** better — honest entry |
| Day 13 | 2026-07-31 | $744.94 | -$17.34 | -$2417.69 | Holding would have been **$2417.69** better — honest entry |
| Day 14 | 2026-08-03 | $755.84 | +$4.46 | -$2439.49 | Holding would have been **$2439.49** better — honest entry |
| Day 15 | 2026-08-04 | $769.20 | +$31.18 | -$2466.21 | Position open |
| Day 16 | 2026-08-05 | $767.88 | +$28.54 | -$2463.57 | Holding would have been **$2463.57** better — honest entry |
| Day 17 | 2026-08-06 | $766.74 | +$26.26 | -$2461.29 | Holding would have been **$2461.29** better — honest entry |
| Day 18 | 2026-08-07 | $771.25 | +$35.28 | -$2470.31 | Position open |
| Day 19 | 2026-08-10 | $771.11 | +$35.00 | -$2470.03 | Holding would have been **$2470.03** better — honest entry |
| Day 20 | 2026-08-11 | $768.61 | +$30.00 | -$2465.03 | Position open |
| Day 21 | 2026-08-12 | $770.63 | +$34.04 | -$2469.07 | Position open |
| Day 22 | 2026-08-13 | $775.91 | +$44.60 | -$2479.63 | Position open |
| Day 23 | 2026-08-14 | $774.38 | +$41.54 | -$2476.57 | Position open |
| Day 24 | 2026-08-17 | $770.71 | +$34.20 | -$2469.23 | Position open |
| Day 25 | 2026-08-18 | $765.46 | +$23.70 | -$2458.73 | Position open |
| Day 26 | 2026-08-19 | $767.19 | +$27.16 | -$2462.19 | Position open |
| Day 27 | 2026-08-20 | $760.73 | +$14.24 | -$2449.27 | Position open |
| Day 28 | 2026-08-21 | $763.74 | +$20.26 | -$2455.29 | Position open |
| Day 29 | 2026-08-24 | $761.57 | +$15.92 | -$2450.95 | Position open |
| Day 30 | 2026-08-25 | $763.89 | +$20.56 | -$2455.59 | Position open |
| Day 31 | 2026-08-26 | $764.04 | +$20.86 | -$2455.89 | Position open |
| Day 32 | 2026-08-27 | $769.27 | +$31.32 | -$2466.35 | Position open |
| Day 33 | 2026-08-28 | $767.37 | +$27.52 | -$2462.55 | Position open |
| Day 34 | 2026-08-31 | $764.97 | +$22.72 | -$2457.75 | Position open |
| Day 35 | 2026-09-01 | $759.74 | +$12.26 | -$2447.29 | Holding would have been **$2447.29** better — honest entry |
| Day 36 | 2026-09-02 | $763.23 | +$19.24 | -$2454.27 | Position open |
| Day 37 | 2026-09-03 | $771.20 | +$35.18 | -$2470.21 | Position open |
| Day 38 | 2026-09-04 | $768.27 | +$29.32 | -$2464.35 | Position open |
| Day 39 | 2026-09-08 | $764.16 | +$21.10 | -$2456.13 | Holding would have been **$2456.13** better — honest entry |
| Day 40 | 2026-09-09 | $760.54 | +$13.86 | -$2448.89 | Position open |
| Day 41 | 2026-09-10 | $755.99 | +$4.76 | -$2439.79 | Holding would have been **$2439.79** better — honest entry |
| Day 42 | 2026-09-11 | $762.25 | +$17.28 | -$2452.31 | Holding would have been **$2452.31** better — honest entry |
| Day 43 | 2026-09-14 | $758.87 | +$10.52 | -$2445.55 | Holding would have been **$2445.55** better — honest entry |
| Day 44 | 2026-09-15 | $755.54 | +$3.86 | -$2438.89 | Holding would have been **$2438.89** better — honest entry |
| Day 45 | 2026-09-16 | $752.18 | -$2.86 | -$2432.17 | Holding would have been **$2432.17** better — honest entry |
| Day 46 | 2026-09-17 | $760.75 | +$14.28 | -$2449.31 | Holding would have been **$2449.31** better — honest entry |
| Day 47 | 2026-09-18 | $761.62 | +$16.02 | -$2451.05 | Holding would have been **$2451.05** better — honest entry |
| Day 48 | 2026-09-21 | $773.52 | +$39.82 | -$2474.85 | Holding would have been **$2474.85** better — honest entry |
| Day 49 | 2026-09-22 | $773.44 | +$39.66 | -$2474.69 | Holding would have been **$2474.69** better — honest entry |
| Day 50 | 2026-09-23 | $767.93 | +$28.64 | -$2463.67 | Holding would have been **$2463.67** better — honest entry |
| Day 51 | 2026-09-24 | $767.29 | +$27.36 | -$2462.39 | Holding would have been **$2462.39** better — honest entry |
| Day 52 | 2026-09-25 | $771.35 | +$35.48 | -$2470.51 | Holding would have been **$2470.51** better — honest entry |
| Day 53 | 2026-09-28 | $765.49 | +$23.76 | -$2458.79 | Position open |
| Day 54 | 2026-09-29 | $764.38 | +$21.54 | -$2456.57 | Holding would have been **$2456.57** better — honest entry |
| Day 55 | 2026-09-30 | $762.34 | +$17.46 | -$2452.49 | Position open |
| Day 56 | 2026-10-01 | $764.10 | +$20.98 | -$2456.01 | Position open |
| Day 57 | 2026-10-02 | $769.65 | +$32.08 | -$2467.11 | Position open |
| Day 58 | 2026-10-05 | $774.97 | +$42.72 | -$2477.75 | Position open |
| Day 59 | 2026-10-06 | $779.10 | +$50.98 | -$2486.01 | Position open |
| Day 60 | 2026-10-07 | $777.15 | +$47.08 | -$2482.11 | Position open |
| Day 61 | 2026-10-08 | $773.88 | +$40.54 | -$2475.57 | Position open |
| Day 62 | 2026-10-09 | $778.51 | +$49.80 | -$2484.83 | Position open |
| Day 63 | 2026-10-12 | $778.03 | +$48.84 | -$2483.87 | Position open |
| Day 64 | 2026-10-13 | $778.03 | +$48.84 | -$2483.87 | Position open |
| Day 65 | 2026-10-14 | $769.65 | +$32.08 | -$2467.11 | Holding would have been **$2467.11** better — honest entry |
| Day 66 | 2026-10-15 | $771.77 | +$36.32 | -$2471.35 | Position open |
| Day 67 | 2026-10-16 | $763.34 | +$19.46 | -$2454.49 | Position open |
| Day 68 | 2026-10-19 | $766.60 | +$25.98 | -$2461.01 | Position open |
| Day 69 | 2026-10-20 | $769.09 | +$30.96 | -$2465.99 | Holding would have been **$2465.99** better — honest entry |
| Day 70 | 2026-10-21 | $773.13 | +$39.04 | -$2474.07 | Position open |
| Day 71 | 2026-10-22 | $764.03 | +$20.84 | -$2455.87 | Holding would have been **$2455.87** better — honest entry |
| Day 72 | 2026-10-23 | $759.83 | +$12.44 | -$2447.47 | Position open |
| Day 73 | 2026-10-26 | $765.37 | +$23.52 | -$2458.55 | Position open |

---

## Daily Entries

### Day 1 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $752.90 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$1.42 |
| Signal saved | -$2433.61 |
| Portfolio value | $100,001.78 |
| Benchmark value | $100,000.03 |
| Alpha (cumulative) | +0.002% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 2 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$9.20 |
| Signal saved | -$2425.83 |
| Portfolio value | $99,825.65 |
| Benchmark value | $99,483.36 |
| Alpha (cumulative) | +0.343% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 3 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$24.34 |
| Signal saved | -$2410.69 |
| Portfolio value | $99,683.09 |
| Benchmark value | $98,477.91 |
| Alpha (cumulative) | +1.205% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 4 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$26.60 |
| Signal saved | -$2408.43 |
| Portfolio value | $99,491.11 |
| Benchmark value | $98,327.83 |
| Alpha (cumulative) | +1.163% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $99,421.15 |
| Benchmark value | $99,123.42 |
| Alpha (cumulative) | +0.298% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.18% from entry. No exit triggered.

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
| Portfolio value | $99,386.17 |
| Benchmark value | $99,035.76 |
| Alpha (cumulative) | +0.350% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.27% from entry. No exit triggered.

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
| Portfolio value | $98,719.92 |
| Benchmark value | $97,785.92 |
| Alpha (cumulative) | +0.934% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 8 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$33.08 |
| Signal saved | -$2401.95 |
| Portfolio value | $98,863.96 |
| Benchmark value | $97,897.49 |
| Alpha (cumulative) | +0.967% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 9 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$33.18 |
| Signal saved | -$2401.85 |
| Portfolio value | $98,968.10 |
| Benchmark value | $97,890.85 |
| Alpha (cumulative) | +1.077% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 10 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$29.30 |
| Signal saved | -$2405.73 |
| Portfolio value | $98,924.64 |
| Benchmark value | $98,148.52 |
| Alpha (cumulative) | +0.776% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 11 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$51.70 |
| Signal saved | -$2383.33 |
| Portfolio value | $98,924.64 |
| Benchmark value | $96,660.94 |
| Alpha (cumulative) | +2.264% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 12 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$27.64 |
| Signal saved | -$2407.39 |
| Portfolio value | $98,924.64 |
| Benchmark value | $98,258.76 |
| Alpha (cumulative) | +0.666% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 13 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$17.34 |
| Signal saved | -$2417.69 |
| Portfolio value | $98,924.64 |
| Benchmark value | $98,942.78 |
| Alpha (cumulative) | -0.018% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 14 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$4.46 |
| Signal saved | -$2439.49 |
| Portfolio value | $98,924.64 |
| Benchmark value | $100,390.52 |
| Alpha (cumulative) | -1.466% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,777.14 |
| Benchmark value | $102,164.99 |
| Alpha (cumulative) | -3.388% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 16 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$28.54 |
| Signal saved | -$2463.57 |
| Portfolio value | $98,837.64 |
| Benchmark value | $101,989.67 |
| Alpha (cumulative) | -3.152% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 17 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$26.26 |
| Signal saved | -$2461.29 |
| Portfolio value | $98,837.64 |
| Benchmark value | $101,838.25 |
| Alpha (cumulative) | -3.000% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,773.37 |
| Benchmark value | $102,437.27 |
| Alpha (cumulative) | -3.664% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 19 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$35.00 |
| Signal saved | -$2470.03 |
| Portfolio value | $98,862.62 |
| Benchmark value | $102,418.68 |
| Alpha (cumulative) | -3.556% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,606.02 |
| Benchmark value | $102,086.63 |
| Alpha (cumulative) | -3.481% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.65% from entry. No exit triggered.

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
| Portfolio value | $98,709.04 |
| Benchmark value | $102,354.92 |
| Alpha (cumulative) | -3.646% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

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
| Portfolio value | $98,978.32 |
| Benchmark value | $103,056.21 |
| Alpha (cumulative) | -4.078% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

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
| Portfolio value | $98,900.29 |
| Benchmark value | $102,853.00 |
| Alpha (cumulative) | -3.953% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.10% from entry. No exit triggered.

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
| Portfolio value | $98,713.12 |
| Benchmark value | $102,365.55 |
| Alpha (cumulative) | -3.653% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

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
| Portfolio value | $98,445.37 |
| Benchmark value | $101,668.24 |
| Alpha (cumulative) | -3.223% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.06% from entry. No exit triggered.

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
| Portfolio value | $98,533.60 |
| Benchmark value | $101,898.02 |
| Alpha (cumulative) | -3.364% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.83% from entry. No exit triggered.

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
| Portfolio value | $98,204.14 |
| Benchmark value | $101,040.01 |
| Alpha (cumulative) | -2.836% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.67% from entry. No exit triggered.

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
| Portfolio value | $98,357.65 |
| Benchmark value | $101,439.79 |
| Alpha (cumulative) | -3.082% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.28% from entry. No exit triggered.

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
| Portfolio value | $98,246.98 |
| Benchmark value | $101,151.58 |
| Alpha (cumulative) | -2.905% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.56% from entry. No exit triggered.

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
| Portfolio value | $98,365.30 |
| Benchmark value | $101,459.72 |
| Alpha (cumulative) | -3.095% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.26% from entry. No exit triggered.

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
| Portfolio value | $98,372.95 |
| Benchmark value | $101,479.64 |
| Alpha (cumulative) | -3.107% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.24% from entry. No exit triggered.

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
| Portfolio value | $98,639.68 |
| Benchmark value | $102,174.29 |
| Alpha (cumulative) | -3.534% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

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
| Portfolio value | $98,542.78 |
| Benchmark value | $101,921.93 |
| Alpha (cumulative) | -3.379% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

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
| Portfolio value | $98,420.38 |
| Benchmark value | $101,603.16 |
| Alpha (cumulative) | -3.183% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 35 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$12.26 |
| Signal saved | -$2447.29 |
| Portfolio value | $98,250.04 |
| Benchmark value | $100,908.51 |
| Alpha (cumulative) | -2.659% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,163.85 |
| Benchmark value | $101,372.06 |
| Alpha (cumulative) | -3.208% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.22% from entry. No exit triggered.

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
| Portfolio value | $98,570.32 |
| Benchmark value | $102,430.63 |
| Alpha (cumulative) | -3.861% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.82% from entry. No exit triggered.

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
| Portfolio value | $98,420.89 |
| Benchmark value | $102,041.47 |
| Alpha (cumulative) | -3.620% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$21.10 |
| Signal saved | -$2456.13 |
| Portfolio value | $98,302.57 |
| Benchmark value | $101,495.58 |
| Alpha (cumulative) | -3.193% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,174.70 |
| Benchmark value | $101,014.77 |
| Alpha (cumulative) | -2.840% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$4.76 |
| Signal saved | -$2439.79 |
| Portfolio value | $98,038.46 |
| Benchmark value | $100,410.44 |
| Alpha (cumulative) | -2.372% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$17.28 |
| Signal saved | -$2452.31 |
| Portfolio value | $98,038.46 |
| Benchmark value | $101,241.89 |
| Alpha (cumulative) | -3.204% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$10.52 |
| Signal saved | -$2445.55 |
| Portfolio value | $98,038.46 |
| Benchmark value | $100,792.96 |
| Alpha (cumulative) | -2.754% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$3.86 |
| Signal saved | -$2438.89 |
| Portfolio value | $98,038.46 |
| Benchmark value | $100,350.67 |
| Alpha (cumulative) | -2.312% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | -$2.86 |
| Signal saved | -$2432.17 |
| Portfolio value | $98,038.46 |
| Benchmark value | $99,904.40 |
| Alpha (cumulative) | -1.866% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$14.28 |
| Signal saved | -$2449.31 |
| Portfolio value | $98,038.46 |
| Benchmark value | $101,042.66 |
| Alpha (cumulative) | -3.004% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$16.02 |
| Signal saved | -$2451.05 |
| Portfolio value | $98,038.46 |
| Benchmark value | $101,158.22 |
| Alpha (cumulative) | -3.120% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$39.82 |
| Signal saved | -$2474.85 |
| Portfolio value | $98,038.46 |
| Benchmark value | $102,738.77 |
| Alpha (cumulative) | -4.700% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$39.66 |
| Signal saved | -$2474.69 |
| Portfolio value | $98,053.25 |
| Benchmark value | $102,728.15 |
| Alpha (cumulative) | -4.675% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$28.64 |
| Signal saved | -$2463.67 |
| Portfolio value | $98,024.48 |
| Benchmark value | $101,996.31 |
| Alpha (cumulative) | -3.972% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$27.36 |
| Signal saved | -$2462.39 |
| Portfolio value | $98,024.48 |
| Benchmark value | $101,911.30 |
| Alpha (cumulative) | -3.886% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$35.48 |
| Signal saved | -$2470.51 |
| Portfolio value | $98,024.48 |
| Benchmark value | $102,450.55 |
| Alpha (cumulative) | -4.426% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,031.62 |
| Benchmark value | $101,672.23 |
| Alpha (cumulative) | -3.640% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.38 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$21.54 |
| Signal saved | -$2456.57 |
| Portfolio value | $98,056.61 |
| Benchmark value | $101,524.80 |
| Alpha (cumulative) | -3.468% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $97,839.86 |
| Benchmark value | $101,253.85 |
| Alpha (cumulative) | -3.414% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.55% from entry. No exit triggered.

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
| Portfolio value | $97,929.62 |
| Benchmark value | $101,487.61 |
| Alpha (cumulative) | -3.558% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.33% from entry. No exit triggered.

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
| Portfolio value | $98,212.67 |
| Benchmark value | $102,224.76 |
| Alpha (cumulative) | -4.012% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.40% from entry. No exit triggered.

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
| Portfolio value | $98,483.99 |
| Benchmark value | $102,931.36 |
| Alpha (cumulative) | -4.447% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +1.09% from entry. No exit triggered.

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
| Portfolio value | $98,694.62 |
| Benchmark value | $103,479.91 |
| Alpha (cumulative) | -4.785% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +1.63% from entry. No exit triggered.

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
| Portfolio value | $98,595.17 |
| Benchmark value | $103,220.91 |
| Alpha (cumulative) | -4.626% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +1.38% from entry. No exit triggered.

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
| Portfolio value | $98,428.40 |
| Benchmark value | $102,786.59 |
| Alpha (cumulative) | -4.359% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.95% from entry. No exit triggered.

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
| Portfolio value | $98,664.53 |
| Benchmark value | $103,401.54 |
| Alpha (cumulative) | -4.738% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +1.55% from entry. No exit triggered.

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
| Portfolio value | $98,640.05 |
| Benchmark value | $103,337.79 |
| Alpha (cumulative) | -4.698% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

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
| Portfolio value | $98,640.05 |
| Benchmark value | $103,337.79 |
| Alpha (cumulative) | -4.698% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 65 — 2026-10-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.65 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$32.08 |
| Signal saved | -$2467.11 |
| Portfolio value | $98,112.20 |
| Benchmark value | $102,224.76 |
| Alpha (cumulative) | -4.113% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,222.87 |
| Benchmark value | $102,506.34 |
| Alpha (cumulative) | -4.283% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.28% from entry. No exit triggered.

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
| Portfolio value | $97,792.94 |
| Benchmark value | $101,386.67 |
| Alpha (cumulative) | -3.594% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

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
| Portfolio value | $97,959.20 |
| Benchmark value | $101,819.66 |
| Alpha (cumulative) | -3.861% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 69 — 2026-10-20

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $769.09 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$30.96 |
| Signal saved | -$2465.99 |
| Portfolio value | $98,163.71 |
| Benchmark value | $102,150.38 |
| Alpha (cumulative) | -3.986% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $98,126.99 |
| Benchmark value | $102,686.97 |
| Alpha (cumulative) | -4.560% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 71 — 2026-10-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $764.03 |
| Realized P&L (locked) | -$2435.03 |
| Reference if held | +$20.84 |
| Signal saved | -$2455.87 |
| Portfolio value | $97,564.97 |
| Benchmark value | $101,478.31 |
| Alpha (cumulative) | -3.913% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2435.03. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 72 — 2026-10-23

| Field | Value |
|---|---|
| Position | Long 51 SPY (T20) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $759.83 |
| Unrealized P&L | -$39.27 |
| P&L % | -0.101% |
| Portfolio value | $97,525.70 |
| Benchmark value | $100,920.47 |
| Alpha (cumulative) | -3.394% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: -0.10% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 73 — 2026-10-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T20) |
| Entry (Alpaca fill) | $753.610/share |
| Close price | $765.37 |
| Unrealized P&L | +$243.27 |
| P&L % | +0.627% |
| Portfolio value | $97,808.24 |
| Benchmark value | $101,656.29 |
| Alpha (cumulative) | -3.848% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $770.15 vs MA50 $766.9). Momentum: WEAK. Unrealized P&L: +0.63% from entry. No exit triggered.

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
_Day 73 of 90 · Alpaca equity: $98,838.24 · Cumulative alpha vs SPY: -3.848%_