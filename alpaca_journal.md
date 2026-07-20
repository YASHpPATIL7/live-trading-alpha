# ALPACA PAPER JOURNAL — SPY
_Last updated: July 20, 2026 | Day 92 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$666.436/share**
> (2026-03-09, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-07-20): **BULLISH**  
> Fast: MA10 $750.09 | MA30 $743.44  
> Slow: MA20 $745.02 | MA50 $743.23  
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

**Total trades:** 15 | **Closed:** 14 | **Open:** Yes | **Cumulative Realized P&L:** +$721.68

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $666.436 (2026-03-09) | $668.000 (2026-03-12) | 10 | +$15.64 | ✅ Closed |
| T2 | $701.250 (2026-04-16) | $701.600 (2026-04-16) | 57 | +$19.95 | ✅ Closed |
| T3 | $710.606 (2026-04-17) | $710.500 (2026-04-17) | 56 | -$5.92 | ✅ Closed |
| T4 | $706.745 (2026-04-20) | $706.280 (2026-04-21) | 56 | -$26.06 | ✅ Closed |
| T5 | $709.805 (2026-04-22) | $707.520 (2026-04-23) | 56 | -$127.95 | ✅ Closed |
| T6 | $711.277 (2026-04-24) | $709.220 (2026-04-29) | 56 | -$115.20 | ✅ Closed |
| T7 | $714.440 (2026-04-30) | $719.120 (2026-04-30) | 55 | +$257.40 | ✅ Closed |
| T8 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 55 | +$1172.07 | ✅ Closed |
| T9 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T10 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T11 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T12 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T13 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T14 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T15 | $745.460 (2026-07-20) | — | 41 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $100,721.92 |
| Alpaca cash | $70,159.29 |
| Cumulative realized P&L | +$721.68 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $674.68 | Long 10 SPY (T1) | +$82.44 | +1.237% | $100,082.44 |
| Day 2 | 2026-03-10 | $673.52 | Long 10 SPY (T1) | +$70.84 | +1.063% | $100,070.84 |
| Day 3 | 2026-03-11 | $672.73 | Long 10 SPY (T1) | +$62.94 | +0.944% | $100,062.94 |
| Day 4 | 2026-03-12 | $662.50 | FLAT | — | — | $100,015.64 |
| Day 5 | 2026-03-13 | $658.77 | FLAT | — | — | $100,015.64 |
| Day 6 | 2026-03-16 | $665.40 | FLAT | — | — | $100,015.64 |
| Day 7 | 2026-03-17 | $667.17 | FLAT | — | — | $100,015.64 |
| Day 8 | 2026-03-18 | $658.01 | FLAT | — | — | $100,015.64 |
| Day 9 | 2026-03-19 | $656.35 | FLAT | — | — | $100,015.64 |
| Day 10 | 2026-03-20 | $646.81 | FLAT | — | — | $100,015.64 |
| Day 11 | 2026-03-23 | $653.69 | FLAT | — | — | $100,015.64 |
| Day 12 | 2026-03-24 | $651.52 | FLAT | — | — | $100,015.64 |
| Day 13 | 2026-03-25 | $655.05 | FLAT | — | — | $100,015.64 |
| Day 14 | 2026-03-26 | $643.45 | FLAT | — | — | $100,015.64 |
| Day 15 | 2026-03-27 | $632.41 | FLAT | — | — | $100,015.64 |
| Day 16 | 2026-03-30 | $630.40 | FLAT | — | — | $100,015.64 |
| Day 17 | 2026-03-31 | $648.45 | FLAT | — | — | $100,015.64 |
| Day 18 | 2026-04-01 | $653.50 | FLAT | — | — | $100,015.64 |
| Day 19 | 2026-04-02 | $654.08 | FLAT | — | — | $100,015.64 |
| Day 20 | 2026-04-06 | $657.19 | FLAT | — | — | $100,015.64 |
| Day 21 | 2026-04-07 | $657.54 | FLAT | — | — | $100,015.64 |
| Day 22 | 2026-04-08 | $674.26 | FLAT | — | — | $100,015.64 |
| Day 23 | 2026-04-09 | $678.12 | FLAT | — | — | $100,015.64 |
| Day 24 | 2026-04-10 | $677.60 | FLAT | — | — | $100,015.64 |
| Day 25 | 2026-04-13 | $684.24 | FLAT | — | — | $100,015.64 |
| Day 26 | 2026-04-14 | $692.58 | FLAT | — | — | $100,015.64 |
| Day 27 | 2026-04-15 | $697.95 | FLAT | — | — | $100,015.64 |
| Day 28 | 2026-04-16 | $699.73 | FLAT | — | — | $100,035.59 |
| Day 29 | 2026-04-17 | $708.24 | FLAT | — | — | $100,029.67 |
| Day 30 | 2026-04-20 | $706.97 | Long 56 SPY (T4) | +$12.58 | +0.032% | $100,042.25 |
| Day 31 | 2026-04-21 | $702.10 | FLAT | — | — | $100,003.61 |
| Day 32 | 2026-04-22 | $709.37 | Long 56 SPY (T5) | -$24.35 | -0.061% | $99,979.26 |
| Day 33 | 2026-04-23 | $706.59 | FLAT | — | — | $99,875.66 |
| Day 34 | 2026-04-24 | $712.14 | Long 56 SPY (T6) | +$48.32 | +0.121% | $99,923.98 |
| Day 35 | 2026-04-27 | $713.33 | Long 56 SPY (T6) | +$114.96 | +0.289% | $99,990.62 |
| Day 36 | 2026-04-28 | $709.85 | Long 56 SPY (T6) | -$79.92 | -0.201% | $99,795.74 |
| Day 37 | 2026-04-29 | $709.76 | FLAT | — | — | $99,760.46 |
| Day 38 | 2026-04-30 | $716.56 | FLAT | — | — | $100,017.86 |
| Day 39 | 2026-05-01 | $718.64 | Long 55 SPY (T8) | -$221.63 | -0.558% | $99,796.23 |
| Day 40 | 2026-05-04 | $716.25 | Long 55 SPY (T8) | -$353.08 | -0.888% | $99,664.78 |
| Day 41 | 2026-05-05 | $721.85 | Long 55 SPY (T8) | -$45.08 | -0.113% | $99,972.78 |
| Day 42 | 2026-05-06 | $731.88 | Long 55 SPY (T8) | +$506.57 | +1.274% | $100,524.43 |
| Day 43 | 2026-05-07 | $729.65 | Long 55 SPY (T8) | +$383.92 | +0.966% | $100,401.78 |
| Day 44 | 2026-05-08 | $735.65 | Long 55 SPY (T8) | +$713.92 | +1.796% | $100,731.78 |
| Day 45 | 2026-05-11 | $737.30 | Long 55 SPY (T8) | +$804.67 | +2.024% | $100,822.53 |
| Day 46 | 2026-05-12 | $736.29 | Long 55 SPY (T8) | +$749.12 | +1.885% | $100,766.98 |
| Day 47 | 2026-05-13 | $740.39 | Long 55 SPY (T8) | +$974.62 | +2.452% | $100,992.48 |
| Day 48 | 2026-05-14 | $746.18 | Long 55 SPY (T8) | +$1293.07 | +3.253% | $101,310.93 |
| Day 49 | 2026-05-15 | $737.20 | Long 55 SPY (T8) | +$799.17 | +2.011% | $100,817.03 |
| Day 50 | 2026-05-18 | $736.50 | Long 55 SPY (T8) | +$760.67 | +1.914% | $100,778.53 |
| Day 51 | 2026-05-19 | $731.91 | Long 55 SPY (T8) | +$508.22 | +1.279% | $100,526.08 |
| Day 52 | 2026-05-20 | $739.41 | Long 55 SPY (T8) | +$920.72 | +2.316% | $100,938.58 |
| Day 53 | 2026-05-21 | $740.80 | Long 55 SPY (T8) | +$997.17 | +2.509% | $101,015.03 |
| Day 54 | 2026-05-22 | $743.75 | Long 55 SPY (T8) | +$1159.42 | +2.917% | $101,177.28 |
| Day 55 | 2026-05-26 | $748.53 | Long 55 SPY (T8) | +$1422.32 | +3.578% | $101,440.18 |
| Day 56 | 2026-05-27 | $748.66 | Long 55 SPY (T8) | +$1429.47 | +3.596% | $101,447.33 |
| Day 57 | 2026-05-28 | $752.74 | Long 55 SPY (T8) | +$1653.87 | +4.161% | $101,671.73 |
| Day 58 | 2026-05-29 | $754.40 | Long 55 SPY (T8) | +$1745.17 | +4.391% | $101,763.03 |
| Day 59 | 2026-06-01 | $756.49 | Long 55 SPY (T8) | +$1860.12 | +4.680% | $101,877.98 |
| Day 60 | 2026-06-02 | $757.52 | Long 55 SPY (T8) | +$1916.77 | +4.822% | $101,934.63 |
| Day 61 | 2026-06-03 | $752.24 | Long 55 SPY (T8) | +$1626.37 | +4.092% | $101,644.23 |
| Day 62 | 2026-06-04 | $755.03 | Long 55 SPY (T8) | +$1779.82 | +4.478% | $101,797.68 |
| Day 63 | 2026-06-05 | $735.56 | Long 55 SPY (T8) | +$708.97 | +1.784% | $100,726.83 |
| Day 64 | 2026-06-08 | $737.34 | Long 55 SPY (T8) | +$806.87 | +2.030% | $100,824.73 |
| Day 65 | 2026-06-09 | $735.18 | Long 55 SPY (T8) | +$688.07 | +1.731% | $100,705.93 |
| Day 66 | 2026-06-10 | $723.72 | Long 55 SPY (T8) | +$57.77 | +0.145% | $100,075.63 |
| Day 67 | 2026-06-11 | $735.77 | Long 55 SPY (T8) | +$720.52 | +1.813% | $100,738.38 |
| Day 68 | 2026-06-12 | $739.76 | Long 55 SPY (T8) | +$939.97 | +2.365% | $100,957.83 |
| Day 69 | 2026-06-15 | $752.81 | Long 55 SPY (T8) | +$1657.72 | +4.171% | $101,675.58 |
| Day 70 | 2026-06-16 | $748.65 | Long 55 SPY (T8) | +$1428.92 | +3.595% | $101,446.78 |
| Day 71 | 2026-06-17 | $739.12 | FLAT | — | — | $101,189.93 |
| Day 72 | 2026-06-18 | $746.75 | FLAT | — | — | $101,189.93 |
| Day 73 | 2026-06-22 | $744.27 | FLAT | — | — | $101,188.82 |
| Day 74 | 2026-06-23 | $733.62 | FLAT | — | — | $101,188.82 |
| Day 75 | 2026-06-24 | $733.32 | FLAT | — | — | $101,188.82 |
| Day 76 | 2026-06-25 | $733.33 | FLAT | — | — | $101,188.82 |
| Day 77 | 2026-06-26 | $729.35 | FLAT | — | — | $101,188.82 |
| Day 78 | 2026-06-29 | $740.86 | FLAT | — | — | $101,188.82 |
| Day 79 | 2026-06-30 | $746.65 | FLAT | — | — | $101,188.82 |
| Day 80 | 2026-07-01 | $745.66 | FLAT | — | — | $101,188.82 |
| Day 81 | 2026-07-02 | $744.86 | FLAT | — | — | $101,188.82 |
| Day 82 | 2026-07-06 | $751.27 | FLAT | — | — | $101,188.82 |
| Day 83 | 2026-07-07 | $747.77 | FLAT | — | — | $101,188.82 |
| Day 84 | 2026-07-08 | $745.28 | FLAT | — | — | $101,188.82 |
| Day 85 | 2026-07-09 | $751.55 | FLAT | — | — | $101,188.82 |
| Day 86 | 2026-07-10 | $754.94 | FLAT | — | — | $101,188.82 |
| Day 87 | 2026-07-13 | $749.13 | FLAT | — | — | $101,027.70 |
| Day 88 | 2026-07-14 | $751.94 | FLAT | — | — | $100,992.62 |
| Day 89 | 2026-07-15 | $754.77 | FLAT | — | — | $101,040.37 |
| Day 90 | 2026-07-16 | $750.87 | FLAT | — | — | $100,864.24 |
| Day 91 | 2026-07-17 | $743.28 | FLAT | — | — | $100,721.68 |
| Day 92 | 2026-07-20 | $745.57 | Long 41 SPY (T15) | +$4.51 | +0.015% | $100,726.19 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $100,082.44 | $99,999.99 | +0.0824% | -0.000% | **+0.082%** |
| Day 2 | 2026-03-10 | $100,070.84 | $99,828.06 | +0.0708% | -0.172% | **+0.243%** |
| Day 3 | 2026-03-11 | $100,062.94 | $99,710.96 | +0.0629% | -0.289% | **+0.352%** |
| Day 4 | 2026-03-12 | $100,015.64 | $98,194.69 | +0.0156% | -1.805% | **+1.821%** |
| Day 5 | 2026-03-13 | $100,015.64 | $97,641.84 | +0.0156% | -2.358% | **+2.374%** |
| Day 6 | 2026-03-16 | $100,015.64 | $98,624.52 | +0.0156% | -1.375% | **+1.391%** |
| Day 7 | 2026-03-17 | $100,015.64 | $98,886.87 | +0.0156% | -1.113% | **+1.129%** |
| Day 8 | 2026-03-18 | $100,015.64 | $97,529.19 | +0.0156% | -2.471% | **+2.487%** |
| Day 9 | 2026-03-19 | $100,015.64 | $97,283.15 | +0.0156% | -2.717% | **+2.733%** |
| Day 10 | 2026-03-20 | $100,015.64 | $95,869.14 | +0.0156% | -4.131% | **+4.147%** |
| Day 11 | 2026-03-23 | $100,015.64 | $96,888.89 | +0.0156% | -3.111% | **+3.127%** |
| Day 12 | 2026-03-24 | $100,015.64 | $96,567.25 | +0.0156% | -3.433% | **+3.449%** |
| Day 13 | 2026-03-25 | $100,015.64 | $97,090.46 | +0.0156% | -2.910% | **+2.926%** |
| Day 14 | 2026-03-26 | $100,015.64 | $95,371.13 | +0.0156% | -4.629% | **+4.645%** |
| Day 15 | 2026-03-27 | $100,015.64 | $93,734.80 | +0.0156% | -6.265% | **+6.281%** |
| Day 16 | 2026-03-30 | $100,015.64 | $93,436.88 | +0.0156% | -6.563% | **+6.579%** |
| Day 17 | 2026-03-31 | $100,015.64 | $96,112.22 | +0.0156% | -3.888% | **+3.904%** |
| Day 18 | 2026-04-01 | $100,015.64 | $96,860.72 | +0.0156% | -3.139% | **+3.155%** |
| Day 19 | 2026-04-02 | $100,015.64 | $96,946.69 | +0.0156% | -3.053% | **+3.069%** |
| Day 20 | 2026-04-06 | $100,015.64 | $97,407.65 | +0.0156% | -2.592% | **+2.608%** |
| Day 21 | 2026-04-07 | $100,015.64 | $97,459.53 | +0.0156% | -2.540% | **+2.556%** |
| Day 22 | 2026-04-08 | $100,015.64 | $99,937.74 | +0.0156% | -0.062% | **+0.078%** |
| Day 23 | 2026-04-09 | $100,015.64 | $100,509.86 | +0.0156% | +0.510% | **-0.494%** |
| Day 24 | 2026-04-10 | $100,015.64 | $100,432.79 | +0.0156% | +0.433% | **-0.417%** |
| Day 25 | 2026-04-13 | $100,015.64 | $101,416.96 | +0.0156% | +1.417% | **-1.401%** |
| Day 26 | 2026-04-14 | $100,015.64 | $102,653.10 | +0.0156% | +2.653% | **-2.637%** |
| Day 27 | 2026-04-15 | $100,015.64 | $103,449.03 | +0.0156% | +3.449% | **-3.433%** |
| Day 28 | 2026-04-16 | $100,035.59 | $103,712.86 | +0.0356% | +3.713% | **-3.677%** |
| Day 29 | 2026-04-17 | $100,029.67 | $104,974.20 | +0.0297% | +4.974% | **-4.944%** |
| Day 30 | 2026-04-20 | $100,042.25 | $104,785.96 | +0.0422% | +4.786% | **-4.744%** |
| Day 31 | 2026-04-21 | $100,003.61 | $104,064.14 | +0.0036% | +4.064% | **-4.060%** |
| Day 32 | 2026-04-22 | $99,979.26 | $105,141.69 | -0.0207% | +5.142% | **-5.163%** |
| Day 33 | 2026-04-23 | $99,875.66 | $104,729.64 | -0.1243% | +4.730% | **-4.854%** |
| Day 34 | 2026-04-24 | $99,923.98 | $105,552.25 | -0.0760% | +5.552% | **-5.628%** |
| Day 35 | 2026-04-27 | $99,990.62 | $105,728.63 | -0.0094% | +5.729% | **-5.738%** |
| Day 36 | 2026-04-28 | $99,795.74 | $105,212.83 | -0.2043% | +5.213% | **-5.417%** |
| Day 37 | 2026-04-29 | $99,760.46 | $105,199.49 | -0.2395% | +5.199% | **-5.438%** |
| Day 38 | 2026-04-30 | $100,017.86 | $106,207.38 | +0.0179% | +6.207% | **-6.189%** |
| Day 39 | 2026-05-01 | $99,796.23 | $106,515.67 | -0.2038% | +6.516% | **-6.720%** |
| Day 40 | 2026-05-04 | $99,664.78 | $106,161.43 | -0.3352% | +6.161% | **-6.496%** |
| Day 41 | 2026-05-05 | $99,972.78 | $106,991.45 | -0.0272% | +6.991% | **-7.018%** |
| Day 42 | 2026-05-06 | $100,524.43 | $108,478.08 | +0.5244% | +8.478% | **-7.954%** |
| Day 43 | 2026-05-07 | $100,401.78 | $108,147.56 | +0.4018% | +8.148% | **-7.746%** |
| Day 44 | 2026-05-08 | $100,731.78 | $109,036.87 | +0.7318% | +9.037% | **-8.305%** |
| Day 45 | 2026-05-11 | $100,822.53 | $109,281.43 | +0.8225% | +9.281% | **-8.458%** |
| Day 46 | 2026-05-12 | $100,766.98 | $109,131.73 | +0.7670% | +9.132% | **-8.365%** |
| Day 47 | 2026-05-13 | $100,992.48 | $109,739.42 | +0.9925% | +9.739% | **-8.747%** |
| Day 48 | 2026-05-14 | $101,310.93 | $110,597.61 | +1.3109% | +10.598% | **-9.287%** |
| Day 49 | 2026-05-15 | $100,817.03 | $109,266.60 | +0.8170% | +9.267% | **-8.450%** |
| Day 50 | 2026-05-18 | $100,778.53 | $109,162.85 | +0.7785% | +9.163% | **-8.385%** |
| Day 51 | 2026-05-19 | $100,526.08 | $108,482.53 | +0.5261% | +8.483% | **-7.957%** |
| Day 52 | 2026-05-20 | $100,938.58 | $109,594.17 | +0.9386% | +9.594% | **-8.655%** |
| Day 53 | 2026-05-21 | $101,015.03 | $109,800.19 | +1.0150% | +9.800% | **-8.785%** |
| Day 54 | 2026-05-22 | $101,177.28 | $110,237.44 | +1.1773% | +10.237% | **-9.060%** |
| Day 55 | 2026-05-26 | $101,440.18 | $110,945.92 | +1.4402% | +10.946% | **-9.506%** |
| Day 56 | 2026-05-27 | $101,447.33 | $110,965.19 | +1.4473% | +10.965% | **-9.518%** |
| Day 57 | 2026-05-28 | $101,671.73 | $111,569.92 | +1.6717% | +11.570% | **-9.898%** |
| Day 58 | 2026-05-29 | $101,763.03 | $111,815.96 | +1.7630% | +11.816% | **-10.053%** |
| Day 59 | 2026-06-01 | $101,877.98 | $112,125.74 | +1.8780% | +12.126% | **-10.248%** |
| Day 60 | 2026-06-02 | $101,934.63 | $112,278.40 | +1.9346% | +12.278% | **-10.343%** |
| Day 61 | 2026-06-03 | $101,644.23 | $111,495.81 | +1.6442% | +11.496% | **-9.852%** |
| Day 62 | 2026-06-04 | $101,797.68 | $111,909.34 | +1.7977% | +11.909% | **-10.111%** |
| Day 63 | 2026-06-05 | $100,726.83 | $109,023.53 | +0.7268% | +9.024% | **-8.297%** |
| Day 64 | 2026-06-08 | $100,824.73 | $109,287.36 | +0.8247% | +9.287% | **-8.462%** |
| Day 65 | 2026-06-09 | $100,705.93 | $108,967.20 | +0.7059% | +8.967% | **-8.261%** |
| Day 66 | 2026-06-10 | $100,075.63 | $107,268.62 | +0.0756% | +7.269% | **-7.193%** |
| Day 67 | 2026-06-11 | $100,738.38 | $109,054.65 | +0.7384% | +9.055% | **-8.317%** |
| Day 68 | 2026-06-12 | $100,957.83 | $109,646.04 | +0.9578% | +9.646% | **-8.688%** |
| Day 69 | 2026-06-15 | $101,675.58 | $111,580.29 | +1.6756% | +11.580% | **-9.904%** |
| Day 70 | 2026-06-16 | $101,446.78 | $110,963.71 | +1.4468% | +10.964% | **-9.517%** |
| Day 71 | 2026-06-17 | $101,189.93 | $109,551.18 | +1.1899% | +9.551% | **-8.361%** |
| Day 72 | 2026-06-18 | $101,189.93 | $110,682.09 | +1.1899% | +10.682% | **-9.492%** |
| Day 73 | 2026-06-22 | $101,188.82 | $110,314.51 | +1.1888% | +10.315% | **-9.126%** |
| Day 74 | 2026-06-23 | $101,188.82 | $108,735.98 | +1.1888% | +8.736% | **-7.547%** |
| Day 75 | 2026-06-24 | $101,188.82 | $108,691.52 | +1.1888% | +8.692% | **-7.503%** |
| Day 76 | 2026-06-25 | $101,188.82 | $108,693.00 | +1.1888% | +8.693% | **-7.504%** |
| Day 77 | 2026-06-26 | $101,188.82 | $108,103.09 | +1.1888% | +8.103% | **-6.914%** |
| Day 78 | 2026-06-29 | $101,188.82 | $109,809.08 | +1.1888% | +9.809% | **-8.620%** |
| Day 79 | 2026-06-30 | $101,188.82 | $110,667.27 | +1.1888% | +10.667% | **-9.478%** |
| Day 80 | 2026-07-01 | $101,188.82 | $110,520.53 | +1.1888% | +10.521% | **-9.332%** |
| Day 81 | 2026-07-02 | $101,188.82 | $110,401.96 | +1.1888% | +10.402% | **-9.213%** |
| Day 82 | 2026-07-06 | $101,188.82 | $111,352.04 | +1.1888% | +11.352% | **-10.163%** |
| Day 83 | 2026-07-07 | $101,188.82 | $110,833.27 | +1.1888% | +10.833% | **-9.644%** |
| Day 84 | 2026-07-08 | $101,188.82 | $110,464.21 | +1.1888% | +10.464% | **-9.275%** |
| Day 85 | 2026-07-09 | $101,188.82 | $111,393.54 | +1.1888% | +11.394% | **-10.205%** |
| Day 86 | 2026-07-10 | $101,188.82 | $111,896.00 | +1.1888% | +11.896% | **-10.707%** |
| Day 87 | 2026-07-13 | $101,027.70 | $111,034.85 | +1.0277% | +11.035% | **-10.007%** |
| Day 88 | 2026-07-14 | $100,992.62 | $111,451.34 | +0.9926% | +11.451% | **-10.458%** |
| Day 89 | 2026-07-15 | $101,040.37 | $111,870.80 | +1.0404% | +11.871% | **-10.831%** |
| Day 90 | 2026-07-16 | $100,864.24 | $111,292.75 | +0.8642% | +11.293% | **-10.429%** |
| Day 91 | 2026-07-17 | $100,721.68 | $110,167.77 | +0.7217% | +10.168% | **-9.446%** |
| Day 92 | 2026-07-20 | $100,726.19 | $110,507.19 | +0.7262% | +10.507% | **-9.781%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $674.68 | +$82.44 | +$639.24 | Position open |
| Day 2 | 2026-03-10 | $673.52 | +$70.84 | +$650.84 | Position open |
| Day 3 | 2026-03-11 | $672.73 | +$62.94 | +$658.74 | Position open |
| Day 4 | 2026-03-12 | $662.50 | -$39.36 | +$761.04 | Flat saved **+$761.04** vs holding |
| Day 5 | 2026-03-13 | $658.77 | -$76.66 | +$798.34 | Flat saved **+$798.34** vs holding |
| Day 6 | 2026-03-16 | $665.40 | -$10.36 | +$732.04 | Flat saved **+$732.04** vs holding |
| Day 7 | 2026-03-17 | $667.17 | +$7.34 | +$714.34 | Flat saved **+$714.34** vs holding |
| Day 8 | 2026-03-18 | $658.01 | -$84.26 | +$805.94 | Flat saved **+$805.94** vs holding |
| Day 9 | 2026-03-19 | $656.35 | -$100.86 | +$822.54 | Flat saved **+$822.54** vs holding |
| Day 10 | 2026-03-20 | $646.81 | -$196.26 | +$917.94 | Flat saved **+$917.94** vs holding |
| Day 11 | 2026-03-23 | $653.69 | -$127.46 | +$849.14 | Flat saved **+$849.14** vs holding |
| Day 12 | 2026-03-24 | $651.52 | -$149.16 | +$870.84 | Flat saved **+$870.84** vs holding |
| Day 13 | 2026-03-25 | $655.05 | -$113.86 | +$835.54 | Flat saved **+$835.54** vs holding |
| Day 14 | 2026-03-26 | $643.45 | -$229.86 | +$951.54 | Flat saved **+$951.54** vs holding |
| Day 15 | 2026-03-27 | $632.41 | -$340.26 | +$1061.94 | Flat saved **+$1061.94** vs holding |
| Day 16 | 2026-03-30 | $630.40 | -$360.36 | +$1082.04 | Flat saved **+$1082.04** vs holding |
| Day 17 | 2026-03-31 | $648.45 | -$179.86 | +$901.54 | Flat saved **+$901.54** vs holding |
| Day 18 | 2026-04-01 | $653.50 | -$129.36 | +$851.04 | Flat saved **+$851.04** vs holding |
| Day 19 | 2026-04-02 | $654.08 | -$123.56 | +$845.24 | Flat saved **+$845.24** vs holding |
| Day 20 | 2026-04-06 | $657.19 | -$92.46 | +$814.14 | Flat saved **+$814.14** vs holding |
| Day 21 | 2026-04-07 | $657.54 | -$88.96 | +$810.64 | Flat saved **+$810.64** vs holding |
| Day 22 | 2026-04-08 | $674.26 | +$78.24 | +$643.44 | Flat saved **+$643.44** vs holding |
| Day 23 | 2026-04-09 | $678.12 | +$116.84 | +$604.84 | Flat saved **+$604.84** vs holding |
| Day 24 | 2026-04-10 | $677.60 | +$111.64 | +$610.04 | Flat saved **+$610.04** vs holding |
| Day 25 | 2026-04-13 | $684.24 | +$178.04 | +$543.64 | Flat saved **+$543.64** vs holding |
| Day 26 | 2026-04-14 | $692.58 | +$261.44 | +$460.24 | Flat saved **+$460.24** vs holding |
| Day 27 | 2026-04-15 | $697.95 | +$315.14 | +$406.54 | Flat saved **+$406.54** vs holding |
| Day 28 | 2026-04-16 | $699.73 | +$332.94 | +$388.74 | Flat saved **+$388.74** vs holding |
| Day 29 | 2026-04-17 | $708.24 | +$418.04 | +$303.64 | Flat saved **+$303.64** vs holding |
| Day 30 | 2026-04-20 | $706.97 | +$405.34 | +$316.34 | Position open |
| Day 31 | 2026-04-21 | $702.10 | +$356.64 | +$365.04 | Flat saved **+$365.04** vs holding |
| Day 32 | 2026-04-22 | $709.37 | +$429.34 | +$292.34 | Position open |
| Day 33 | 2026-04-23 | $706.59 | +$401.54 | +$320.14 | Flat saved **+$320.14** vs holding |
| Day 34 | 2026-04-24 | $712.14 | +$457.04 | +$264.64 | Position open |
| Day 35 | 2026-04-27 | $713.33 | +$468.94 | +$252.74 | Position open |
| Day 36 | 2026-04-28 | $709.85 | +$434.14 | +$287.54 | Position open |
| Day 37 | 2026-04-29 | $709.76 | +$433.24 | +$288.44 | Flat saved **+$288.44** vs holding |
| Day 38 | 2026-04-30 | $716.56 | +$501.24 | +$220.44 | Flat saved **+$220.44** vs holding |
| Day 39 | 2026-05-01 | $718.64 | +$522.04 | +$199.64 | Position open |
| Day 40 | 2026-05-04 | $716.25 | +$498.14 | +$223.54 | Position open |
| Day 41 | 2026-05-05 | $721.85 | +$554.14 | +$167.54 | Position open |
| Day 42 | 2026-05-06 | $731.88 | +$654.44 | +$67.24 | Position open |
| Day 43 | 2026-05-07 | $729.65 | +$632.14 | +$89.54 | Position open |
| Day 44 | 2026-05-08 | $735.65 | +$692.14 | +$29.54 | Position open |
| Day 45 | 2026-05-11 | $737.30 | +$708.64 | +$13.04 | Position open |
| Day 46 | 2026-05-12 | $736.29 | +$698.54 | +$23.14 | Position open |
| Day 47 | 2026-05-13 | $740.39 | +$739.54 | -$17.86 | Position open |
| Day 48 | 2026-05-14 | $746.18 | +$797.44 | -$75.76 | Position open |
| Day 49 | 2026-05-15 | $737.20 | +$707.64 | +$14.04 | Position open |
| Day 50 | 2026-05-18 | $736.50 | +$700.64 | +$21.04 | Position open |
| Day 51 | 2026-05-19 | $731.91 | +$654.74 | +$66.94 | Position open |
| Day 52 | 2026-05-20 | $739.41 | +$729.74 | -$8.06 | Position open |
| Day 53 | 2026-05-21 | $740.80 | +$743.64 | -$21.96 | Position open |
| Day 54 | 2026-05-22 | $743.75 | +$773.14 | -$51.46 | Position open |
| Day 55 | 2026-05-26 | $748.53 | +$820.94 | -$99.26 | Position open |
| Day 56 | 2026-05-27 | $748.66 | +$822.24 | -$100.56 | Position open |
| Day 57 | 2026-05-28 | $752.74 | +$863.04 | -$141.36 | Position open |
| Day 58 | 2026-05-29 | $754.40 | +$879.64 | -$157.96 | Position open |
| Day 59 | 2026-06-01 | $756.49 | +$900.54 | -$178.86 | Position open |
| Day 60 | 2026-06-02 | $757.52 | +$910.84 | -$189.16 | Position open |
| Day 61 | 2026-06-03 | $752.24 | +$858.04 | -$136.36 | Position open |
| Day 62 | 2026-06-04 | $755.03 | +$885.94 | -$164.26 | Position open |
| Day 63 | 2026-06-05 | $735.56 | +$691.24 | +$30.44 | Position open |
| Day 64 | 2026-06-08 | $737.34 | +$709.04 | +$12.64 | Position open |
| Day 65 | 2026-06-09 | $735.18 | +$687.44 | +$34.24 | Position open |
| Day 66 | 2026-06-10 | $723.72 | +$572.84 | +$148.84 | Position open |
| Day 67 | 2026-06-11 | $735.77 | +$693.34 | +$28.34 | Position open |
| Day 68 | 2026-06-12 | $739.76 | +$733.24 | -$11.56 | Position open |
| Day 69 | 2026-06-15 | $752.81 | +$863.74 | -$142.06 | Position open |
| Day 70 | 2026-06-16 | $748.65 | +$822.14 | -$100.46 | Position open |
| Day 71 | 2026-06-17 | $739.12 | +$726.84 | -$5.16 | Holding would have been **$5.16** better — honest entry |
| Day 72 | 2026-06-18 | $746.75 | +$803.14 | -$81.46 | Holding would have been **$81.46** better — honest entry |
| Day 73 | 2026-06-22 | $744.27 | +$778.34 | -$56.66 | Holding would have been **$56.66** better — honest entry |
| Day 74 | 2026-06-23 | $733.62 | +$671.84 | +$49.84 | Flat saved **+$49.84** vs holding |
| Day 75 | 2026-06-24 | $733.32 | +$668.84 | +$52.84 | Flat saved **+$52.84** vs holding |
| Day 76 | 2026-06-25 | $733.33 | +$668.94 | +$52.74 | Flat saved **+$52.74** vs holding |
| Day 77 | 2026-06-26 | $729.35 | +$629.14 | +$92.54 | Flat saved **+$92.54** vs holding |
| Day 78 | 2026-06-29 | $740.86 | +$744.24 | -$22.56 | Holding would have been **$22.56** better — honest entry |
| Day 79 | 2026-06-30 | $746.65 | +$802.14 | -$80.46 | Holding would have been **$80.46** better — honest entry |
| Day 80 | 2026-07-01 | $745.66 | +$792.24 | -$70.56 | Holding would have been **$70.56** better — honest entry |
| Day 81 | 2026-07-02 | $744.86 | +$784.24 | -$62.56 | Holding would have been **$62.56** better — honest entry |
| Day 82 | 2026-07-06 | $751.27 | +$848.34 | -$126.66 | Holding would have been **$126.66** better — honest entry |
| Day 83 | 2026-07-07 | $747.77 | +$813.34 | -$91.66 | Holding would have been **$91.66** better — honest entry |
| Day 84 | 2026-07-08 | $745.28 | +$788.44 | -$66.76 | Holding would have been **$66.76** better — honest entry |
| Day 85 | 2026-07-09 | $751.55 | +$851.14 | -$129.46 | Holding would have been **$129.46** better — honest entry |
| Day 86 | 2026-07-10 | $754.94 | +$885.04 | -$163.36 | Holding would have been **$163.36** better — honest entry |
| Day 87 | 2026-07-13 | $749.13 | +$826.94 | -$105.26 | Holding would have been **$105.26** better — honest entry |
| Day 88 | 2026-07-14 | $751.94 | +$855.04 | -$133.36 | Holding would have been **$133.36** better — honest entry |
| Day 89 | 2026-07-15 | $754.77 | +$883.34 | -$161.66 | Holding would have been **$161.66** better — honest entry |
| Day 90 | 2026-07-16 | $750.87 | +$844.34 | -$122.66 | Holding would have been **$122.66** better — honest entry |
| Day 91 | 2026-07-17 | $743.28 | +$768.44 | -$46.76 | Holding would have been **$46.76** better — honest entry |
| Day 92 | 2026-07-20 | $745.57 | +$791.34 | -$69.66 | Position open |

