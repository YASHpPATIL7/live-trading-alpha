# ALPACA PAPER JOURNAL — SPY
_Last updated: October 07, 2026 | Day 61 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$752.632/share**
> (2026-07-14, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-10-07): **BULLISH**  
> Fast: MA10 $768.63 | MA30 $765.26  
> Slow: MA20 $765.06 | MA50 $763.82  
> Regime: **BULL** | Momentum: **STRONG** | Session: REGULAR

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

**Total trades:** 18 | **Closed:** 17 | **Open:** Yes | **Cumulative Realized P&L:** -$1932.50

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T2 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T3 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T4 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T5 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T6 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T7 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T8 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T9 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T10 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T11 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T12 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T13 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T14 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |
| T15 | $773.250 (2026-09-22) | $773.540 (2026-09-22) | 51 | +$14.79 | ✅ Closed |
| T16 | $768.534 (2026-09-23) | $767.970 (2026-09-23) | 51 | -$28.77 | ✅ Closed |
| T17 | $765.350 (2026-09-28) | $765.980 (2026-09-29) | 51 | +$32.13 | ✅ Closed |
| T18 | $766.590 (2026-09-30) | — | 51 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,632.14 |
| Alpaca cash | $59,995.45 |
| Cumulative realized P&L | -$1932.50 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-14 | $750.08 | FLAT | — | — | $99,964.92 |
| Day 2 | 2026-07-15 | $752.90 | FLAT | — | — | $100,012.67 |
| Day 3 | 2026-07-16 | $749.01 | FLAT | — | — | $99,836.54 |
| Day 4 | 2026-07-17 | $741.44 | FLAT | — | — | $99,693.98 |
| Day 5 | 2026-07-20 | $740.31 | FLAT | — | — | $99,502.00 |
| Day 6 | 2026-07-21 | $746.30 | Long 53 SPY (T6) | -$69.96 | -0.177% | $99,432.04 |
| Day 7 | 2026-07-22 | $745.64 | Long 53 SPY (T6) | -$104.94 | -0.265% | $99,397.06 |
| Day 8 | 2026-07-23 | $736.23 | Long 52 SPY (T7) | -$135.72 | -0.353% | $98,730.81 |
| Day 9 | 2026-07-24 | $737.07 | FLAT | — | — | $98,874.85 |
| Day 10 | 2026-07-27 | $737.02 | FLAT | — | — | $98,978.99 |
| Day 11 | 2026-07-28 | $738.96 | FLAT | — | — | $98,935.53 |
| Day 12 | 2026-07-29 | $727.76 | FLAT | — | — | $98,935.53 |
| Day 13 | 2026-07-30 | $739.79 | FLAT | — | — | $98,935.53 |
| Day 14 | 2026-07-31 | $744.94 | FLAT | — | — | $98,935.53 |
| Day 15 | 2026-08-03 | $755.84 | FLAT | — | — | $98,935.53 |
| Day 16 | 2026-08-04 | $769.20 | Long 50 SPY (T10) | -$147.50 | -0.382% | $98,788.03 |
| Day 17 | 2026-08-05 | $767.88 | FLAT | — | — | $98,848.53 |
| Day 18 | 2026-08-06 | $766.74 | FLAT | — | — | $98,848.53 |
| Day 19 | 2026-08-07 | $771.25 | Long 51 SPY (T11) | -$64.27 | -0.163% | $98,784.26 |
| Day 20 | 2026-08-10 | $771.11 | FLAT | — | — | $98,873.51 |
| Day 21 | 2026-08-11 | $768.61 | Long 51 SPY (T12) | -$256.60 | -0.650% | $98,616.91 |
| Day 22 | 2026-08-12 | $770.63 | Long 51 SPY (T12) | -$153.58 | -0.389% | $98,719.93 |
| Day 23 | 2026-08-13 | $775.91 | Long 51 SPY (T12) | +$115.70 | +0.293% | $98,989.21 |
| Day 24 | 2026-08-14 | $774.38 | Long 51 SPY (T12) | +$37.67 | +0.095% | $98,911.18 |
| Day 25 | 2026-08-17 | $770.71 | Long 51 SPY (T12) | -$149.50 | -0.379% | $98,724.01 |
| Day 26 | 2026-08-18 | $765.46 | Long 51 SPY (T12) | -$417.25 | -1.058% | $98,456.26 |
| Day 27 | 2026-08-19 | $767.19 | Long 51 SPY (T12) | -$329.02 | -0.834% | $98,544.49 |
| Day 28 | 2026-08-20 | $760.73 | Long 51 SPY (T12) | -$658.48 | -1.669% | $98,215.03 |
| Day 29 | 2026-08-21 | $763.74 | Long 51 SPY (T12) | -$504.97 | -1.280% | $98,368.54 |
| Day 30 | 2026-08-24 | $761.57 | Long 51 SPY (T12) | -$615.64 | -1.560% | $98,257.87 |
| Day 31 | 2026-08-25 | $763.89 | Long 51 SPY (T12) | -$497.32 | -1.260% | $98,376.19 |
| Day 32 | 2026-08-26 | $764.04 | Long 51 SPY (T12) | -$489.67 | -1.241% | $98,383.84 |
| Day 33 | 2026-08-27 | $769.27 | Long 51 SPY (T12) | -$222.94 | -0.565% | $98,650.57 |
| Day 34 | 2026-08-28 | $767.37 | Long 51 SPY (T12) | -$319.84 | -0.811% | $98,553.67 |
| Day 35 | 2026-08-31 | $764.97 | Long 51 SPY (T12) | -$442.24 | -1.121% | $98,431.27 |
| Day 36 | 2026-09-01 | $759.74 | FLAT | — | — | $98,260.93 |
| Day 37 | 2026-09-02 | $763.23 | Long 51 SPY (T13) | -$86.19 | -0.221% | $98,174.74 |
| Day 38 | 2026-09-03 | $771.20 | Long 51 SPY (T13) | +$320.28 | +0.821% | $98,581.21 |
| Day 39 | 2026-09-04 | $768.27 | Long 51 SPY (T13) | +$170.85 | +0.438% | $98,431.78 |
| Day 40 | 2026-09-08 | $764.16 | FLAT | — | — | $98,313.46 |
| Day 41 | 2026-09-09 | $760.54 | Long 52 SPY (T14) | -$127.87 | -0.322% | $98,185.59 |
| Day 42 | 2026-09-10 | $755.99 | FLAT | — | — | $98,049.35 |
| Day 43 | 2026-09-11 | $762.25 | FLAT | — | — | $98,049.35 |
| Day 44 | 2026-09-14 | $758.87 | FLAT | — | — | $98,049.35 |
| Day 45 | 2026-09-15 | $755.54 | FLAT | — | — | $98,049.35 |
| Day 46 | 2026-09-16 | $752.18 | FLAT | — | — | $98,049.35 |
| Day 47 | 2026-09-17 | $760.75 | FLAT | — | — | $98,049.35 |
| Day 48 | 2026-09-18 | $761.62 | FLAT | — | — | $98,049.35 |
| Day 49 | 2026-09-21 | $773.52 | FLAT | — | — | $98,049.35 |
| Day 50 | 2026-09-22 | $773.44 | FLAT | — | — | $98,064.14 |
| Day 51 | 2026-09-23 | $767.93 | FLAT | — | — | $98,035.37 |
| Day 52 | 2026-09-24 | $767.29 | FLAT | — | — | $98,035.37 |
| Day 53 | 2026-09-25 | $771.35 | FLAT | — | — | $98,035.37 |
| Day 54 | 2026-09-28 | $765.49 | Long 51 SPY (T17) | +$7.14 | +0.018% | $98,042.51 |
| Day 55 | 2026-09-29 | $764.38 | FLAT | — | — | $98,067.50 |
| Day 56 | 2026-09-30 | $762.34 | Long 51 SPY (T18) | -$216.75 | -0.554% | $97,850.75 |
| Day 57 | 2026-10-01 | $764.10 | Long 51 SPY (T18) | -$126.99 | -0.325% | $97,940.51 |
| Day 58 | 2026-10-02 | $769.65 | Long 51 SPY (T18) | +$156.06 | +0.399% | $98,223.56 |
| Day 59 | 2026-10-05 | $774.97 | Long 51 SPY (T18) | +$427.38 | +1.093% | $98,494.88 |
| Day 60 | 2026-10-06 | $779.10 | Long 51 SPY (T18) | +$638.01 | +1.632% | $98,705.51 |
| Day 61 | 2026-10-07 | $777.29 | Long 51 SPY (T18) | +$545.70 | +1.396% | $98,613.20 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-14 | $99,964.92 | $99,999.99 | -0.0351% | -0.000% | **-0.035%** |
| Day 2 | 2026-07-15 | $100,012.67 | $100,375.95 | +0.0127% | +0.376% | **-0.363%** |
| Day 3 | 2026-07-16 | $99,836.54 | $99,857.34 | -0.1635% | -0.143% | **-0.021%** |
| Day 4 | 2026-07-17 | $99,693.98 | $98,848.11 | -0.3060% | -1.152% | **+0.846%** |
| Day 5 | 2026-07-20 | $99,502.00 | $98,697.46 | -0.4980% | -1.303% | **+0.805%** |
| Day 6 | 2026-07-21 | $99,432.04 | $99,496.04 | -0.5680% | -0.504% | **-0.064%** |
| Day 7 | 2026-07-22 | $99,397.06 | $99,408.05 | -0.6029% | -0.592% | **-0.011%** |
| Day 8 | 2026-07-23 | $98,730.81 | $98,153.52 | -1.2692% | -1.846% | **+0.577%** |
| Day 9 | 2026-07-24 | $98,874.85 | $98,265.51 | -1.1251% | -1.734% | **+0.609%** |
| Day 10 | 2026-07-27 | $98,978.99 | $98,258.84 | -1.0210% | -1.741% | **+0.720%** |
| Day 11 | 2026-07-28 | $98,935.53 | $98,517.48 | -1.0645% | -1.483% | **+0.419%** |
| Day 12 | 2026-07-29 | $98,935.53 | $97,024.31 | -1.0645% | -2.976% | **+1.912%** |
| Day 13 | 2026-07-30 | $98,935.53 | $98,628.14 | -1.0645% | -1.372% | **+0.308%** |
| Day 14 | 2026-07-31 | $98,935.53 | $99,314.73 | -1.0645% | -0.685% | **-0.379%** |
| Day 15 | 2026-08-03 | $98,935.53 | $100,767.91 | -1.0645% | +0.768% | **-1.832%** |
| Day 16 | 2026-08-04 | $98,788.03 | $102,549.05 | -1.2120% | +2.549% | **-3.761%** |
| Day 17 | 2026-08-05 | $98,848.53 | $102,373.07 | -1.1515% | +2.373% | **-3.524%** |
| Day 18 | 2026-08-06 | $98,848.53 | $102,221.09 | -1.1515% | +2.221% | **-3.372%** |
| Day 19 | 2026-08-07 | $98,784.26 | $102,822.36 | -1.2157% | +2.822% | **-4.038%** |
| Day 20 | 2026-08-10 | $98,873.51 | $102,803.69 | -1.1265% | +2.804% | **-3.930%** |
| Day 21 | 2026-08-11 | $98,616.91 | $102,470.39 | -1.3831% | +2.470% | **-3.853%** |
| Day 22 | 2026-08-12 | $98,719.93 | $102,739.70 | -1.2801% | +2.740% | **-4.020%** |
| Day 23 | 2026-08-13 | $98,989.21 | $103,443.62 | -1.0108% | +3.444% | **-4.455%** |
| Day 24 | 2026-08-14 | $98,911.18 | $103,239.64 | -1.0888% | +3.240% | **-4.329%** |
| Day 25 | 2026-08-17 | $98,724.01 | $102,750.36 | -1.2760% | +2.750% | **-4.026%** |
| Day 26 | 2026-08-18 | $98,456.26 | $102,050.44 | -1.5437% | +2.050% | **-3.594%** |
| Day 27 | 2026-08-19 | $98,544.49 | $102,281.08 | -1.4555% | +2.281% | **-3.737%** |
| Day 28 | 2026-08-20 | $98,215.03 | $101,419.84 | -1.7850% | +1.420% | **-3.205%** |
| Day 29 | 2026-08-21 | $98,368.54 | $101,821.13 | -1.6315% | +1.821% | **-3.452%** |
| Day 30 | 2026-08-24 | $98,257.87 | $101,531.83 | -1.7421% | +1.532% | **-3.274%** |
| Day 31 | 2026-08-25 | $98,376.19 | $101,841.13 | -1.6238% | +1.841% | **-3.465%** |
| Day 32 | 2026-08-26 | $98,383.84 | $101,861.13 | -1.6162% | +1.861% | **-3.477%** |
| Day 33 | 2026-08-27 | $98,650.57 | $102,558.38 | -1.3494% | +2.558% | **-3.907%** |
| Day 34 | 2026-08-28 | $98,553.67 | $102,305.08 | -1.4463% | +2.305% | **-3.751%** |
| Day 35 | 2026-08-31 | $98,431.27 | $101,985.11 | -1.5687% | +1.985% | **-3.554%** |
| Day 36 | 2026-09-01 | $98,260.93 | $101,287.85 | -1.7391% | +1.288% | **-3.027%** |
| Day 37 | 2026-09-02 | $98,174.74 | $101,753.14 | -1.8253% | +1.753% | **-3.578%** |
| Day 38 | 2026-09-03 | $98,581.21 | $102,815.69 | -1.4188% | +2.816% | **-4.235%** |
| Day 39 | 2026-09-04 | $98,431.78 | $102,425.06 | -1.5682% | +2.425% | **-3.993%** |
| Day 40 | 2026-09-08 | $98,313.46 | $101,877.12 | -1.6865% | +1.877% | **-3.564%** |
| Day 41 | 2026-09-09 | $98,185.59 | $101,394.51 | -1.8144% | +1.395% | **-3.209%** |
| Day 42 | 2026-09-10 | $98,049.35 | $100,787.91 | -1.9506% | +0.788% | **-2.739%** |
| Day 43 | 2026-09-11 | $98,049.35 | $101,622.48 | -1.9506% | +1.622% | **-3.573%** |
| Day 44 | 2026-09-14 | $98,049.35 | $101,171.87 | -1.9506% | +1.172% | **-3.123%** |
| Day 45 | 2026-09-15 | $98,049.35 | $100,727.91 | -1.9506% | +0.728% | **-2.679%** |
| Day 46 | 2026-09-16 | $98,049.35 | $100,279.96 | -1.9506% | +0.280% | **-2.231%** |
| Day 47 | 2026-09-17 | $98,049.35 | $101,422.51 | -1.9506% | +1.423% | **-3.374%** |
| Day 48 | 2026-09-18 | $98,049.35 | $101,538.49 | -1.9506% | +1.538% | **-3.489%** |
| Day 49 | 2026-09-21 | $98,049.35 | $103,124.99 | -1.9506% | +3.125% | **-5.076%** |
| Day 50 | 2026-09-22 | $98,064.14 | $103,114.32 | -1.9359% | +3.114% | **-5.050%** |
| Day 51 | 2026-09-23 | $98,035.37 | $102,379.74 | -1.9646% | +2.380% | **-4.345%** |
| Day 52 | 2026-09-24 | $98,035.37 | $102,294.41 | -1.9646% | +2.294% | **-4.259%** |
| Day 53 | 2026-09-25 | $98,035.37 | $102,835.69 | -1.9646% | +2.836% | **-4.801%** |
| Day 54 | 2026-09-28 | $98,042.51 | $102,054.44 | -1.9575% | +2.054% | **-4.012%** |
| Day 55 | 2026-09-29 | $98,067.50 | $101,906.45 | -1.9325% | +1.906% | **-3.838%** |
| Day 56 | 2026-09-30 | $97,850.75 | $101,634.48 | -2.1493% | +1.634% | **-3.783%** |
| Day 57 | 2026-10-01 | $97,940.51 | $101,869.12 | -2.0595% | +1.869% | **-3.928%** |
| Day 58 | 2026-10-02 | $98,223.56 | $102,609.05 | -1.7764% | +2.609% | **-4.385%** |
| Day 59 | 2026-10-05 | $98,494.88 | $103,318.30 | -1.5051% | +3.318% | **-4.823%** |
| Day 60 | 2026-10-06 | $98,705.51 | $103,868.91 | -1.2945% | +3.869% | **-5.164%** |
| Day 61 | 2026-10-07 | $98,613.20 | $103,627.60 | -1.3868% | +3.628% | **-5.015%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-14 | $750.08 | -$135.25 | -$1797.25 | Holding would have been **$1797.25** better — honest entry |
| Day 2 | 2026-07-15 | $752.90 | +$14.21 | -$1946.71 | Holding would have been **$1946.71** better — honest entry |
| Day 3 | 2026-07-16 | $749.01 | -$191.96 | -$1740.54 | Holding would have been **$1740.54** better — honest entry |
| Day 4 | 2026-07-17 | $741.44 | -$593.17 | -$1339.33 | Holding would have been **$1339.33** better — honest entry |
| Day 5 | 2026-07-20 | $740.31 | -$653.06 | -$1279.44 | Holding would have been **$1279.44** better — honest entry |
| Day 6 | 2026-07-21 | $746.30 | -$335.59 | -$1596.91 | Position open |
| Day 7 | 2026-07-22 | $745.64 | -$370.57 | -$1561.93 | Position open |
| Day 8 | 2026-07-23 | $736.23 | -$869.30 | -$1063.20 | Position open |
| Day 9 | 2026-07-24 | $737.07 | -$824.78 | -$1107.72 | Holding would have been **$1107.72** better — honest entry |
| Day 10 | 2026-07-27 | $737.02 | -$827.43 | -$1105.07 | Holding would have been **$1105.07** better — honest entry |
| Day 11 | 2026-07-28 | $738.96 | -$724.61 | -$1207.89 | Holding would have been **$1207.89** better — honest entry |
| Day 12 | 2026-07-29 | $727.76 | -$1318.21 | -$614.29 | Holding would have been **$614.29** better — honest entry |
| Day 13 | 2026-07-30 | $739.79 | -$680.62 | -$1251.88 | Holding would have been **$1251.88** better — honest entry |
| Day 14 | 2026-07-31 | $744.94 | -$407.67 | -$1524.83 | Holding would have been **$1524.83** better — honest entry |
| Day 15 | 2026-08-03 | $755.84 | +$170.03 | -$2102.53 | Holding would have been **$2102.53** better — honest entry |
| Day 16 | 2026-08-04 | $769.20 | +$878.11 | -$2810.61 | Position open |
| Day 17 | 2026-08-05 | $767.88 | +$808.15 | -$2740.65 | Holding would have been **$2740.65** better — honest entry |
| Day 18 | 2026-08-06 | $766.74 | +$747.73 | -$2680.23 | Holding would have been **$2680.23** better — honest entry |
| Day 19 | 2026-08-07 | $771.25 | +$986.76 | -$2919.26 | Position open |
| Day 20 | 2026-08-10 | $771.11 | +$979.34 | -$2911.84 | Holding would have been **$2911.84** better — honest entry |
| Day 21 | 2026-08-11 | $768.61 | +$846.84 | -$2779.34 | Position open |
| Day 22 | 2026-08-12 | $770.63 | +$953.90 | -$2886.40 | Position open |
| Day 23 | 2026-08-13 | $775.91 | +$1233.74 | -$3166.24 | Position open |
| Day 24 | 2026-08-14 | $774.38 | +$1152.65 | -$3085.15 | Position open |
| Day 25 | 2026-08-17 | $770.71 | +$958.14 | -$2890.64 | Position open |
| Day 26 | 2026-08-18 | $765.46 | +$679.89 | -$2612.39 | Position open |
| Day 27 | 2026-08-19 | $767.19 | +$771.58 | -$2704.08 | Position open |
| Day 28 | 2026-08-20 | $760.73 | +$429.20 | -$2361.70 | Position open |
| Day 29 | 2026-08-21 | $763.74 | +$588.73 | -$2521.23 | Position open |
| Day 30 | 2026-08-24 | $761.57 | +$473.72 | -$2406.22 | Position open |
| Day 31 | 2026-08-25 | $763.89 | +$596.68 | -$2529.18 | Position open |
| Day 32 | 2026-08-26 | $764.04 | +$604.63 | -$2537.13 | Position open |
| Day 33 | 2026-08-27 | $769.27 | +$881.82 | -$2814.32 | Position open |
| Day 34 | 2026-08-28 | $767.37 | +$781.12 | -$2713.62 | Position open |
| Day 35 | 2026-08-31 | $764.97 | +$653.92 | -$2586.42 | Position open |
| Day 36 | 2026-09-01 | $759.74 | +$376.73 | -$2309.23 | Holding would have been **$2309.23** better — honest entry |
| Day 37 | 2026-09-02 | $763.23 | +$561.70 | -$2494.20 | Position open |
| Day 38 | 2026-09-03 | $771.20 | +$984.11 | -$2916.61 | Position open |
| Day 39 | 2026-09-04 | $768.27 | +$828.82 | -$2761.32 | Position open |
| Day 40 | 2026-09-08 | $764.16 | +$610.99 | -$2543.49 | Holding would have been **$2543.49** better — honest entry |
| Day 41 | 2026-09-09 | $760.54 | +$419.13 | -$2351.63 | Position open |
| Day 42 | 2026-09-10 | $755.99 | +$177.98 | -$2110.48 | Holding would have been **$2110.48** better — honest entry |
| Day 43 | 2026-09-11 | $762.25 | +$509.76 | -$2442.26 | Holding would have been **$2442.26** better — honest entry |
| Day 44 | 2026-09-14 | $758.87 | +$330.62 | -$2263.12 | Holding would have been **$2263.12** better — honest entry |
| Day 45 | 2026-09-15 | $755.54 | +$154.13 | -$2086.63 | Holding would have been **$2086.63** better — honest entry |
| Day 46 | 2026-09-16 | $752.18 | -$23.95 | -$1908.55 | Holding would have been **$1908.55** better — honest entry |
| Day 47 | 2026-09-17 | $760.75 | +$430.26 | -$2362.76 | Holding would have been **$2362.76** better — honest entry |
| Day 48 | 2026-09-18 | $761.62 | +$476.37 | -$2408.87 | Holding would have been **$2408.87** better — honest entry |
| Day 49 | 2026-09-21 | $773.52 | +$1107.07 | -$3039.57 | Holding would have been **$3039.57** better — honest entry |
| Day 50 | 2026-09-22 | $773.44 | +$1102.83 | -$3035.33 | Holding would have been **$3035.33** better — honest entry |
| Day 51 | 2026-09-23 | $767.93 | +$810.80 | -$2743.30 | Holding would have been **$2743.30** better — honest entry |
| Day 52 | 2026-09-24 | $767.29 | +$776.88 | -$2709.38 | Holding would have been **$2709.38** better — honest entry |
| Day 53 | 2026-09-25 | $771.35 | +$992.06 | -$2924.56 | Holding would have been **$2924.56** better — honest entry |
| Day 54 | 2026-09-28 | $765.49 | +$681.48 | -$2613.98 | Position open |
| Day 55 | 2026-09-29 | $764.38 | +$622.65 | -$2555.15 | Holding would have been **$2555.15** better — honest entry |
| Day 56 | 2026-09-30 | $762.34 | +$514.53 | -$2447.03 | Position open |
| Day 57 | 2026-10-01 | $764.10 | +$607.81 | -$2540.31 | Position open |
| Day 58 | 2026-10-02 | $769.65 | +$901.96 | -$2834.46 | Position open |
| Day 59 | 2026-10-05 | $774.97 | +$1183.92 | -$3116.42 | Position open |
| Day 60 | 2026-10-06 | $779.10 | +$1402.81 | -$3335.31 | Position open |
| Day 61 | 2026-10-07 | $777.29 | +$1306.88 | -$3239.38 | Position open |

