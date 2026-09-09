# ALPACA PAPER JOURNAL — SPY
_Last updated: September 09, 2026 | Day 90 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$722.670/share**
> (2026-05-01, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-09-09): **BULLISH**  
> Fast: MA10 $767.22 | MA30 $765.61  
> Slow: MA20 $768.29 | MA50 $758.02  
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

**Total trades:** 17 | **Closed:** 16 | **Open:** Yes | **Cumulative Realized P&L:** -$1784.84

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 3 | +$63.93 | ✅ Closed |
| T2 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T3 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T4 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T5 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T6 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T7 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T8 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T9 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T10 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T11 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T12 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T13 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T14 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T15 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T16 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T17 | $762.999 (2026-09-09) | — | 52 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,323.13 |
| Alpaca cash | $59,663.25 |
| Cumulative realized P&L | -$1784.84 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-05-01 | $718.64 | Long 3 SPY (T1) | -$12.09 | -0.558% | $99,987.91 |
| Day 2 | 2026-05-04 | $716.25 | Long 3 SPY (T1) | -$19.26 | -0.888% | $99,980.74 |
| Day 3 | 2026-05-05 | $721.85 | Long 3 SPY (T1) | -$2.46 | -0.113% | $99,997.54 |
| Day 4 | 2026-05-06 | $731.88 | Long 3 SPY (T1) | +$27.63 | +1.274% | $100,027.63 |
| Day 5 | 2026-05-07 | $729.65 | Long 3 SPY (T1) | +$20.94 | +0.966% | $100,020.94 |
| Day 6 | 2026-05-08 | $735.65 | Long 3 SPY (T1) | +$38.94 | +1.796% | $100,038.94 |
| Day 7 | 2026-05-11 | $737.30 | Long 3 SPY (T1) | +$43.89 | +2.024% | $100,043.89 |
| Day 8 | 2026-05-12 | $736.29 | Long 3 SPY (T1) | +$40.86 | +1.885% | $100,040.86 |
| Day 9 | 2026-05-13 | $740.39 | Long 3 SPY (T1) | +$53.16 | +2.452% | $100,053.16 |
| Day 10 | 2026-05-14 | $746.18 | Long 3 SPY (T1) | +$70.53 | +3.253% | $100,070.53 |
| Day 11 | 2026-05-15 | $737.20 | Long 3 SPY (T1) | +$43.59 | +2.011% | $100,043.59 |
| Day 12 | 2026-05-18 | $736.50 | Long 3 SPY (T1) | +$41.49 | +1.914% | $100,041.49 |
| Day 13 | 2026-05-19 | $731.91 | Long 3 SPY (T1) | +$27.72 | +1.279% | $100,027.72 |
| Day 14 | 2026-05-20 | $739.41 | Long 3 SPY (T1) | +$50.22 | +2.316% | $100,050.22 |
| Day 15 | 2026-05-21 | $740.80 | Long 3 SPY (T1) | +$54.39 | +2.509% | $100,054.39 |
| Day 16 | 2026-05-22 | $743.75 | Long 3 SPY (T1) | +$63.24 | +2.917% | $100,063.24 |
| Day 17 | 2026-05-26 | $748.53 | Long 3 SPY (T1) | +$77.58 | +3.578% | $100,077.58 |
| Day 18 | 2026-05-27 | $748.66 | Long 3 SPY (T1) | +$77.97 | +3.596% | $100,077.97 |
| Day 19 | 2026-05-28 | $752.74 | Long 3 SPY (T1) | +$90.21 | +4.161% | $100,090.21 |
| Day 20 | 2026-05-29 | $754.40 | Long 3 SPY (T1) | +$95.19 | +4.391% | $100,095.19 |
| Day 21 | 2026-06-01 | $756.49 | Long 3 SPY (T1) | +$101.46 | +4.680% | $100,101.46 |
| Day 22 | 2026-06-02 | $757.52 | Long 3 SPY (T1) | +$104.55 | +4.822% | $100,104.55 |
| Day 23 | 2026-06-03 | $752.24 | Long 3 SPY (T1) | +$88.71 | +4.092% | $100,088.71 |
| Day 24 | 2026-06-04 | $755.03 | Long 3 SPY (T1) | +$97.08 | +4.478% | $100,097.08 |
| Day 25 | 2026-06-05 | $735.56 | Long 3 SPY (T1) | +$38.67 | +1.784% | $100,038.67 |
| Day 26 | 2026-06-08 | $737.34 | Long 3 SPY (T1) | +$44.01 | +2.030% | $100,044.01 |
| Day 27 | 2026-06-09 | $735.18 | Long 3 SPY (T1) | +$37.53 | +1.731% | $100,037.53 |
| Day 28 | 2026-06-10 | $723.72 | Long 3 SPY (T1) | +$3.15 | +0.145% | $100,003.15 |
| Day 29 | 2026-06-11 | $735.77 | Long 3 SPY (T1) | +$39.30 | +1.813% | $100,039.30 |
| Day 30 | 2026-06-12 | $739.76 | Long 3 SPY (T1) | +$51.27 | +2.365% | $100,051.27 |
| Day 31 | 2026-06-15 | $752.81 | Long 3 SPY (T1) | +$90.42 | +4.171% | $100,090.42 |
| Day 32 | 2026-06-16 | $748.65 | Long 3 SPY (T1) | +$77.94 | +3.595% | $100,077.94 |
| Day 33 | 2026-06-17 | $739.12 | FLAT | — | — | $100,063.93 |
| Day 34 | 2026-06-18 | $746.75 | FLAT | — | — | $100,063.93 |
| Day 35 | 2026-06-22 | $744.27 | FLAT | — | — | $100,062.82 |
| Day 36 | 2026-06-23 | $733.62 | FLAT | — | — | $100,062.82 |
| Day 37 | 2026-06-24 | $733.32 | FLAT | — | — | $100,062.82 |
| Day 38 | 2026-06-25 | $733.33 | FLAT | — | — | $100,062.82 |
| Day 39 | 2026-06-26 | $729.35 | FLAT | — | — | $100,062.82 |
| Day 40 | 2026-06-29 | $740.86 | FLAT | — | — | $100,062.82 |
| Day 41 | 2026-06-30 | $746.65 | FLAT | — | — | $100,062.82 |
| Day 42 | 2026-07-01 | $745.66 | FLAT | — | — | $100,062.82 |
| Day 43 | 2026-07-02 | $744.86 | FLAT | — | — | $100,062.82 |
| Day 44 | 2026-07-06 | $751.27 | FLAT | — | — | $100,062.82 |
| Day 45 | 2026-07-07 | $747.77 | FLAT | — | — | $100,062.82 |
| Day 46 | 2026-07-08 | $745.28 | FLAT | — | — | $100,062.82 |
| Day 47 | 2026-07-09 | $751.55 | FLAT | — | — | $100,062.82 |
| Day 48 | 2026-07-10 | $754.94 | FLAT | — | — | $100,062.82 |
| Day 49 | 2026-07-13 | $749.13 | FLAT | — | — | $99,901.70 |
| Day 50 | 2026-07-14 | $751.94 | FLAT | — | — | $99,866.62 |
| Day 51 | 2026-07-15 | $754.77 | FLAT | — | — | $99,914.37 |
| Day 52 | 2026-07-16 | $750.87 | FLAT | — | — | $99,738.24 |
| Day 53 | 2026-07-17 | $743.28 | FLAT | — | — | $99,595.68 |
| Day 54 | 2026-07-20 | $742.15 | FLAT | — | — | $99,403.70 |
| Day 55 | 2026-07-21 | $748.15 | Long 53 SPY (T9) | +$28.09 | +0.071% | $99,431.79 |
| Day 56 | 2026-07-22 | $747.49 | Long 53 SPY (T9) | -$6.89 | -0.017% | $99,396.81 |
| Day 57 | 2026-07-23 | $738.06 | Long 52 SPY (T10) | -$40.56 | -0.106% | $98,727.67 |
| Day 58 | 2026-07-24 | $738.90 | FLAT | — | — | $98,776.55 |
| Day 59 | 2026-07-27 | $738.85 | FLAT | — | — | $98,880.69 |
| Day 60 | 2026-07-28 | $740.79 | FLAT | — | — | $98,837.23 |
| Day 61 | 2026-07-29 | $729.57 | FLAT | — | — | $98,837.23 |
| Day 62 | 2026-07-30 | $741.63 | FLAT | — | — | $98,837.23 |
| Day 63 | 2026-07-31 | $746.79 | FLAT | — | — | $98,837.23 |
| Day 64 | 2026-08-03 | $757.72 | FLAT | — | — | $98,837.23 |
| Day 65 | 2026-08-04 | $771.11 | Long 50 SPY (T13) | -$52.00 | -0.135% | $98,785.23 |
| Day 66 | 2026-08-05 | $769.79 | FLAT | — | — | $98,750.23 |
| Day 67 | 2026-08-06 | $768.64 | FLAT | — | — | $98,750.23 |
| Day 68 | 2026-08-07 | $773.16 | Long 51 SPY (T14) | +$33.14 | +0.084% | $98,783.37 |
| Day 69 | 2026-08-10 | $773.02 | FLAT | — | — | $98,775.21 |
| Day 70 | 2026-08-11 | $770.52 | Long 51 SPY (T15) | -$159.19 | -0.403% | $98,616.02 |
| Day 71 | 2026-08-12 | $772.54 | Long 51 SPY (T15) | -$56.17 | -0.142% | $98,719.04 |
| Day 72 | 2026-08-13 | $777.84 | Long 51 SPY (T15) | +$214.13 | +0.543% | $98,989.34 |
| Day 73 | 2026-08-14 | $776.30 | Long 51 SPY (T15) | +$135.59 | +0.344% | $98,910.80 |
| Day 74 | 2026-08-17 | $772.62 | Long 51 SPY (T15) | -$52.09 | -0.132% | $98,723.12 |
| Day 75 | 2026-08-18 | $767.37 | Long 51 SPY (T15) | -$319.84 | -0.811% | $98,455.37 |
| Day 76 | 2026-08-19 | $769.09 | Long 51 SPY (T15) | -$232.12 | -0.588% | $98,543.09 |
| Day 77 | 2026-08-20 | $762.62 | Long 51 SPY (T15) | -$562.09 | -1.425% | $98,213.12 |
| Day 78 | 2026-08-21 | $765.64 | Long 51 SPY (T15) | -$408.07 | -1.034% | $98,367.14 |
| Day 79 | 2026-08-24 | $763.46 | Long 51 SPY (T15) | -$519.25 | -1.316% | $98,255.96 |
| Day 80 | 2026-08-25 | $765.79 | Long 51 SPY (T15) | -$400.42 | -1.015% | $98,374.79 |
| Day 81 | 2026-08-26 | $765.94 | Long 51 SPY (T15) | -$392.77 | -0.995% | $98,382.44 |
| Day 82 | 2026-08-27 | $771.18 | Long 51 SPY (T15) | -$125.53 | -0.318% | $98,649.68 |
| Day 83 | 2026-08-28 | $769.28 | Long 51 SPY (T15) | -$222.43 | -0.564% | $98,552.78 |
| Day 84 | 2026-08-31 | $766.87 | Long 51 SPY (T15) | -$345.34 | -0.875% | $98,429.87 |
| Day 85 | 2026-09-01 | $761.63 | FLAT | — | — | $98,162.63 |
| Day 86 | 2026-09-02 | $765.13 | Long 51 SPY (T16) | +$10.71 | +0.027% | $98,173.34 |
| Day 87 | 2026-09-03 | $773.12 | Long 51 SPY (T16) | +$418.20 | +1.072% | $98,580.83 |
| Day 88 | 2026-09-04 | $770.18 | Long 51 SPY (T16) | +$268.26 | +0.688% | $98,430.89 |
| Day 89 | 2026-09-08 | $766.06 | FLAT | — | — | $98,215.16 |
| Day 90 | 2026-09-09 | $762.42 | Long 52 SPY (T17) | -$30.11 | -0.076% | $98,185.05 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-05-01 | $99,987.91 | $99,999.98 | -0.0121% | -0.000% | **-0.012%** |
| Day 2 | 2026-05-04 | $99,980.74 | $99,667.41 | -0.0193% | -0.333% | **+0.314%** |
| Day 3 | 2026-05-05 | $99,997.54 | $100,446.65 | -0.0025% | +0.447% | **-0.450%** |
| Day 4 | 2026-05-06 | $100,027.63 | $101,842.35 | +0.0276% | +1.842% | **-1.814%** |
| Day 5 | 2026-05-07 | $100,020.94 | $101,532.04 | +0.0209% | +1.532% | **-1.511%** |
| Day 6 | 2026-05-08 | $100,038.94 | $102,366.95 | +0.0389% | +2.367% | **-2.328%** |
| Day 7 | 2026-05-11 | $100,043.89 | $102,596.55 | +0.0439% | +2.597% | **-2.553%** |
| Day 8 | 2026-05-12 | $100,040.86 | $102,456.01 | +0.0409% | +2.456% | **-2.415%** |
| Day 9 | 2026-05-13 | $100,053.16 | $103,026.53 | +0.0532% | +3.027% | **-2.974%** |
| Day 10 | 2026-05-14 | $100,070.53 | $103,832.22 | +0.0705% | +3.832% | **-3.762%** |
| Day 11 | 2026-05-15 | $100,043.59 | $102,582.63 | +0.0436% | +2.583% | **-2.539%** |
| Day 12 | 2026-05-18 | $100,041.49 | $102,485.23 | +0.0415% | +2.485% | **-2.444%** |
| Day 13 | 2026-05-19 | $100,027.72 | $101,846.52 | +0.0277% | +1.847% | **-1.819%** |
| Day 14 | 2026-05-20 | $100,050.22 | $102,890.16 | +0.0502% | +2.890% | **-2.840%** |
| Day 15 | 2026-05-21 | $100,054.39 | $103,083.58 | +0.0544% | +3.084% | **-3.030%** |
| Day 16 | 2026-05-22 | $100,063.24 | $103,494.08 | +0.0632% | +3.494% | **-3.431%** |
| Day 17 | 2026-05-26 | $100,077.58 | $104,159.22 | +0.0776% | +4.159% | **-4.081%** |
| Day 18 | 2026-05-27 | $100,077.97 | $104,177.31 | +0.0780% | +4.177% | **-4.099%** |
| Day 19 | 2026-05-28 | $100,090.21 | $104,745.05 | +0.0902% | +4.745% | **-4.655%** |
| Day 20 | 2026-05-29 | $100,095.19 | $104,976.04 | +0.0952% | +4.976% | **-4.881%** |
| Day 21 | 2026-06-01 | $100,101.46 | $105,266.87 | +0.1015% | +5.267% | **-5.166%** |
| Day 22 | 2026-06-02 | $100,104.55 | $105,410.20 | +0.1046% | +5.410% | **-5.305%** |
| Day 23 | 2026-06-03 | $100,088.71 | $104,675.47 | +0.0887% | +4.675% | **-4.586%** |
| Day 24 | 2026-06-04 | $100,097.08 | $105,063.71 | +0.0971% | +5.064% | **-4.967%** |
| Day 25 | 2026-06-05 | $100,038.67 | $102,354.42 | +0.0387% | +2.354% | **-2.315%** |
| Day 26 | 2026-06-08 | $100,044.01 | $102,602.11 | +0.0440% | +2.602% | **-2.558%** |
| Day 27 | 2026-06-09 | $100,037.53 | $102,301.55 | +0.0375% | +2.302% | **-2.264%** |
| Day 28 | 2026-06-10 | $100,003.15 | $100,706.87 | +0.0031% | +0.707% | **-0.704%** |
| Day 29 | 2026-06-11 | $100,039.30 | $102,383.65 | +0.0393% | +2.384% | **-2.345%** |
| Day 30 | 2026-06-12 | $100,051.27 | $102,938.86 | +0.0513% | +2.939% | **-2.888%** |
| Day 31 | 2026-06-15 | $100,090.42 | $104,754.79 | +0.0904% | +4.755% | **-4.665%** |
| Day 32 | 2026-06-16 | $100,077.94 | $104,175.92 | +0.0779% | +4.176% | **-4.098%** |
| Day 33 | 2026-06-17 | $100,063.93 | $102,849.80 | +0.0639% | +2.850% | **-2.786%** |
| Day 34 | 2026-06-18 | $100,063.93 | $103,911.53 | +0.0639% | +3.912% | **-3.848%** |
| Day 35 | 2026-06-22 | $100,062.82 | $103,566.44 | +0.0628% | +3.566% | **-3.503%** |
| Day 36 | 2026-06-23 | $100,062.82 | $102,084.47 | +0.0628% | +2.084% | **-2.021%** |
| Day 37 | 2026-06-24 | $100,062.82 | $102,042.72 | +0.0628% | +2.043% | **-1.980%** |
| Day 38 | 2026-06-25 | $100,062.82 | $102,044.12 | +0.0628% | +2.044% | **-1.981%** |
| Day 39 | 2026-06-26 | $100,062.82 | $101,490.29 | +0.0628% | +1.490% | **-1.427%** |
| Day 40 | 2026-06-29 | $100,062.82 | $103,091.93 | +0.0628% | +3.092% | **-3.029%** |
| Day 41 | 2026-06-30 | $100,062.82 | $103,897.62 | +0.0628% | +3.898% | **-3.835%** |
| Day 42 | 2026-07-01 | $100,062.82 | $103,759.86 | +0.0628% | +3.760% | **-3.697%** |
| Day 43 | 2026-07-02 | $100,062.82 | $103,648.54 | +0.0628% | +3.649% | **-3.586%** |
| Day 44 | 2026-07-06 | $100,062.82 | $104,540.50 | +0.0628% | +4.540% | **-4.477%** |
| Day 45 | 2026-07-07 | $100,062.82 | $104,053.47 | +0.0628% | +4.053% | **-3.990%** |
| Day 46 | 2026-07-08 | $100,062.82 | $103,706.98 | +0.0628% | +3.707% | **-3.644%** |
| Day 47 | 2026-07-09 | $100,062.82 | $104,579.46 | +0.0628% | +4.579% | **-4.516%** |
| Day 48 | 2026-07-10 | $100,062.82 | $105,051.18 | +0.0628% | +5.051% | **-4.988%** |
| Day 49 | 2026-07-13 | $99,901.70 | $104,242.71 | -0.0983% | +4.243% | **-4.341%** |
| Day 50 | 2026-07-14 | $99,866.62 | $104,633.73 | -0.1334% | +4.634% | **-4.767%** |
| Day 51 | 2026-07-15 | $99,914.37 | $105,027.53 | -0.0856% | +5.028% | **-5.114%** |
| Day 52 | 2026-07-16 | $99,738.24 | $104,484.84 | -0.2618% | +4.485% | **-4.747%** |
| Day 53 | 2026-07-17 | $99,595.68 | $103,428.68 | -0.4043% | +3.429% | **-3.833%** |
| Day 54 | 2026-07-20 | $99,403.70 | $103,271.43 | -0.5963% | +3.271% | **-3.867%** |
| Day 55 | 2026-07-21 | $99,431.79 | $104,106.34 | -0.5682% | +4.106% | **-4.674%** |
| Day 56 | 2026-07-22 | $99,396.81 | $104,014.50 | -0.6032% | +4.014% | **-4.617%** |
| Day 57 | 2026-07-23 | $98,727.67 | $102,702.30 | -1.2723% | +2.702% | **-3.974%** |
| Day 58 | 2026-07-24 | $98,776.55 | $102,819.19 | -1.2234% | +2.819% | **-4.042%** |
| Day 59 | 2026-07-27 | $98,880.69 | $102,812.23 | -1.1193% | +2.812% | **-3.931%** |
| Day 60 | 2026-07-28 | $98,837.23 | $103,082.19 | -1.1628% | +3.082% | **-4.245%** |
| Day 61 | 2026-07-29 | $98,837.23 | $101,520.91 | -1.1628% | +1.521% | **-2.684%** |
| Day 62 | 2026-07-30 | $98,837.23 | $103,199.08 | -1.1628% | +3.199% | **-4.362%** |
| Day 63 | 2026-07-31 | $98,837.23 | $103,917.10 | -1.1628% | +3.917% | **-5.080%** |
| Day 64 | 2026-08-03 | $98,837.23 | $105,438.03 | -1.1628% | +5.438% | **-6.601%** |
| Day 65 | 2026-08-04 | $98,785.23 | $107,301.27 | -1.2148% | +7.301% | **-8.516%** |
| Day 66 | 2026-08-05 | $98,750.23 | $107,117.59 | -1.2498% | +7.118% | **-8.368%** |
| Day 67 | 2026-08-06 | $98,750.23 | $106,957.56 | -1.2498% | +6.958% | **-8.208%** |
| Day 68 | 2026-08-07 | $98,783.37 | $107,586.53 | -1.2166% | +7.587% | **-8.804%** |
| Day 69 | 2026-08-10 | $98,775.21 | $107,567.05 | -1.2248% | +7.567% | **-8.792%** |
| Day 70 | 2026-08-11 | $98,616.02 | $107,219.17 | -1.3840% | +7.219% | **-8.603%** |
| Day 71 | 2026-08-12 | $98,719.04 | $107,500.25 | -1.2810% | +7.500% | **-8.781%** |
| Day 72 | 2026-08-13 | $98,989.34 | $108,237.76 | -1.0107% | +8.238% | **-9.249%** |
| Day 73 | 2026-08-14 | $98,910.80 | $108,023.46 | -1.0892% | +8.023% | **-9.112%** |
| Day 74 | 2026-08-17 | $98,723.12 | $107,511.39 | -1.2769% | +7.511% | **-8.788%** |
| Day 75 | 2026-08-18 | $98,455.37 | $106,780.84 | -1.5446% | +6.781% | **-8.326%** |
| Day 76 | 2026-08-19 | $98,543.09 | $107,020.18 | -1.4569% | +7.020% | **-8.477%** |
| Day 77 | 2026-08-20 | $98,213.12 | $106,119.87 | -1.7869% | +6.120% | **-7.907%** |
| Day 78 | 2026-08-21 | $98,367.14 | $106,540.11 | -1.6329% | +6.540% | **-8.173%** |
| Day 79 | 2026-08-24 | $98,255.96 | $106,236.76 | -1.7440% | +6.237% | **-7.981%** |
| Day 80 | 2026-08-25 | $98,374.79 | $106,560.98 | -1.6252% | +6.561% | **-8.186%** |
| Day 81 | 2026-08-26 | $98,382.44 | $106,581.85 | -1.6176% | +6.582% | **-8.200%** |
| Day 82 | 2026-08-27 | $98,649.68 | $107,311.01 | -1.3503% | +7.311% | **-8.661%** |
| Day 83 | 2026-08-28 | $98,552.78 | $107,046.62 | -1.4472% | +7.047% | **-8.494%** |
| Day 84 | 2026-08-31 | $98,429.87 | $106,711.26 | -1.5701% | +6.711% | **-8.281%** |
| Day 85 | 2026-09-01 | $98,162.63 | $105,982.11 | -1.8374% | +5.982% | **-7.819%** |
| Day 86 | 2026-09-02 | $98,173.34 | $106,469.14 | -1.8267% | +6.469% | **-8.296%** |
| Day 87 | 2026-09-03 | $98,580.83 | $107,580.96 | -1.4192% | +7.581% | **-9.000%** |
| Day 88 | 2026-09-04 | $98,430.89 | $107,171.86 | -1.5691% | +7.172% | **-8.741%** |
| Day 89 | 2026-09-08 | $98,215.16 | $106,598.55 | -1.7848% | +6.599% | **-8.384%** |
| Day 90 | 2026-09-09 | $98,185.05 | $106,092.04 | -1.8149% | +6.092% | **-7.907%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-05-01 | $718.64 | -$12.09 | -$1772.75 | Position open |
| Day 2 | 2026-05-04 | $716.25 | -$19.26 | -$1765.58 | Position open |
| Day 3 | 2026-05-05 | $721.85 | -$2.46 | -$1782.38 | Position open |
| Day 4 | 2026-05-06 | $731.88 | +$27.63 | -$1812.47 | Position open |
| Day 5 | 2026-05-07 | $729.65 | +$20.94 | -$1805.78 | Position open |
| Day 6 | 2026-05-08 | $735.65 | +$38.94 | -$1823.78 | Position open |
| Day 7 | 2026-05-11 | $737.30 | +$43.89 | -$1828.73 | Position open |
| Day 8 | 2026-05-12 | $736.29 | +$40.86 | -$1825.70 | Position open |
| Day 9 | 2026-05-13 | $740.39 | +$53.16 | -$1838.00 | Position open |
| Day 10 | 2026-05-14 | $746.18 | +$70.53 | -$1855.37 | Position open |
| Day 11 | 2026-05-15 | $737.20 | +$43.59 | -$1828.43 | Position open |
| Day 12 | 2026-05-18 | $736.50 | +$41.49 | -$1826.33 | Position open |
| Day 13 | 2026-05-19 | $731.91 | +$27.72 | -$1812.56 | Position open |
| Day 14 | 2026-05-20 | $739.41 | +$50.22 | -$1835.06 | Position open |
| Day 15 | 2026-05-21 | $740.80 | +$54.39 | -$1839.23 | Position open |
| Day 16 | 2026-05-22 | $743.75 | +$63.24 | -$1848.08 | Position open |
| Day 17 | 2026-05-26 | $748.53 | +$77.58 | -$1862.42 | Position open |
| Day 18 | 2026-05-27 | $748.66 | +$77.97 | -$1862.81 | Position open |
| Day 19 | 2026-05-28 | $752.74 | +$90.21 | -$1875.05 | Position open |
| Day 20 | 2026-05-29 | $754.40 | +$95.19 | -$1880.03 | Position open |
| Day 21 | 2026-06-01 | $756.49 | +$101.46 | -$1886.30 | Position open |
| Day 22 | 2026-06-02 | $757.52 | +$104.55 | -$1889.39 | Position open |
| Day 23 | 2026-06-03 | $752.24 | +$88.71 | -$1873.55 | Position open |
| Day 24 | 2026-06-04 | $755.03 | +$97.08 | -$1881.92 | Position open |
| Day 25 | 2026-06-05 | $735.56 | +$38.67 | -$1823.51 | Position open |
| Day 26 | 2026-06-08 | $737.34 | +$44.01 | -$1828.85 | Position open |
| Day 27 | 2026-06-09 | $735.18 | +$37.53 | -$1822.37 | Position open |
| Day 28 | 2026-06-10 | $723.72 | +$3.15 | -$1787.99 | Position open |
| Day 29 | 2026-06-11 | $735.77 | +$39.30 | -$1824.14 | Position open |
| Day 30 | 2026-06-12 | $739.76 | +$51.27 | -$1836.11 | Position open |
| Day 31 | 2026-06-15 | $752.81 | +$90.42 | -$1875.26 | Position open |
| Day 32 | 2026-06-16 | $748.65 | +$77.94 | -$1862.78 | Position open |
| Day 33 | 2026-06-17 | $739.12 | +$49.35 | -$1834.19 | Holding would have been **$1834.19** better — honest entry |
| Day 34 | 2026-06-18 | $746.75 | +$72.24 | -$1857.08 | Holding would have been **$1857.08** better — honest entry |
| Day 35 | 2026-06-22 | $744.27 | +$64.80 | -$1849.64 | Holding would have been **$1849.64** better — honest entry |
| Day 36 | 2026-06-23 | $733.62 | +$32.85 | -$1817.69 | Holding would have been **$1817.69** better — honest entry |
| Day 37 | 2026-06-24 | $733.32 | +$31.95 | -$1816.79 | Holding would have been **$1816.79** better — honest entry |
| Day 38 | 2026-06-25 | $733.33 | +$31.98 | -$1816.82 | Holding would have been **$1816.82** better — honest entry |
| Day 39 | 2026-06-26 | $729.35 | +$20.04 | -$1804.88 | Holding would have been **$1804.88** better — honest entry |
| Day 40 | 2026-06-29 | $740.86 | +$54.57 | -$1839.41 | Holding would have been **$1839.41** better — honest entry |
| Day 41 | 2026-06-30 | $746.65 | +$71.94 | -$1856.78 | Holding would have been **$1856.78** better — honest entry |
| Day 42 | 2026-07-01 | $745.66 | +$68.97 | -$1853.81 | Holding would have been **$1853.81** better — honest entry |
| Day 43 | 2026-07-02 | $744.86 | +$66.57 | -$1851.41 | Holding would have been **$1851.41** better — honest entry |
| Day 44 | 2026-07-06 | $751.27 | +$85.80 | -$1870.64 | Holding would have been **$1870.64** better — honest entry |
| Day 45 | 2026-07-07 | $747.77 | +$75.30 | -$1860.14 | Holding would have been **$1860.14** better — honest entry |
| Day 46 | 2026-07-08 | $745.28 | +$67.83 | -$1852.67 | Holding would have been **$1852.67** better — honest entry |
| Day 47 | 2026-07-09 | $751.55 | +$86.64 | -$1871.48 | Holding would have been **$1871.48** better — honest entry |
| Day 48 | 2026-07-10 | $754.94 | +$96.81 | -$1881.65 | Holding would have been **$1881.65** better — honest entry |
| Day 49 | 2026-07-13 | $749.13 | +$79.38 | -$1864.22 | Holding would have been **$1864.22** better — honest entry |
| Day 50 | 2026-07-14 | $751.94 | +$87.81 | -$1872.65 | Holding would have been **$1872.65** better — honest entry |
| Day 51 | 2026-07-15 | $754.77 | +$96.30 | -$1881.14 | Holding would have been **$1881.14** better — honest entry |
| Day 52 | 2026-07-16 | $750.87 | +$84.60 | -$1869.44 | Holding would have been **$1869.44** better — honest entry |
| Day 53 | 2026-07-17 | $743.28 | +$61.83 | -$1846.67 | Holding would have been **$1846.67** better — honest entry |
| Day 54 | 2026-07-20 | $742.15 | +$58.44 | -$1843.28 | Holding would have been **$1843.28** better — honest entry |
| Day 55 | 2026-07-21 | $748.15 | +$76.44 | -$1861.28 | Position open |
| Day 56 | 2026-07-22 | $747.49 | +$74.46 | -$1859.30 | Position open |
| Day 57 | 2026-07-23 | $738.06 | +$46.17 | -$1831.01 | Position open |
| Day 58 | 2026-07-24 | $738.90 | +$48.69 | -$1833.53 | Holding would have been **$1833.53** better — honest entry |
| Day 59 | 2026-07-27 | $738.85 | +$48.54 | -$1833.38 | Holding would have been **$1833.38** better — honest entry |
| Day 60 | 2026-07-28 | $740.79 | +$54.36 | -$1839.20 | Holding would have been **$1839.20** better — honest entry |
| Day 61 | 2026-07-29 | $729.57 | +$20.70 | -$1805.54 | Holding would have been **$1805.54** better — honest entry |
| Day 62 | 2026-07-30 | $741.63 | +$56.88 | -$1841.72 | Holding would have been **$1841.72** better — honest entry |
| Day 63 | 2026-07-31 | $746.79 | +$72.36 | -$1857.20 | Holding would have been **$1857.20** better — honest entry |
| Day 64 | 2026-08-03 | $757.72 | +$105.15 | -$1889.99 | Holding would have been **$1889.99** better — honest entry |
| Day 65 | 2026-08-04 | $771.11 | +$145.32 | -$1930.16 | Position open |
| Day 66 | 2026-08-05 | $769.79 | +$141.36 | -$1926.20 | Holding would have been **$1926.20** better — honest entry |
| Day 67 | 2026-08-06 | $768.64 | +$137.91 | -$1922.75 | Holding would have been **$1922.75** better — honest entry |
| Day 68 | 2026-08-07 | $773.16 | +$151.47 | -$1936.31 | Position open |
| Day 69 | 2026-08-10 | $773.02 | +$151.05 | -$1935.89 | Holding would have been **$1935.89** better — honest entry |
| Day 70 | 2026-08-11 | $770.52 | +$143.55 | -$1928.39 | Position open |
| Day 71 | 2026-08-12 | $772.54 | +$149.61 | -$1934.45 | Position open |
| Day 72 | 2026-08-13 | $777.84 | +$165.51 | -$1950.35 | Position open |
| Day 73 | 2026-08-14 | $776.30 | +$160.89 | -$1945.73 | Position open |
| Day 74 | 2026-08-17 | $772.62 | +$149.85 | -$1934.69 | Position open |
| Day 75 | 2026-08-18 | $767.37 | +$134.10 | -$1918.94 | Position open |
| Day 76 | 2026-08-19 | $769.09 | +$139.26 | -$1924.10 | Position open |
| Day 77 | 2026-08-20 | $762.62 | +$119.85 | -$1904.69 | Position open |
| Day 78 | 2026-08-21 | $765.64 | +$128.91 | -$1913.75 | Position open |
| Day 79 | 2026-08-24 | $763.46 | +$122.37 | -$1907.21 | Position open |
| Day 80 | 2026-08-25 | $765.79 | +$129.36 | -$1914.20 | Position open |
| Day 81 | 2026-08-26 | $765.94 | +$129.81 | -$1914.65 | Position open |
| Day 82 | 2026-08-27 | $771.18 | +$145.53 | -$1930.37 | Position open |
| Day 83 | 2026-08-28 | $769.28 | +$139.83 | -$1924.67 | Position open |
| Day 84 | 2026-08-31 | $766.87 | +$132.60 | -$1917.44 | Position open |
| Day 85 | 2026-09-01 | $761.63 | +$116.88 | -$1901.72 | Holding would have been **$1901.72** better — honest entry |
| Day 86 | 2026-09-02 | $765.13 | +$127.38 | -$1912.22 | Position open |
| Day 87 | 2026-09-03 | $773.12 | +$151.35 | -$1936.19 | Position open |
| Day 88 | 2026-09-04 | $770.18 | +$142.53 | -$1927.37 | Position open |
| Day 89 | 2026-09-08 | $766.06 | +$130.17 | -$1915.01 | Holding would have been **$1915.01** better — honest entry |
| Day 90 | 2026-09-09 | $762.42 | +$119.25 | -$1904.09 | Position open |