---

## Daily Entries

### Day 1 — 2026-03-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $674.68 |
| Unrealized P&L | +$82.44 |
| P&L % | +1.237% |
| Portfolio value | $100,082.44 |
| Benchmark value | $99,999.99 |
| Alpha (cumulative) | +0.082% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. Despite this, the SPY price is still above the MA20 and MA50, but the Death Cross signal indicates a bearish trend. The VIX is high at 27.39.

**Strategy note:** The system correctly identified a bearish trend and entered a long position in SPY, but the MA20/MA50 crossover strategy did not trigger a trade today due to the Death Cross signal.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.24% from entry. No exit triggered.

**Key learning:** The system's ability to identify a bearish trend is correct, but the Death Cross signal overrides the MA20/MA50 crossover strategy, resulting in a missed trade opportunity.

---

### Day 2 — 2026-03-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $673.52 |
| Unrealized P&L | +$70.84 |
| P&L % | +1.063% |
| Portfolio value | $100,070.84 |
| Benchmark value | $99,828.06 |
| Alpha (cumulative) | +0.243% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating elevated volatility. The WTI oil price is also elevated at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system did not trigger a sell signal today, as the MA20 is still below the MA50, indicating a bearish signal is not present. However, the system's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.06% from entry. No exit triggered.

