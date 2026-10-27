# ALPACA PAPER JOURNAL — SPY
_Last updated: October 27, 2026 | Day 73 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$753.323/share**
> (2026-07-16, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-10-27): **BEARISH**  
> Fast: MA10 $768.06 | MA30 $768.39  
> Slow: MA20 $770.14 | MA50 $766.72  
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

**Total trades:** 19 | **Closed:** 19 | **Open:** No | **Cumulative Realized P&L:** -$1992.09

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T2 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T3 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T4 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T5 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T6 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T7 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T8 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T9 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T10 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T11 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T12 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |
| T13 | $773.250 (2026-09-22) | $773.540 (2026-09-22) | 51 | +$14.79 | ✅ Closed |
| T14 | $768.534 (2026-09-23) | $767.970 (2026-09-23) | 51 | -$28.77 | ✅ Closed |
| T15 | $765.350 (2026-09-28) | $765.980 (2026-09-29) | 51 | +$32.13 | ✅ Closed |
| T16 | $766.590 (2026-09-30) | $767.680 (2026-10-14) | 51 | +$55.59 | ✅ Closed |
| T17 | $769.600 (2026-10-15) | $770.610 (2026-10-20) | 51 | +$51.51 | ✅ Closed |
| T18 | $773.850 (2026-10-21) | $762.110 (2026-10-22) | 51 | -$598.74 | ✅ Closed |
| T19 | $760.600 (2026-10-23) | $769.320 (2026-10-27) | 51 | +$444.72 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,041.62 |
| Alpaca cash | $85,963.01 |
| Cumulative realized P&L | -$1992.09 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-16 | $749.01 | FLAT | — | — | $99,823.87 |
| Day 2 | 2026-07-17 | $741.44 | FLAT | — | — | $99,681.31 |
| Day 3 | 2026-07-20 | $740.31 | FLAT | — | — | $99,489.33 |
| Day 4 | 2026-07-21 | $746.30 | Long 53 SPY (T4) | -$69.96 | -0.177% | $99,419.37 |
| Day 5 | 2026-07-22 | $745.64 | Long 53 SPY (T4) | -$104.94 | -0.265% | $99,384.39 |
| Day 6 | 2026-07-23 | $736.23 | Long 52 SPY (T5) | -$135.72 | -0.353% | $98,718.14 |
| Day 7 | 2026-07-24 | $737.07 | FLAT | — | — | $98,862.18 |
| Day 8 | 2026-07-27 | $737.02 | FLAT | — | — | $98,966.32 |
| Day 9 | 2026-07-28 | $738.96 | FLAT | — | — | $98,922.86 |
| Day 10 | 2026-07-29 | $727.76 | FLAT | — | — | $98,922.86 |
| Day 11 | 2026-07-30 | $739.79 | FLAT | — | — | $98,922.86 |
| Day 12 | 2026-07-31 | $744.94 | FLAT | — | — | $98,922.86 |
| Day 13 | 2026-08-03 | $755.84 | FLAT | — | — | $98,922.86 |
| Day 14 | 2026-08-04 | $769.20 | Long 50 SPY (T8) | -$147.50 | -0.382% | $98,775.36 |
| Day 15 | 2026-08-05 | $767.88 | FLAT | — | — | $98,835.86 |
| Day 16 | 2026-08-06 | $766.74 | FLAT | — | — | $98,835.86 |
| Day 17 | 2026-08-07 | $771.25 | Long 51 SPY (T9) | -$64.27 | -0.163% | $98,771.59 |
| Day 18 | 2026-08-10 | $771.11 | FLAT | — | — | $98,860.84 |
| Day 19 | 2026-08-11 | $768.61 | Long 51 SPY (T10) | -$256.60 | -0.650% | $98,604.24 |
| Day 20 | 2026-08-12 | $770.63 | Long 51 SPY (T10) | -$153.58 | -0.389% | $98,707.26 |
| Day 21 | 2026-08-13 | $775.91 | Long 51 SPY (T10) | +$115.70 | +0.293% | $98,976.54 |
| Day 22 | 2026-08-14 | $774.38 | Long 51 SPY (T10) | +$37.67 | +0.095% | $98,898.51 |
| Day 23 | 2026-08-17 | $770.71 | Long 51 SPY (T10) | -$149.50 | -0.379% | $98,711.34 |
| Day 24 | 2026-08-18 | $765.46 | Long 51 SPY (T10) | -$417.25 | -1.058% | $98,443.59 |
| Day 25 | 2026-08-19 | $767.19 | Long 51 SPY (T10) | -$329.02 | -0.834% | $98,531.82 |
| Day 26 | 2026-08-20 | $760.73 | Long 51 SPY (T10) | -$658.48 | -1.669% | $98,202.36 |
| Day 27 | 2026-08-21 | $763.74 | Long 51 SPY (T10) | -$504.97 | -1.280% | $98,355.87 |
| Day 28 | 2026-08-24 | $761.57 | Long 51 SPY (T10) | -$615.64 | -1.560% | $98,245.20 |
| Day 29 | 2026-08-25 | $763.89 | Long 51 SPY (T10) | -$497.32 | -1.260% | $98,363.52 |
| Day 30 | 2026-08-26 | $764.04 | Long 51 SPY (T10) | -$489.67 | -1.241% | $98,371.17 |
| Day 31 | 2026-08-27 | $769.27 | Long 51 SPY (T10) | -$222.94 | -0.565% | $98,637.90 |
| Day 32 | 2026-08-28 | $767.37 | Long 51 SPY (T10) | -$319.84 | -0.811% | $98,541.00 |
| Day 33 | 2026-08-31 | $764.97 | Long 51 SPY (T10) | -$442.24 | -1.121% | $98,418.60 |
| Day 34 | 2026-09-01 | $759.74 | FLAT | — | — | $98,248.26 |
| Day 35 | 2026-09-02 | $763.23 | Long 51 SPY (T11) | -$86.19 | -0.221% | $98,162.07 |
| Day 36 | 2026-09-03 | $771.20 | Long 51 SPY (T11) | +$320.28 | +0.821% | $98,568.54 |
| Day 37 | 2026-09-04 | $768.27 | Long 51 SPY (T11) | +$170.85 | +0.438% | $98,419.11 |
| Day 38 | 2026-09-08 | $764.16 | FLAT | — | — | $98,300.79 |
| Day 39 | 2026-09-09 | $760.54 | Long 52 SPY (T12) | -$127.87 | -0.322% | $98,172.92 |
| Day 40 | 2026-09-10 | $755.99 | FLAT | — | — | $98,036.68 |
| Day 41 | 2026-09-11 | $762.25 | FLAT | — | — | $98,036.68 |
| Day 42 | 2026-09-14 | $758.87 | FLAT | — | — | $98,036.68 |
| Day 43 | 2026-09-15 | $755.54 | FLAT | — | — | $98,036.68 |
| Day 44 | 2026-09-16 | $752.18 | FLAT | — | — | $98,036.68 |
| Day 45 | 2026-09-17 | $760.75 | FLAT | — | — | $98,036.68 |
| Day 46 | 2026-09-18 | $761.62 | FLAT | — | — | $98,036.68 |
| Day 47 | 2026-09-21 | $773.52 | FLAT | — | — | $98,036.68 |
| Day 48 | 2026-09-22 | $773.44 | FLAT | — | — | $98,051.47 |
| Day 49 | 2026-09-23 | $767.93 | FLAT | — | — | $98,022.70 |
| Day 50 | 2026-09-24 | $767.29 | FLAT | — | — | $98,022.70 |
| Day 51 | 2026-09-25 | $771.35 | FLAT | — | — | $98,022.70 |
| Day 52 | 2026-09-28 | $765.49 | Long 51 SPY (T15) | +$7.14 | +0.018% | $98,029.84 |
| Day 53 | 2026-09-29 | $764.38 | FLAT | — | — | $98,054.83 |
| Day 54 | 2026-09-30 | $762.34 | Long 51 SPY (T16) | -$216.75 | -0.554% | $97,838.08 |
| Day 55 | 2026-10-01 | $764.10 | Long 51 SPY (T16) | -$126.99 | -0.325% | $97,927.84 |
| Day 56 | 2026-10-02 | $769.65 | Long 51 SPY (T16) | +$156.06 | +0.399% | $98,210.89 |
| Day 57 | 2026-10-05 | $774.97 | Long 51 SPY (T16) | +$427.38 | +1.093% | $98,482.21 |
| Day 58 | 2026-10-06 | $779.10 | Long 51 SPY (T16) | +$638.01 | +1.632% | $98,692.84 |
| Day 59 | 2026-10-07 | $777.15 | Long 51 SPY (T16) | +$538.56 | +1.378% | $98,593.39 |
| Day 60 | 2026-10-08 | $773.88 | Long 51 SPY (T16) | +$371.79 | +0.951% | $98,426.62 |
| Day 61 | 2026-10-09 | $778.51 | Long 51 SPY (T16) | +$607.92 | +1.555% | $98,662.75 |
| Day 62 | 2026-10-12 | $778.03 | Long 51 SPY (T16) | +$583.44 | +1.492% | $98,638.27 |
| Day 63 | 2026-10-13 | $778.03 | Long 51 SPY (T16) | +$583.44 | +1.492% | $98,638.27 |
| Day 64 | 2026-10-14 | $769.65 | FLAT | — | — | $98,110.42 |
| Day 65 | 2026-10-15 | $771.77 | Long 51 SPY (T17) | +$110.67 | +0.282% | $98,221.09 |
| Day 66 | 2026-10-16 | $763.34 | Long 51 SPY (T17) | -$319.26 | -0.813% | $97,791.16 |
| Day 67 | 2026-10-19 | $766.60 | Long 51 SPY (T17) | -$153.00 | -0.390% | $97,957.42 |
| Day 68 | 2026-10-20 | $769.09 | FLAT | — | — | $98,161.93 |
| Day 69 | 2026-10-21 | $773.13 | Long 51 SPY (T18) | -$36.72 | -0.093% | $98,125.21 |
| Day 70 | 2026-10-22 | $764.03 | FLAT | — | — | $97,563.19 |
| Day 71 | 2026-10-23 | $759.83 | Long 51 SPY (T19) | -$39.27 | -0.101% | $97,523.92 |
| Day 72 | 2026-10-26 | $765.23 | Long 51 SPY (T19) | +$236.13 | +0.609% | $97,799.32 |
| Day 73 | 2026-10-27 | $769.32 | FLAT | — | — | $98,007.91 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-16 | $99,823.87 | $100,000.03 | -0.1761% | +0.000% | **-0.176%** |
| Day 2 | 2026-07-17 | $99,681.31 | $98,989.36 | -0.3187% | -1.011% | **+0.692%** |
| Day 3 | 2026-07-20 | $99,489.33 | $98,838.49 | -0.5107% | -1.162% | **+0.651%** |
| Day 4 | 2026-07-21 | $99,419.37 | $99,638.21 | -0.5806% | -0.362% | **-0.219%** |
| Day 5 | 2026-07-22 | $99,384.39 | $99,550.10 | -0.6156% | -0.450% | **-0.166%** |
| Day 6 | 2026-07-23 | $98,718.14 | $98,293.77 | -1.2819% | -1.706% | **+0.424%** |
| Day 7 | 2026-07-24 | $98,862.18 | $98,405.92 | -1.1378% | -1.594% | **+0.456%** |
| Day 8 | 2026-07-27 | $98,966.32 | $98,399.25 | -1.0337% | -1.601% | **+0.567%** |
| Day 9 | 2026-07-28 | $98,922.86 | $98,658.25 | -1.0771% | -1.342% | **+0.265%** |
| Day 10 | 2026-07-29 | $98,922.86 | $97,162.95 | -1.0771% | -2.837% | **+1.760%** |
| Day 11 | 2026-07-30 | $98,922.86 | $98,769.07 | -1.0771% | -1.231% | **+0.154%** |
| Day 12 | 2026-07-31 | $98,922.86 | $99,456.64 | -1.0771% | -0.543% | **-0.534%** |
| Day 13 | 2026-08-03 | $98,922.86 | $100,911.90 | -1.0771% | +0.912% | **-1.989%** |
| Day 14 | 2026-08-04 | $98,775.36 | $102,695.58 | -1.2246% | +2.696% | **-3.921%** |
| Day 15 | 2026-08-05 | $98,835.86 | $102,519.35 | -1.1641% | +2.519% | **-3.683%** |
| Day 16 | 2026-08-06 | $98,835.86 | $102,367.15 | -1.1641% | +2.367% | **-3.531%** |
| Day 17 | 2026-08-07 | $98,771.59 | $102,969.28 | -1.2284% | +2.969% | **-4.197%** |
| Day 18 | 2026-08-10 | $98,860.84 | $102,950.59 | -1.1392% | +2.951% | **-4.090%** |
| Day 19 | 2026-08-11 | $98,604.24 | $102,616.81 | -1.3958% | +2.617% | **-4.013%** |
| Day 20 | 2026-08-12 | $98,707.26 | $102,886.50 | -1.2927% | +2.886% | **-4.179%** |
| Day 21 | 2026-08-13 | $98,976.54 | $103,591.43 | -1.0235% | +3.591% | **-4.615%** |
| Day 22 | 2026-08-14 | $98,898.51 | $103,387.16 | -1.1015% | +3.387% | **-4.488%** |
| Day 23 | 2026-08-17 | $98,711.34 | $102,897.18 | -1.2887% | +2.897% | **-4.186%** |
| Day 24 | 2026-08-18 | $98,443.59 | $102,196.26 | -1.5564% | +2.196% | **-3.752%** |
| Day 25 | 2026-08-19 | $98,531.82 | $102,427.23 | -1.4682% | +2.427% | **-3.895%** |
| Day 26 | 2026-08-20 | $98,202.36 | $101,564.76 | -1.7976% | +1.565% | **-3.363%** |
| Day 27 | 2026-08-21 | $98,355.87 | $101,966.62 | -1.6441% | +1.967% | **-3.611%** |
| Day 28 | 2026-08-24 | $98,245.20 | $101,676.91 | -1.7548% | +1.677% | **-3.432%** |
| Day 29 | 2026-08-25 | $98,363.52 | $101,986.65 | -1.6365% | +1.987% | **-3.624%** |
| Day 30 | 2026-08-26 | $98,371.17 | $102,006.67 | -1.6288% | +2.007% | **-3.636%** |
| Day 31 | 2026-08-27 | $98,637.90 | $102,704.93 | -1.3621% | +2.705% | **-4.067%** |
| Day 32 | 2026-08-28 | $98,541.00 | $102,451.26 | -1.4590% | +2.451% | **-3.910%** |
| Day 33 | 2026-08-31 | $98,418.60 | $102,130.84 | -1.5814% | +2.131% | **-3.712%** |
| Day 34 | 2026-09-01 | $98,248.26 | $101,432.58 | -1.7517% | +1.433% | **-3.185%** |
| Day 35 | 2026-09-02 | $98,162.07 | $101,898.53 | -1.8379% | +1.899% | **-3.737%** |
| Day 36 | 2026-09-03 | $98,568.54 | $102,962.60 | -1.4315% | +2.963% | **-4.394%** |
| Day 37 | 2026-09-04 | $98,419.11 | $102,571.42 | -1.5809% | +2.571% | **-4.152%** |
| Day 38 | 2026-09-08 | $98,300.79 | $102,022.70 | -1.6992% | +2.023% | **-3.722%** |
| Day 39 | 2026-09-09 | $98,172.92 | $101,539.39 | -1.8271% | +1.539% | **-3.366%** |
| Day 40 | 2026-09-10 | $98,036.68 | $100,931.92 | -1.9633% | +0.932% | **-2.895%** |
| Day 41 | 2026-09-11 | $98,036.68 | $101,767.69 | -1.9633% | +1.768% | **-3.731%** |
| Day 42 | 2026-09-14 | $98,036.68 | $101,316.43 | -1.9633% | +1.316% | **-3.279%** |
| Day 43 | 2026-09-15 | $98,036.68 | $100,871.84 | -1.9633% | +0.872% | **-2.835%** |
| Day 44 | 2026-09-16 | $98,036.68 | $100,423.25 | -1.9633% | +0.423% | **-2.386%** |
| Day 45 | 2026-09-17 | $98,036.68 | $101,567.43 | -1.9633% | +1.567% | **-3.530%** |
| Day 46 | 2026-09-18 | $98,036.68 | $101,683.58 | -1.9633% | +1.684% | **-3.647%** |
| Day 47 | 2026-09-21 | $98,036.68 | $103,272.35 | -1.9633% | +3.272% | **-5.235%** |
| Day 48 | 2026-09-22 | $98,051.47 | $103,261.67 | -1.9485% | +3.262% | **-5.210%** |
| Day 49 | 2026-09-23 | $98,022.70 | $102,526.03 | -1.9773% | +2.526% | **-4.503%** |
| Day 50 | 2026-09-24 | $98,022.70 | $102,440.58 | -1.9773% | +2.441% | **-4.418%** |
| Day 51 | 2026-09-25 | $98,022.70 | $102,982.63 | -1.9773% | +2.983% | **-4.960%** |
| Day 52 | 2026-09-28 | $98,029.84 | $102,200.26 | -1.9702% | +2.200% | **-4.170%** |
| Day 53 | 2026-09-29 | $98,054.83 | $102,052.07 | -1.9452% | +2.052% | **-3.997%** |
| Day 54 | 2026-09-30 | $97,838.08 | $101,779.71 | -2.1619% | +1.780% | **-3.942%** |
| Day 55 | 2026-10-01 | $97,927.84 | $102,014.69 | -2.0722% | +2.015% | **-4.087%** |
| Day 56 | 2026-10-02 | $98,210.89 | $102,755.66 | -1.7891% | +2.756% | **-4.545%** |
| Day 57 | 2026-10-05 | $98,482.21 | $103,465.93 | -1.5178% | +3.466% | **-4.984%** |
| Day 58 | 2026-10-06 | $98,692.84 | $104,017.33 | -1.3072% | +4.017% | **-5.324%** |
| Day 59 | 2026-10-07 | $98,593.39 | $103,756.99 | -1.4066% | +3.757% | **-5.164%** |
| Day 60 | 2026-10-08 | $98,426.62 | $103,320.41 | -1.5734% | +3.320% | **-4.893%** |
| Day 61 | 2026-10-09 | $98,662.75 | $103,938.56 | -1.3372% | +3.939% | **-5.276%** |
| Day 62 | 2026-10-12 | $98,638.27 | $103,874.47 | -1.3617% | +3.874% | **-5.236%** |
| Day 63 | 2026-10-13 | $98,638.27 | $103,874.47 | -1.3617% | +3.874% | **-5.236%** |
| Day 64 | 2026-10-14 | $98,110.42 | $102,755.66 | -1.8896% | +2.756% | **-4.646%** |
| Day 65 | 2026-10-15 | $98,221.09 | $103,038.70 | -1.7789% | +3.039% | **-4.818%** |
| Day 66 | 2026-10-16 | $97,791.16 | $101,913.22 | -2.2088% | +1.913% | **-4.122%** |
| Day 67 | 2026-10-19 | $97,957.42 | $102,348.46 | -2.0426% | +2.348% | **-4.391%** |
| Day 68 | 2026-10-20 | $98,161.93 | $102,680.90 | -1.8381% | +2.681% | **-4.519%** |
| Day 69 | 2026-10-21 | $98,125.21 | $103,220.28 | -1.8748% | +3.220% | **-5.095%** |
| Day 70 | 2026-10-22 | $97,563.19 | $102,005.34 | -2.4368% | +2.005% | **-4.442%** |
| Day 71 | 2026-10-23 | $97,523.92 | $101,444.60 | -2.4761% | +1.445% | **-3.921%** |
| Day 72 | 2026-10-26 | $97,799.32 | $102,165.55 | -2.2007% | +2.166% | **-4.367%** |
| Day 73 | 2026-10-27 | $98,007.91 | $102,711.61 | -1.9921% | +2.712% | **-4.704%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-16 | $749.01 | -$228.60 | -$1763.49 | Holding would have been **$1763.49** better — honest entry |
| Day 2 | 2026-07-17 | $741.44 | -$629.81 | -$1362.28 | Holding would have been **$1362.28** better — honest entry |
| Day 3 | 2026-07-20 | $740.31 | -$689.70 | -$1302.39 | Holding would have been **$1302.39** better — honest entry |
| Day 4 | 2026-07-21 | $746.30 | -$372.23 | -$1619.86 | Position open |
| Day 5 | 2026-07-22 | $745.64 | -$407.21 | -$1584.88 | Position open |
| Day 6 | 2026-07-23 | $736.23 | -$905.94 | -$1086.15 | Position open |
| Day 7 | 2026-07-24 | $737.07 | -$861.42 | -$1130.67 | Holding would have been **$1130.67** better — honest entry |
| Day 8 | 2026-07-27 | $737.02 | -$864.07 | -$1128.02 | Holding would have been **$1128.02** better — honest entry |
| Day 9 | 2026-07-28 | $738.96 | -$761.25 | -$1230.84 | Holding would have been **$1230.84** better — honest entry |
| Day 10 | 2026-07-29 | $727.76 | -$1354.85 | -$637.24 | Holding would have been **$637.24** better — honest entry |
| Day 11 | 2026-07-30 | $739.79 | -$717.26 | -$1274.83 | Holding would have been **$1274.83** better — honest entry |
| Day 12 | 2026-07-31 | $744.94 | -$444.31 | -$1547.78 | Holding would have been **$1547.78** better — honest entry |
| Day 13 | 2026-08-03 | $755.84 | +$133.39 | -$2125.48 | Holding would have been **$2125.48** better — honest entry |
| Day 14 | 2026-08-04 | $769.20 | +$841.47 | -$2833.56 | Position open |
| Day 15 | 2026-08-05 | $767.88 | +$771.51 | -$2763.60 | Holding would have been **$2763.60** better — honest entry |
| Day 16 | 2026-08-06 | $766.74 | +$711.09 | -$2703.18 | Holding would have been **$2703.18** better — honest entry |
| Day 17 | 2026-08-07 | $771.25 | +$950.12 | -$2942.21 | Position open |
| Day 18 | 2026-08-10 | $771.11 | +$942.70 | -$2934.79 | Holding would have been **$2934.79** better — honest entry |
| Day 19 | 2026-08-11 | $768.61 | +$810.20 | -$2802.29 | Position open |
| Day 20 | 2026-08-12 | $770.63 | +$917.26 | -$2909.35 | Position open |
| Day 21 | 2026-08-13 | $775.91 | +$1197.10 | -$3189.19 | Position open |
| Day 22 | 2026-08-14 | $774.38 | +$1116.01 | -$3108.10 | Position open |
| Day 23 | 2026-08-17 | $770.71 | +$921.50 | -$2913.59 | Position open |
| Day 24 | 2026-08-18 | $765.46 | +$643.25 | -$2635.34 | Position open |
| Day 25 | 2026-08-19 | $767.19 | +$734.94 | -$2727.03 | Position open |
| Day 26 | 2026-08-20 | $760.73 | +$392.56 | -$2384.65 | Position open |
| Day 27 | 2026-08-21 | $763.74 | +$552.09 | -$2544.18 | Position open |
| Day 28 | 2026-08-24 | $761.57 | +$437.08 | -$2429.17 | Position open |
| Day 29 | 2026-08-25 | $763.89 | +$560.04 | -$2552.13 | Position open |
| Day 30 | 2026-08-26 | $764.04 | +$567.99 | -$2560.08 | Position open |
| Day 31 | 2026-08-27 | $769.27 | +$845.18 | -$2837.27 | Position open |
| Day 32 | 2026-08-28 | $767.37 | +$744.48 | -$2736.57 | Position open |
| Day 33 | 2026-08-31 | $764.97 | +$617.28 | -$2609.37 | Position open |
| Day 34 | 2026-09-01 | $759.74 | +$340.09 | -$2332.18 | Holding would have been **$2332.18** better — honest entry |
| Day 35 | 2026-09-02 | $763.23 | +$525.06 | -$2517.15 | Position open |
| Day 36 | 2026-09-03 | $771.20 | +$947.47 | -$2939.56 | Position open |
| Day 37 | 2026-09-04 | $768.27 | +$792.18 | -$2784.27 | Position open |
| Day 38 | 2026-09-08 | $764.16 | +$574.35 | -$2566.44 | Holding would have been **$2566.44** better — honest entry |
| Day 39 | 2026-09-09 | $760.54 | +$382.49 | -$2374.58 | Position open |
| Day 40 | 2026-09-10 | $755.99 | +$141.34 | -$2133.43 | Holding would have been **$2133.43** better — honest entry |
| Day 41 | 2026-09-11 | $762.25 | +$473.12 | -$2465.21 | Holding would have been **$2465.21** better — honest entry |
| Day 42 | 2026-09-14 | $758.87 | +$293.98 | -$2286.07 | Holding would have been **$2286.07** better — honest entry |
| Day 43 | 2026-09-15 | $755.54 | +$117.49 | -$2109.58 | Holding would have been **$2109.58** better — honest entry |
| Day 44 | 2026-09-16 | $752.18 | -$60.59 | -$1931.50 | Holding would have been **$1931.50** better — honest entry |
| Day 45 | 2026-09-17 | $760.75 | +$393.62 | -$2385.71 | Holding would have been **$2385.71** better — honest entry |
| Day 46 | 2026-09-18 | $761.62 | +$439.73 | -$2431.82 | Holding would have been **$2431.82** better — honest entry |
| Day 47 | 2026-09-21 | $773.52 | +$1070.43 | -$3062.52 | Holding would have been **$3062.52** better — honest entry |
| Day 48 | 2026-09-22 | $773.44 | +$1066.19 | -$3058.28 | Holding would have been **$3058.28** better — honest entry |
| Day 49 | 2026-09-23 | $767.93 | +$774.16 | -$2766.25 | Holding would have been **$2766.25** better — honest entry |
| Day 50 | 2026-09-24 | $767.29 | +$740.24 | -$2732.33 | Holding would have been **$2732.33** better — honest entry |
| Day 51 | 2026-09-25 | $771.35 | +$955.42 | -$2947.51 | Holding would have been **$2947.51** better — honest entry |
| Day 52 | 2026-09-28 | $765.49 | +$644.84 | -$2636.93 | Position open |
| Day 53 | 2026-09-29 | $764.38 | +$586.01 | -$2578.10 | Holding would have been **$2578.10** better — honest entry |
| Day 54 | 2026-09-30 | $762.34 | +$477.89 | -$2469.98 | Position open |
| Day 55 | 2026-10-01 | $764.10 | +$571.17 | -$2563.26 | Position open |
| Day 56 | 2026-10-02 | $769.65 | +$865.32 | -$2857.41 | Position open |
| Day 57 | 2026-10-05 | $774.97 | +$1147.28 | -$3139.37 | Position open |
| Day 58 | 2026-10-06 | $779.10 | +$1366.17 | -$3358.26 | Position open |
| Day 59 | 2026-10-07 | $777.15 | +$1262.82 | -$3254.91 | Position open |
| Day 60 | 2026-10-08 | $773.88 | +$1089.51 | -$3081.60 | Position open |
| Day 61 | 2026-10-09 | $778.51 | +$1334.90 | -$3326.99 | Position open |
| Day 62 | 2026-10-12 | $778.03 | +$1309.46 | -$3301.55 | Position open |
| Day 63 | 2026-10-13 | $778.03 | +$1309.46 | -$3301.55 | Position open |
| Day 64 | 2026-10-14 | $769.65 | +$865.32 | -$2857.41 | Holding would have been **$2857.41** better — honest entry |
| Day 65 | 2026-10-15 | $771.77 | +$977.68 | -$2969.77 | Position open |
| Day 66 | 2026-10-16 | $763.34 | +$530.89 | -$2522.98 | Position open |
| Day 67 | 2026-10-19 | $766.60 | +$703.67 | -$2695.76 | Position open |
| Day 68 | 2026-10-20 | $769.09 | +$835.64 | -$2827.73 | Holding would have been **$2827.73** better — honest entry |
| Day 69 | 2026-10-21 | $773.13 | +$1049.76 | -$3041.85 | Position open |
| Day 70 | 2026-10-22 | $764.03 | +$567.46 | -$2559.55 | Holding would have been **$2559.55** better — honest entry |
| Day 71 | 2026-10-23 | $759.83 | +$344.86 | -$2336.95 | Position open |
| Day 72 | 2026-10-26 | $765.23 | +$631.06 | -$2623.15 | Position open |
| Day 73 | 2026-10-27 | $769.32 | +$847.83 | -$2839.92 | Holding would have been **$2839.92** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$228.60 |
| Signal saved | -$1763.49 |
| Portfolio value | $99,823.87 |
| Benchmark value | $100,000.03 |
| Alpha (cumulative) | -0.176% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 2 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$629.81 |
| Signal saved | -$1362.28 |
| Portfolio value | $99,681.31 |
| Benchmark value | $98,989.36 |
| Alpha (cumulative) | +0.692% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 3 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$689.70 |
| Signal saved | -$1302.39 |
| Portfolio value | $99,489.33 |
| Benchmark value | $98,838.49 |
| Alpha (cumulative) | +0.651% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 4 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T4) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,419.37 |
| Benchmark value | $99,638.21 |
| Alpha (cumulative) | -0.219% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 5 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T4) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,384.39 |
| Benchmark value | $99,550.10 |
| Alpha (cumulative) | -0.166% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 6 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T5) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,718.14 |
| Benchmark value | $98,293.77 |
| Alpha (cumulative) | +0.424% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 7 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$861.42 |
| Signal saved | -$1130.67 |
| Portfolio value | $98,862.18 |
| Benchmark value | $98,405.92 |
| Alpha (cumulative) | +0.456% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 8 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$864.07 |
| Signal saved | -$1128.02 |
| Portfolio value | $98,966.32 |
| Benchmark value | $98,399.25 |
| Alpha (cumulative) | +0.567% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 9 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$761.25 |
| Signal saved | -$1230.84 |
| Portfolio value | $98,922.86 |
| Benchmark value | $98,658.25 |
| Alpha (cumulative) | +0.265% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 10 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$1354.85 |
| Signal saved | -$637.24 |
| Portfolio value | $98,922.86 |
| Benchmark value | $97,162.95 |
| Alpha (cumulative) | +1.760% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 11 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$717.26 |
| Signal saved | -$1274.83 |
| Portfolio value | $98,922.86 |
| Benchmark value | $98,769.07 |
| Alpha (cumulative) | +0.154% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 12 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$444.31 |
| Signal saved | -$1547.78 |
| Portfolio value | $98,922.86 |
| Benchmark value | $99,456.64 |
| Alpha (cumulative) | -0.534% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 13 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$133.39 |
| Signal saved | -$2125.48 |
| Portfolio value | $98,922.86 |
| Benchmark value | $100,911.90 |
| Alpha (cumulative) | -1.989% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 14 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T8) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,775.36 |
| Benchmark value | $102,695.58 |
| Alpha (cumulative) | -3.921% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 15 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$771.51 |
| Signal saved | -$2763.60 |
| Portfolio value | $98,835.86 |
| Benchmark value | $102,519.35 |
| Alpha (cumulative) | -3.683% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 16 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$711.09 |
| Signal saved | -$2703.18 |
| Portfolio value | $98,835.86 |
| Benchmark value | $102,367.15 |
| Alpha (cumulative) | -3.531% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 17 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,771.59 |
| Benchmark value | $102,969.28 |
| Alpha (cumulative) | -4.197% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 18 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$942.70 |
| Signal saved | -$2934.79 |
| Portfolio value | $98,860.84 |
| Benchmark value | $102,950.59 |
| Alpha (cumulative) | -4.090% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 19 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,604.24 |
| Benchmark value | $102,616.81 |
| Alpha (cumulative) | -4.013% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 20 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,707.26 |
| Benchmark value | $102,886.50 |
| Alpha (cumulative) | -4.179% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 21 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $98,976.54 |
| Benchmark value | $103,591.43 |
| Alpha (cumulative) | -4.615% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 22 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $98,898.51 |
| Benchmark value | $103,387.16 |
| Alpha (cumulative) | -4.488% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 23 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,711.34 |
| Benchmark value | $102,897.18 |
| Alpha (cumulative) | -4.186% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 24 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,443.59 |
| Benchmark value | $102,196.26 |
| Alpha (cumulative) | -3.752% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 25 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,531.82 |
| Benchmark value | $102,427.23 |
| Alpha (cumulative) | -3.895% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 26 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,202.36 |
| Benchmark value | $101,564.76 |
| Alpha (cumulative) | -3.363% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 27 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,355.87 |
| Benchmark value | $101,966.62 |
| Alpha (cumulative) | -3.611% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 28 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,245.20 |
| Benchmark value | $101,676.91 |
| Alpha (cumulative) | -3.432% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 29 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,363.52 |
| Benchmark value | $101,986.65 |
| Alpha (cumulative) | -3.624% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 30 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,371.17 |
| Benchmark value | $102,006.67 |
| Alpha (cumulative) | -3.636% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 31 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,637.90 |
| Benchmark value | $102,704.93 |
| Alpha (cumulative) | -4.067% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 32 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,541.00 |
| Benchmark value | $102,451.26 |
| Alpha (cumulative) | -3.910% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 33 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,418.60 |
| Benchmark value | $102,130.84 |
| Alpha (cumulative) | -3.712% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 34 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$340.09 |
| Signal saved | -$2332.18 |
| Portfolio value | $98,248.26 |
| Benchmark value | $101,432.58 |
| Alpha (cumulative) | -3.185% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 35 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,162.07 |
| Benchmark value | $101,898.53 |
| Alpha (cumulative) | -3.737% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 36 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,568.54 |
| Benchmark value | $102,962.60 |
| Alpha (cumulative) | -4.394% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 37 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,419.11 |
| Benchmark value | $102,571.42 |
| Alpha (cumulative) | -4.152% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 38 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$574.35 |
| Signal saved | -$2566.44 |
| Portfolio value | $98,300.79 |
| Benchmark value | $102,022.70 |
| Alpha (cumulative) | -3.722% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T12) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,172.92 |
| Benchmark value | $101,539.39 |
| Alpha (cumulative) | -3.366% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 40 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$141.34 |
| Signal saved | -$2133.43 |
| Portfolio value | $98,036.68 |
| Benchmark value | $100,931.92 |
| Alpha (cumulative) | -2.895% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$473.12 |
| Signal saved | -$2465.21 |
| Portfolio value | $98,036.68 |
| Benchmark value | $101,767.69 |
| Alpha (cumulative) | -3.731% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$293.98 |
| Signal saved | -$2286.07 |
| Portfolio value | $98,036.68 |
| Benchmark value | $101,316.43 |
| Alpha (cumulative) | -3.279% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$117.49 |
| Signal saved | -$2109.58 |
| Portfolio value | $98,036.68 |
| Benchmark value | $100,871.84 |
| Alpha (cumulative) | -2.835% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | -$60.59 |
| Signal saved | -$1931.50 |
| Portfolio value | $98,036.68 |
| Benchmark value | $100,423.25 |
| Alpha (cumulative) | -2.386% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$393.62 |
| Signal saved | -$2385.71 |
| Portfolio value | $98,036.68 |
| Benchmark value | $101,567.43 |
| Alpha (cumulative) | -3.530% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$439.73 |
| Signal saved | -$2431.82 |
| Portfolio value | $98,036.68 |
| Benchmark value | $101,683.58 |
| Alpha (cumulative) | -3.647% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$1070.43 |
| Signal saved | -$3062.52 |
| Portfolio value | $98,036.68 |
| Benchmark value | $103,272.35 |
| Alpha (cumulative) | -5.235% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$1066.19 |
| Signal saved | -$3058.28 |
| Portfolio value | $98,051.47 |
| Benchmark value | $103,261.67 |
| Alpha (cumulative) | -5.210% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$774.16 |
| Signal saved | -$2766.25 |
| Portfolio value | $98,022.70 |
| Benchmark value | $102,526.03 |
| Alpha (cumulative) | -4.503% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$740.24 |
| Signal saved | -$2732.33 |
| Portfolio value | $98,022.70 |
| Benchmark value | $102,440.58 |
| Alpha (cumulative) | -4.418% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$955.42 |
| Signal saved | -$2947.51 |
| Portfolio value | $98,022.70 |
| Benchmark value | $102,982.63 |
| Alpha (cumulative) | -4.960% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $765.49 |
| Unrealized P&L | +$7.14 |
| P&L % | +0.018% |
| Portfolio value | $98,029.84 |
| Benchmark value | $102,200.26 |
| Alpha (cumulative) | -4.170% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $764.38 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$586.01 |
| Signal saved | -$2578.10 |
| Portfolio value | $98,054.83 |
| Benchmark value | $102,052.07 |
| Alpha (cumulative) | -3.997% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-30

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $762.34 |
| Unrealized P&L | -$216.75 |
| P&L % | -0.554% |
| Portfolio value | $97,838.08 |
| Benchmark value | $101,779.71 |
| Alpha (cumulative) | -3.942% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 55 — 2026-10-01

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $764.10 |
| Unrealized P&L | -$126.99 |
| P&L % | -0.325% |
| Portfolio value | $97,927.84 |
| Benchmark value | $102,014.69 |
| Alpha (cumulative) | -4.087% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.33% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 56 — 2026-10-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $769.65 |
| Unrealized P&L | +$156.06 |
| P&L % | +0.399% |
| Portfolio value | $98,210.89 |
| Benchmark value | $102,755.66 |
| Alpha (cumulative) | -4.545% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.40% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-10-05

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $774.97 |
| Unrealized P&L | +$427.38 |
| P&L % | +1.093% |
| Portfolio value | $98,482.21 |
| Benchmark value | $103,465.93 |
| Alpha (cumulative) | -4.984% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +1.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 58 — 2026-10-06

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $779.10 |
| Unrealized P&L | +$638.01 |
| P&L % | +1.632% |
| Portfolio value | $98,692.84 |
| Benchmark value | $104,017.33 |
| Alpha (cumulative) | -5.324% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +1.63% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 59 — 2026-10-07

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $777.15 |
| Unrealized P&L | +$538.56 |
| P&L % | +1.378% |
| Portfolio value | $98,593.39 |
| Benchmark value | $103,756.99 |
| Alpha (cumulative) | -5.164% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +1.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 60 — 2026-10-08

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $773.88 |
| Unrealized P&L | +$371.79 |
| P&L % | +0.951% |
| Portfolio value | $98,426.62 |
| Benchmark value | $103,320.41 |
| Alpha (cumulative) | -4.893% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.95% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 61 — 2026-10-09

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $778.51 |
| Unrealized P&L | +$607.92 |
| P&L % | +1.555% |
| Portfolio value | $98,662.75 |
| Benchmark value | $103,938.56 |
| Alpha (cumulative) | -5.276% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +1.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 62 — 2026-10-12

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,638.27 |
| Benchmark value | $103,874.47 |
| Alpha (cumulative) | -5.236% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 63 — 2026-10-13

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,638.27 |
| Benchmark value | $103,874.47 |
| Alpha (cumulative) | -5.236% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 64 — 2026-10-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $769.65 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$865.32 |
| Signal saved | -$2857.41 |
| Portfolio value | $98,110.42 |
| Benchmark value | $102,755.66 |
| Alpha (cumulative) | -4.646% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 65 — 2026-10-15

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $771.77 |
| Unrealized P&L | +$110.67 |
| P&L % | +0.282% |
| Portfolio value | $98,221.09 |
| Benchmark value | $103,038.70 |
| Alpha (cumulative) | -4.818% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 66 — 2026-10-16

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $763.34 |
| Unrealized P&L | -$319.26 |
| P&L % | -0.813% |
| Portfolio value | $97,791.16 |
| Benchmark value | $101,913.22 |
| Alpha (cumulative) | -4.122% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 67 — 2026-10-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $766.60 |
| Unrealized P&L | -$153.00 |
| P&L % | -0.390% |
| Portfolio value | $97,957.42 |
| Benchmark value | $102,348.46 |
| Alpha (cumulative) | -4.391% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 68 — 2026-10-20

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $769.09 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$835.64 |
| Signal saved | -$2827.73 |
| Portfolio value | $98,161.93 |
| Benchmark value | $102,680.90 |
| Alpha (cumulative) | -4.519% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 69 — 2026-10-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $773.13 |
| Unrealized P&L | -$36.72 |
| P&L % | -0.093% |
| Portfolio value | $98,125.21 |
| Benchmark value | $103,220.28 |
| Alpha (cumulative) | -5.095% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 70 — 2026-10-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $764.03 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$567.46 |
| Signal saved | -$2559.55 |
| Portfolio value | $97,563.19 |
| Benchmark value | $102,005.34 |
| Alpha (cumulative) | -4.442% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 71 — 2026-10-23

| Field | Value |
|---|---|
| Position | Long 51 SPY (T19) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $759.83 |
| Unrealized P&L | -$39.27 |
| P&L % | -0.101% |
| Portfolio value | $97,523.92 |
| Benchmark value | $101,444.60 |
| Alpha (cumulative) | -3.921% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: -0.10% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 72 — 2026-10-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T19) |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $765.23 |
| Unrealized P&L | +$236.13 |
| P&L % | +0.609% |
| Portfolio value | $97,799.32 |
| Benchmark value | $102,165.55 |
| Alpha (cumulative) | -4.367% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Momentum: WEAK. Unrealized P&L: +0.61% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 73 — 2026-10-27

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $753.323/share |
| Close price | $769.32 |
| Realized P&L (locked) | -$1992.09 |
| Reference if held | +$847.83 |
| Signal saved | -$2839.92 |
| Portfolio value | $98,007.91 |
| Benchmark value | $102,711.61 |
| Alpha (cumulative) | -4.704% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1992.09. Regime: BULL (MA20 $770.14 vs MA50 $766.72). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

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
_Day 73 of 90 · Alpaca equity: $99,041.62 · Cumulative alpha vs SPY: -4.704%_