---

## Daily Entries

### Day 1 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $718.64 |
| Unrealized P&L | -$12.09 |
| P&L % | -0.558% |
| Portfolio value | $99,987.91 |
| Benchmark value | $99,999.98 |
| Alpha (cumulative) | -0.012% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 2 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $716.25 |
| Unrealized P&L | -$19.26 |
| P&L % | -0.888% |
| Portfolio value | $99,980.74 |
| Benchmark value | $99,667.41 |
| Alpha (cumulative) | +0.314% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 3 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $721.85 |
| Unrealized P&L | -$2.46 |
| P&L % | -0.113% |
| Portfolio value | $99,997.54 |
| Benchmark value | $100,446.65 |
| Alpha (cumulative) | -0.450% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 4 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $731.88 |
| Unrealized P&L | +$27.63 |
| P&L % | +1.274% |
| Portfolio value | $100,027.63 |
| Benchmark value | $101,842.35 |
| Alpha (cumulative) | -1.814% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 5 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $729.65 |
| Unrealized P&L | +$20.94 |
| P&L % | +0.966% |
| Portfolio value | $100,020.94 |
| Benchmark value | $101,532.04 |
| Alpha (cumulative) | -1.511% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 6 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.65 |
| Unrealized P&L | +$38.94 |
| P&L % | +1.796% |
| Portfolio value | $100,038.94 |
| Benchmark value | $102,366.95 |
| Alpha (cumulative) | -2.328% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 7 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $737.30 |
| Unrealized P&L | +$43.89 |
| P&L % | +2.024% |
| Portfolio value | $100,043.89 |
| Benchmark value | $102,596.55 |
| Alpha (cumulative) | -2.553% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 8 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $736.29 |
| Unrealized P&L | +$40.86 |
| P&L % | +1.885% |
| Portfolio value | $100,040.86 |
| Benchmark value | $102,456.01 |
| Alpha (cumulative) | -2.415% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 9 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.39 |
| Unrealized P&L | +$53.16 |
| P&L % | +2.452% |
| Portfolio value | $100,053.16 |
| Benchmark value | $103,026.53 |
| Alpha (cumulative) | -2.974% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 10 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.18 |
| Unrealized P&L | +$70.53 |
| P&L % | +3.253% |
| Portfolio value | $100,070.53 |
| Benchmark value | $103,832.22 |
| Alpha (cumulative) | -3.762% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 11 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $737.20 |
| Unrealized P&L | +$43.59 |
| P&L % | +2.011% |
| Portfolio value | $100,043.59 |
| Benchmark value | $102,582.63 |
| Alpha (cumulative) | -2.539% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 12 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $736.50 |
| Unrealized P&L | +$41.49 |
| P&L % | +1.914% |
| Portfolio value | $100,041.49 |
| Benchmark value | $102,485.23 |
| Alpha (cumulative) | -2.444% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 13 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $731.91 |
| Unrealized P&L | +$27.72 |
| P&L % | +1.279% |
| Portfolio value | $100,027.72 |
| Benchmark value | $101,846.52 |
| Alpha (cumulative) | -1.819% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 14 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $739.41 |
| Unrealized P&L | +$50.22 |
| P&L % | +2.316% |
| Portfolio value | $100,050.22 |
| Benchmark value | $102,890.16 |
| Alpha (cumulative) | -2.840% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 15 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.80 |
| Unrealized P&L | +$54.39 |
| P&L % | +2.509% |
| Portfolio value | $100,054.39 |
| Benchmark value | $103,083.58 |
| Alpha (cumulative) | -3.030% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 16 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $743.75 |
| Unrealized P&L | +$63.24 |
| P&L % | +2.917% |
| Portfolio value | $100,063.24 |
| Benchmark value | $103,494.08 |
| Alpha (cumulative) | -3.431% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 17 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.53 |
| Unrealized P&L | +$77.58 |
| P&L % | +3.578% |
| Portfolio value | $100,077.58 |
| Benchmark value | $104,159.22 |
| Alpha (cumulative) | -4.081% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 18 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.66 |
| Unrealized P&L | +$77.97 |
| P&L % | +3.596% |
| Portfolio value | $100,077.97 |
| Benchmark value | $104,177.31 |
| Alpha (cumulative) | -4.099% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 19 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $752.74 |
| Unrealized P&L | +$90.21 |
| P&L % | +4.161% |
| Portfolio value | $100,090.21 |
| Benchmark value | $104,745.05 |
| Alpha (cumulative) | -4.655% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 20 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $754.40 |
| Unrealized P&L | +$95.19 |
| P&L % | +4.391% |
| Portfolio value | $100,095.19 |
| Benchmark value | $104,976.04 |
| Alpha (cumulative) | -4.881% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 21 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $756.49 |
| Unrealized P&L | +$101.46 |
| P&L % | +4.680% |
| Portfolio value | $100,101.46 |
| Benchmark value | $105,266.87 |
| Alpha (cumulative) | -5.166% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 22 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $757.52 |
| Unrealized P&L | +$104.55 |
| P&L % | +4.822% |
| Portfolio value | $100,104.55 |
| Benchmark value | $105,410.20 |
| Alpha (cumulative) | -5.305% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 23 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $752.24 |
| Unrealized P&L | +$88.71 |
| P&L % | +4.092% |
| Portfolio value | $100,088.71 |
| Benchmark value | $104,675.47 |
| Alpha (cumulative) | -4.586% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 24 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $755.03 |
| Unrealized P&L | +$97.08 |
| P&L % | +4.478% |
| Portfolio value | $100,097.08 |
| Benchmark value | $105,063.71 |
| Alpha (cumulative) | -4.967% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 25 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.56 |
| Unrealized P&L | +$38.67 |
| P&L % | +1.784% |
| Portfolio value | $100,038.67 |
| Benchmark value | $102,354.42 |
| Alpha (cumulative) | -2.315% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 26 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $737.34 |
| Unrealized P&L | +$44.01 |
| P&L % | +2.030% |
| Portfolio value | $100,044.01 |
| Benchmark value | $102,602.11 |
| Alpha (cumulative) | -2.558% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 27 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.18 |
| Unrealized P&L | +$37.53 |
| P&L % | +1.731% |
| Portfolio value | $100,037.53 |
| Benchmark value | $102,301.55 |
| Alpha (cumulative) | -2.264% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 28 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $723.72 |
| Unrealized P&L | +$3.15 |
| P&L % | +0.145% |
| Portfolio value | $100,003.15 |
| Benchmark value | $100,706.87 |
| Alpha (cumulative) | -0.704% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 29 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.77 |
| Unrealized P&L | +$39.30 |
| P&L % | +1.813% |
| Portfolio value | $100,039.30 |
| Benchmark value | $102,383.65 |
| Alpha (cumulative) | -2.345% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 30 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $739.76 |
| Unrealized P&L | +$51.27 |
| P&L % | +2.365% |
| Portfolio value | $100,051.27 |
| Benchmark value | $102,938.86 |
| Alpha (cumulative) | -2.888% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 31 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $752.81 |
| Unrealized P&L | +$90.42 |
| P&L % | +4.171% |
| Portfolio value | $100,090.42 |
| Benchmark value | $104,754.79 |
| Alpha (cumulative) | -4.665% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 32 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 3 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.65 |
| Unrealized P&L | +$77.94 |
| P&L % | +3.595% |
| Portfolio value | $100,077.94 |
| Benchmark value | $104,175.92 |
| Alpha (cumulative) | -4.098% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 33 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $739.12 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$49.35 |
| Signal saved | -$1834.19 |
| Portfolio value | $100,063.93 |
| Benchmark value | $102,849.80 |
| Alpha (cumulative) | -2.786% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 34 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.75 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$72.24 |
| Signal saved | -$1857.08 |
| Portfolio value | $100,063.93 |
| Benchmark value | $103,911.53 |
| Alpha (cumulative) | -3.848% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 35 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $744.27 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$64.80 |
| Signal saved | -$1849.64 |
| Portfolio value | $100,062.82 |
| Benchmark value | $103,566.44 |
| Alpha (cumulative) | -3.503% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 36 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $733.62 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$32.85 |
| Signal saved | -$1817.69 |
| Portfolio value | $100,062.82 |
| Benchmark value | $102,084.47 |
| Alpha (cumulative) | -2.021% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 37 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $733.32 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$31.95 |
| Signal saved | -$1816.79 |
| Portfolio value | $100,062.82 |
| Benchmark value | $102,042.72 |
| Alpha (cumulative) | -1.980% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 38 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $733.33 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$31.98 |
| Signal saved | -$1816.82 |
| Portfolio value | $100,062.82 |
| Benchmark value | $102,044.12 |
| Alpha (cumulative) | -1.981% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 39 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $729.35 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$20.04 |
| Signal saved | -$1804.88 |
| Portfolio value | $100,062.82 |
| Benchmark value | $101,490.29 |
| Alpha (cumulative) | -1.427% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 40 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.86 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$54.57 |
| Signal saved | -$1839.41 |
| Portfolio value | $100,062.82 |
| Benchmark value | $103,091.93 |
| Alpha (cumulative) | -3.029% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 41 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.65 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$71.94 |
| Signal saved | -$1856.78 |
| Portfolio value | $100,062.82 |
| Benchmark value | $103,897.62 |
| Alpha (cumulative) | -3.835% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 42 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $745.66 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$68.97 |
| Signal saved | -$1853.81 |
| Portfolio value | $100,062.82 |
| Benchmark value | $103,759.86 |
| Alpha (cumulative) | -3.697% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 43 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $744.86 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$66.57 |
| Signal saved | -$1851.41 |
| Portfolio value | $100,062.82 |
| Benchmark value | $103,648.54 |
| Alpha (cumulative) | -3.586% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 44 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $751.27 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$85.80 |
| Signal saved | -$1870.64 |
| Portfolio value | $100,062.82 |
| Benchmark value | $104,540.50 |
| Alpha (cumulative) | -4.477% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 45 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $747.77 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$75.30 |
| Signal saved | -$1860.14 |
| Portfolio value | $100,062.82 |
| Benchmark value | $104,053.47 |
| Alpha (cumulative) | -3.990% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 46 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $745.28 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$67.83 |
| Signal saved | -$1852.67 |
| Portfolio value | $100,062.82 |
| Benchmark value | $103,706.98 |
| Alpha (cumulative) | -3.644% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 47 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $751.55 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$86.64 |
| Signal saved | -$1871.48 |
| Portfolio value | $100,062.82 |
| Benchmark value | $104,579.46 |
| Alpha (cumulative) | -4.516% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 48 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $754.94 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$96.81 |
| Signal saved | -$1881.65 |
| Portfolio value | $100,062.82 |
| Benchmark value | $105,051.18 |
| Alpha (cumulative) | -4.988% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 49 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $749.13 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$79.38 |
| Signal saved | -$1864.22 |
| Portfolio value | $99,901.70 |
| Benchmark value | $104,242.71 |
| Alpha (cumulative) | -4.341% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 50 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $751.94 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$87.81 |
| Signal saved | -$1872.65 |
| Portfolio value | $99,866.62 |
| Benchmark value | $104,633.73 |
| Alpha (cumulative) | -4.767% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 51 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $754.77 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$96.30 |
| Signal saved | -$1881.14 |
| Portfolio value | $99,914.37 |
| Benchmark value | $105,027.53 |
| Alpha (cumulative) | -5.114% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 52 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $750.87 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$84.60 |
| Signal saved | -$1869.44 |
| Portfolio value | $99,738.24 |
| Benchmark value | $104,484.84 |
| Alpha (cumulative) | -4.747% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 53 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $743.28 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$61.83 |
| Signal saved | -$1846.67 |
| Portfolio value | $99,595.68 |
| Benchmark value | $103,428.68 |
| Alpha (cumulative) | -3.833% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 54 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $742.15 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$58.44 |
| Signal saved | -$1843.28 |
| Portfolio value | $99,403.70 |
| Benchmark value | $103,271.43 |
| Alpha (cumulative) | -3.867% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 55 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T9) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $99,431.79 |
| Benchmark value | $104,106.34 |
| Alpha (cumulative) | -4.674% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 56 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T9) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $99,396.81 |
| Benchmark value | $104,014.50 |
| Alpha (cumulative) | -4.617% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 57 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T10) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $98,727.67 |
| Benchmark value | $102,702.30 |
| Alpha (cumulative) | -3.974% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 58 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $738.90 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$48.69 |
| Signal saved | -$1833.53 |
| Portfolio value | $98,776.55 |
| Benchmark value | $102,819.19 |
| Alpha (cumulative) | -4.042% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 59 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $738.85 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$48.54 |
| Signal saved | -$1833.38 |
| Portfolio value | $98,880.69 |
| Benchmark value | $102,812.23 |
| Alpha (cumulative) | -3.931% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 60 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.79 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$54.36 |
| Signal saved | -$1839.20 |
| Portfolio value | $98,837.23 |
| Benchmark value | $103,082.19 |
| Alpha (cumulative) | -4.245% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 61 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $729.57 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$20.70 |
| Signal saved | -$1805.54 |
| Portfolio value | $98,837.23 |
| Benchmark value | $101,520.91 |
| Alpha (cumulative) | -2.684% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 62 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $741.63 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$56.88 |
| Signal saved | -$1841.72 |
| Portfolio value | $98,837.23 |
| Benchmark value | $103,199.08 |
| Alpha (cumulative) | -4.362% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 63 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.79 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$72.36 |
| Signal saved | -$1857.20 |
| Portfolio value | $98,837.23 |
| Benchmark value | $103,917.10 |
| Alpha (cumulative) | -5.080% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 64 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $757.72 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$105.15 |
| Signal saved | -$1889.99 |
| Portfolio value | $98,837.23 |
| Benchmark value | $105,438.03 |
| Alpha (cumulative) | -6.601% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 65 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T13) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $771.11 |
| Unrealized P&L | -$52.00 |
| P&L % | -0.135% |
| Portfolio value | $98,785.23 |
| Benchmark value | $107,301.27 |
| Alpha (cumulative) | -8.516% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 66 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $769.79 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$141.36 |
| Signal saved | -$1926.20 |
| Portfolio value | $98,750.23 |
| Benchmark value | $107,117.59 |
| Alpha (cumulative) | -8.368% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 67 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $768.64 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$137.91 |
| Signal saved | -$1922.75 |
| Portfolio value | $98,750.23 |
| Benchmark value | $106,957.56 |
| Alpha (cumulative) | -8.208% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 68 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $773.16 |
| Unrealized P&L | +$33.14 |
| P&L % | +0.084% |
| Portfolio value | $98,783.37 |
| Benchmark value | $107,586.53 |
| Alpha (cumulative) | -8.804% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.08% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 69 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $773.02 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$151.05 |
| Signal saved | -$1935.89 |
| Portfolio value | $98,775.21 |
| Benchmark value | $107,567.05 |
| Alpha (cumulative) | -8.792% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 70 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $770.52 |
| Unrealized P&L | -$159.19 |
| P&L % | -0.403% |
| Portfolio value | $98,616.02 |
| Benchmark value | $107,219.17 |
| Alpha (cumulative) | -8.603% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.40% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 71 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $772.54 |
| Unrealized P&L | -$56.17 |
| P&L % | -0.142% |
| Portfolio value | $98,719.04 |
| Benchmark value | $107,500.25 |
| Alpha (cumulative) | -8.781% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 72 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $777.84 |
| Unrealized P&L | +$214.13 |
| P&L % | +0.543% |
| Portfolio value | $98,989.34 |
| Benchmark value | $108,237.76 |
| Alpha (cumulative) | -9.249% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.54% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 73 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $776.30 |
| Unrealized P&L | +$135.59 |
| P&L % | +0.344% |
| Portfolio value | $98,910.80 |
| Benchmark value | $108,023.46 |
| Alpha (cumulative) | -9.112% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.34% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 74 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $772.62 |
| Unrealized P&L | -$52.09 |
| P&L % | -0.132% |
| Portfolio value | $98,723.12 |
| Benchmark value | $107,511.39 |
| Alpha (cumulative) | -8.788% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.13% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 75 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,455.37 |
| Benchmark value | $106,780.84 |
| Alpha (cumulative) | -8.326% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 76 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $769.09 |
| Unrealized P&L | -$232.12 |
| P&L % | -0.588% |
| Portfolio value | $98,543.09 |
| Benchmark value | $107,020.18 |
| Alpha (cumulative) | -8.477% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.59% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 77 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $762.62 |
| Unrealized P&L | -$562.09 |
| P&L % | -1.425% |
| Portfolio value | $98,213.12 |
| Benchmark value | $106,119.87 |
| Alpha (cumulative) | -7.907% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -1.43% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 78 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $765.64 |
| Unrealized P&L | -$408.07 |
| P&L % | -1.034% |
| Portfolio value | $98,367.14 |
| Benchmark value | $106,540.11 |
| Alpha (cumulative) | -8.173% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -1.03% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 79 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $763.46 |
| Unrealized P&L | -$519.25 |
| P&L % | -1.316% |
| Portfolio value | $98,255.96 |
| Benchmark value | $106,236.76 |
| Alpha (cumulative) | -7.981% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -1.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 80 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $765.79 |
| Unrealized P&L | -$400.42 |
| P&L % | -1.015% |
| Portfolio value | $98,374.79 |
| Benchmark value | $106,560.98 |
| Alpha (cumulative) | -8.186% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -1.01% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 81 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $765.94 |
| Unrealized P&L | -$392.77 |
| P&L % | -0.995% |
| Portfolio value | $98,382.44 |
| Benchmark value | $106,581.85 |
| Alpha (cumulative) | -8.200% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.99% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 82 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $771.18 |
| Unrealized P&L | -$125.53 |
| P&L % | -0.318% |
| Portfolio value | $98,649.68 |
| Benchmark value | $107,311.01 |
| Alpha (cumulative) | -8.661% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 83 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $769.28 |
| Unrealized P&L | -$222.43 |
| P&L % | -0.564% |
| Portfolio value | $98,552.78 |
| Benchmark value | $107,046.62 |
| Alpha (cumulative) | -8.494% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 84 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $766.87 |
| Unrealized P&L | -$345.34 |
| P&L % | -0.875% |
| Portfolio value | $98,429.87 |
| Benchmark value | $106,711.26 |
| Alpha (cumulative) | -8.281% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.88% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 85 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $761.63 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$116.88 |
| Signal saved | -$1901.72 |
| Portfolio value | $98,162.63 |
| Benchmark value | $105,982.11 |
| Alpha (cumulative) | -7.819% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 86 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $765.13 |
| Unrealized P&L | +$10.71 |
| P&L % | +0.027% |
| Portfolio value | $98,173.34 |
| Benchmark value | $106,469.14 |
| Alpha (cumulative) | -8.296% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.03% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 87 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $773.12 |
| Unrealized P&L | +$418.20 |
| P&L % | +1.072% |
| Portfolio value | $98,580.83 |
| Benchmark value | $107,580.96 |
| Alpha (cumulative) | -9.000% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +1.07% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 88 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $770.18 |
| Unrealized P&L | +$268.26 |
| P&L % | +0.688% |
| Portfolio value | $98,430.89 |
| Benchmark value | $107,171.86 |
| Alpha (cumulative) | -8.741% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: +0.69% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 89 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $766.06 |
| Realized P&L (locked) | -$1784.84 |
| Reference if held | +$130.17 |
| Signal saved | -$1915.01 |
| Portfolio value | $98,215.16 |
| Benchmark value | $106,598.55 |
| Alpha (cumulative) | -8.384% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-1784.84. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 90 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T17) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $762.42 |
| Unrealized P&L | -$30.11 |
| P&L % | -0.076% |
| Portfolio value | $98,185.05 |
| Benchmark value | $106,092.04 |
| Alpha (cumulative) | -7.907% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $768.29 vs MA50 $758.02). Momentum: WEAK. Unrealized P&L: -0.08% from entry. No exit triggered.

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
_Day 90 of 90 · Alpaca equity: $99,323.13 · Cumulative alpha vs SPY: -7.907%_