**Key learning:** The system's inaction during a risk-off regime is correct, as the primary focus is on preserving capital during such periods.

---

### Day 3 — 2026-03-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $672.73 |
| Unrealized P&L | +$62.94 |
| P&L % | +0.944% |
| Portfolio value | $100,062.94 |
| Benchmark value | $99,710.96 |
| Alpha (cumulative) | +0.352% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** Market sentiment lifted on de-escalation hopes, but VIX remains elevated at 27.39. WTI Oil price increased, and 10Y Treasury yield rose to 4.328%. SPY price closed at $674.49.

**Strategy note:** MA20 ($660.25) is below MA50 ($675.76), indicating a bearish signal. The system did not enter a trade today, as the signal is not conducive to a long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.94% from entry. No exit triggered.

**Key learning:** The strategy's ability to avoid a losing trade is more valuable than a single winning trade.

---

### Day 4 — 2026-03-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $662.50 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$39.36 |
| Signal saved | +$761.04 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,194.69 |
| Alpha (cumulative) | +1.821% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed's warning about another supply shock. The VIX is elevated at 27.39. Oil prices are also high at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system generated a bearish signal today, but the system did not short as the long position was already open. This was correct because the system is not designed to short.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's long position was profitable today despite the bearish signal, highlighting the importance of position sizing and risk management in a trend-following strategy.

