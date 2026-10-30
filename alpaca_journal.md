# ALPACA PAPER JOURNAL — SPY
_Last updated: October 30, 2026 | Day 74 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$745.500/share**
> (2026-07-17, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-10-30): **NEUTRAL**  
> Fast: MA10 $nan | MA30 $nan  
> Slow: MA20 $nan | MA50 $nan  
> Regime: **BEAR** | Momentum: **WEAK** | Session: CLOSED

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

**Total trades:** 18 | **Closed:** 18 | **Open:** No | **Cumulative Realized P&L:** -$1815.96

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T2 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T3 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T4 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T5 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T6 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T7 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T8 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T9 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T10 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T11 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |
| T12 | $773.250 (2026-09-22) | $773.540 (2026-09-22) | 51 | +$14.79 | ✅ Closed |
| T13 | $768.534 (2026-09-23) | $767.970 (2026-09-23) | 51 | -$28.77 | ✅ Closed |
| T14 | $765.350 (2026-09-28) | $765.980 (2026-09-29) | 51 | +$32.13 | ✅ Closed |
| T15 | $766.590 (2026-09-30) | $767.680 (2026-10-14) | 51 | +$55.59 | ✅ Closed |
| T16 | $769.600 (2026-10-15) | $770.610 (2026-10-20) | 51 | +$51.51 | ✅ Closed |
| T17 | $773.850 (2026-10-21) | $762.110 (2026-10-22) | 51 | -$598.74 | ✅ Closed |
| T18 | $760.600 (2026-10-23) | $769.320 (2026-10-27) | 51 | +$444.72 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,040.41 |
| Alpaca cash | $99,040.41 |
| Cumulative realized P&L | -$1815.96 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-17 | $741.44 | FLAT | — | — | $99,857.44 |
| Day 2 | 2026-07-20 | $740.31 | FLAT | — | — | $99,665.46 |
| Day 3 | 2026-07-21 | $746.30 | Long 53 SPY (T3) | -$69.96 | -0.177% | $99,595.50 |
| Day 4 | 2026-07-22 | $745.64 | Long 53 SPY (T3) | -$104.94 | -0.265% | $99,560.52 |
| Day 5 | 2026-07-23 | $736.23 | Long 52 SPY (T4) | -$135.72 | -0.353% | $98,894.27 |
| Day 6 | 2026-07-24 | $737.07 | FLAT | — | — | $99,038.31 |
| Day 7 | 2026-07-27 | $737.02 | FLAT | — | — | $99,142.45 |
| Day 8 | 2026-07-28 | $738.96 | FLAT | — | — | $99,098.99 |
| Day 9 | 2026-07-29 | $727.76 | FLAT | — | — | $99,098.99 |
| Day 10 | 2026-07-30 | $739.79 | FLAT | — | — | $99,098.99 |
| Day 11 | 2026-07-31 | $744.94 | FLAT | — | — | $99,098.99 |
| Day 12 | 2026-08-03 | $755.84 | FLAT | — | — | $99,098.99 |
| Day 13 | 2026-08-04 | $769.20 | Long 50 SPY (T7) | -$147.50 | -0.382% | $98,951.49 |
| Day 14 | 2026-08-05 | $767.88 | FLAT | — | — | $99,011.99 |
| Day 15 | 2026-08-06 | $766.74 | FLAT | — | — | $99,011.99 |
| Day 16 | 2026-08-07 | $771.25 | Long 51 SPY (T8) | -$64.27 | -0.163% | $98,947.72 |
| Day 17 | 2026-08-10 | $771.11 | FLAT | — | — | $99,036.97 |
| Day 18 | 2026-08-11 | $768.61 | Long 51 SPY (T9) | -$256.60 | -0.650% | $98,780.37 |
| Day 19 | 2026-08-12 | $770.63 | Long 51 SPY (T9) | -$153.58 | -0.389% | $98,883.39 |
| Day 20 | 2026-08-13 | $775.91 | Long 51 SPY (T9) | +$115.70 | +0.293% | $99,152.67 |
| Day 21 | 2026-08-14 | $774.38 | Long 51 SPY (T9) | +$37.67 | +0.095% | $99,074.64 |
| Day 22 | 2026-08-17 | $770.71 | Long 51 SPY (T9) | -$149.50 | -0.379% | $98,887.47 |
| Day 23 | 2026-08-18 | $765.46 | Long 51 SPY (T9) | -$417.25 | -1.058% | $98,619.72 |
| Day 24 | 2026-08-19 | $767.19 | Long 51 SPY (T9) | -$329.02 | -0.834% | $98,707.95 |
| Day 25 | 2026-08-20 | $760.73 | Long 51 SPY (T9) | -$658.48 | -1.669% | $98,378.49 |
| Day 26 | 2026-08-21 | $763.74 | Long 51 SPY (T9) | -$504.97 | -1.280% | $98,532.00 |
| Day 27 | 2026-08-24 | $761.57 | Long 51 SPY (T9) | -$615.64 | -1.560% | $98,421.33 |
| Day 28 | 2026-08-25 | $763.89 | Long 51 SPY (T9) | -$497.32 | -1.260% | $98,539.65 |
| Day 29 | 2026-08-26 | $764.04 | Long 51 SPY (T9) | -$489.67 | -1.241% | $98,547.30 |
| Day 30 | 2026-08-27 | $769.27 | Long 51 SPY (T9) | -$222.94 | -0.565% | $98,814.03 |
| Day 31 | 2026-08-28 | $767.37 | Long 51 SPY (T9) | -$319.84 | -0.811% | $98,717.13 |
| Day 32 | 2026-08-31 | $764.97 | Long 51 SPY (T9) | -$442.24 | -1.121% | $98,594.73 |
| Day 33 | 2026-09-01 | $759.74 | FLAT | — | — | $98,424.39 |
| Day 34 | 2026-09-02 | $763.23 | Long 51 SPY (T10) | -$86.19 | -0.221% | $98,338.20 |
| Day 35 | 2026-09-03 | $771.20 | Long 51 SPY (T10) | +$320.28 | +0.821% | $98,744.67 |
| Day 36 | 2026-09-04 | $768.27 | Long 51 SPY (T10) | +$170.85 | +0.438% | $98,595.24 |
| Day 37 | 2026-09-08 | $764.16 | FLAT | — | — | $98,476.92 |
| Day 38 | 2026-09-09 | $760.54 | Long 52 SPY (T11) | -$127.87 | -0.322% | $98,349.05 |
| Day 39 | 2026-09-10 | $755.99 | FLAT | — | — | $98,212.81 |
| Day 40 | 2026-09-11 | $762.25 | FLAT | — | — | $98,212.81 |
| Day 41 | 2026-09-14 | $758.87 | FLAT | — | — | $98,212.81 |
| Day 42 | 2026-09-15 | $755.54 | FLAT | — | — | $98,212.81 |
| Day 43 | 2026-09-16 | $752.18 | FLAT | — | — | $98,212.81 |
| Day 44 | 2026-09-17 | $760.75 | FLAT | — | — | $98,212.81 |
| Day 45 | 2026-09-18 | $761.62 | FLAT | — | — | $98,212.81 |
| Day 46 | 2026-09-21 | $773.52 | FLAT | — | — | $98,212.81 |
| Day 47 | 2026-09-22 | $773.44 | FLAT | — | — | $98,227.60 |
| Day 48 | 2026-09-23 | $767.93 | FLAT | — | — | $98,198.83 |
| Day 49 | 2026-09-24 | $767.29 | FLAT | — | — | $98,198.83 |
| Day 50 | 2026-09-25 | $771.35 | FLAT | — | — | $98,198.83 |
| Day 51 | 2026-09-28 | $765.49 | Long 51 SPY (T14) | +$7.14 | +0.018% | $98,205.97 |
| Day 52 | 2026-09-29 | $764.38 | FLAT | — | — | $98,230.96 |
| Day 53 | 2026-09-30 | $762.34 | Long 51 SPY (T15) | -$216.75 | -0.554% | $98,014.21 |
| Day 54 | 2026-10-01 | $764.10 | Long 51 SPY (T15) | -$126.99 | -0.325% | $98,103.97 |
| Day 55 | 2026-10-02 | $769.65 | Long 51 SPY (T15) | +$156.06 | +0.399% | $98,387.02 |
| Day 56 | 2026-10-05 | $774.97 | Long 51 SPY (T15) | +$427.38 | +1.093% | $98,658.34 |
| Day 57 | 2026-10-06 | $779.10 | Long 51 SPY (T15) | +$638.01 | +1.632% | $98,868.97 |
| Day 58 | 2026-10-07 | $777.15 | Long 51 SPY (T15) | +$538.56 | +1.378% | $98,769.52 |
| Day 59 | 2026-10-08 | $773.88 | Long 51 SPY (T15) | +$371.79 | +0.951% | $98,602.75 |
| Day 60 | 2026-10-09 | $778.51 | Long 51 SPY (T15) | +$607.92 | +1.555% | $98,838.88 |
| Day 61 | 2026-10-12 | $778.03 | Long 51 SPY (T15) | +$583.44 | +1.492% | $98,814.40 |
| Day 62 | 2026-10-13 | $778.03 | Long 51 SPY (T15) | +$583.44 | +1.492% | $98,814.40 |
| Day 63 | 2026-10-14 | $769.65 | FLAT | — | — | $98,286.55 |
| Day 64 | 2026-10-15 | $771.77 | Long 51 SPY (T16) | +$110.67 | +0.282% | $98,397.22 |
| Day 65 | 2026-10-16 | $763.34 | Long 51 SPY (T16) | -$319.26 | -0.813% | $97,967.29 |
| Day 66 | 2026-10-19 | $766.60 | Long 51 SPY (T16) | -$153.00 | -0.390% | $98,133.55 |
| Day 67 | 2026-10-20 | $769.09 | FLAT | — | — | $98,338.06 |
| Day 68 | 2026-10-21 | $773.13 | Long 51 SPY (T17) | -$36.72 | -0.093% | $98,301.34 |
| Day 69 | 2026-10-22 | $764.03 | FLAT | — | — | $97,739.32 |
| Day 70 | 2026-10-23 | $759.83 | Long 51 SPY (T18) | -$39.27 | -0.101% | $97,700.05 |
| Day 71 | 2026-10-26 | $765.23 | Long 51 SPY (T18) | +$236.13 | +0.609% | $97,975.45 |
| Day 72 | 2026-10-27 | $769.70 | FLAT | — | — | $98,184.04 |
| Day 73 | 2026-10-28 | $772.28 | FLAT | — | — | $98,184.04 |
| Day 74 | 2026-10-29 | $769.49 | FLAT | — | — | $98,184.04 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-17 | $99,857.44 | $100,000.01 | -0.1426% | +0.000% | **-0.143%** |
| Day 2 | 2026-07-20 | $99,665.46 | $99,847.61 | -0.3345% | -0.152% | **-0.183%** |
| Day 3 | 2026-07-21 | $99,595.50 | $100,655.50 | -0.4045% | +0.656% | **-1.060%** |
| Day 4 | 2026-07-22 | $99,560.52 | $100,566.48 | -0.4395% | +0.566% | **-1.006%** |
| Day 5 | 2026-07-23 | $98,894.27 | $99,297.33 | -1.1057% | -0.703% | **-0.403%** |
| Day 6 | 2026-07-24 | $99,038.31 | $99,410.62 | -0.9617% | -0.589% | **-0.373%** |
| Day 7 | 2026-07-27 | $99,142.45 | $99,403.88 | -0.8576% | -0.596% | **-0.262%** |
| Day 8 | 2026-07-28 | $99,098.99 | $99,665.53 | -0.9010% | -0.334% | **-0.567%** |
| Day 9 | 2026-07-29 | $99,098.99 | $98,154.96 | -0.9010% | -1.845% | **+0.944%** |
| Day 10 | 2026-07-30 | $99,098.99 | $99,777.47 | -0.9010% | -0.223% | **-0.678%** |
| Day 11 | 2026-07-31 | $99,098.99 | $100,472.07 | -0.9010% | +0.472% | **-1.373%** |
| Day 12 | 2026-08-03 | $99,098.99 | $101,942.18 | -0.9010% | +1.942% | **-2.843%** |
| Day 13 | 2026-08-04 | $98,951.49 | $103,744.08 | -1.0485% | +3.744% | **-4.792%** |
| Day 14 | 2026-08-05 | $99,011.99 | $103,566.05 | -0.9880% | +3.566% | **-4.554%** |
| Day 15 | 2026-08-06 | $99,011.99 | $103,412.29 | -0.9880% | +3.412% | **-4.400%** |
| Day 16 | 2026-08-07 | $98,947.72 | $104,020.57 | -1.0523% | +4.021% | **-5.073%** |
| Day 17 | 2026-08-10 | $99,036.97 | $104,001.69 | -0.9630% | +4.002% | **-4.965%** |
| Day 18 | 2026-08-11 | $98,780.37 | $103,664.51 | -1.2196% | +3.665% | **-4.885%** |
| Day 19 | 2026-08-12 | $98,883.39 | $103,936.95 | -1.1166% | +3.937% | **-5.054%** |
| Day 20 | 2026-08-13 | $99,152.67 | $104,649.08 | -0.8473% | +4.649% | **-5.496%** |
| Day 21 | 2026-08-14 | $99,074.64 | $104,442.72 | -0.9254% | +4.443% | **-5.368%** |
| Day 22 | 2026-08-17 | $98,887.47 | $103,947.74 | -1.1125% | +3.948% | **-5.060%** |
| Day 23 | 2026-08-18 | $98,619.72 | $103,239.66 | -1.3803% | +3.240% | **-4.620%** |
| Day 24 | 2026-08-19 | $98,707.95 | $103,472.99 | -1.2921% | +3.473% | **-4.765%** |
| Day 25 | 2026-08-20 | $98,378.49 | $102,601.71 | -1.6215% | +2.602% | **-4.224%** |
| Day 26 | 2026-08-21 | $98,532.00 | $103,007.68 | -1.4680% | +3.008% | **-4.476%** |
| Day 27 | 2026-08-24 | $98,421.33 | $102,715.00 | -1.5787% | +2.715% | **-4.294%** |
| Day 28 | 2026-08-25 | $98,539.65 | $103,027.91 | -1.4604% | +3.028% | **-4.488%** |
| Day 29 | 2026-08-26 | $98,547.30 | $103,048.14 | -1.4527% | +3.048% | **-4.501%** |
| Day 30 | 2026-08-27 | $98,814.03 | $103,753.52 | -1.1860% | +3.754% | **-4.940%** |
| Day 31 | 2026-08-28 | $98,717.13 | $103,497.26 | -1.2829% | +3.497% | **-4.780%** |
| Day 32 | 2026-08-31 | $98,594.73 | $103,173.57 | -1.4053% | +3.174% | **-4.579%** |
| Day 33 | 2026-09-01 | $98,424.39 | $102,468.19 | -1.5756% | +2.468% | **-4.044%** |
| Day 34 | 2026-09-02 | $98,338.20 | $102,938.89 | -1.6618% | +2.939% | **-4.601%** |
| Day 35 | 2026-09-03 | $98,744.67 | $104,013.83 | -1.2553% | +4.014% | **-5.269%** |
| Day 36 | 2026-09-04 | $98,595.24 | $103,618.65 | -1.4048% | +3.619% | **-5.024%** |
| Day 37 | 2026-09-08 | $98,476.92 | $103,064.32 | -1.5231% | +3.064% | **-4.587%** |
| Day 38 | 2026-09-09 | $98,349.05 | $102,576.08 | -1.6509% | +2.576% | **-4.227%** |
| Day 39 | 2026-09-10 | $98,212.81 | $101,962.41 | -1.7872% | +1.962% | **-3.749%** |
| Day 40 | 2026-09-11 | $98,212.81 | $102,806.72 | -1.7872% | +2.807% | **-4.594%** |
| Day 41 | 2026-09-14 | $98,212.81 | $102,350.85 | -1.7872% | +2.351% | **-4.138%** |
| Day 42 | 2026-09-15 | $98,212.81 | $101,901.72 | -1.7872% | +1.902% | **-3.689%** |
| Day 43 | 2026-09-16 | $98,212.81 | $101,448.55 | -1.7872% | +1.449% | **-3.236%** |
| Day 44 | 2026-09-17 | $98,212.81 | $102,604.41 | -1.7872% | +2.604% | **-4.391%** |
| Day 45 | 2026-09-18 | $98,212.81 | $102,721.75 | -1.7872% | +2.722% | **-4.509%** |
| Day 46 | 2026-09-21 | $98,212.81 | $104,326.73 | -1.7872% | +4.327% | **-6.114%** |
| Day 47 | 2026-09-22 | $98,227.60 | $104,315.94 | -1.7724% | +4.316% | **-6.088%** |
| Day 48 | 2026-09-23 | $98,198.83 | $103,572.79 | -1.8012% | +3.573% | **-5.374%** |
| Day 49 | 2026-09-24 | $98,198.83 | $103,486.47 | -1.8012% | +3.486% | **-5.287%** |
| Day 50 | 2026-09-25 | $98,198.83 | $104,034.06 | -1.8012% | +4.034% | **-5.835%** |
| Day 51 | 2026-09-28 | $98,205.97 | $103,243.70 | -1.7940% | +3.244% | **-5.038%** |
| Day 52 | 2026-09-29 | $98,230.96 | $103,093.99 | -1.7690% | +3.094% | **-4.863%** |
| Day 53 | 2026-09-30 | $98,014.21 | $102,818.85 | -1.9858% | +2.819% | **-4.805%** |
| Day 54 | 2026-10-01 | $98,103.97 | $103,056.23 | -1.8960% | +3.056% | **-4.952%** |
| Day 55 | 2026-10-02 | $98,387.02 | $103,804.77 | -1.6130% | +3.805% | **-5.418%** |
| Day 56 | 2026-10-05 | $98,658.34 | $104,522.30 | -1.3417% | +4.522% | **-5.864%** |
| Day 57 | 2026-10-06 | $98,868.97 | $105,079.32 | -1.1310% | +5.079% | **-6.210%** |
| Day 58 | 2026-10-07 | $98,769.52 | $104,816.32 | -1.2305% | +4.816% | **-6.046%** |
| Day 59 | 2026-10-08 | $98,602.75 | $104,375.29 | -1.3973% | +4.375% | **-5.772%** |
| Day 60 | 2026-10-09 | $98,838.88 | $104,999.75 | -1.1611% | +5.000% | **-6.161%** |
| Day 61 | 2026-10-12 | $98,814.40 | $104,935.01 | -1.1856% | +4.935% | **-6.121%** |
| Day 62 | 2026-10-13 | $98,814.40 | $104,935.01 | -1.1856% | +4.935% | **-6.121%** |
| Day 63 | 2026-10-14 | $98,286.55 | $103,804.77 | -1.7134% | +3.805% | **-5.518%** |
| Day 64 | 2026-10-15 | $98,397.22 | $104,090.70 | -1.6028% | +4.091% | **-5.694%** |
| Day 65 | 2026-10-16 | $97,967.29 | $102,953.73 | -2.0327% | +2.954% | **-4.987%** |
| Day 66 | 2026-10-19 | $98,133.55 | $103,393.41 | -1.8664% | +3.393% | **-5.259%** |
| Day 67 | 2026-10-20 | $98,338.06 | $103,729.24 | -1.6619% | +3.729% | **-5.391%** |
| Day 68 | 2026-10-21 | $98,301.34 | $104,274.13 | -1.6987% | +4.274% | **-5.973%** |
| Day 69 | 2026-10-22 | $97,739.32 | $103,046.79 | -2.2607% | +3.047% | **-5.308%** |
| Day 70 | 2026-10-23 | $97,700.05 | $102,480.32 | -2.2999% | +2.480% | **-4.780%** |
| Day 71 | 2026-10-26 | $97,975.45 | $103,208.64 | -2.0246% | +3.209% | **-5.234%** |
| Day 72 | 2026-10-27 | $98,184.04 | $103,811.52 | -1.8160% | +3.812% | **-5.628%** |
| Day 73 | 2026-10-28 | $98,184.04 | $104,159.49 | -1.8160% | +4.159% | **-5.975%** |
| Day 74 | 2026-10-29 | $98,184.04 | $103,783.19 | -1.8160% | +3.783% | **-5.599%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-17 | $741.44 | -$219.24 | -$1596.72 | Holding would have been **$1596.72** better — honest entry |
| Day 2 | 2026-07-20 | $740.31 | -$280.26 | -$1535.70 | Holding would have been **$1535.70** better — honest entry |
| Day 3 | 2026-07-21 | $746.30 | +$43.20 | -$1859.16 | Position open |
| Day 4 | 2026-07-22 | $745.64 | +$7.56 | -$1823.52 | Position open |
| Day 5 | 2026-07-23 | $736.23 | -$500.58 | -$1315.38 | Position open |
| Day 6 | 2026-07-24 | $737.07 | -$455.22 | -$1360.74 | Holding would have been **$1360.74** better — honest entry |
| Day 7 | 2026-07-27 | $737.02 | -$457.92 | -$1358.04 | Holding would have been **$1358.04** better — honest entry |
| Day 8 | 2026-07-28 | $738.96 | -$353.16 | -$1462.80 | Holding would have been **$1462.80** better — honest entry |
| Day 9 | 2026-07-29 | $727.76 | -$957.96 | -$858.00 | Holding would have been **$858.00** better — honest entry |
| Day 10 | 2026-07-30 | $739.79 | -$308.34 | -$1507.62 | Holding would have been **$1507.62** better — honest entry |
| Day 11 | 2026-07-31 | $744.94 | -$30.24 | -$1785.72 | Holding would have been **$1785.72** better — honest entry |
| Day 12 | 2026-08-03 | $755.84 | +$558.36 | -$2374.32 | Holding would have been **$2374.32** better — honest entry |
| Day 13 | 2026-08-04 | $769.20 | +$1279.80 | -$3095.76 | Position open |
| Day 14 | 2026-08-05 | $767.88 | +$1208.52 | -$3024.48 | Holding would have been **$3024.48** better — honest entry |
| Day 15 | 2026-08-06 | $766.74 | +$1146.96 | -$2962.92 | Holding would have been **$2962.92** better — honest entry |
| Day 16 | 2026-08-07 | $771.25 | +$1390.50 | -$3206.46 | Position open |
| Day 17 | 2026-08-10 | $771.11 | +$1382.94 | -$3198.90 | Holding would have been **$3198.90** better — honest entry |
| Day 18 | 2026-08-11 | $768.61 | +$1247.94 | -$3063.90 | Position open |
| Day 19 | 2026-08-12 | $770.63 | +$1357.02 | -$3172.98 | Position open |
| Day 20 | 2026-08-13 | $775.91 | +$1642.14 | -$3458.10 | Position open |
| Day 21 | 2026-08-14 | $774.38 | +$1559.52 | -$3375.48 | Position open |
| Day 22 | 2026-08-17 | $770.71 | +$1361.34 | -$3177.30 | Position open |
| Day 23 | 2026-08-18 | $765.46 | +$1077.84 | -$2893.80 | Position open |
| Day 24 | 2026-08-19 | $767.19 | +$1171.26 | -$2987.22 | Position open |
| Day 25 | 2026-08-20 | $760.73 | +$822.42 | -$2638.38 | Position open |
| Day 26 | 2026-08-21 | $763.74 | +$984.96 | -$2800.92 | Position open |
| Day 27 | 2026-08-24 | $761.57 | +$867.78 | -$2683.74 | Position open |
| Day 28 | 2026-08-25 | $763.89 | +$993.06 | -$2809.02 | Position open |
| Day 29 | 2026-08-26 | $764.04 | +$1001.16 | -$2817.12 | Position open |
| Day 30 | 2026-08-27 | $769.27 | +$1283.58 | -$3099.54 | Position open |
| Day 31 | 2026-08-28 | $767.37 | +$1180.98 | -$2996.94 | Position open |
| Day 32 | 2026-08-31 | $764.97 | +$1051.38 | -$2867.34 | Position open |
| Day 33 | 2026-09-01 | $759.74 | +$768.96 | -$2584.92 | Holding would have been **$2584.92** better — honest entry |
| Day 34 | 2026-09-02 | $763.23 | +$957.42 | -$2773.38 | Position open |
| Day 35 | 2026-09-03 | $771.20 | +$1387.80 | -$3203.76 | Position open |
| Day 36 | 2026-09-04 | $768.27 | +$1229.58 | -$3045.54 | Position open |
| Day 37 | 2026-09-08 | $764.16 | +$1007.64 | -$2823.60 | Holding would have been **$2823.60** better — honest entry |
| Day 38 | 2026-09-09 | $760.54 | +$812.16 | -$2628.12 | Position open |
| Day 39 | 2026-09-10 | $755.99 | +$566.46 | -$2382.42 | Holding would have been **$2382.42** better — honest entry |
| Day 40 | 2026-09-11 | $762.25 | +$904.50 | -$2720.46 | Holding would have been **$2720.46** better — honest entry |
| Day 41 | 2026-09-14 | $758.87 | +$721.98 | -$2537.94 | Holding would have been **$2537.94** better — honest entry |
| Day 42 | 2026-09-15 | $755.54 | +$542.16 | -$2358.12 | Holding would have been **$2358.12** better — honest entry |
| Day 43 | 2026-09-16 | $752.18 | +$360.72 | -$2176.68 | Holding would have been **$2176.68** better — honest entry |
| Day 44 | 2026-09-17 | $760.75 | +$823.50 | -$2639.46 | Holding would have been **$2639.46** better — honest entry |
| Day 45 | 2026-09-18 | $761.62 | +$870.48 | -$2686.44 | Holding would have been **$2686.44** better — honest entry |
| Day 46 | 2026-09-21 | $773.52 | +$1513.08 | -$3329.04 | Holding would have been **$3329.04** better — honest entry |
| Day 47 | 2026-09-22 | $773.44 | +$1508.76 | -$3324.72 | Holding would have been **$3324.72** better — honest entry |
| Day 48 | 2026-09-23 | $767.93 | +$1211.22 | -$3027.18 | Holding would have been **$3027.18** better — honest entry |
| Day 49 | 2026-09-24 | $767.29 | +$1176.66 | -$2992.62 | Holding would have been **$2992.62** better — honest entry |
| Day 50 | 2026-09-25 | $771.35 | +$1395.90 | -$3211.86 | Holding would have been **$3211.86** better — honest entry |
| Day 51 | 2026-09-28 | $765.49 | +$1079.46 | -$2895.42 | Position open |
| Day 52 | 2026-09-29 | $764.38 | +$1019.52 | -$2835.48 | Holding would have been **$2835.48** better — honest entry |
| Day 53 | 2026-09-30 | $762.34 | +$909.36 | -$2725.32 | Position open |
| Day 54 | 2026-10-01 | $764.10 | +$1004.40 | -$2820.36 | Position open |
| Day 55 | 2026-10-02 | $769.65 | +$1304.10 | -$3120.06 | Position open |
| Day 56 | 2026-10-05 | $774.97 | +$1591.38 | -$3407.34 | Position open |
| Day 57 | 2026-10-06 | $779.10 | +$1814.40 | -$3630.36 | Position open |
| Day 58 | 2026-10-07 | $777.15 | +$1709.10 | -$3525.06 | Position open |
| Day 59 | 2026-10-08 | $773.88 | +$1532.52 | -$3348.48 | Position open |
| Day 60 | 2026-10-09 | $778.51 | +$1782.54 | -$3598.50 | Position open |
| Day 61 | 2026-10-12 | $778.03 | +$1756.62 | -$3572.58 | Position open |
| Day 62 | 2026-10-13 | $778.03 | +$1756.62 | -$3572.58 | Position open |
| Day 63 | 2026-10-14 | $769.65 | +$1304.10 | -$3120.06 | Holding would have been **$3120.06** better — honest entry |
| Day 64 | 2026-10-15 | $771.77 | +$1418.58 | -$3234.54 | Position open |
| Day 65 | 2026-10-16 | $763.34 | +$963.36 | -$2779.32 | Position open |
| Day 66 | 2026-10-19 | $766.60 | +$1139.40 | -$2955.36 | Position open |
| Day 67 | 2026-10-20 | $769.09 | +$1273.86 | -$3089.82 | Holding would have been **$3089.82** better — honest entry |
| Day 68 | 2026-10-21 | $773.13 | +$1492.02 | -$3307.98 | Position open |
| Day 69 | 2026-10-22 | $764.03 | +$1000.62 | -$2816.58 | Holding would have been **$2816.58** better — honest entry |
| Day 70 | 2026-10-23 | $759.83 | +$773.82 | -$2589.78 | Position open |
| Day 71 | 2026-10-26 | $765.23 | +$1065.42 | -$2881.38 | Position open |
| Day 72 | 2026-10-27 | $769.70 | +$1306.80 | -$3122.76 | Holding would have been **$3122.76** better — honest entry |
| Day 73 | 2026-10-28 | $772.28 | +$1446.12 | -$3262.08 | Holding would have been **$3262.08** better — honest entry |
| Day 74 | 2026-10-29 | $769.49 | +$1295.46 | -$3111.42 | Holding would have been **$3111.42** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$219.24 |
| Signal saved | -$1596.72 |
| Portfolio value | $99,857.44 |
| Benchmark value | $100,000.01 |
| Alpha (cumulative) | -0.143% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 2 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$280.26 |
| Signal saved | -$1535.70 |
| Portfolio value | $99,665.46 |
| Benchmark value | $99,847.61 |
| Alpha (cumulative) | -0.183% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 3 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T3) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,595.50 |
| Benchmark value | $100,655.50 |
| Alpha (cumulative) | -1.060% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 4 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T3) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,560.52 |
| Benchmark value | $100,566.48 |
| Alpha (cumulative) | -1.006% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 5 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T4) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,894.27 |
| Benchmark value | $99,297.33 |
| Alpha (cumulative) | -0.403% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 6 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$455.22 |
| Signal saved | -$1360.74 |
| Portfolio value | $99,038.31 |
| Benchmark value | $99,410.62 |
| Alpha (cumulative) | -0.373% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 7 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$457.92 |
| Signal saved | -$1358.04 |
| Portfolio value | $99,142.45 |
| Benchmark value | $99,403.88 |
| Alpha (cumulative) | -0.262% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 8 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$353.16 |
| Signal saved | -$1462.80 |
| Portfolio value | $99,098.99 |
| Benchmark value | $99,665.53 |
| Alpha (cumulative) | -0.567% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 9 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$957.96 |
| Signal saved | -$858.00 |
| Portfolio value | $99,098.99 |
| Benchmark value | $98,154.96 |
| Alpha (cumulative) | +0.944% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 10 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$308.34 |
| Signal saved | -$1507.62 |
| Portfolio value | $99,098.99 |
| Benchmark value | $99,777.47 |
| Alpha (cumulative) | -0.678% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 11 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | -$30.24 |
| Signal saved | -$1785.72 |
| Portfolio value | $99,098.99 |
| Benchmark value | $100,472.07 |
| Alpha (cumulative) | -1.373% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 12 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$558.36 |
| Signal saved | -$2374.32 |
| Portfolio value | $99,098.99 |
| Benchmark value | $101,942.18 |
| Alpha (cumulative) | -2.843% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 13 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T7) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,951.49 |
| Benchmark value | $103,744.08 |
| Alpha (cumulative) | -4.792% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 14 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1208.52 |
| Signal saved | -$3024.48 |
| Portfolio value | $99,011.99 |
| Benchmark value | $103,566.05 |
| Alpha (cumulative) | -4.554% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 15 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1146.96 |
| Signal saved | -$2962.92 |
| Portfolio value | $99,011.99 |
| Benchmark value | $103,412.29 |
| Alpha (cumulative) | -4.400% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 16 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T8) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,947.72 |
| Benchmark value | $104,020.57 |
| Alpha (cumulative) | -5.073% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 17 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1382.94 |
| Signal saved | -$3198.90 |
| Portfolio value | $99,036.97 |
| Benchmark value | $104,001.69 |
| Alpha (cumulative) | -4.965% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 18 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,780.37 |
| Benchmark value | $103,664.51 |
| Alpha (cumulative) | -4.885% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 19 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,883.39 |
| Benchmark value | $103,936.95 |
| Alpha (cumulative) | -5.054% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 20 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $99,152.67 |
| Benchmark value | $104,649.08 |
| Alpha (cumulative) | -5.496% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 21 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $99,074.64 |
| Benchmark value | $104,442.72 |
| Alpha (cumulative) | -5.368% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 22 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,887.47 |
| Benchmark value | $103,947.74 |
| Alpha (cumulative) | -5.060% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 23 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,619.72 |
| Benchmark value | $103,239.66 |
| Alpha (cumulative) | -4.620% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 24 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,707.95 |
| Benchmark value | $103,472.99 |
| Alpha (cumulative) | -4.765% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 25 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,378.49 |
| Benchmark value | $102,601.71 |
| Alpha (cumulative) | -4.224% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 26 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,532.00 |
| Benchmark value | $103,007.68 |
| Alpha (cumulative) | -4.476% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 27 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,421.33 |
| Benchmark value | $102,715.00 |
| Alpha (cumulative) | -4.294% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 28 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,539.65 |
| Benchmark value | $103,027.91 |
| Alpha (cumulative) | -4.488% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 29 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,547.30 |
| Benchmark value | $103,048.14 |
| Alpha (cumulative) | -4.501% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 30 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,814.03 |
| Benchmark value | $103,753.52 |
| Alpha (cumulative) | -4.940% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 31 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,717.13 |
| Benchmark value | $103,497.26 |
| Alpha (cumulative) | -4.780% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 32 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T9) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,594.73 |
| Benchmark value | $103,173.57 |
| Alpha (cumulative) | -4.579% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 33 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$768.96 |
| Signal saved | -$2584.92 |
| Portfolio value | $98,424.39 |
| Benchmark value | $102,468.19 |
| Alpha (cumulative) | -4.044% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 34 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,338.20 |
| Benchmark value | $102,938.89 |
| Alpha (cumulative) | -4.601% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 35 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,744.67 |
| Benchmark value | $104,013.83 |
| Alpha (cumulative) | -5.269% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 36 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T10) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,595.24 |
| Benchmark value | $103,618.65 |
| Alpha (cumulative) | -5.024% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 37 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1007.64 |
| Signal saved | -$2823.60 |
| Portfolio value | $98,476.92 |
| Benchmark value | $103,064.32 |
| Alpha (cumulative) | -4.587% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 38 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T11) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,349.05 |
| Benchmark value | $102,576.08 |
| Alpha (cumulative) | -4.227% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$566.46 |
| Signal saved | -$2382.42 |
| Portfolio value | $98,212.81 |
| Benchmark value | $101,962.41 |
| Alpha (cumulative) | -3.749% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 40 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$904.50 |
| Signal saved | -$2720.46 |
| Portfolio value | $98,212.81 |
| Benchmark value | $102,806.72 |
| Alpha (cumulative) | -4.594% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$721.98 |
| Signal saved | -$2537.94 |
| Portfolio value | $98,212.81 |
| Benchmark value | $102,350.85 |
| Alpha (cumulative) | -4.138% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$542.16 |
| Signal saved | -$2358.12 |
| Portfolio value | $98,212.81 |
| Benchmark value | $101,901.72 |
| Alpha (cumulative) | -3.689% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$360.72 |
| Signal saved | -$2176.68 |
| Portfolio value | $98,212.81 |
| Benchmark value | $101,448.55 |
| Alpha (cumulative) | -3.236% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$823.50 |
| Signal saved | -$2639.46 |
| Portfolio value | $98,212.81 |
| Benchmark value | $102,604.41 |
| Alpha (cumulative) | -4.391% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$870.48 |
| Signal saved | -$2686.44 |
| Portfolio value | $98,212.81 |
| Benchmark value | $102,721.75 |
| Alpha (cumulative) | -4.509% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1513.08 |
| Signal saved | -$3329.04 |
| Portfolio value | $98,212.81 |
| Benchmark value | $104,326.73 |
| Alpha (cumulative) | -6.114% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1508.76 |
| Signal saved | -$3324.72 |
| Portfolio value | $98,227.60 |
| Benchmark value | $104,315.94 |
| Alpha (cumulative) | -6.088% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1211.22 |
| Signal saved | -$3027.18 |
| Portfolio value | $98,198.83 |
| Benchmark value | $103,572.79 |
| Alpha (cumulative) | -5.374% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1176.66 |
| Signal saved | -$2992.62 |
| Portfolio value | $98,198.83 |
| Benchmark value | $103,486.47 |
| Alpha (cumulative) | -5.287% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1395.90 |
| Signal saved | -$3211.86 |
| Portfolio value | $98,198.83 |
| Benchmark value | $104,034.06 |
| Alpha (cumulative) | -5.835% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $765.49 |
| Unrealized P&L | +$7.14 |
| P&L % | +0.018% |
| Portfolio value | $98,205.97 |
| Benchmark value | $103,243.70 |
| Alpha (cumulative) | -5.038% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $764.38 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1019.52 |
| Signal saved | -$2835.48 |
| Portfolio value | $98,230.96 |
| Benchmark value | $103,093.99 |
| Alpha (cumulative) | -4.863% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-30

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $762.34 |
| Unrealized P&L | -$216.75 |
| P&L % | -0.554% |
| Portfolio value | $98,014.21 |
| Benchmark value | $102,818.85 |
| Alpha (cumulative) | -4.805% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 54 — 2026-10-01

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $764.10 |
| Unrealized P&L | -$126.99 |
| P&L % | -0.325% |
| Portfolio value | $98,103.97 |
| Benchmark value | $103,056.23 |
| Alpha (cumulative) | -4.952% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.33% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 55 — 2026-10-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.65 |
| Unrealized P&L | +$156.06 |
| P&L % | +0.399% |
| Portfolio value | $98,387.02 |
| Benchmark value | $103,804.77 |
| Alpha (cumulative) | -5.418% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.40% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 56 — 2026-10-05

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $774.97 |
| Unrealized P&L | +$427.38 |
| P&L % | +1.093% |
| Portfolio value | $98,658.34 |
| Benchmark value | $104,522.30 |
| Alpha (cumulative) | -5.864% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +1.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-10-06

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $779.10 |
| Unrealized P&L | +$638.01 |
| P&L % | +1.632% |
| Portfolio value | $98,868.97 |
| Benchmark value | $105,079.32 |
| Alpha (cumulative) | -6.210% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +1.63% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 58 — 2026-10-07

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $777.15 |
| Unrealized P&L | +$538.56 |
| P&L % | +1.378% |
| Portfolio value | $98,769.52 |
| Benchmark value | $104,816.32 |
| Alpha (cumulative) | -6.046% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +1.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 59 — 2026-10-08

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $773.88 |
| Unrealized P&L | +$371.79 |
| P&L % | +0.951% |
| Portfolio value | $98,602.75 |
| Benchmark value | $104,375.29 |
| Alpha (cumulative) | -5.772% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.95% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 60 — 2026-10-09

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $778.51 |
| Unrealized P&L | +$607.92 |
| P&L % | +1.555% |
| Portfolio value | $98,838.88 |
| Benchmark value | $104,999.75 |
| Alpha (cumulative) | -6.161% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +1.55% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 61 — 2026-10-12

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,814.40 |
| Benchmark value | $104,935.01 |
| Alpha (cumulative) | -6.121% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 62 — 2026-10-13

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $778.03 |
| Unrealized P&L | +$583.44 |
| P&L % | +1.492% |
| Portfolio value | $98,814.40 |
| Benchmark value | $104,935.01 |
| Alpha (cumulative) | -6.121% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +1.49% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 63 — 2026-10-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.65 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1304.10 |
| Signal saved | -$3120.06 |
| Portfolio value | $98,286.55 |
| Benchmark value | $103,804.77 |
| Alpha (cumulative) | -5.518% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 64 — 2026-10-15

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $771.77 |
| Unrealized P&L | +$110.67 |
| P&L % | +0.282% |
| Portfolio value | $98,397.22 |
| Benchmark value | $104,090.70 |
| Alpha (cumulative) | -5.694% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 65 — 2026-10-16

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $763.34 |
| Unrealized P&L | -$319.26 |
| P&L % | -0.813% |
| Portfolio value | $97,967.29 |
| Benchmark value | $102,953.73 |
| Alpha (cumulative) | -4.987% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 66 — 2026-10-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $766.60 |
| Unrealized P&L | -$153.00 |
| P&L % | -0.390% |
| Portfolio value | $98,133.55 |
| Benchmark value | $103,393.41 |
| Alpha (cumulative) | -5.259% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 67 — 2026-10-20

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.09 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1273.86 |
| Signal saved | -$3089.82 |
| Portfolio value | $98,338.06 |
| Benchmark value | $103,729.24 |
| Alpha (cumulative) | -5.391% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 68 — 2026-10-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $773.13 |
| Unrealized P&L | -$36.72 |
| P&L % | -0.093% |
| Portfolio value | $98,301.34 |
| Benchmark value | $104,274.13 |
| Alpha (cumulative) | -5.973% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.09% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 69 — 2026-10-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $764.03 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1000.62 |
| Signal saved | -$2816.58 |
| Portfolio value | $97,739.32 |
| Benchmark value | $103,046.79 |
| Alpha (cumulative) | -5.308% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 70 — 2026-10-23

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $759.83 |
| Unrealized P&L | -$39.27 |
| P&L % | -0.101% |
| Portfolio value | $97,700.05 |
| Benchmark value | $102,480.32 |
| Alpha (cumulative) | -4.780% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: -0.10% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 71 — 2026-10-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $765.23 |
| Unrealized P&L | +$236.13 |
| P&L % | +0.609% |
| Portfolio value | $97,975.45 |
| Benchmark value | $103,208.64 |
| Alpha (cumulative) | -5.234% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained NEUTRAL. Regime: BEAR (MA20 $nan vs MA50 $nan). Momentum: WEAK. Unrealized P&L: +0.61% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 72 — 2026-10-27

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.70 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1306.80 |
| Signal saved | -$3122.76 |
| Portfolio value | $98,184.04 |
| Benchmark value | $103,811.52 |
| Alpha (cumulative) | -5.628% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 73 — 2026-10-28

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $772.28 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1446.12 |
| Signal saved | -$3262.08 |
| Portfolio value | $98,184.04 |
| Benchmark value | $104,159.49 |
| Alpha (cumulative) | -5.975% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 74 — 2026-10-29

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $745.500/share |
| Close price | $769.49 |
| Realized P&L (locked) | -$1815.96 |
| Reference if held | +$1295.46 |
| Signal saved | -$3111.42 |
| Portfolio value | $98,184.04 |
| Benchmark value | $103,783.19 |
| Alpha (cumulative) | -5.599% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1815.96. Regime: BEAR (MA20 $nan vs MA50 $nan). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

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
_Day 74 of 90 · Alpaca equity: $99,040.41 · Cumulative alpha vs SPY: -5.599%_