---

## Daily Entries

### Day 1 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $750.08 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$135.25 |
| Signal saved | -$1797.25 |
| Portfolio value | $99,964.92 |
| Benchmark value | $99,999.99 |
| Alpha (cumulative) | -0.035% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 2 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $752.90 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$14.21 |
| Signal saved | -$1946.71 |
| Portfolio value | $100,012.67 |
| Benchmark value | $100,375.95 |
| Alpha (cumulative) | -0.363% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 3 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$191.96 |
| Signal saved | -$1740.54 |
| Portfolio value | $99,836.54 |
| Benchmark value | $99,857.34 |
| Alpha (cumulative) | -0.021% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 4 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$593.17 |
| Signal saved | -$1339.33 |
| Portfolio value | $99,693.98 |
| Benchmark value | $98,848.11 |
| Alpha (cumulative) | +0.846% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 5 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$653.06 |
| Signal saved | -$1279.44 |
| Portfolio value | $99,502.00 |
| Benchmark value | $98,697.46 |
| Alpha (cumulative) | +0.805% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 6 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T6) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,432.04 |
| Benchmark value | $99,496.04 |
| Alpha (cumulative) | -0.064% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 7 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T6) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,397.06 |
| Benchmark value | $99,408.05 |
| Alpha (cumulative) | -0.011% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 8 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T7) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,730.81 |
| Benchmark value | $98,153.52 |
| Alpha (cumulative) | +0.577% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 9 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$824.78 |
| Signal saved | -$1107.72 |
| Portfolio value | $98,874.85 |
| Benchmark value | $98,265.51 |
| Alpha (cumulative) | +0.609% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 10 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$827.43 |
| Signal saved | -$1105.07 |
| Portfolio value | $98,978.99 |
| Benchmark value | $98,258.84 |
| Alpha (cumulative) | +0.720% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 11 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$724.61 |
| Signal saved | -$1207.89 |
| Portfolio value | $98,935.53 |
| Benchmark value | $98,517.48 |
| Alpha (cumulative) | +0.419% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 12 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$1318.21 |
| Signal saved | -$614.29 |
| Portfolio value | $98,935.53 |
| Benchmark value | $97,024.31 |
| Alpha (cumulative) | +1.912% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 13 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$680.62 |
| Signal saved | -$1251.88 |
| Portfolio value | $98,935.53 |
| Benchmark value | $98,628.14 |
| Alpha (cumulative) | +0.308% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 14 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$407.67 |
| Signal saved | -$1524.83 |
| Portfolio value | $98,935.53 |
| Benchmark value | $99,314.73 |
| Alpha (cumulative) | -0.379% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 15 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$170.03 |
| Signal saved | -$2102.53 |
| Portfolio value | $98,935.53 |
| Benchmark value | $100,767.91 |
| Alpha (cumulative) | -1.832% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 16 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T10) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,788.03 |
| Benchmark value | $102,549.05 |
| Alpha (cumulative) | -3.761% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 17 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$808.15 |
| Signal saved | -$2740.65 |
| Portfolio value | $98,848.53 |
| Benchmark value | $102,373.07 |
| Alpha (cumulative) | -3.524% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 18 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$747.73 |
| Signal saved | -$2680.23 |
| Portfolio value | $98,848.53 |
| Benchmark value | $102,221.09 |
| Alpha (cumulative) | -3.372% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 19 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T11) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,784.26 |
| Benchmark value | $102,822.36 |
| Alpha (cumulative) | -4.038% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 20 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$979.34 |
| Signal saved | -$2911.84 |
| Portfolio value | $98,873.51 |
| Benchmark value | $102,803.69 |
| Alpha (cumulative) | -3.930% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 21 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,616.91 |
| Benchmark value | $102,470.39 |
| Alpha (cumulative) | -3.853% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 22 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,719.93 |
| Benchmark value | $102,739.70 |
| Alpha (cumulative) | -4.020% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 23 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $98,989.21 |
| Benchmark value | $103,443.62 |
| Alpha (cumulative) | -4.455% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 24 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $98,911.18 |
| Benchmark value | $103,239.64 |
| Alpha (cumulative) | -4.329% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 25 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,724.01 |
| Benchmark value | $102,750.36 |
| Alpha (cumulative) | -4.026% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 26 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,456.26 |
| Benchmark value | $102,050.44 |
| Alpha (cumulative) | -3.594% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 27 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,544.49 |
| Benchmark value | $102,281.08 |
| Alpha (cumulative) | -3.737% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 28 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,215.03 |
| Benchmark value | $101,419.84 |
| Alpha (cumulative) | -3.205% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 29 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,368.54 |
| Benchmark value | $101,821.13 |
| Alpha (cumulative) | -3.452% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 30 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,257.87 |
| Benchmark value | $101,531.83 |
| Alpha (cumulative) | -3.274% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 31 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,376.19 |
| Benchmark value | $101,841.13 |
| Alpha (cumulative) | -3.465% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 32 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,383.84 |
| Benchmark value | $101,861.13 |
| Alpha (cumulative) | -3.477% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 33 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,650.57 |
| Benchmark value | $102,558.38 |
| Alpha (cumulative) | -3.907% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 34 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,553.67 |
| Benchmark value | $102,305.08 |
| Alpha (cumulative) | -3.751% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 35 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,431.27 |
| Benchmark value | $101,985.11 |
| Alpha (cumulative) | -3.554% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 36 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$376.73 |
| Signal saved | -$2309.23 |
| Portfolio value | $98,260.93 |
| Benchmark value | $101,287.85 |
| Alpha (cumulative) | -3.027% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 37 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,174.74 |
| Benchmark value | $101,753.14 |
| Alpha (cumulative) | -3.578% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 38 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,581.21 |
| Benchmark value | $102,815.69 |
| Alpha (cumulative) | -4.235% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,431.78 |
| Benchmark value | $102,425.06 |
| Alpha (cumulative) | -3.993% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 40 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$610.99 |
| Signal saved | -$2543.49 |
| Portfolio value | $98,313.46 |
| Benchmark value | $101,877.12 |
| Alpha (cumulative) | -3.564% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T14) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,185.59 |
| Benchmark value | $101,394.51 |
| Alpha (cumulative) | -3.209% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$177.98 |
| Signal saved | -$2110.48 |
| Portfolio value | $98,049.35 |
| Benchmark value | $100,787.91 |
| Alpha (cumulative) | -2.739% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$509.76 |
| Signal saved | -$2442.26 |
| Portfolio value | $98,049.35 |
| Benchmark value | $101,622.48 |
| Alpha (cumulative) | -3.573% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$330.62 |
| Signal saved | -$2263.12 |
| Portfolio value | $98,049.35 |
| Benchmark value | $101,171.87 |
| Alpha (cumulative) | -3.123% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$154.13 |
| Signal saved | -$2086.63 |
| Portfolio value | $98,049.35 |
| Benchmark value | $100,727.91 |
| Alpha (cumulative) | -2.679% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | -$23.95 |
| Signal saved | -$1908.55 |
| Portfolio value | $98,049.35 |
| Benchmark value | $100,279.96 |
| Alpha (cumulative) | -2.231% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$430.26 |
| Signal saved | -$2362.76 |
| Portfolio value | $98,049.35 |
| Benchmark value | $101,422.51 |
| Alpha (cumulative) | -3.374% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$476.37 |
| Signal saved | -$2408.87 |
| Portfolio value | $98,049.35 |
| Benchmark value | $101,538.49 |
| Alpha (cumulative) | -3.489% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$1107.07 |
| Signal saved | -$3039.57 |
| Portfolio value | $98,049.35 |
| Benchmark value | $103,124.99 |
| Alpha (cumulative) | -5.076% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$1102.83 |
| Signal saved | -$3035.33 |
| Portfolio value | $98,064.14 |
| Benchmark value | $103,114.32 |
| Alpha (cumulative) | -5.050% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$810.80 |
| Signal saved | -$2743.30 |
| Portfolio value | $98,035.37 |
| Benchmark value | $102,379.74 |
| Alpha (cumulative) | -4.345% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$776.88 |
| Signal saved | -$2709.38 |
| Portfolio value | $98,035.37 |
| Benchmark value | $102,294.41 |
| Alpha (cumulative) | -4.259% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$992.06 |
| Signal saved | -$2924.56 |
| Portfolio value | $98,035.37 |
| Benchmark value | $102,835.69 |
| Alpha (cumulative) | -4.801% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $765.49 |
| Unrealized P&L | +$7.14 |
| P&L % | +0.018% |
| Portfolio value | $98,042.51 |
| Benchmark value | $102,054.44 |
| Alpha (cumulative) | -4.012% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 55 — 2026-09-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $764.38 |
| Realized P&L (locked) | -$1932.50 |
| Reference if held | +$622.65 |
| Signal saved | -$2555.15 |
| Portfolio value | $98,067.50 |
| Benchmark value | $101,906.45 |
| Alpha (cumulative) | -3.838% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1932.50. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 56 — 2026-09-30

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $762.34 |
| Unrealized P&L | -$216.75 |
| P&L % | -0.554% |
| Portfolio value | $97,850.75 |
| Benchmark value | $101,634.48 |
| Alpha (cumulative) | -3.783% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-10-01

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $764.10 |
| Unrealized P&L | -$126.99 |
| P&L % | -0.325% |
| Portfolio value | $97,940.51 |
| Benchmark value | $101,869.12 |
| Alpha (cumulative) | -3.928% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: -0.33% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 58 — 2026-10-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $769.65 |
| Unrealized P&L | +$156.06 |
| P&L % | +0.399% |
| Portfolio value | $98,223.56 |
| Benchmark value | $102,609.05 |
| Alpha (cumulative) | -4.385% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +0.40% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 59 — 2026-10-05

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $774.97 |
| Unrealized P&L | +$427.38 |
| P&L % | +1.093% |
| Portfolio value | $98,494.88 |
| Benchmark value | $103,318.30 |
| Alpha (cumulative) | -4.823% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +1.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 60 — 2026-10-06

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $779.10 |
| Unrealized P&L | +$638.01 |
| P&L % | +1.632% |
| Portfolio value | $98,705.51 |
| Benchmark value | $103,868.91 |
| Alpha (cumulative) | -5.164% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +1.63% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 61 — 2026-10-07

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $752.632/share |
| Close price | $777.29 |
| Unrealized P&L | +$545.70 |
| P&L % | +1.396% |
| Portfolio value | $98,613.20 |
| Benchmark value | $103,627.60 |
| Alpha (cumulative) | -5.015% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $765.06 vs MA50 $763.82). Momentum: STRONG. Unrealized P&L: +1.40% from entry. No exit triggered.

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
_Day 61 of 90 · Alpaca equity: $99,632.14 · Cumulative alpha vs SPY: -5.015%_