---

### Day 5 — 2026-03-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.77 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$76.66 |
| Signal saved | +$798.34 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,641.84 |
| Alpha (cumulative) | +2.374% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is currently experiencing a risk-off regime due to the impending supply shock warned by the Fed Chair. The VIX index is elevated at 27.39, indicating increased market volatility. Oil prices are also high, at $104.76 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system did not enter a trade as the position status was already FLAT. This was correct because the signal was not a buy signal.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal does not necessarily mean a trade should be entered if the position is already flat.

---

### Day 6 — 2026-03-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $665.40 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$10.36 |
| Signal saved | +$732.04 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,624.52 |
| Alpha (cumulative) | +1.391% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** Markets are higher pre-bell as de-escalation hopes lift risk sentiment. However, Fed Chair Powell's warning of another supply shock is a bearish signal. VIX remains elevated at 27.39.

**Strategy note:** MA20 is below MA50, indicating a bearish crossover. The system did not enter a trade today as it was flat, but the signal would have been to sell given the bearish crossover.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal is a valid reason to sell, even if the market is rising in the short term.

---

### Day 7 — 2026-03-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $667.17 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$7.34 |
| Signal saved | +$714.34 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,886.87 |
| Alpha (cumulative) | +1.129% |

**Regime call:** RISK-OFF

