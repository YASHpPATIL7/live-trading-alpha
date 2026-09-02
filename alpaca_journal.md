# ALPACA PAPER JOURNAL — SPY
_Last updated: September 02, 2026 | Day 86 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$722.670/share**
> (2026-05-01, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-09-02): **BULLISH**  
> Fast: MA10 $766.21 | MA30 $761.19  
> Slow: MA20 $769.21 | MA50 $754.71  
> Regime: **BULL** | Momentum: **RECOVERING** | Session: REGULAR

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

**Total trades:** 15 | **Closed:** 15 | **Open:** No | **Cumulative Realized P&L:** -$729.23

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 55 | +$1172.07 | ✅ Closed |
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

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,287.39 |
| Alpaca cash | $96,227.83 |
| Cumulative realized P&L | -$729.23 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-05-01 | $718.64 | Long 55 SPY (T1) | -$221.63 | -0.558% | $99,778.37 |
| Day 2 | 2026-05-04 | $716.25 | Long 55 SPY (T1) | -$353.08 | -0.888% | $99,646.92 |
| Day 3 | 2026-05-05 | $721.85 | Long 55 SPY (T1) | -$45.08 | -0.113% | $99,954.92 |
| Day 4 | 2026-05-06 | $731.88 | Long 55 SPY (T1) | +$506.57 | +1.274% | $100,506.57 |
| Day 5 | 2026-05-07 | $729.65 | Long 55 SPY (T1) | +$383.92 | +0.966% | $100,383.92 |
| Day 6 | 2026-05-08 | $735.65 | Long 55 SPY (T1) | +$713.92 | +1.796% | $100,713.92 |
| Day 7 | 2026-05-11 | $737.30 | Long 55 SPY (T1) | +$804.67 | +2.024% | $100,804.67 |
| Day 8 | 2026-05-12 | $736.29 | Long 55 SPY (T1) | +$749.12 | +1.885% | $100,749.12 |
| Day 9 | 2026-05-13 | $740.39 | Long 55 SPY (T1) | +$974.62 | +2.452% | $100,974.62 |
| Day 10 | 2026-05-14 | $746.18 | Long 55 SPY (T1) | +$1293.07 | +3.253% | $101,293.07 |
| Day 11 | 2026-05-15 | $737.20 | Long 55 SPY (T1) | +$799.17 | +2.011% | $100,799.17 |
| Day 12 | 2026-05-18 | $736.50 | Long 55 SPY (T1) | +$760.67 | +1.914% | $100,760.67 |
| Day 13 | 2026-05-19 | $731.91 | Long 55 SPY (T1) | +$508.22 | +1.279% | $100,508.22 |
| Day 14 | 2026-05-20 | $739.41 | Long 55 SPY (T1) | +$920.72 | +2.316% | $100,920.72 |
| Day 15 | 2026-05-21 | $740.80 | Long 55 SPY (T1) | +$997.17 | +2.509% | $100,997.17 |
| Day 16 | 2026-05-22 | $743.75 | Long 55 SPY (T1) | +$1159.42 | +2.917% | $101,159.42 |
| Day 17 | 2026-05-26 | $748.53 | Long 55 SPY (T1) | +$1422.32 | +3.578% | $101,422.32 |
| Day 18 | 2026-05-27 | $748.66 | Long 55 SPY (T1) | +$1429.47 | +3.596% | $101,429.47 |
| Day 19 | 2026-05-28 | $752.74 | Long 55 SPY (T1) | +$1653.87 | +4.161% | $101,653.87 |
| Day 20 | 2026-05-29 | $754.40 | Long 55 SPY (T1) | +$1745.17 | +4.391% | $101,745.17 |
| Day 21 | 2026-06-01 | $756.49 | Long 55 SPY (T1) | +$1860.12 | +4.680% | $101,860.12 |
| Day 22 | 2026-06-02 | $757.52 | Long 55 SPY (T1) | +$1916.77 | +4.822% | $101,916.77 |
| Day 23 | 2026-06-03 | $752.24 | Long 55 SPY (T1) | +$1626.37 | +4.092% | $101,626.37 |
| Day 24 | 2026-06-04 | $755.03 | Long 55 SPY (T1) | +$1779.82 | +4.478% | $101,779.82 |
| Day 25 | 2026-06-05 | $735.56 | Long 55 SPY (T1) | +$708.97 | +1.784% | $100,708.97 |
| Day 26 | 2026-06-08 | $737.34 | Long 55 SPY (T1) | +$806.87 | +2.030% | $100,806.87 |
| Day 27 | 2026-06-09 | $735.18 | Long 55 SPY (T1) | +$688.07 | +1.731% | $100,688.07 |
| Day 28 | 2026-06-10 | $723.72 | Long 55 SPY (T1) | +$57.77 | +0.145% | $100,057.77 |
| Day 29 | 2026-06-11 | $735.77 | Long 55 SPY (T1) | +$720.52 | +1.813% | $100,720.52 |
| Day 30 | 2026-06-12 | $739.76 | Long 55 SPY (T1) | +$939.97 | +2.365% | $100,939.97 |
| Day 31 | 2026-06-15 | $752.81 | Long 55 SPY (T1) | +$1657.72 | +4.171% | $101,657.72 |
| Day 32 | 2026-06-16 | $748.65 | Long 55 SPY (T1) | +$1428.92 | +3.595% | $101,428.92 |
| Day 33 | 2026-06-17 | $739.12 | FLAT | — | — | $101,172.07 |
| Day 34 | 2026-06-18 | $746.75 | FLAT | — | — | $101,172.07 |
| Day 35 | 2026-06-22 | $744.27 | FLAT | — | — | $101,170.96 |
| Day 36 | 2026-06-23 | $733.62 | FLAT | — | — | $101,170.96 |
| Day 37 | 2026-06-24 | $733.32 | FLAT | — | — | $101,170.96 |
| Day 38 | 2026-06-25 | $733.33 | FLAT | — | — | $101,170.96 |
| Day 39 | 2026-06-26 | $729.35 | FLAT | — | — | $101,170.96 |
| Day 40 | 2026-06-29 | $740.86 | FLAT | — | — | $101,170.96 |
| Day 41 | 2026-06-30 | $746.65 | FLAT | — | — | $101,170.96 |
| Day 42 | 2026-07-01 | $745.66 | FLAT | — | — | $101,170.96 |
| Day 43 | 2026-07-02 | $744.86 | FLAT | — | — | $101,170.96 |
| Day 44 | 2026-07-06 | $751.27 | FLAT | — | — | $101,170.96 |
| Day 45 | 2026-07-07 | $747.77 | FLAT | — | — | $101,170.96 |
| Day 46 | 2026-07-08 | $745.28 | FLAT | — | — | $101,170.96 |
| Day 47 | 2026-07-09 | $751.55 | FLAT | — | — | $101,170.96 |
| Day 48 | 2026-07-10 | $754.94 | FLAT | — | — | $101,170.96 |
| Day 49 | 2026-07-13 | $749.13 | FLAT | — | — | $101,009.84 |
| Day 50 | 2026-07-14 | $751.94 | FLAT | — | — | $100,974.76 |
| Day 51 | 2026-07-15 | $754.77 | FLAT | — | — | $101,022.51 |
| Day 52 | 2026-07-16 | $750.87 | FLAT | — | — | $100,846.38 |
| Day 53 | 2026-07-17 | $743.28 | FLAT | — | — | $100,703.82 |
| Day 54 | 2026-07-20 | $742.15 | FLAT | — | — | $100,511.84 |
| Day 55 | 2026-07-21 | $748.15 | Long 53 SPY (T9) | +$28.09 | +0.071% | $100,539.93 |
| Day 56 | 2026-07-22 | $747.49 | Long 53 SPY (T9) | -$6.89 | -0.017% | $100,504.95 |
| Day 57 | 2026-07-23 | $738.06 | Long 52 SPY (T10) | -$40.56 | -0.106% | $99,835.81 |
| Day 58 | 2026-07-24 | $738.90 | FLAT | — | — | $99,884.69 |
| Day 59 | 2026-07-27 | $738.85 | FLAT | — | — | $99,988.83 |
| Day 60 | 2026-07-28 | $740.79 | FLAT | — | — | $99,945.37 |
| Day 61 | 2026-07-29 | $729.57 | FLAT | — | — | $99,945.37 |
| Day 62 | 2026-07-30 | $741.63 | FLAT | — | — | $99,945.37 |
| Day 63 | 2026-07-31 | $746.79 | FLAT | — | — | $99,945.37 |
| Day 64 | 2026-08-03 | $757.72 | FLAT | — | — | $99,945.37 |
| Day 65 | 2026-08-04 | $771.11 | Long 50 SPY (T13) | -$52.00 | -0.135% | $99,893.37 |
| Day 66 | 2026-08-05 | $769.79 | FLAT | — | — | $99,858.37 |
| Day 67 | 2026-08-06 | $768.64 | FLAT | — | — | $99,858.37 |
| Day 68 | 2026-08-07 | $773.16 | Long 51 SPY (T14) | +$33.14 | +0.084% | $99,891.51 |
| Day 69 | 2026-08-10 | $773.02 | FLAT | — | — | $99,883.35 |
| Day 70 | 2026-08-11 | $770.52 | Long 51 SPY (T15) | -$159.19 | -0.403% | $99,724.16 |
| Day 71 | 2026-08-12 | $772.54 | Long 51 SPY (T15) | -$56.17 | -0.142% | $99,827.18 |
| Day 72 | 2026-08-13 | $777.84 | Long 51 SPY (T15) | +$214.13 | +0.543% | $100,097.48 |
| Day 73 | 2026-08-14 | $776.30 | Long 51 SPY (T15) | +$135.59 | +0.344% | $100,018.94 |
| Day 74 | 2026-08-17 | $772.62 | Long 51 SPY (T15) | -$52.09 | -0.132% | $99,831.26 |
| Day 75 | 2026-08-18 | $767.37 | Long 51 SPY (T15) | -$319.84 | -0.811% | $99,563.51 |
| Day 76 | 2026-08-19 | $769.09 | Long 51 SPY (T15) | -$232.12 | -0.588% | $99,651.23 |
| Day 77 | 2026-08-20 | $762.62 | Long 51 SPY (T15) | -$562.09 | -1.425% | $99,321.26 |
| Day 78 | 2026-08-21 | $765.64 | Long 51 SPY (T15) | -$408.07 | -1.034% | $99,475.28 |
| Day 79 | 2026-08-24 | $763.46 | Long 51 SPY (T15) | -$519.25 | -1.316% | $99,364.10 |
| Day 80 | 2026-08-25 | $765.79 | Long 51 SPY (T15) | -$400.42 | -1.015% | $99,482.93 |
| Day 81 | 2026-08-26 | $765.94 | Long 51 SPY (T15) | -$392.77 | -0.995% | $99,490.58 |
| Day 82 | 2026-08-27 | $771.18 | Long 51 SPY (T15) | -$125.53 | -0.318% | $99,757.82 |
| Day 83 | 2026-08-28 | $769.28 | Long 51 SPY (T15) | -$222.43 | -0.564% | $99,660.92 |
| Day 84 | 2026-08-31 | $766.87 | Long 51 SPY (T15) | -$345.34 | -0.875% | $99,538.01 |
| Day 85 | 2026-09-01 | $761.63 | FLAT | — | — | $99,270.77 |
| Day 86 | 2026-09-02 | $764.95 | FLAT | — | — | $99,270.77 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-05-01 | $99,778.37 | $99,999.98 | -0.2216% | -0.000% | **-0.222%** |
| Day 2 | 2026-05-04 | $99,646.92 | $99,667.41 | -0.3531% | -0.333% | **-0.020%** |
| Day 3 | 2026-05-05 | $99,954.92 | $100,446.65 | -0.0451% | +0.447% | **-0.492%** |
| Day 4 | 2026-05-06 | $100,506.57 | $101,842.35 | +0.5066% | +1.842% | **-1.335%** |
| Day 5 | 2026-05-07 | $100,383.92 | $101,532.04 | +0.3839% | +1.532% | **-1.148%** |
| Day 6 | 2026-05-08 | $100,713.92 | $102,366.95 | +0.7139% | +2.367% | **-1.653%** |
| Day 7 | 2026-05-11 | $100,804.67 | $102,596.55 | +0.8047% | +2.597% | **-1.792%** |
| Day 8 | 2026-05-12 | $100,749.12 | $102,456.01 | +0.7491% | +2.456% | **-1.707%** |
| Day 9 | 2026-05-13 | $100,974.62 | $103,026.53 | +0.9746% | +3.027% | **-2.052%** |
| Day 10 | 2026-05-14 | $101,293.07 | $103,832.22 | +1.2931% | +3.832% | **-2.539%** |
| Day 11 | 2026-05-15 | $100,799.17 | $102,582.63 | +0.7992% | +2.583% | **-1.784%** |
| Day 12 | 2026-05-18 | $100,760.67 | $102,485.23 | +0.7607% | +2.485% | **-1.724%** |
| Day 13 | 2026-05-19 | $100,508.22 | $101,846.52 | +0.5082% | +1.847% | **-1.339%** |
| Day 14 | 2026-05-20 | $100,920.72 | $102,890.16 | +0.9207% | +2.890% | **-1.969%** |
| Day 15 | 2026-05-21 | $100,997.17 | $103,083.58 | +0.9972% | +3.084% | **-2.087%** |
| Day 16 | 2026-05-22 | $101,159.42 | $103,494.08 | +1.1594% | +3.494% | **-2.335%** |
| Day 17 | 2026-05-26 | $101,422.32 | $104,159.22 | +1.4223% | +4.159% | **-2.737%** |
| Day 18 | 2026-05-27 | $101,429.47 | $104,177.31 | +1.4295% | +4.177% | **-2.747%** |
| Day 19 | 2026-05-28 | $101,653.87 | $104,745.05 | +1.6539% | +4.745% | **-3.091%** |
| Day 20 | 2026-05-29 | $101,745.17 | $104,976.04 | +1.7452% | +4.976% | **-3.231%** |
| Day 21 | 2026-06-01 | $101,860.12 | $105,266.87 | +1.8601% | +5.267% | **-3.407%** |
| Day 22 | 2026-06-02 | $101,916.77 | $105,410.20 | +1.9168% | +5.410% | **-3.493%** |
| Day 23 | 2026-06-03 | $101,626.37 | $104,675.47 | +1.6264% | +4.675% | **-3.049%** |
| Day 24 | 2026-06-04 | $101,779.82 | $105,063.71 | +1.7798% | +5.064% | **-3.284%** |
| Day 25 | 2026-06-05 | $100,708.97 | $102,354.42 | +0.7090% | +2.354% | **-1.645%** |
| Day 26 | 2026-06-08 | $100,806.87 | $102,602.11 | +0.8069% | +2.602% | **-1.795%** |
| Day 27 | 2026-06-09 | $100,688.07 | $102,301.55 | +0.6881% | +2.302% | **-1.614%** |
| Day 28 | 2026-06-10 | $100,057.77 | $100,706.87 | +0.0578% | +0.707% | **-0.649%** |
| Day 29 | 2026-06-11 | $100,720.52 | $102,383.65 | +0.7205% | +2.384% | **-1.664%** |
| Day 30 | 2026-06-12 | $100,939.97 | $102,938.86 | +0.9400% | +2.939% | **-1.999%** |
| Day 31 | 2026-06-15 | $101,657.72 | $104,754.79 | +1.6577% | +4.755% | **-3.097%** |
| Day 32 | 2026-06-16 | $101,428.92 | $104,175.92 | +1.4289% | +4.176% | **-2.747%** |
| Day 33 | 2026-06-17 | $101,172.07 | $102,849.80 | +1.1721% | +2.850% | **-1.678%** |
| Day 34 | 2026-06-18 | $101,172.07 | $103,911.53 | +1.1721% | +3.912% | **-2.740%** |
| Day 35 | 2026-06-22 | $101,170.96 | $103,566.44 | +1.1710% | +3.566% | **-2.395%** |
| Day 36 | 2026-06-23 | $101,170.96 | $102,084.47 | +1.1710% | +2.084% | **-0.913%** |
| Day 37 | 2026-06-24 | $101,170.96 | $102,042.72 | +1.1710% | +2.043% | **-0.872%** |
| Day 38 | 2026-06-25 | $101,170.96 | $102,044.12 | +1.1710% | +2.044% | **-0.873%** |
| Day 39 | 2026-06-26 | $101,170.96 | $101,490.29 | +1.1710% | +1.490% | **-0.319%** |
| Day 40 | 2026-06-29 | $101,170.96 | $103,091.93 | +1.1710% | +3.092% | **-1.921%** |
| Day 41 | 2026-06-30 | $101,170.96 | $103,897.62 | +1.1710% | +3.898% | **-2.727%** |
| Day 42 | 2026-07-01 | $101,170.96 | $103,759.86 | +1.1710% | +3.760% | **-2.589%** |
| Day 43 | 2026-07-02 | $101,170.96 | $103,648.54 | +1.1710% | +3.649% | **-2.478%** |
| Day 44 | 2026-07-06 | $101,170.96 | $104,540.50 | +1.1710% | +4.540% | **-3.369%** |
| Day 45 | 2026-07-07 | $101,170.96 | $104,053.47 | +1.1710% | +4.053% | **-2.882%** |
| Day 46 | 2026-07-08 | $101,170.96 | $103,706.98 | +1.1710% | +3.707% | **-2.536%** |
| Day 47 | 2026-07-09 | $101,170.96 | $104,579.46 | +1.1710% | +4.579% | **-3.408%** |
| Day 48 | 2026-07-10 | $101,170.96 | $105,051.18 | +1.1710% | +5.051% | **-3.880%** |
| Day 49 | 2026-07-13 | $101,009.84 | $104,242.71 | +1.0098% | +4.243% | **-3.233%** |
| Day 50 | 2026-07-14 | $100,974.76 | $104,633.73 | +0.9748% | +4.634% | **-3.659%** |
| Day 51 | 2026-07-15 | $101,022.51 | $105,027.53 | +1.0225% | +5.028% | **-4.005%** |
| Day 52 | 2026-07-16 | $100,846.38 | $104,484.84 | +0.8464% | +4.485% | **-3.639%** |
| Day 53 | 2026-07-17 | $100,703.82 | $103,428.68 | +0.7038% | +3.429% | **-2.725%** |
| Day 54 | 2026-07-20 | $100,511.84 | $103,271.43 | +0.5118% | +3.271% | **-2.759%** |
| Day 55 | 2026-07-21 | $100,539.93 | $104,106.34 | +0.5399% | +4.106% | **-3.566%** |
| Day 56 | 2026-07-22 | $100,504.95 | $104,014.50 | +0.5049% | +4.014% | **-3.509%** |
| Day 57 | 2026-07-23 | $99,835.81 | $102,702.30 | -0.1642% | +2.702% | **-2.866%** |
| Day 58 | 2026-07-24 | $99,884.69 | $102,819.19 | -0.1153% | +2.819% | **-2.934%** |
| Day 59 | 2026-07-27 | $99,988.83 | $102,812.23 | -0.0112% | +2.812% | **-2.823%** |
| Day 60 | 2026-07-28 | $99,945.37 | $103,082.19 | -0.0546% | +3.082% | **-3.137%** |
| Day 61 | 2026-07-29 | $99,945.37 | $101,520.91 | -0.0546% | +1.521% | **-1.576%** |
| Day 62 | 2026-07-30 | $99,945.37 | $103,199.08 | -0.0546% | +3.199% | **-3.254%** |
| Day 63 | 2026-07-31 | $99,945.37 | $103,917.10 | -0.0546% | +3.917% | **-3.972%** |
| Day 64 | 2026-08-03 | $99,945.37 | $105,438.03 | -0.0546% | +5.438% | **-5.493%** |
| Day 65 | 2026-08-04 | $99,893.37 | $107,301.27 | -0.1066% | +7.301% | **-7.408%** |
| Day 66 | 2026-08-05 | $99,858.37 | $107,117.59 | -0.1416% | +7.118% | **-7.260%** |
| Day 67 | 2026-08-06 | $99,858.37 | $106,957.56 | -0.1416% | +6.958% | **-7.100%** |
| Day 68 | 2026-08-07 | $99,891.51 | $107,586.53 | -0.1085% | +7.587% | **-7.696%** |
| Day 69 | 2026-08-10 | $99,883.35 | $107,567.05 | -0.1166% | +7.567% | **-7.684%** |
| Day 70 | 2026-08-11 | $99,724.16 | $107,219.17 | -0.2758% | +7.219% | **-7.495%** |
| Day 71 | 2026-08-12 | $99,827.18 | $107,500.25 | -0.1728% | +7.500% | **-7.673%** |
| Day 72 | 2026-08-13 | $100,097.48 | $108,237.76 | +0.0975% | +8.238% | **-8.140%** |
| Day 73 | 2026-08-14 | $100,018.94 | $108,023.46 | +0.0189% | +8.023% | **-8.004%** |
| Day 74 | 2026-08-17 | $99,831.26 | $107,511.39 | -0.1687% | +7.511% | **-7.680%** |
| Day 75 | 2026-08-18 | $99,563.51 | $106,780.84 | -0.4365% | +6.781% | **-7.217%** |
| Day 76 | 2026-08-19 | $99,651.23 | $107,020.18 | -0.3488% | +7.020% | **-7.369%** |
| Day 77 | 2026-08-20 | $99,321.26 | $106,119.87 | -0.6787% | +6.120% | **-6.799%** |
| Day 78 | 2026-08-21 | $99,475.28 | $106,540.11 | -0.5247% | +6.540% | **-7.065%** |
| Day 79 | 2026-08-24 | $99,364.10 | $106,236.76 | -0.6359% | +6.237% | **-6.873%** |
| Day 80 | 2026-08-25 | $99,482.93 | $106,560.98 | -0.5171% | +6.561% | **-7.078%** |
| Day 81 | 2026-08-26 | $99,490.58 | $106,581.85 | -0.5094% | +6.582% | **-7.091%** |
| Day 82 | 2026-08-27 | $99,757.82 | $107,311.01 | -0.2422% | +7.311% | **-7.553%** |
| Day 83 | 2026-08-28 | $99,660.92 | $107,046.62 | -0.3391% | +7.047% | **-7.386%** |
| Day 84 | 2026-08-31 | $99,538.01 | $106,711.26 | -0.4620% | +6.711% | **-7.173%** |
| Day 85 | 2026-09-01 | $99,270.77 | $105,982.11 | -0.7292% | +5.982% | **-6.711%** |
| Day 86 | 2026-09-02 | $99,270.77 | $106,444.09 | -0.7292% | +6.444% | **-7.173%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-05-01 | $718.64 | -$221.63 | -$507.60 | Position open |
| Day 2 | 2026-05-04 | $716.25 | -$353.08 | -$376.15 | Position open |
| Day 3 | 2026-05-05 | $721.85 | -$45.08 | -$684.15 | Position open |
| Day 4 | 2026-05-06 | $731.88 | +$506.57 | -$1235.80 | Position open |
| Day 5 | 2026-05-07 | $729.65 | +$383.92 | -$1113.15 | Position open |
| Day 6 | 2026-05-08 | $735.65 | +$713.92 | -$1443.15 | Position open |
| Day 7 | 2026-05-11 | $737.30 | +$804.67 | -$1533.90 | Position open |
| Day 8 | 2026-05-12 | $736.29 | +$749.12 | -$1478.35 | Position open |
| Day 9 | 2026-05-13 | $740.39 | +$974.62 | -$1703.85 | Position open |
| Day 10 | 2026-05-14 | $746.18 | +$1293.07 | -$2022.30 | Position open |
| Day 11 | 2026-05-15 | $737.20 | +$799.17 | -$1528.40 | Position open |
| Day 12 | 2026-05-18 | $736.50 | +$760.67 | -$1489.90 | Position open |
| Day 13 | 2026-05-19 | $731.91 | +$508.22 | -$1237.45 | Position open |
| Day 14 | 2026-05-20 | $739.41 | +$920.72 | -$1649.95 | Position open |
| Day 15 | 2026-05-21 | $740.80 | +$997.17 | -$1726.40 | Position open |
| Day 16 | 2026-05-22 | $743.75 | +$1159.42 | -$1888.65 | Position open |
| Day 17 | 2026-05-26 | $748.53 | +$1422.32 | -$2151.55 | Position open |
| Day 18 | 2026-05-27 | $748.66 | +$1429.47 | -$2158.70 | Position open |
| Day 19 | 2026-05-28 | $752.74 | +$1653.87 | -$2383.10 | Position open |
| Day 20 | 2026-05-29 | $754.40 | +$1745.17 | -$2474.40 | Position open |
| Day 21 | 2026-06-01 | $756.49 | +$1860.12 | -$2589.35 | Position open |
| Day 22 | 2026-06-02 | $757.52 | +$1916.77 | -$2646.00 | Position open |
| Day 23 | 2026-06-03 | $752.24 | +$1626.37 | -$2355.60 | Position open |
| Day 24 | 2026-06-04 | $755.03 | +$1779.82 | -$2509.05 | Position open |
| Day 25 | 2026-06-05 | $735.56 | +$708.97 | -$1438.20 | Position open |
| Day 26 | 2026-06-08 | $737.34 | +$806.87 | -$1536.10 | Position open |
| Day 27 | 2026-06-09 | $735.18 | +$688.07 | -$1417.30 | Position open |
| Day 28 | 2026-06-10 | $723.72 | +$57.77 | -$787.00 | Position open |
| Day 29 | 2026-06-11 | $735.77 | +$720.52 | -$1449.75 | Position open |
| Day 30 | 2026-06-12 | $739.76 | +$939.97 | -$1669.20 | Position open |
| Day 31 | 2026-06-15 | $752.81 | +$1657.72 | -$2386.95 | Position open |
| Day 32 | 2026-06-16 | $748.65 | +$1428.92 | -$2158.15 | Position open |
| Day 33 | 2026-06-17 | $739.12 | +$904.77 | -$1634.00 | Holding would have been **$1634.00** better — honest entry |
| Day 34 | 2026-06-18 | $746.75 | +$1324.42 | -$2053.65 | Holding would have been **$2053.65** better — honest entry |
| Day 35 | 2026-06-22 | $744.27 | +$1188.02 | -$1917.25 | Holding would have been **$1917.25** better — honest entry |
| Day 36 | 2026-06-23 | $733.62 | +$602.27 | -$1331.50 | Holding would have been **$1331.50** better — honest entry |
| Day 37 | 2026-06-24 | $733.32 | +$585.77 | -$1315.00 | Holding would have been **$1315.00** better — honest entry |
| Day 38 | 2026-06-25 | $733.33 | +$586.32 | -$1315.55 | Holding would have been **$1315.55** better — honest entry |
| Day 39 | 2026-06-26 | $729.35 | +$367.42 | -$1096.65 | Holding would have been **$1096.65** better — honest entry |
| Day 40 | 2026-06-29 | $740.86 | +$1000.47 | -$1729.70 | Holding would have been **$1729.70** better — honest entry |
| Day 41 | 2026-06-30 | $746.65 | +$1318.92 | -$2048.15 | Holding would have been **$2048.15** better — honest entry |
| Day 42 | 2026-07-01 | $745.66 | +$1264.47 | -$1993.70 | Holding would have been **$1993.70** better — honest entry |
| Day 43 | 2026-07-02 | $744.86 | +$1220.47 | -$1949.70 | Holding would have been **$1949.70** better — honest entry |
| Day 44 | 2026-07-06 | $751.27 | +$1573.02 | -$2302.25 | Holding would have been **$2302.25** better — honest entry |
| Day 45 | 2026-07-07 | $747.77 | +$1380.52 | -$2109.75 | Holding would have been **$2109.75** better — honest entry |
| Day 46 | 2026-07-08 | $745.28 | +$1243.57 | -$1972.80 | Holding would have been **$1972.80** better — honest entry |
| Day 47 | 2026-07-09 | $751.55 | +$1588.42 | -$2317.65 | Holding would have been **$2317.65** better — honest entry |
| Day 48 | 2026-07-10 | $754.94 | +$1774.87 | -$2504.10 | Holding would have been **$2504.10** better — honest entry |
| Day 49 | 2026-07-13 | $749.13 | +$1455.32 | -$2184.55 | Holding would have been **$2184.55** better — honest entry |
| Day 50 | 2026-07-14 | $751.94 | +$1609.87 | -$2339.10 | Holding would have been **$2339.10** better — honest entry |
| Day 51 | 2026-07-15 | $754.77 | +$1765.52 | -$2494.75 | Holding would have been **$2494.75** better — honest entry |
| Day 52 | 2026-07-16 | $750.87 | +$1551.02 | -$2280.25 | Holding would have been **$2280.25** better — honest entry |
| Day 53 | 2026-07-17 | $743.28 | +$1133.57 | -$1862.80 | Holding would have been **$1862.80** better — honest entry |
| Day 54 | 2026-07-20 | $742.15 | +$1071.42 | -$1800.65 | Holding would have been **$1800.65** better — honest entry |
| Day 55 | 2026-07-21 | $748.15 | +$1401.42 | -$2130.65 | Position open |
| Day 56 | 2026-07-22 | $747.49 | +$1365.12 | -$2094.35 | Position open |
| Day 57 | 2026-07-23 | $738.06 | +$846.47 | -$1575.70 | Position open |
| Day 58 | 2026-07-24 | $738.90 | +$892.67 | -$1621.90 | Holding would have been **$1621.90** better — honest entry |
| Day 59 | 2026-07-27 | $738.85 | +$889.92 | -$1619.15 | Holding would have been **$1619.15** better — honest entry |
| Day 60 | 2026-07-28 | $740.79 | +$996.62 | -$1725.85 | Holding would have been **$1725.85** better — honest entry |
| Day 61 | 2026-07-29 | $729.57 | +$379.52 | -$1108.75 | Holding would have been **$1108.75** better — honest entry |
| Day 62 | 2026-07-30 | $741.63 | +$1042.82 | -$1772.05 | Holding would have been **$1772.05** better — honest entry |
| Day 63 | 2026-07-31 | $746.79 | +$1326.62 | -$2055.85 | Holding would have been **$2055.85** better — honest entry |
| Day 64 | 2026-08-03 | $757.72 | +$1927.77 | -$2657.00 | Holding would have been **$2657.00** better — honest entry |
| Day 65 | 2026-08-04 | $771.11 | +$2664.22 | -$3393.45 | Position open |
| Day 66 | 2026-08-05 | $769.79 | +$2591.62 | -$3320.85 | Holding would have been **$3320.85** better — honest entry |
| Day 67 | 2026-08-06 | $768.64 | +$2528.37 | -$3257.60 | Holding would have been **$3257.60** better — honest entry |
| Day 68 | 2026-08-07 | $773.16 | +$2776.97 | -$3506.20 | Position open |
| Day 69 | 2026-08-10 | $773.02 | +$2769.27 | -$3498.50 | Holding would have been **$3498.50** better — honest entry |
| Day 70 | 2026-08-11 | $770.52 | +$2631.77 | -$3361.00 | Position open |
| Day 71 | 2026-08-12 | $772.54 | +$2742.87 | -$3472.10 | Position open |
| Day 72 | 2026-08-13 | $777.84 | +$3034.37 | -$3763.60 | Position open |
| Day 73 | 2026-08-14 | $776.30 | +$2949.67 | -$3678.90 | Position open |
| Day 74 | 2026-08-17 | $772.62 | +$2747.27 | -$3476.50 | Position open |
| Day 75 | 2026-08-18 | $767.37 | +$2458.52 | -$3187.75 | Position open |
| Day 76 | 2026-08-19 | $769.09 | +$2553.12 | -$3282.35 | Position open |
| Day 77 | 2026-08-20 | $762.62 | +$2197.27 | -$2926.50 | Position open |
| Day 78 | 2026-08-21 | $765.64 | +$2363.37 | -$3092.60 | Position open |
| Day 79 | 2026-08-24 | $763.46 | +$2243.47 | -$2972.70 | Position open |
| Day 80 | 2026-08-25 | $765.79 | +$2371.62 | -$3100.85 | Position open |
| Day 81 | 2026-08-26 | $765.94 | +$2379.87 | -$3109.10 | Position open |
| Day 82 | 2026-08-27 | $771.18 | +$2668.07 | -$3397.30 | Position open |
| Day 83 | 2026-08-28 | $769.28 | +$2563.57 | -$3292.80 | Position open |
| Day 84 | 2026-08-31 | $766.87 | +$2431.02 | -$3160.25 | Position open |
| Day 85 | 2026-09-01 | $761.63 | +$2142.82 | -$2872.05 | Holding would have been **$2872.05** better — honest entry |
| Day 86 | 2026-09-02 | $764.95 | +$2325.42 | -$3054.65 | Holding would have been **$3054.65** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,778.37 |
| Benchmark value | $99,999.98 |
| Alpha (cumulative) | -0.222% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 2 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,646.92 |
| Benchmark value | $99,667.41 |
| Alpha (cumulative) | -0.020% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 3 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $99,954.92 |
| Benchmark value | $100,446.65 |
| Alpha (cumulative) | -0.492% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 4 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,506.57 |
| Benchmark value | $101,842.35 |
| Alpha (cumulative) | -1.335% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 5 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,383.92 |
| Benchmark value | $101,532.04 |
| Alpha (cumulative) | -1.148% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 6 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,713.92 |
| Benchmark value | $102,366.95 |
| Alpha (cumulative) | -1.653% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 7 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,804.67 |
| Benchmark value | $102,596.55 |
| Alpha (cumulative) | -1.792% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 8 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,749.12 |
| Benchmark value | $102,456.01 |
| Alpha (cumulative) | -1.707% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 9 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $100,974.62 |
| Benchmark value | $103,026.53 |
| Alpha (cumulative) | -2.052% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 10 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,293.07 |
| Benchmark value | $103,832.22 |
| Alpha (cumulative) | -2.539% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 11 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,799.17 |
| Benchmark value | $102,582.63 |
| Alpha (cumulative) | -1.784% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 12 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,760.67 |
| Benchmark value | $102,485.23 |
| Alpha (cumulative) | -1.724% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 13 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,508.22 |
| Benchmark value | $101,846.52 |
| Alpha (cumulative) | -1.339% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 14 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $100,920.72 |
| Benchmark value | $102,890.16 |
| Alpha (cumulative) | -1.969% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 15 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $100,997.17 |
| Benchmark value | $103,083.58 |
| Alpha (cumulative) | -2.087% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 16 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,159.42 |
| Benchmark value | $103,494.08 |
| Alpha (cumulative) | -2.335% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 17 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,422.32 |
| Benchmark value | $104,159.22 |
| Alpha (cumulative) | -2.737% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 18 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,429.47 |
| Benchmark value | $104,177.31 |
| Alpha (cumulative) | -2.747% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 19 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,653.87 |
| Benchmark value | $104,745.05 |
| Alpha (cumulative) | -3.091% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 20 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,745.17 |
| Benchmark value | $104,976.04 |
| Alpha (cumulative) | -3.231% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 21 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $101,860.12 |
| Benchmark value | $105,266.87 |
| Alpha (cumulative) | -3.407% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 22 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $101,916.77 |
| Benchmark value | $105,410.20 |
| Alpha (cumulative) | -3.493% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 23 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,626.37 |
| Benchmark value | $104,675.47 |
| Alpha (cumulative) | -3.049% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 24 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,779.82 |
| Benchmark value | $105,063.71 |
| Alpha (cumulative) | -3.284% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 25 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,708.97 |
| Benchmark value | $102,354.42 |
| Alpha (cumulative) | -1.645% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 26 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,806.87 |
| Benchmark value | $102,602.11 |
| Alpha (cumulative) | -1.795% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 27 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,688.07 |
| Benchmark value | $102,301.55 |
| Alpha (cumulative) | -1.614% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 28 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,057.77 |
| Benchmark value | $100,706.87 |
| Alpha (cumulative) | -0.649% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 29 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,720.52 |
| Benchmark value | $102,383.65 |
| Alpha (cumulative) | -1.664% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 30 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $100,939.97 |
| Benchmark value | $102,938.86 |
| Alpha (cumulative) | -1.999% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 31 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,657.72 |
| Benchmark value | $104,754.79 |
| Alpha (cumulative) | -3.097% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 32 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T1) |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,428.92 |
| Benchmark value | $104,175.92 |
| Alpha (cumulative) | -2.747% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 33 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $739.12 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$904.77 |
| Signal saved | -$1634.00 |
| Portfolio value | $101,172.07 |
| Benchmark value | $102,849.80 |
| Alpha (cumulative) | -1.678% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 34 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.75 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1324.42 |
| Signal saved | -$2053.65 |
| Portfolio value | $101,172.07 |
| Benchmark value | $103,911.53 |
| Alpha (cumulative) | -2.740% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 35 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $744.27 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1188.02 |
| Signal saved | -$1917.25 |
| Portfolio value | $101,170.96 |
| Benchmark value | $103,566.44 |
| Alpha (cumulative) | -2.395% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 36 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $733.62 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$602.27 |
| Signal saved | -$1331.50 |
| Portfolio value | $101,170.96 |
| Benchmark value | $102,084.47 |
| Alpha (cumulative) | -0.913% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 37 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $733.32 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$585.77 |
| Signal saved | -$1315.00 |
| Portfolio value | $101,170.96 |
| Benchmark value | $102,042.72 |
| Alpha (cumulative) | -0.872% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 38 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $733.33 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$586.32 |
| Signal saved | -$1315.55 |
| Portfolio value | $101,170.96 |
| Benchmark value | $102,044.12 |
| Alpha (cumulative) | -0.873% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 39 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $729.35 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$367.42 |
| Signal saved | -$1096.65 |
| Portfolio value | $101,170.96 |
| Benchmark value | $101,490.29 |
| Alpha (cumulative) | -0.319% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 40 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.86 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1000.47 |
| Signal saved | -$1729.70 |
| Portfolio value | $101,170.96 |
| Benchmark value | $103,091.93 |
| Alpha (cumulative) | -1.921% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 41 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.65 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1318.92 |
| Signal saved | -$2048.15 |
| Portfolio value | $101,170.96 |
| Benchmark value | $103,897.62 |
| Alpha (cumulative) | -2.727% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 42 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $745.66 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1264.47 |
| Signal saved | -$1993.70 |
| Portfolio value | $101,170.96 |
| Benchmark value | $103,759.86 |
| Alpha (cumulative) | -2.589% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 43 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $744.86 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1220.47 |
| Signal saved | -$1949.70 |
| Portfolio value | $101,170.96 |
| Benchmark value | $103,648.54 |
| Alpha (cumulative) | -2.478% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 44 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $751.27 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1573.02 |
| Signal saved | -$2302.25 |
| Portfolio value | $101,170.96 |
| Benchmark value | $104,540.50 |
| Alpha (cumulative) | -3.369% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 45 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $747.77 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1380.52 |
| Signal saved | -$2109.75 |
| Portfolio value | $101,170.96 |
| Benchmark value | $104,053.47 |
| Alpha (cumulative) | -2.882% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 46 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $745.28 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1243.57 |
| Signal saved | -$1972.80 |
| Portfolio value | $101,170.96 |
| Benchmark value | $103,706.98 |
| Alpha (cumulative) | -2.536% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 47 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $751.55 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1588.42 |
| Signal saved | -$2317.65 |
| Portfolio value | $101,170.96 |
| Benchmark value | $104,579.46 |
| Alpha (cumulative) | -3.408% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 48 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $754.94 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1774.87 |
| Signal saved | -$2504.10 |
| Portfolio value | $101,170.96 |
| Benchmark value | $105,051.18 |
| Alpha (cumulative) | -3.880% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 49 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $749.13 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1455.32 |
| Signal saved | -$2184.55 |
| Portfolio value | $101,009.84 |
| Benchmark value | $104,242.71 |
| Alpha (cumulative) | -3.233% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 50 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $751.94 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1609.87 |
| Signal saved | -$2339.10 |
| Portfolio value | $100,974.76 |
| Benchmark value | $104,633.73 |
| Alpha (cumulative) | -3.659% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 51 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $754.77 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1765.52 |
| Signal saved | -$2494.75 |
| Portfolio value | $101,022.51 |
| Benchmark value | $105,027.53 |
| Alpha (cumulative) | -4.005% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 52 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $750.87 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1551.02 |
| Signal saved | -$2280.25 |
| Portfolio value | $100,846.38 |
| Benchmark value | $104,484.84 |
| Alpha (cumulative) | -3.639% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 53 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $743.28 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1133.57 |
| Signal saved | -$1862.80 |
| Portfolio value | $100,703.82 |
| Benchmark value | $103,428.68 |
| Alpha (cumulative) | -2.725% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 54 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $742.15 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1071.42 |
| Signal saved | -$1800.65 |
| Portfolio value | $100,511.84 |
| Benchmark value | $103,271.43 |
| Alpha (cumulative) | -2.759% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $100,539.93 |
| Benchmark value | $104,106.34 |
| Alpha (cumulative) | -3.566% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +0.07% from entry. No exit triggered.

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
| Portfolio value | $100,504.95 |
| Benchmark value | $104,014.50 |
| Alpha (cumulative) | -3.509% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.02% from entry. No exit triggered.

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
| Portfolio value | $99,835.81 |
| Benchmark value | $102,702.30 |
| Alpha (cumulative) | -2.866% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 58 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $738.90 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$892.67 |
| Signal saved | -$1621.90 |
| Portfolio value | $99,884.69 |
| Benchmark value | $102,819.19 |
| Alpha (cumulative) | -2.934% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 59 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $738.85 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$889.92 |
| Signal saved | -$1619.15 |
| Portfolio value | $99,988.83 |
| Benchmark value | $102,812.23 |
| Alpha (cumulative) | -2.823% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 60 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $740.79 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$996.62 |
| Signal saved | -$1725.85 |
| Portfolio value | $99,945.37 |
| Benchmark value | $103,082.19 |
| Alpha (cumulative) | -3.137% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 61 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $729.57 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$379.52 |
| Signal saved | -$1108.75 |
| Portfolio value | $99,945.37 |
| Benchmark value | $101,520.91 |
| Alpha (cumulative) | -1.576% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 62 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $741.63 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1042.82 |
| Signal saved | -$1772.05 |
| Portfolio value | $99,945.37 |
| Benchmark value | $103,199.08 |
| Alpha (cumulative) | -3.254% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 63 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $746.79 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1326.62 |
| Signal saved | -$2055.85 |
| Portfolio value | $99,945.37 |
| Benchmark value | $103,917.10 |
| Alpha (cumulative) | -3.972% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 64 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $757.72 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$1927.77 |
| Signal saved | -$2657.00 |
| Portfolio value | $99,945.37 |
| Benchmark value | $105,438.03 |
| Alpha (cumulative) | -5.493% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $99,893.37 |
| Benchmark value | $107,301.27 |
| Alpha (cumulative) | -7.408% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 66 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $769.79 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$2591.62 |
| Signal saved | -$3320.85 |
| Portfolio value | $99,858.37 |
| Benchmark value | $107,117.59 |
| Alpha (cumulative) | -7.260% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 67 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $768.64 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$2528.37 |
| Signal saved | -$3257.60 |
| Portfolio value | $99,858.37 |
| Benchmark value | $106,957.56 |
| Alpha (cumulative) | -7.100% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $99,891.51 |
| Benchmark value | $107,586.53 |
| Alpha (cumulative) | -7.696% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +0.08% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 69 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $773.02 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$2769.27 |
| Signal saved | -$3498.50 |
| Portfolio value | $99,883.35 |
| Benchmark value | $107,567.05 |
| Alpha (cumulative) | -7.684% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Portfolio value | $99,724.16 |
| Benchmark value | $107,219.17 |
| Alpha (cumulative) | -7.495% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.40% from entry. No exit triggered.

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
| Portfolio value | $99,827.18 |
| Benchmark value | $107,500.25 |
| Alpha (cumulative) | -7.673% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.14% from entry. No exit triggered.

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
| Portfolio value | $100,097.48 |
| Benchmark value | $108,237.76 |
| Alpha (cumulative) | -8.140% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +0.54% from entry. No exit triggered.

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
| Portfolio value | $100,018.94 |
| Benchmark value | $108,023.46 |
| Alpha (cumulative) | -8.004% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: +0.34% from entry. No exit triggered.

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
| Portfolio value | $99,831.26 |
| Benchmark value | $107,511.39 |
| Alpha (cumulative) | -7.680% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.13% from entry. No exit triggered.

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
| Portfolio value | $99,563.51 |
| Benchmark value | $106,780.84 |
| Alpha (cumulative) | -7.217% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.81% from entry. No exit triggered.

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
| Portfolio value | $99,651.23 |
| Benchmark value | $107,020.18 |
| Alpha (cumulative) | -7.369% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.59% from entry. No exit triggered.

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
| Portfolio value | $99,321.26 |
| Benchmark value | $106,119.87 |
| Alpha (cumulative) | -6.799% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -1.43% from entry. No exit triggered.

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
| Portfolio value | $99,475.28 |
| Benchmark value | $106,540.11 |
| Alpha (cumulative) | -7.065% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -1.03% from entry. No exit triggered.

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
| Portfolio value | $99,364.10 |
| Benchmark value | $106,236.76 |
| Alpha (cumulative) | -6.873% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -1.32% from entry. No exit triggered.

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
| Portfolio value | $99,482.93 |
| Benchmark value | $106,560.98 |
| Alpha (cumulative) | -7.078% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -1.01% from entry. No exit triggered.

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
| Portfolio value | $99,490.58 |
| Benchmark value | $106,581.85 |
| Alpha (cumulative) | -7.091% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.99% from entry. No exit triggered.

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
| Portfolio value | $99,757.82 |
| Benchmark value | $107,311.01 |
| Alpha (cumulative) | -7.553% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.32% from entry. No exit triggered.

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
| Portfolio value | $99,660.92 |
| Benchmark value | $107,046.62 |
| Alpha (cumulative) | -7.386% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.56% from entry. No exit triggered.

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
| Portfolio value | $99,538.01 |
| Benchmark value | $106,711.26 |
| Alpha (cumulative) | -7.173% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Momentum: RECOVERING. Unrealized P&L: -0.88% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 85 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $761.63 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$2142.82 |
| Signal saved | -$2872.05 |
| Portfolio value | $99,270.77 |
| Benchmark value | $105,982.11 |
| Alpha (cumulative) | -6.711% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 86 — 2026-09-02

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $722.670/share |
| Close price | $764.95 |
| Realized P&L (locked) | -$729.23 |
| Reference if held | +$2325.42 |
| Signal saved | -$3054.65 |
| Portfolio value | $99,270.77 |
| Benchmark value | $106,444.09 |
| Alpha (cumulative) | -7.173% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-729.23. Regime: BULL (MA20 $769.21 vs MA50 $754.71). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
_Day 86 of 90 · Alpaca equity: $99,287.39 · Cumulative alpha vs SPY: -7.173%_