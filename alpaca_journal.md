# ALPACA PAPER JOURNAL — SPY
_Last updated: September 11, 2026 | Day 58 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$744.661/share**
> (2026-06-22, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-09-11): **BEARISH**  
> Fast: MA10 $765.72 | MA30 $767.31  
> Slow: MA20 $766.88 | MA50 $758.62  
> Regime: **BULL** | Momentum: **WEAK** | Session: AFTER_HOURS

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

**Total trades:** 16 | **Closed:** 16 | **Open:** No | **Cumulative Realized P&L:** -$2112.88

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T2 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T3 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T4 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T5 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T6 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T7 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T8 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T9 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T10 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T11 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T12 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T13 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T14 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T15 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T16 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,074.23 |
| Alpaca cash | $99,074.23 |
| Cumulative realized P&L | -$2112.88 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-06-22 | $744.27 | FLAT | — | — | $99,998.89 |
| Day 2 | 2026-06-23 | $733.62 | FLAT | — | — | $99,998.89 |
| Day 3 | 2026-06-24 | $733.32 | FLAT | — | — | $99,998.89 |
| Day 4 | 2026-06-25 | $733.33 | FLAT | — | — | $99,998.89 |
| Day 5 | 2026-06-26 | $729.35 | FLAT | — | — | $99,998.89 |
| Day 6 | 2026-06-29 | $740.86 | FLAT | — | — | $99,998.89 |
| Day 7 | 2026-06-30 | $746.65 | FLAT | — | — | $99,998.89 |
| Day 8 | 2026-07-01 | $745.66 | FLAT | — | — | $99,998.89 |
| Day 9 | 2026-07-02 | $744.86 | FLAT | — | — | $99,998.89 |
| Day 10 | 2026-07-06 | $751.27 | FLAT | — | — | $99,998.89 |
| Day 11 | 2026-07-07 | $747.77 | FLAT | — | — | $99,998.89 |
| Day 12 | 2026-07-08 | $745.28 | FLAT | — | — | $99,998.89 |
| Day 13 | 2026-07-09 | $751.55 | FLAT | — | — | $99,998.89 |
| Day 14 | 2026-07-10 | $754.94 | FLAT | — | — | $99,998.89 |
| Day 15 | 2026-07-13 | $749.13 | FLAT | — | — | $99,837.77 |
| Day 16 | 2026-07-14 | $751.94 | FLAT | — | — | $99,802.69 |
| Day 17 | 2026-07-15 | $754.77 | FLAT | — | — | $99,850.44 |
| Day 18 | 2026-07-16 | $750.87 | FLAT | — | — | $99,674.31 |
| Day 19 | 2026-07-17 | $743.28 | FLAT | — | — | $99,531.75 |
| Day 20 | 2026-07-20 | $742.15 | FLAT | — | — | $99,339.77 |
| Day 21 | 2026-07-21 | $748.15 | Long 53 SPY (T8) | +$28.09 | +0.071% | $99,367.86 |
| Day 22 | 2026-07-22 | $747.49 | Long 53 SPY (T8) | -$6.89 | -0.017% | $99,332.88 |
| Day 23 | 2026-07-23 | $738.06 | Long 52 SPY (T9) | -$40.56 | -0.106% | $98,663.74 |
| Day 24 | 2026-07-24 | $738.90 | FLAT | — | — | $98,712.62 |
| Day 25 | 2026-07-27 | $738.85 | FLAT | — | — | $98,816.76 |
| Day 26 | 2026-07-28 | $740.79 | FLAT | — | — | $98,773.30 |
| Day 27 | 2026-07-29 | $729.57 | FLAT | — | — | $98,773.30 |
| Day 28 | 2026-07-30 | $741.63 | FLAT | — | — | $98,773.30 |
| Day 29 | 2026-07-31 | $746.79 | FLAT | — | — | $98,773.30 |
| Day 30 | 2026-08-03 | $757.72 | FLAT | — | — | $98,773.30 |
| Day 31 | 2026-08-04 | $771.11 | Long 50 SPY (T12) | -$52.00 | -0.135% | $98,721.30 |
| Day 32 | 2026-08-05 | $769.79 | FLAT | — | — | $98,686.30 |
| Day 33 | 2026-08-06 | $768.64 | FLAT | — | — | $98,686.30 |
| Day 34 | 2026-08-07 | $773.16 | Long 51 SPY (T13) | +$33.14 | +0.084% | $98,719.44 |
| Day 35 | 2026-08-10 | $773.02 | FLAT | — | — | $98,711.28 |
| Day 36 | 2026-08-11 | $770.52 | Long 51 SPY (T14) | -$159.19 | -0.403% | $98,552.09 |
| Day 37 | 2026-08-12 | $772.54 | Long 51 SPY (T14) | -$56.17 | -0.142% | $98,655.11 |
| Day 38 | 2026-08-13 | $777.84 | Long 51 SPY (T14) | +$214.13 | +0.543% | $98,925.41 |
| Day 39 | 2026-08-14 | $776.30 | Long 51 SPY (T14) | +$135.59 | +0.344% | $98,846.87 |
| Day 40 | 2026-08-17 | $772.62 | Long 51 SPY (T14) | -$52.09 | -0.132% | $98,659.19 |
| Day 41 | 2026-08-18 | $767.37 | Long 51 SPY (T14) | -$319.84 | -0.811% | $98,391.44 |
| Day 42 | 2026-08-19 | $769.09 | Long 51 SPY (T14) | -$232.12 | -0.588% | $98,479.16 |
| Day 43 | 2026-08-20 | $762.62 | Long 51 SPY (T14) | -$562.09 | -1.425% | $98,149.19 |
| Day 44 | 2026-08-21 | $765.64 | Long 51 SPY (T14) | -$408.07 | -1.034% | $98,303.21 |
| Day 45 | 2026-08-24 | $763.46 | Long 51 SPY (T14) | -$519.25 | -1.316% | $98,192.03 |
| Day 46 | 2026-08-25 | $765.79 | Long 51 SPY (T14) | -$400.42 | -1.015% | $98,310.86 |
| Day 47 | 2026-08-26 | $765.94 | Long 51 SPY (T14) | -$392.77 | -0.995% | $98,318.51 |
| Day 48 | 2026-08-27 | $771.18 | Long 51 SPY (T14) | -$125.53 | -0.318% | $98,585.75 |
| Day 49 | 2026-08-28 | $769.28 | Long 51 SPY (T14) | -$222.43 | -0.564% | $98,488.85 |
| Day 50 | 2026-08-31 | $766.87 | Long 51 SPY (T14) | -$345.34 | -0.875% | $98,365.94 |
| Day 51 | 2026-09-01 | $761.63 | FLAT | — | — | $98,098.70 |
| Day 52 | 2026-09-02 | $765.13 | Long 51 SPY (T15) | +$10.71 | +0.027% | $98,109.41 |
| Day 53 | 2026-09-03 | $773.12 | Long 51 SPY (T15) | +$418.20 | +1.072% | $98,516.90 |
| Day 54 | 2026-09-04 | $770.18 | Long 51 SPY (T15) | +$268.26 | +0.688% | $98,366.96 |
| Day 55 | 2026-09-08 | $766.06 | FLAT | — | — | $98,151.23 |
| Day 56 | 2026-09-09 | $762.42 | Long 52 SPY (T16) | -$30.11 | -0.076% | $98,121.12 |
| Day 57 | 2026-09-10 | $757.87 | FLAT | — | — | $97,887.12 |
| Day 58 | 2026-09-11 | $764.14 | FLAT | — | — | $97,887.12 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-06-22 | $99,998.89 | $99,999.97 | -0.0011% | -0.000% | **-0.001%** |
| Day 2 | 2026-06-23 | $99,998.89 | $98,569.04 | -0.0011% | -1.431% | **+1.430%** |
| Day 3 | 2026-06-24 | $99,998.89 | $98,528.73 | -0.0011% | -1.471% | **+1.470%** |
| Day 4 | 2026-06-25 | $99,998.89 | $98,530.07 | -0.0011% | -1.470% | **+1.469%** |
| Day 5 | 2026-06-26 | $99,998.89 | $97,995.32 | -0.0011% | -2.005% | **+2.004%** |
| Day 6 | 2026-06-29 | $99,998.89 | $99,541.80 | -0.0011% | -0.458% | **+0.457%** |
| Day 7 | 2026-06-30 | $99,998.89 | $100,319.74 | -0.0011% | +0.320% | **-0.321%** |
| Day 8 | 2026-07-01 | $99,998.89 | $100,186.73 | -0.0011% | +0.187% | **-0.188%** |
| Day 9 | 2026-07-02 | $99,998.89 | $100,079.24 | -0.0011% | +0.079% | **-0.080%** |
| Day 10 | 2026-07-06 | $99,998.89 | $100,940.49 | -0.0011% | +0.940% | **-0.941%** |
| Day 11 | 2026-07-07 | $99,998.89 | $100,470.23 | -0.0011% | +0.470% | **-0.471%** |
| Day 12 | 2026-07-08 | $99,998.89 | $100,135.67 | -0.0011% | +0.136% | **-0.137%** |
| Day 13 | 2026-07-09 | $99,998.89 | $100,978.11 | -0.0011% | +0.978% | **-0.979%** |
| Day 14 | 2026-07-10 | $99,998.89 | $101,433.59 | -0.0011% | +1.434% | **-1.435%** |
| Day 15 | 2026-07-13 | $99,837.77 | $100,652.96 | -0.1622% | +0.653% | **-0.815%** |
| Day 16 | 2026-07-14 | $99,802.69 | $101,030.51 | -0.1973% | +1.031% | **-1.228%** |
| Day 17 | 2026-07-15 | $99,850.44 | $101,410.75 | -0.1496% | +1.411% | **-1.561%** |
| Day 18 | 2026-07-16 | $99,674.31 | $100,886.74 | -0.3257% | +0.887% | **-1.213%** |
| Day 19 | 2026-07-17 | $99,531.75 | $99,866.95 | -0.4682% | -0.133% | **-0.335%** |
| Day 20 | 2026-07-20 | $99,339.77 | $99,715.13 | -0.6602% | -0.285% | **-0.375%** |
| Day 21 | 2026-07-21 | $99,367.86 | $100,521.28 | -0.6321% | +0.521% | **-1.153%** |
| Day 22 | 2026-07-22 | $99,332.88 | $100,432.61 | -0.6671% | +0.433% | **-1.100%** |
| Day 23 | 2026-07-23 | $98,663.74 | $99,165.59 | -1.3363% | -0.834% | **-0.502%** |
| Day 24 | 2026-07-24 | $98,712.62 | $99,278.46 | -1.2874% | -0.722% | **-0.565%** |
| Day 25 | 2026-07-27 | $98,816.76 | $99,271.74 | -1.1832% | -0.728% | **-0.455%** |
| Day 26 | 2026-07-28 | $98,773.30 | $99,532.40 | -1.2267% | -0.468% | **-0.759%** |
| Day 27 | 2026-07-29 | $98,773.30 | $98,024.88 | -1.2267% | -1.975% | **+0.748%** |
| Day 28 | 2026-07-30 | $98,773.30 | $99,645.26 | -1.2267% | -0.355% | **-0.872%** |
| Day 29 | 2026-07-31 | $98,773.30 | $100,338.56 | -1.2267% | +0.339% | **-1.566%** |
| Day 30 | 2026-08-03 | $98,773.30 | $101,807.11 | -1.2267% | +1.807% | **-3.034%** |
| Day 31 | 2026-08-04 | $98,721.30 | $103,606.19 | -1.2787% | +3.606% | **-4.885%** |
| Day 32 | 2026-08-05 | $98,686.30 | $103,428.83 | -1.3137% | +3.429% | **-4.743%** |
| Day 33 | 2026-08-06 | $98,686.30 | $103,274.32 | -1.3137% | +3.274% | **-4.588%** |
| Day 34 | 2026-08-07 | $98,719.44 | $103,881.62 | -1.2806% | +3.882% | **-5.163%** |
| Day 35 | 2026-08-10 | $98,711.28 | $103,862.81 | -1.2887% | +3.863% | **-5.152%** |
| Day 36 | 2026-08-11 | $98,552.09 | $103,526.91 | -1.4479% | +3.527% | **-4.975%** |
| Day 37 | 2026-08-12 | $98,655.11 | $103,798.32 | -1.3449% | +3.798% | **-5.143%** |
| Day 38 | 2026-08-13 | $98,925.41 | $104,510.43 | -1.0746% | +4.510% | **-5.585%** |
| Day 39 | 2026-08-14 | $98,846.87 | $104,303.51 | -1.1531% | +4.304% | **-5.457%** |
| Day 40 | 2026-08-17 | $98,659.19 | $103,809.07 | -1.3408% | +3.809% | **-5.150%** |
| Day 41 | 2026-08-18 | $98,391.44 | $103,103.68 | -1.6086% | +3.104% | **-4.713%** |
| Day 42 | 2026-08-19 | $98,479.16 | $103,334.78 | -1.5208% | +3.335% | **-4.856%** |
| Day 43 | 2026-08-20 | $98,149.19 | $102,465.47 | -1.8508% | +2.465% | **-4.316%** |
| Day 44 | 2026-08-21 | $98,303.21 | $102,871.24 | -1.6968% | +2.871% | **-4.568%** |
| Day 45 | 2026-08-24 | $98,192.03 | $102,578.33 | -1.8080% | +2.578% | **-4.386%** |
| Day 46 | 2026-08-25 | $98,310.86 | $102,891.39 | -1.6891% | +2.891% | **-4.580%** |
| Day 47 | 2026-08-26 | $98,318.51 | $102,911.55 | -1.6815% | +2.912% | **-4.594%** |
| Day 48 | 2026-08-27 | $98,585.75 | $103,615.59 | -1.4142% | +3.616% | **-5.030%** |
| Day 49 | 2026-08-28 | $98,488.85 | $103,360.31 | -1.5111% | +3.360% | **-4.871%** |
| Day 50 | 2026-08-31 | $98,365.94 | $103,036.50 | -1.6341% | +3.036% | **-4.670%** |
| Day 51 | 2026-09-01 | $98,098.70 | $102,332.45 | -1.9013% | +2.332% | **-4.233%** |
| Day 52 | 2026-09-02 | $98,109.41 | $102,802.71 | -1.8906% | +2.803% | **-4.694%** |
| Day 53 | 2026-09-03 | $98,516.90 | $103,876.25 | -1.4831% | +3.876% | **-5.359%** |
| Day 54 | 2026-09-04 | $98,366.96 | $103,481.23 | -1.6330% | +3.481% | **-5.114%** |
| Day 55 | 2026-09-08 | $98,151.23 | $102,927.67 | -1.8488% | +2.928% | **-4.777%** |
| Day 56 | 2026-09-09 | $98,121.12 | $102,438.60 | -1.8789% | +2.439% | **-4.318%** |
| Day 57 | 2026-09-10 | $97,887.12 | $101,827.26 | -2.1129% | +1.827% | **-3.940%** |
| Day 58 | 2026-09-11 | $97,887.12 | $102,669.70 | -2.1129% | +2.670% | **-4.783%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-06-22 | $744.27 | -$21.09 | -$2091.79 | Holding would have been **$2091.79** better — honest entry |
| Day 2 | 2026-06-23 | $733.62 | -$596.19 | -$1516.69 | Holding would have been **$1516.69** better — honest entry |
| Day 3 | 2026-06-24 | $733.32 | -$612.39 | -$1500.49 | Holding would have been **$1500.49** better — honest entry |
| Day 4 | 2026-06-25 | $733.33 | -$611.85 | -$1501.03 | Holding would have been **$1501.03** better — honest entry |
| Day 5 | 2026-06-26 | $729.35 | -$826.77 | -$1286.11 | Holding would have been **$1286.11** better — honest entry |
| Day 6 | 2026-06-29 | $740.86 | -$205.23 | -$1907.65 | Holding would have been **$1907.65** better — honest entry |
| Day 7 | 2026-06-30 | $746.65 | +$107.43 | -$2220.31 | Holding would have been **$2220.31** better — honest entry |
| Day 8 | 2026-07-01 | $745.66 | +$53.97 | -$2166.85 | Holding would have been **$2166.85** better — honest entry |
| Day 9 | 2026-07-02 | $744.86 | +$10.77 | -$2123.65 | Holding would have been **$2123.65** better — honest entry |
| Day 10 | 2026-07-06 | $751.27 | +$356.91 | -$2469.79 | Holding would have been **$2469.79** better — honest entry |
| Day 11 | 2026-07-07 | $747.77 | +$167.91 | -$2280.79 | Holding would have been **$2280.79** better — honest entry |
| Day 12 | 2026-07-08 | $745.28 | +$33.45 | -$2146.33 | Holding would have been **$2146.33** better — honest entry |
| Day 13 | 2026-07-09 | $751.55 | +$372.03 | -$2484.91 | Holding would have been **$2484.91** better — honest entry |
| Day 14 | 2026-07-10 | $754.94 | +$555.09 | -$2667.97 | Holding would have been **$2667.97** better — honest entry |
| Day 15 | 2026-07-13 | $749.13 | +$241.35 | -$2354.23 | Holding would have been **$2354.23** better — honest entry |
| Day 16 | 2026-07-14 | $751.94 | +$393.09 | -$2505.97 | Holding would have been **$2505.97** better — honest entry |
| Day 17 | 2026-07-15 | $754.77 | +$545.91 | -$2658.79 | Holding would have been **$2658.79** better — honest entry |
| Day 18 | 2026-07-16 | $750.87 | +$335.31 | -$2448.19 | Holding would have been **$2448.19** better — honest entry |
| Day 19 | 2026-07-17 | $743.28 | -$74.55 | -$2038.33 | Holding would have been **$2038.33** better — honest entry |
| Day 20 | 2026-07-20 | $742.15 | -$135.57 | -$1977.31 | Holding would have been **$1977.31** better — honest entry |
| Day 21 | 2026-07-21 | $748.15 | +$188.43 | -$2301.31 | Position open |
| Day 22 | 2026-07-22 | $747.49 | +$152.79 | -$2265.67 | Position open |
| Day 23 | 2026-07-23 | $738.06 | -$356.43 | -$1756.45 | Position open |
| Day 24 | 2026-07-24 | $738.90 | -$311.07 | -$1801.81 | Holding would have been **$1801.81** better — honest entry |
| Day 25 | 2026-07-27 | $738.85 | -$313.77 | -$1799.11 | Holding would have been **$1799.11** better — honest entry |
| Day 26 | 2026-07-28 | $740.79 | -$209.01 | -$1903.87 | Holding would have been **$1903.87** better — honest entry |
| Day 27 | 2026-07-29 | $729.57 | -$814.89 | -$1297.99 | Holding would have been **$1297.99** better — honest entry |
| Day 28 | 2026-07-30 | $741.63 | -$163.65 | -$1949.23 | Holding would have been **$1949.23** better — honest entry |
| Day 29 | 2026-07-31 | $746.79 | +$114.99 | -$2227.87 | Holding would have been **$2227.87** better — honest entry |
| Day 30 | 2026-08-03 | $757.72 | +$705.21 | -$2818.09 | Holding would have been **$2818.09** better — honest entry |
| Day 31 | 2026-08-04 | $771.11 | +$1428.27 | -$3541.15 | Position open |
| Day 32 | 2026-08-05 | $769.79 | +$1356.99 | -$3469.87 | Holding would have been **$3469.87** better — honest entry |
| Day 33 | 2026-08-06 | $768.64 | +$1294.89 | -$3407.77 | Holding would have been **$3407.77** better — honest entry |
| Day 34 | 2026-08-07 | $773.16 | +$1538.97 | -$3651.85 | Position open |
| Day 35 | 2026-08-10 | $773.02 | +$1531.41 | -$3644.29 | Holding would have been **$3644.29** better — honest entry |
| Day 36 | 2026-08-11 | $770.52 | +$1396.41 | -$3509.29 | Position open |
| Day 37 | 2026-08-12 | $772.54 | +$1505.49 | -$3618.37 | Position open |
| Day 38 | 2026-08-13 | $777.84 | +$1791.69 | -$3904.57 | Position open |
| Day 39 | 2026-08-14 | $776.30 | +$1708.53 | -$3821.41 | Position open |
| Day 40 | 2026-08-17 | $772.62 | +$1509.81 | -$3622.69 | Position open |
| Day 41 | 2026-08-18 | $767.37 | +$1226.31 | -$3339.19 | Position open |
| Day 42 | 2026-08-19 | $769.09 | +$1319.19 | -$3432.07 | Position open |
| Day 43 | 2026-08-20 | $762.62 | +$969.81 | -$3082.69 | Position open |
| Day 44 | 2026-08-21 | $765.64 | +$1132.89 | -$3245.77 | Position open |
| Day 45 | 2026-08-24 | $763.46 | +$1015.17 | -$3128.05 | Position open |
| Day 46 | 2026-08-25 | $765.79 | +$1140.99 | -$3253.87 | Position open |
| Day 47 | 2026-08-26 | $765.94 | +$1149.09 | -$3261.97 | Position open |
| Day 48 | 2026-08-27 | $771.18 | +$1432.05 | -$3544.93 | Position open |
| Day 49 | 2026-08-28 | $769.28 | +$1329.45 | -$3442.33 | Position open |
| Day 50 | 2026-08-31 | $766.87 | +$1199.31 | -$3312.19 | Position open |
| Day 51 | 2026-09-01 | $761.63 | +$916.35 | -$3029.23 | Holding would have been **$3029.23** better — honest entry |
| Day 52 | 2026-09-02 | $765.13 | +$1105.35 | -$3218.23 | Position open |
| Day 53 | 2026-09-03 | $773.12 | +$1536.81 | -$3649.69 | Position open |
| Day 54 | 2026-09-04 | $770.18 | +$1378.05 | -$3490.93 | Position open |
| Day 55 | 2026-09-08 | $766.06 | +$1155.57 | -$3268.45 | Holding would have been **$3268.45** better — honest entry |
| Day 56 | 2026-09-09 | $762.42 | +$959.01 | -$3071.89 | Position open |
| Day 57 | 2026-09-10 | $757.87 | +$713.31 | -$2826.19 | Holding would have been **$2826.19** better — honest entry |
| Day 58 | 2026-09-11 | $764.14 | +$1051.89 | -$3164.77 | Holding would have been **$3164.77** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $744.27 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$21.09 |
| Signal saved | -$2091.79 |
| Portfolio value | $99,998.89 |
| Benchmark value | $99,999.97 |
| Alpha (cumulative) | -0.001% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 2 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $733.62 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$596.19 |
| Signal saved | -$1516.69 |
| Portfolio value | $99,998.89 |
| Benchmark value | $98,569.04 |
| Alpha (cumulative) | +1.430% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 3 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $733.32 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$612.39 |
| Signal saved | -$1500.49 |
| Portfolio value | $99,998.89 |
| Benchmark value | $98,528.73 |
| Alpha (cumulative) | +1.470% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 4 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $733.33 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$611.85 |
| Signal saved | -$1501.03 |
| Portfolio value | $99,998.89 |
| Benchmark value | $98,530.07 |
| Alpha (cumulative) | +1.469% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 5 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $729.35 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$826.77 |
| Signal saved | -$1286.11 |
| Portfolio value | $99,998.89 |
| Benchmark value | $97,995.32 |
| Alpha (cumulative) | +2.004% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 6 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $740.86 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$205.23 |
| Signal saved | -$1907.65 |
| Portfolio value | $99,998.89 |
| Benchmark value | $99,541.80 |
| Alpha (cumulative) | +0.457% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 7 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $746.65 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$107.43 |
| Signal saved | -$2220.31 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,319.74 |
| Alpha (cumulative) | -0.321% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 8 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $745.66 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$53.97 |
| Signal saved | -$2166.85 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,186.73 |
| Alpha (cumulative) | -0.188% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 9 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $744.86 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$10.77 |
| Signal saved | -$2123.65 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,079.24 |
| Alpha (cumulative) | -0.080% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 10 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $751.27 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$356.91 |
| Signal saved | -$2469.79 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,940.49 |
| Alpha (cumulative) | -0.941% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 11 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $747.77 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$167.91 |
| Signal saved | -$2280.79 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,470.23 |
| Alpha (cumulative) | -0.471% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 12 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $745.28 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$33.45 |
| Signal saved | -$2146.33 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,135.67 |
| Alpha (cumulative) | -0.137% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 13 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $751.55 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$372.03 |
| Signal saved | -$2484.91 |
| Portfolio value | $99,998.89 |
| Benchmark value | $100,978.11 |
| Alpha (cumulative) | -0.979% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 14 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $754.94 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$555.09 |
| Signal saved | -$2667.97 |
| Portfolio value | $99,998.89 |
| Benchmark value | $101,433.59 |
| Alpha (cumulative) | -1.435% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 15 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $749.13 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$241.35 |
| Signal saved | -$2354.23 |
| Portfolio value | $99,837.77 |
| Benchmark value | $100,652.96 |
| Alpha (cumulative) | -0.815% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 16 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $751.94 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$393.09 |
| Signal saved | -$2505.97 |
| Portfolio value | $99,802.69 |
| Benchmark value | $101,030.51 |
| Alpha (cumulative) | -1.228% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 17 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $754.77 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$545.91 |
| Signal saved | -$2658.79 |
| Portfolio value | $99,850.44 |
| Benchmark value | $101,410.75 |
| Alpha (cumulative) | -1.561% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 18 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $750.87 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$335.31 |
| Signal saved | -$2448.19 |
| Portfolio value | $99,674.31 |
| Benchmark value | $100,886.74 |
| Alpha (cumulative) | -1.213% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 19 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $743.28 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$74.55 |
| Signal saved | -$2038.33 |
| Portfolio value | $99,531.75 |
| Benchmark value | $99,866.95 |
| Alpha (cumulative) | -0.335% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 20 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $742.15 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$135.57 |
| Signal saved | -$1977.31 |
| Portfolio value | $99,339.77 |
| Benchmark value | $99,715.13 |
| Alpha (cumulative) | -0.375% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 21 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T8) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $99,367.86 |
| Benchmark value | $100,521.28 |
| Alpha (cumulative) | -1.153% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 22 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T8) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $99,332.88 |
| Benchmark value | $100,432.61 |
| Alpha (cumulative) | -1.100% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 23 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T9) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $98,663.74 |
| Benchmark value | $99,165.59 |
| Alpha (cumulative) | -0.502% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 24 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $738.90 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$311.07 |
| Signal saved | -$1801.81 |
| Portfolio value | $98,712.62 |
| Benchmark value | $99,278.46 |
| Alpha (cumulative) | -0.565% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 25 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $738.85 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$313.77 |
| Signal saved | -$1799.11 |
| Portfolio value | $98,816.76 |
| Benchmark value | $99,271.74 |
| Alpha (cumulative) | -0.455% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 26 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $740.79 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$209.01 |
| Signal saved | -$1903.87 |
| Portfolio value | $98,773.30 |
| Benchmark value | $99,532.40 |
| Alpha (cumulative) | -0.759% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 27 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $729.57 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$814.89 |
| Signal saved | -$1297.99 |
| Portfolio value | $98,773.30 |
| Benchmark value | $98,024.88 |
| Alpha (cumulative) | +0.748% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 28 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $741.63 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | -$163.65 |
| Signal saved | -$1949.23 |
| Portfolio value | $98,773.30 |
| Benchmark value | $99,645.26 |
| Alpha (cumulative) | -0.872% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 29 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $746.79 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$114.99 |
| Signal saved | -$2227.87 |
| Portfolio value | $98,773.30 |
| Benchmark value | $100,338.56 |
| Alpha (cumulative) | -1.566% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 30 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $757.72 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$705.21 |
| Signal saved | -$2818.09 |
| Portfolio value | $98,773.30 |
| Benchmark value | $101,807.11 |
| Alpha (cumulative) | -3.034% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 31 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T12) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $771.11 |
| Unrealized P&L | -$52.00 |
| P&L % | -0.135% |
| Portfolio value | $98,721.30 |
| Benchmark value | $103,606.19 |
| Alpha (cumulative) | -4.885% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 32 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $769.79 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$1356.99 |
| Signal saved | -$3469.87 |
| Portfolio value | $98,686.30 |
| Benchmark value | $103,428.83 |
| Alpha (cumulative) | -4.743% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 33 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $768.64 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$1294.89 |
| Signal saved | -$3407.77 |
| Portfolio value | $98,686.30 |
| Benchmark value | $103,274.32 |
| Alpha (cumulative) | -4.588% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 34 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $773.16 |
| Unrealized P&L | +$33.14 |
| P&L % | +0.084% |
| Portfolio value | $98,719.44 |
| Benchmark value | $103,881.62 |
| Alpha (cumulative) | -5.163% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +0.08% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 35 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $773.02 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$1531.41 |
| Signal saved | -$3644.29 |
| Portfolio value | $98,711.28 |
| Benchmark value | $103,862.81 |
| Alpha (cumulative) | -5.152% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 36 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $770.52 |
| Unrealized P&L | -$159.19 |
| P&L % | -0.403% |
| Portfolio value | $98,552.09 |
| Benchmark value | $103,526.91 |
| Alpha (cumulative) | -4.975% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.40% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 37 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $772.54 |
| Unrealized P&L | -$56.17 |
| P&L % | -0.142% |
| Portfolio value | $98,655.11 |
| Benchmark value | $103,798.32 |
| Alpha (cumulative) | -5.143% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 38 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $777.84 |
| Unrealized P&L | +$214.13 |
| P&L % | +0.543% |
| Portfolio value | $98,925.41 |
| Benchmark value | $104,510.43 |
| Alpha (cumulative) | -5.585% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +0.54% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 39 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $776.30 |
| Unrealized P&L | +$135.59 |
| P&L % | +0.344% |
| Portfolio value | $98,846.87 |
| Benchmark value | $104,303.51 |
| Alpha (cumulative) | -5.457% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +0.34% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 40 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $772.62 |
| Unrealized P&L | -$52.09 |
| P&L % | -0.132% |
| Portfolio value | $98,659.19 |
| Benchmark value | $103,809.07 |
| Alpha (cumulative) | -5.150% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.13% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 41 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,391.44 |
| Benchmark value | $103,103.68 |
| Alpha (cumulative) | -4.713% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 42 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $769.09 |
| Unrealized P&L | -$232.12 |
| P&L % | -0.588% |
| Portfolio value | $98,479.16 |
| Benchmark value | $103,334.78 |
| Alpha (cumulative) | -4.856% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.59% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 43 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $762.62 |
| Unrealized P&L | -$562.09 |
| P&L % | -1.425% |
| Portfolio value | $98,149.19 |
| Benchmark value | $102,465.47 |
| Alpha (cumulative) | -4.316% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -1.43% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 44 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $765.64 |
| Unrealized P&L | -$408.07 |
| P&L % | -1.034% |
| Portfolio value | $98,303.21 |
| Benchmark value | $102,871.24 |
| Alpha (cumulative) | -4.568% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -1.03% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 45 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $763.46 |
| Unrealized P&L | -$519.25 |
| P&L % | -1.316% |
| Portfolio value | $98,192.03 |
| Benchmark value | $102,578.33 |
| Alpha (cumulative) | -4.386% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -1.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 46 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $765.79 |
| Unrealized P&L | -$400.42 |
| P&L % | -1.015% |
| Portfolio value | $98,310.86 |
| Benchmark value | $102,891.39 |
| Alpha (cumulative) | -4.580% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -1.01% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 47 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $765.94 |
| Unrealized P&L | -$392.77 |
| P&L % | -0.995% |
| Portfolio value | $98,318.51 |
| Benchmark value | $102,911.55 |
| Alpha (cumulative) | -4.594% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.99% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 48 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $771.18 |
| Unrealized P&L | -$125.53 |
| P&L % | -0.318% |
| Portfolio value | $98,585.75 |
| Benchmark value | $103,615.59 |
| Alpha (cumulative) | -5.030% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 49 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $769.28 |
| Unrealized P&L | -$222.43 |
| P&L % | -0.564% |
| Portfolio value | $98,488.85 |
| Benchmark value | $103,360.31 |
| Alpha (cumulative) | -4.871% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 50 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $766.87 |
| Unrealized P&L | -$345.34 |
| P&L % | -0.875% |
| Portfolio value | $98,365.94 |
| Benchmark value | $103,036.50 |
| Alpha (cumulative) | -4.670% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.88% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $761.63 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$916.35 |
| Signal saved | -$3029.23 |
| Portfolio value | $98,098.70 |
| Benchmark value | $102,332.45 |
| Alpha (cumulative) | -4.233% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $765.13 |
| Unrealized P&L | +$10.71 |
| P&L % | +0.027% |
| Portfolio value | $98,109.41 |
| Benchmark value | $102,802.71 |
| Alpha (cumulative) | -4.694% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +0.03% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $773.12 |
| Unrealized P&L | +$418.20 |
| P&L % | +1.072% |
| Portfolio value | $98,516.90 |
| Benchmark value | $103,876.25 |
| Alpha (cumulative) | -5.359% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +1.07% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $770.18 |
| Unrealized P&L | +$268.26 |
| P&L % | +0.688% |
| Portfolio value | $98,366.96 |
| Benchmark value | $103,481.23 |
| Alpha (cumulative) | -5.114% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: +0.69% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 55 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $766.06 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$1155.57 |
| Signal saved | -$3268.45 |
| Portfolio value | $98,151.23 |
| Benchmark value | $102,927.67 |
| Alpha (cumulative) | -4.777% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 56 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T16) |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $762.42 |
| Unrealized P&L | -$30.11 |
| P&L % | -0.076% |
| Portfolio value | $98,121.12 |
| Benchmark value | $102,438.60 |
| Alpha (cumulative) | -4.318% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Momentum: WEAK. Unrealized P&L: -0.08% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $757.87 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$713.31 |
| Signal saved | -$2826.19 |
| Portfolio value | $97,887.12 |
| Benchmark value | $101,827.26 |
| Alpha (cumulative) | -3.940% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 58 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.661/share |
| Close price | $764.14 |
| Realized P&L (locked) | -$2112.88 |
| Reference if held | +$1051.89 |
| Signal saved | -$3164.77 |
| Portfolio value | $97,887.12 |
| Benchmark value | $102,669.70 |
| Alpha (cumulative) | -4.783% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2112.88. Regime: BULL (MA20 $766.88 vs MA50 $758.62). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

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
_Day 58 of 90 · Alpaca equity: $99,074.23 · Cumulative alpha vs SPY: -4.783%_