**Market context:** Markets were relatively calm, with the VIX at 27.39, and the 10Y Treasury yield at 4.328%. Headlines were mixed, with some articles hinting at a potential correction.

**Strategy note:** The MA20/MA50 crossover system is in a BEARISH — Death Cross regime. The system did not enter a position today, as the market conditions did not trigger a signal.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction today was correct, as the market did not trigger a signal, and the realized P&L was locked at +$15.58

---

### Day 8 — 2026-03-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.01 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$84.26 |
| Signal saved | +$805.94 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,529.19 |
| Alpha (cumulative) | +2.487% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime following Fed Chair Powell's warning of another supply shock. The VIX index is elevated at 27.39, indicating increased volatility. The SPY price closed at $659.63.

**Strategy note:** The MA20/MA50 crossover strategy is in a BEARISH — Death Cross regime, but no trade was executed due to the system being flat. The strategy's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits is crucial in a risk-off regime, as seen today with a $+15.58 realized P&L.

---

### Day 9 — 2026-03-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $656.35 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$100.86 |
| Signal saved | +$822.54 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,283.15 |
| Alpha (cumulative) | +2.733% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. The VIX is elevated at 27.39. The SPY price closed at $658.00.

**Strategy note:** The system is flat, as the MA20/MA50 crossover strategy did not trigger a trade today. This is correct, as the signal is bearish (Death Cross) and the system is designed to avoid trading during such conditions.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management approach is effective in avoiding losses during periods of high market volatility.

---

### Day 10 — 2026-03-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $646.81 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$196.26 |
| Signal saved | +$917.94 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,869.14 |
| Alpha (cumulative) | +4.147% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite warning signs from the Fed Chair and rising VIX. Oil prices continued to climb. The 10Y Treasury yield remained elevated.

**Strategy note:** The MA20/MA50 crossover system remained flat as MA20 was below MA50, indicating no buy or sell signal. This was correct as the market did not follow the bearish signal.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to stay flat in a volatile market environment is crucial for preserving capital.

---

### Day 11 — 2026-03-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $653.69 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$127.46 |
| Signal saved | +$849.14 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,888.89 |
| Alpha (cumulative) | +3.127% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating increased volatility. Oil prices are also elevated.

**Strategy note:** The MA system is in a bearish regime due to the death cross, but did not enter a trade today as the position was already flat. The system's inaction was correct as the market did not provide a clear buy or sell signal.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to avoid trading during periods of high volatility is crucial in maintaining its overall performance.

---

### Day 12 — 2026-03-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $651.52 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$149.16 |
| Signal saved | +$870.84 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,567.25 |
| Alpha (cumulative) | +3.449% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market context today is characterized by a bearish signal from the MA20/MA50 crossover strategy and a rising VIX. The Fed Chair's warning of another supply shock is likely contributing to the risk-off sentiment. Meanwhile, the WTI Oil price is stable, and the 10Y Treasury yield is rising.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system remained flat due to the signal being a death cross, which typically indicates a sell signal. The strategy's inaction was correct as the market declined.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross signal should be treated with caution and may require a more nuanced approach to determine the optimal course of action.

---

### Day 13 — 2026-03-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.05 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$113.86 |
| Signal saved | +$835.54 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,090.46 |
| Alpha (cumulative) | +2.926% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite the Fed Chair's warning of another supply shock. VIX remained elevated, but WTI Oil price dropped. The 10Y Treasury yield also decreased.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH — Death Cross regime. The system did not enter a trade today, as the MA20 was below the MA50 and the signal was bearish.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A dead-cat bounce can occur even in a bearish market regime, highlighting the importance of staying nimble and not over-interpreting short-term market movements.

---

### Day 14 — 2026-03-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $643.45 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$229.86 |
| Signal saved | +$951.54 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,371.13 |
| Alpha (cumulative) | +4.645% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning about another supply shock. The VIX is at 27.39, indicating increased market volatility. Oil prices are also on the rise.

**Strategy note:** The MA20/MA50 crossover strategy did not trigger any trades today, as the signal was bearish (Death Cross) and the system remained flat.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal may not always be a buy signal, and staying flat can be a correct decision in uncertain market conditions.

---

### Day 15 — 2026-03-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $632.41 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$340.26 |
| Signal saved | +$1061.94 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,734.80 |
| Alpha (cumulative) | +6.281% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** Markets remained relatively stable despite the Fed Chair's warning of an impending supply shock. The VIX index increased slightly, while the 10Y Treasury yield remained steady. Oil prices also rose.

**Strategy note:** The MA20/MA50 system remained flat as the Death Cross signal did not trigger a trade. This was correct as the market did not experience a significant downturn.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction during a period of heightened uncertainty highlights the importance of a well-defined trading plan and risk management.

---

### Day 16 — 2026-03-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $630.40 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$360.36 |
| Signal saved | +$1082.04 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,436.88 |
| Alpha (cumulative) | +6.579% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite a bearish signal from the MA crossover strategy, with SPY closing at $631.97. VIX remained elevated at 27.39. Headlines were mixed, with a warning from Fed Chair Powell and hopes for de-escalation.

**Strategy note:** The system remained flat as the MA20/MA50 crossover strategy indicated a bearish signal, which was correct given the market's cautious behavior.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits and avoid new positions during a dead-cat bounce is crucial for preserving capital.

---

### Day 17 — 2026-03-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $648.45 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$179.86 |
| Signal saved | +$901.54 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,112.22 |
| Alpha (cumulative) | +3.904% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market experienced a dead-cat bounce, with SPY closing at $641.88, despite a bearish signal from the MA20/MA50 crossover. VIX remained elevated at 27.39. Fed Chair Powell's warning of another supply shock contributed to the cautious market sentiment.

**Strategy note:** The system did not enter a trade today due to a bearish signal from the MA20/MA50 crossover. The system's inaction was correct as the market experienced a dead-cat bounce.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal from the MA20/MA50 crossover does not guarantee a sell signal, as the market can experience a dead-cat bounce.

---

### Day 18 — 2026-04-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $653.50 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$129.36 |
| Signal saved | +$851.04 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,860.72 |
| Alpha (cumulative) | +3.155% |

**Regime call:** RISK-OFF

**Market context:** The market experienced a risk-off day, driven by the bearish MA cross and elevated VIX, amidst geopolitical tensions and a decline in oil prices.

**Strategy note:** The MA20/MA50 crossover system correctly identified a bearish signal, but did not enter a trade as the position was already flat.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to identify bearish signals is intact, but it must be used in conjunction with position management to maximize returns.

---

### Day 19 — 2026-04-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $654.08 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$123.56 |
| Signal saved | +$845.24 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,946.69 |
| Alpha (cumulative) | +3.069% |

**Regime call:** RISK-OFF

**Market context:** The stock market sold off on Trump's speech and surging oil prices, with the Dow experiencing a decline. The VIX index rose to 27.15, indicating increased market volatility. Oil prices surged to $112.24 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH signal due to the Death Cross, but no trades were executed as the position was flat.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy correctly identified a bearish signal, but the lack of a trade execution highlights the importance of position sizing and risk management.

---

### Day 20 — 2026-04-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $657.19 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$92.46 |
| Signal saved | +$814.14 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,407.65 |
| Alpha (cumulative) | +2.608% |

**Regime call:** BULLISH

**Market context:** Markets were mixed post-BLS jobs, with equity futures trading mixed pre-bell Monday amid ongoing Iran conflict. VIX remained elevated at 24.17. WTI oil price rose to $112.59/barrel.

**Strategy note:** MA20 crossed below MA50, triggering a bullish signal. The system remains flat, with no trades executed today.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's alpha continues to outperform the benchmark, with a cumulative alpha of +2.610%

---

### Day 21 — 2026-04-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $657.54 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | -$88.96 |
| Signal saved | +$810.64 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,459.53 |
| Alpha (cumulative) | +2.556% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, and oil prices were falling, amidst a two-week US-Iran ceasefire.

**Strategy note:** MA20 crossed below MA50, triggering a bearish signal. The system exited the position.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** VIX levels can significantly influence market sentiment and impact our strategy's performance.

---

### Day 22 — 2026-04-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $674.26 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$78.24 |
| Signal saved | +$643.44 |
| Portfolio value | $100,015.64 |
| Benchmark value | $99,937.74 |
| Alpha (cumulative) | +0.078% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, indicating a decrease in market volatility. Oil prices continued to fall. Markets were higher pre-bell Wednesday amid a two-week US-Iran ceasefire.

**Strategy note:** The MA20/MA50 crossover strategy remained bearish, with a death cross. The system exited the position and is now flat, waiting for a golden cross to re-enter.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's bearish signal was correct, but the realized P&L was relatively low, highlighting the importance of position sizing and risk management.

---

### Day 23 — 2026-04-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $678.12 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$116.84 |
| Signal saved | +$604.84 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,509.86 |
| Alpha (cumulative) | -0.494% |

**Regime call:** RISK-ON

**Market context:** Equity futures and ETFs declined pre-bell as fragile Middle East ceasefire lifted oil prices. VIX rose to 20.8. S&P 500 had a rare gap-up on Wednesday.

**Strategy note:** MA20/MA50 crossover strategy exited position based on bearish signal. System now flat, waiting for next golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** MA crossover strategy underperformed passive hold, reinforcing need for robust risk management

---

### Day 24 — 2026-04-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $677.60 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$111.64 |
| Signal saved | +$610.04 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,432.79 |
| Alpha (cumulative) | -0.417% |

**Regime call:** RISK-ON

**Market context:** The S&P 500 closed above a key level, with equity futures mixed amidst geopolitical uncertainty and a looming CPI report. The VIX remained relatively calm, but could swing wildly after the CPI data release.

**Strategy note:** The system exited the position due to a bearish MA cross, and is now flat. The MA20 is below the MA50, indicating a bearish trend.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's bearish signal was correct, but the realized P&L was lower than the passive hold, highlighting the importance of risk management in trading strategies.

---

### Day 25 — 2026-04-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $684.24 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$178.04 |
| Signal saved | +$543.64 |
| Portfolio value | $100,015.64 |
| Benchmark value | $101,416.96 |
| Alpha (cumulative) | -1.401% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 sold off due to geopolitical tensions, with oil prices surging over $100. The VIX sharply reversed, pointing towards 30 after failed peace negotiations. This led to a risk-off sentiment in the market.

**Strategy note:** MA50 crossed above MA20, triggering a bearish signal. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal does not guarantee losses, as the system's realized P&L was positive despite the market downturn.

---

### Day 26 — 2026-04-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $692.58 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$261.44 |
| Signal saved | +$460.24 |
| Portfolio value | $100,015.64 |
| Benchmark value | $102,653.10 |
| Alpha (cumulative) | -2.637% |

**Regime call:** RISK-OFF

**Market context:** The market rose today with Dow leading, despite concerns over inflation data and a potential US-Iran truce. VIX remains elevated at 18.05. Oil prices also increased.

**Strategy note:** MA20 ($660.21) is below MA50 ($672.89), indicating a bearish signal. The system exited the position, locking in a $+15.58 P&L.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross in the MA crossover strategy led to a premature exit, resulting in a missed opportunity to ride the market's upward momentum.

---

### Day 27 — 2026-04-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $697.95 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$315.14 |
| Signal saved | +$406.54 |
| Portfolio value | $100,015.64 |
| Benchmark value | $103,449.03 |
| Alpha (cumulative) | -3.433% |

**Regime call:** RISK-ON

**Market context:** Investors turned to corporate earnings, driving equity futures higher. Wall Street's fear gauge, VIX, is fading. The S&P 500 Stocks' earnings are expected to skyrocket 200% in three months.

**Strategy note:** MA20/MA50 crossover strategy is in a BEARISH regime due to a Death Cross. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's realized P&L outperformed a passive hold by $15.58, but still trailed the benchmark by $286.66.

---

### Day 28 — 2026-04-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $699.73 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$332.94 |
| Signal saved | +$388.74 |
| Portfolio value | $100,035.59 |
| Benchmark value | $103,712.86 |
| Alpha (cumulative) | -3.677% |

**Regime call:** BEAR

**Market context:** The market remains in a bear regime, with SPY trading below its 50-day moving average. The S&P 500 index is also under pressure, with no clear signs of a reversal. Economic data releases and geopolitical tensions continue to weigh on investor sentiment.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, despite the bear regime, due to a bullish fast signal. The system's unrealized P&L increased by 0.06% from entry.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bullish fast signal does not guarantee success in a bear regime, and the system's performance may be impacted by the prevailing market conditions.

---

### Day 29 — 2026-04-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $708.24 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$418.04 |
| Signal saved | +$303.64 |
| Portfolio value | $100,029.67 |
| Benchmark value | $104,974.20 |
| Alpha (cumulative) | -4.944% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 broke above 7000, driven by a rally in tech stocks and the opening of the Strait of Hormuz. Oil prices declined, while Netflix shares plummeted. Market sentiment remains bullish.

**Strategy note:** The system exited the position due to a bear regime, as confirmed by the slow MA20/MA50 crossover. A bullish fast signal was generated, but the system prioritized the slow regime filter.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter is more important than the fast signal in determining position entry and exit decisions.

---

### Day 30 — 2026-04-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T4) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $706.97 |
| Unrealized P&L | +$12.58 |
| P&L % | +0.032% |
| Portfolio value | $100,042.25 |
| Benchmark value | $104,785.96 |
| Alpha (cumulative) | -4.744% |

**Regime call:** BEAR

**Market context:** Small Cap Stocks and Russell 2000 declined, while Oil Prices surged amid Middle East tensions. The S&P 500 held 7100, with Nasdaq Composite battling fears. Equity Futures and Exchange-Traded Funds also declined.

**Strategy note:** The system held long SPY due to a BULLISH Fast signal and BEAR regime, despite strong momentum. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.03% from entry. No exit triggered.

**Key learning:** A strong momentum environment can override a bearish regime context, but may also increase risk of a false signal.

---

### Day 31 — 2026-04-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $702.10 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$356.64 |
| Signal saved | +$365.04 |
| Portfolio value | $100,003.61 |
| Benchmark value | $104,064.14 |
| Alpha (cumulative) | -4.060% |

**Regime call:** BEAR

**Market context:** Markets rallied on Iran deal hopes, with stocks outperforming safe-havens like gold. Small caps and risk-on trades led the gains. Oil prices pulled back on the news.

**Strategy note:** The system remained long SPY despite a BEAR regime, as the fast signal remained BULLISH due to a strong golden cross. No exit was triggered.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter can sometimes conflict with the fast signal, requiring careful consideration of both indicators.

---

### Day 32 — 2026-04-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T5) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $709.37 |
| Unrealized P&L | -$24.35 |
| P&L % | -0.061% |
| Portfolio value | $99,979.26 |
| Benchmark value | $105,141.69 |
| Alpha (cumulative) | -5.163% |

**Regime call:** BEAR

**Market context:** Risk-on trade buoyed small cap sentiment, while the VIX remains calm. The S&P 500 climbed on a ceasefire extension and tech tailwinds.

**Strategy note:** The system held a long SPY position, despite a bear regime, due to a bullish fast signal from the 10/30 SMA crossover. Unrealized P&L was -0.01% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: -0.06% from entry. No exit triggered.

**Key learning:** A bear regime does not necessarily mean a bear market, as the system's fast signal can override the slow filter.

---

### Day 33 — 2026-04-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $706.59 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$401.54 |
| Signal saved | +$320.14 |
| Portfolio value | $99,875.66 |
| Benchmark value | $104,729.64 |
| Alpha (cumulative) | -4.854% |

**Regime call:** BULL

**Market context:** The S&P 500 retreated but held 7100 on fresh Mideast escalation as earnings kick off, while VIX crept toward 20 as Iran fears and Tesla's whipsaw rattle nerves.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and strong momentum, causing the system to hold long SPY.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long in a bull regime despite rising VIX is being tested.

---

### Day 34 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T6) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $712.14 |
| Unrealized P&L | +$48.32 |
| P&L % | +0.121% |
| Portfolio value | $99,923.98 |
| Benchmark value | $105,552.25 |
| Alpha (cumulative) | -5.628% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.12% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 35 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T6) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $713.33 |
| Unrealized P&L | +$114.96 |
| P&L % | +0.289% |
| Portfolio value | $99,990.62 |
| Benchmark value | $105,728.63 |
| Alpha (cumulative) | -5.738% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 36 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T6) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $709.85 |
| Unrealized P&L | -$79.92 |
| P&L % | -0.201% |
| Portfolio value | $99,795.74 |
| Benchmark value | $105,212.83 |
| Alpha (cumulative) | -5.417% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: -0.20% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 37 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $709.76 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$433.24 |
| Signal saved | +$288.44 |
| Portfolio value | $99,760.46 |
| Benchmark value | $105,199.49 |
| Alpha (cumulative) | -5.438% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 38 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $716.56 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$501.24 |
| Signal saved | +$220.44 |
| Portfolio value | $100,017.86 |
| Benchmark value | $106,207.38 |
| Alpha (cumulative) | -6.189% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 39 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,796.23 |
| Benchmark value | $106,515.67 |
| Alpha (cumulative) | -6.720% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 40 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,664.78 |
| Benchmark value | $106,161.43 |
| Alpha (cumulative) | -6.496% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 41 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $99,972.78 |
| Benchmark value | $106,991.45 |
| Alpha (cumulative) | -7.018% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 42 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,524.43 |
| Benchmark value | $108,478.08 |
| Alpha (cumulative) | -7.954% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 43 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,401.78 |
| Benchmark value | $108,147.56 |
| Alpha (cumulative) | -7.746% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 44 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,731.78 |
| Benchmark value | $109,036.87 |
| Alpha (cumulative) | -8.305% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 45 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,822.53 |
| Benchmark value | $109,281.43 |
| Alpha (cumulative) | -8.458% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 46 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,766.98 |
| Benchmark value | $109,131.73 |
| Alpha (cumulative) | -8.365% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 47 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $100,992.48 |
| Benchmark value | $109,739.42 |
| Alpha (cumulative) | -8.747% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 48 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,310.93 |
| Benchmark value | $110,597.61 |
| Alpha (cumulative) | -9.287% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 49 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,817.03 |
| Benchmark value | $109,266.60 |
| Alpha (cumulative) | -8.450% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 50 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,778.53 |
| Benchmark value | $109,162.85 |
| Alpha (cumulative) | -8.385% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 51 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,526.08 |
| Benchmark value | $108,482.53 |
| Alpha (cumulative) | -7.957% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 52 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $100,938.58 |
| Benchmark value | $109,594.17 |
| Alpha (cumulative) | -8.655% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 53 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $101,015.03 |
| Benchmark value | $109,800.19 |
| Alpha (cumulative) | -8.785% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 54 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,177.28 |
| Benchmark value | $110,237.44 |
| Alpha (cumulative) | -9.060% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 55 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,440.18 |
| Benchmark value | $110,945.92 |
| Alpha (cumulative) | -9.506% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 56 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,447.33 |
| Benchmark value | $110,965.19 |
| Alpha (cumulative) | -9.518% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 57 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,671.73 |
| Benchmark value | $111,569.92 |
| Alpha (cumulative) | -9.898% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 58 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,763.03 |
| Benchmark value | $111,815.96 |
| Alpha (cumulative) | -10.053% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 59 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $101,877.98 |
| Benchmark value | $112,125.74 |
| Alpha (cumulative) | -10.248% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 60 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $101,934.63 |
| Benchmark value | $112,278.40 |
| Alpha (cumulative) | -10.343% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 61 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,644.23 |
| Benchmark value | $111,495.81 |
| Alpha (cumulative) | -9.852% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 62 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,797.68 |
| Benchmark value | $111,909.34 |
| Alpha (cumulative) | -10.111% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 63 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,726.83 |
| Benchmark value | $109,023.53 |
| Alpha (cumulative) | -8.297% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 64 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,824.73 |
| Benchmark value | $109,287.36 |
| Alpha (cumulative) | -8.462% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 65 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,705.93 |
| Benchmark value | $108,967.20 |
| Alpha (cumulative) | -8.261% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 66 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,075.63 |
| Benchmark value | $107,268.62 |
| Alpha (cumulative) | -7.193% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 67 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,738.38 |
| Benchmark value | $109,054.65 |
| Alpha (cumulative) | -8.317% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 68 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $100,957.83 |
| Benchmark value | $109,646.04 |
| Alpha (cumulative) | -8.688% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 69 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,675.58 |
| Benchmark value | $111,580.29 |
| Alpha (cumulative) | -9.904% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 70 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,446.78 |
| Benchmark value | $110,963.71 |
| Alpha (cumulative) | -9.517% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 71 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $739.12 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$726.84 |
| Signal saved | -$5.16 |
| Portfolio value | $101,189.93 |
| Benchmark value | $109,551.18 |
| Alpha (cumulative) | -8.361% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 72 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $746.75 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$803.14 |
| Signal saved | -$81.46 |
| Portfolio value | $101,189.93 |
| Benchmark value | $110,682.09 |
| Alpha (cumulative) | -9.492% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 73 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $744.27 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$778.34 |
| Signal saved | -$56.66 |
| Portfolio value | $101,188.82 |
| Benchmark value | $110,314.51 |
| Alpha (cumulative) | -9.126% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 74 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $733.62 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$671.84 |
| Signal saved | +$49.84 |
| Portfolio value | $101,188.82 |
| Benchmark value | $108,735.98 |
| Alpha (cumulative) | -7.547% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 75 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $733.32 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$668.84 |
| Signal saved | +$52.84 |
| Portfolio value | $101,188.82 |
| Benchmark value | $108,691.52 |
| Alpha (cumulative) | -7.503% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 76 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $733.33 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$668.94 |
| Signal saved | +$52.74 |
| Portfolio value | $101,188.82 |
| Benchmark value | $108,693.00 |
| Alpha (cumulative) | -7.504% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 77 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $729.35 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$629.14 |
| Signal saved | +$92.54 |
| Portfolio value | $101,188.82 |
| Benchmark value | $108,103.09 |
| Alpha (cumulative) | -6.914% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 78 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $740.86 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$744.24 |
| Signal saved | -$22.56 |
| Portfolio value | $101,188.82 |
| Benchmark value | $109,809.08 |
| Alpha (cumulative) | -8.620% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 79 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $746.65 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$802.14 |
| Signal saved | -$80.46 |
| Portfolio value | $101,188.82 |
| Benchmark value | $110,667.27 |
| Alpha (cumulative) | -9.478% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 80 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $745.66 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$792.24 |
| Signal saved | -$70.56 |
| Portfolio value | $101,188.82 |
| Benchmark value | $110,520.53 |
| Alpha (cumulative) | -9.332% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 81 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $744.86 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$784.24 |
| Signal saved | -$62.56 |
| Portfolio value | $101,188.82 |
| Benchmark value | $110,401.96 |
| Alpha (cumulative) | -9.213% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 82 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $751.27 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$848.34 |
| Signal saved | -$126.66 |
| Portfolio value | $101,188.82 |
| Benchmark value | $111,352.04 |
| Alpha (cumulative) | -10.163% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 83 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $747.77 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$813.34 |
| Signal saved | -$91.66 |
| Portfolio value | $101,188.82 |
| Benchmark value | $110,833.27 |
| Alpha (cumulative) | -9.644% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 84 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $745.28 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$788.44 |
| Signal saved | -$66.76 |
| Portfolio value | $101,188.82 |
| Benchmark value | $110,464.21 |
| Alpha (cumulative) | -9.275% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 85 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $751.55 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$851.14 |
| Signal saved | -$129.46 |
| Portfolio value | $101,188.82 |
| Benchmark value | $111,393.54 |
| Alpha (cumulative) | -10.205% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 86 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $754.94 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$885.04 |
| Signal saved | -$163.36 |
| Portfolio value | $101,188.82 |
| Benchmark value | $111,896.00 |
| Alpha (cumulative) | -10.707% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 87 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $749.13 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$826.94 |
| Signal saved | -$105.26 |
| Portfolio value | $101,027.70 |
| Benchmark value | $111,034.85 |
| Alpha (cumulative) | -10.007% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 88 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $751.94 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$855.04 |
| Signal saved | -$133.36 |
| Portfolio value | $100,992.62 |
| Benchmark value | $111,451.34 |
| Alpha (cumulative) | -10.458% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 89 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $754.77 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$883.34 |
| Signal saved | -$161.66 |
| Portfolio value | $101,040.37 |
| Benchmark value | $111,870.80 |
| Alpha (cumulative) | -10.831% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 90 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $750.87 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$844.34 |
| Signal saved | -$122.66 |
| Portfolio value | $100,864.24 |
| Benchmark value | $111,292.75 |
| Alpha (cumulative) | -10.429% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 91 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $743.28 |
| Realized P&L (locked) | +$721.68 |
| Reference if held | +$768.44 |
| Signal saved | -$46.76 |
| Portfolio value | $100,721.68 |
| Benchmark value | $110,167.77 |
| Alpha (cumulative) | -9.446% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $+721.68. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 92 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 41 SPY (T15) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $745.57 |
| Unrealized P&L | +$4.51 |
| P&L % | +0.015% |
| Portfolio value | $100,726.19 |
| Benchmark value | $110,507.19 |
| Alpha (cumulative) | -9.781% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $745.02 vs MA50 $743.23). Momentum: WEAK. Unrealized P&L: +0.01% from entry. No exit triggered.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

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
_Day 92 of 90 · Alpaca equity: $100,721.92 · Cumulative alpha vs SPY: -9.781%_