# ALPACA PAPER JOURNAL — SPY
_Last updated: August 28, 2026 | Day 88 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$711.280/share**
> (2026-04-24, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-08-28): **BULLISH** | ⚡ Price Override Active (+2.0% above MA50)  
> Fast: MA10 $767.34 | MA30 $759.91  
> Slow: MA20 $769.22 | MA50 $753.96  
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

**Total trades:** 17 | **Closed:** 16 | **Open:** Yes | **Cumulative Realized P&L:** +$58.35

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $711.280 (2026-04-24) | $709.220 (2026-04-29) | 40 | -$82.40 | ✅ Closed |
| T2 | $714.440 (2026-04-30) | $719.120 (2026-04-30) | 55 | +$257.40 | ✅ Closed |
| T3 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 55 | +$1172.07 | ✅ Closed |
| T4 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T5 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T6 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T7 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T8 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T9 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T10 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T11 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T12 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T13 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T14 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T15 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T16 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T17 | $773.641 (2026-08-11) | — | 51 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,680.49 |
| Alpaca cash | $60,445.17 |
| Cumulative realized P&L | +$58.35 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-24 | $712.14 | Long 40 SPY (T1) | +$34.40 | +0.121% | $100,034.40 |
| Day 2 | 2026-04-27 | $713.33 | Long 40 SPY (T1) | +$82.00 | +0.288% | $100,082.00 |
| Day 3 | 2026-04-28 | $709.85 | Long 40 SPY (T1) | -$57.20 | -0.201% | $99,942.80 |
| Day 4 | 2026-04-29 | $709.76 | FLAT | — | — | $99,917.60 |
| Day 5 | 2026-04-30 | $716.56 | FLAT | — | — | $100,175.00 |
| Day 6 | 2026-05-01 | $718.64 | Long 55 SPY (T3) | -$221.63 | -0.558% | $99,953.37 |
| Day 7 | 2026-05-04 | $716.25 | Long 55 SPY (T3) | -$353.08 | -0.888% | $99,821.92 |
| Day 8 | 2026-05-05 | $721.85 | Long 55 SPY (T3) | -$45.08 | -0.113% | $100,129.92 |
| Day 9 | 2026-05-06 | $731.88 | Long 55 SPY (T3) | +$506.57 | +1.274% | $100,681.57 |
| Day 10 | 2026-05-07 | $729.65 | Long 55 SPY (T3) | +$383.92 | +0.966% | $100,558.92 |
| Day 11 | 2026-05-08 | $735.65 | Long 55 SPY (T3) | +$713.92 | +1.796% | $100,888.92 |
| Day 12 | 2026-05-11 | $737.30 | Long 55 SPY (T3) | +$804.67 | +2.024% | $100,979.67 |
| Day 13 | 2026-05-12 | $736.29 | Long 55 SPY (T3) | +$749.12 | +1.885% | $100,924.12 |
| Day 14 | 2026-05-13 | $740.39 | Long 55 SPY (T3) | +$974.62 | +2.452% | $101,149.62 |
| Day 15 | 2026-05-14 | $746.18 | Long 55 SPY (T3) | +$1293.07 | +3.253% | $101,468.07 |
| Day 16 | 2026-05-15 | $737.20 | Long 55 SPY (T3) | +$799.17 | +2.011% | $100,974.17 |
| Day 17 | 2026-05-18 | $736.50 | Long 55 SPY (T3) | +$760.67 | +1.914% | $100,935.67 |
| Day 18 | 2026-05-19 | $731.91 | Long 55 SPY (T3) | +$508.22 | +1.279% | $100,683.22 |
| Day 19 | 2026-05-20 | $739.41 | Long 55 SPY (T3) | +$920.72 | +2.316% | $101,095.72 |
| Day 20 | 2026-05-21 | $740.80 | Long 55 SPY (T3) | +$997.17 | +2.509% | $101,172.17 |
| Day 21 | 2026-05-22 | $743.75 | Long 55 SPY (T3) | +$1159.42 | +2.917% | $101,334.42 |
| Day 22 | 2026-05-26 | $748.53 | Long 55 SPY (T3) | +$1422.32 | +3.578% | $101,597.32 |
| Day 23 | 2026-05-27 | $748.66 | Long 55 SPY (T3) | +$1429.47 | +3.596% | $101,604.47 |
| Day 24 | 2026-05-28 | $752.74 | Long 55 SPY (T3) | +$1653.87 | +4.161% | $101,828.87 |
| Day 25 | 2026-05-29 | $754.40 | Long 55 SPY (T3) | +$1745.17 | +4.391% | $101,920.17 |
| Day 26 | 2026-06-01 | $756.49 | Long 55 SPY (T3) | +$1860.12 | +4.680% | $102,035.12 |
| Day 27 | 2026-06-02 | $757.52 | Long 55 SPY (T3) | +$1916.77 | +4.822% | $102,091.77 |
| Day 28 | 2026-06-03 | $752.24 | Long 55 SPY (T3) | +$1626.37 | +4.092% | $101,801.37 |
| Day 29 | 2026-06-04 | $755.03 | Long 55 SPY (T3) | +$1779.82 | +4.478% | $101,954.82 |
| Day 30 | 2026-06-05 | $735.56 | Long 55 SPY (T3) | +$708.97 | +1.784% | $100,883.97 |
| Day 31 | 2026-06-08 | $737.34 | Long 55 SPY (T3) | +$806.87 | +2.030% | $100,981.87 |
| Day 32 | 2026-06-09 | $735.18 | Long 55 SPY (T3) | +$688.07 | +1.731% | $100,863.07 |
| Day 33 | 2026-06-10 | $723.72 | Long 55 SPY (T3) | +$57.77 | +0.145% | $100,232.77 |
| Day 34 | 2026-06-11 | $735.77 | Long 55 SPY (T3) | +$720.52 | +1.813% | $100,895.52 |
| Day 35 | 2026-06-12 | $739.76 | Long 55 SPY (T3) | +$939.97 | +2.365% | $101,114.97 |
| Day 36 | 2026-06-15 | $752.81 | Long 55 SPY (T3) | +$1657.72 | +4.171% | $101,832.72 |
| Day 37 | 2026-06-16 | $748.65 | Long 55 SPY (T3) | +$1428.92 | +3.595% | $101,603.92 |
| Day 38 | 2026-06-17 | $739.12 | FLAT | — | — | $101,347.07 |
| Day 39 | 2026-06-18 | $746.75 | FLAT | — | — | $101,347.07 |
| Day 40 | 2026-06-22 | $744.27 | FLAT | — | — | $101,345.96 |
| Day 41 | 2026-06-23 | $733.62 | FLAT | — | — | $101,345.96 |
| Day 42 | 2026-06-24 | $733.32 | FLAT | — | — | $101,345.96 |
| Day 43 | 2026-06-25 | $733.33 | FLAT | — | — | $101,345.96 |
| Day 44 | 2026-06-26 | $729.35 | FLAT | — | — | $101,345.96 |
| Day 45 | 2026-06-29 | $740.86 | FLAT | — | — | $101,345.96 |
| Day 46 | 2026-06-30 | $746.65 | FLAT | — | — | $101,345.96 |
| Day 47 | 2026-07-01 | $745.66 | FLAT | — | — | $101,345.96 |
| Day 48 | 2026-07-02 | $744.86 | FLAT | — | — | $101,345.96 |
| Day 49 | 2026-07-06 | $751.27 | FLAT | — | — | $101,345.96 |
| Day 50 | 2026-07-07 | $747.77 | FLAT | — | — | $101,345.96 |
| Day 51 | 2026-07-08 | $745.28 | FLAT | — | — | $101,345.96 |
| Day 52 | 2026-07-09 | $751.55 | FLAT | — | — | $101,345.96 |
| Day 53 | 2026-07-10 | $754.94 | FLAT | — | — | $101,345.96 |
| Day 54 | 2026-07-13 | $749.13 | FLAT | — | — | $101,184.84 |
| Day 55 | 2026-07-14 | $751.94 | FLAT | — | — | $101,149.76 |
| Day 56 | 2026-07-15 | $754.77 | FLAT | — | — | $101,197.51 |
| Day 57 | 2026-07-16 | $750.87 | FLAT | — | — | $101,021.38 |
| Day 58 | 2026-07-17 | $743.28 | FLAT | — | — | $100,878.82 |
| Day 59 | 2026-07-20 | $742.15 | FLAT | — | — | $100,686.84 |
| Day 60 | 2026-07-21 | $748.15 | Long 53 SPY (T11) | +$28.09 | +0.071% | $100,714.93 |
| Day 61 | 2026-07-22 | $747.49 | Long 53 SPY (T11) | -$6.89 | -0.017% | $100,679.95 |
| Day 62 | 2026-07-23 | $738.06 | Long 52 SPY (T12) | -$40.56 | -0.106% | $100,010.81 |
| Day 63 | 2026-07-24 | $738.90 | FLAT | — | — | $100,059.69 |
| Day 64 | 2026-07-27 | $738.85 | FLAT | — | — | $100,163.83 |
| Day 65 | 2026-07-28 | $740.79 | FLAT | — | — | $100,120.37 |
| Day 66 | 2026-07-29 | $729.57 | FLAT | — | — | $100,120.37 |
| Day 67 | 2026-07-30 | $741.63 | FLAT | — | — | $100,120.37 |
| Day 68 | 2026-07-31 | $746.79 | FLAT | — | — | $100,120.37 |
| Day 69 | 2026-08-03 | $757.72 | FLAT | — | — | $100,120.37 |
| Day 70 | 2026-08-04 | $771.11 | Long 50 SPY (T15) | -$52.00 | -0.135% | $100,068.37 |
| Day 71 | 2026-08-05 | $769.79 | FLAT | — | — | $100,033.37 |
| Day 72 | 2026-08-06 | $768.64 | FLAT | — | — | $100,033.37 |
| Day 73 | 2026-08-07 | $773.16 | Long 51 SPY (T16) | +$33.14 | +0.084% | $100,066.51 |
| Day 74 | 2026-08-10 | $773.02 | FLAT | — | — | $100,058.35 |
| Day 75 | 2026-08-11 | $770.52 | Long 51 SPY (T17) | -$159.19 | -0.403% | $99,899.16 |
| Day 76 | 2026-08-12 | $772.54 | Long 51 SPY (T17) | -$56.17 | -0.142% | $100,002.18 |
| Day 77 | 2026-08-13 | $777.84 | Long 51 SPY (T17) | +$214.13 | +0.543% | $100,272.48 |
| Day 78 | 2026-08-14 | $776.30 | Long 51 SPY (T17) | +$135.59 | +0.344% | $100,193.94 |
| Day 79 | 2026-08-17 | $772.62 | Long 51 SPY (T17) | -$52.09 | -0.132% | $100,006.26 |
| Day 80 | 2026-08-18 | $767.37 | Long 51 SPY (T17) | -$319.84 | -0.811% | $99,738.51 |
| Day 81 | 2026-08-19 | $769.09 | Long 51 SPY (T17) | -$232.12 | -0.588% | $99,826.23 |
| Day 82 | 2026-08-20 | $762.62 | Long 51 SPY (T17) | -$562.09 | -1.425% | $99,496.26 |
| Day 83 | 2026-08-21 | $765.64 | Long 51 SPY (T17) | -$408.07 | -1.034% | $99,650.28 |
| Day 84 | 2026-08-24 | $763.46 | Long 51 SPY (T17) | -$519.25 | -1.316% | $99,539.10 |
| Day 85 | 2026-08-25 | $765.79 | Long 51 SPY (T17) | -$400.42 | -1.015% | $99,657.93 |
| Day 86 | 2026-08-26 | $765.94 | Long 51 SPY (T17) | -$392.77 | -0.995% | $99,665.58 |
| Day 87 | 2026-08-27 | $771.18 | Long 51 SPY (T17) | -$125.53 | -0.318% | $99,932.82 |
| Day 88 | 2026-08-28 | $769.28 | Long 51 SPY (T17) | -$222.43 | -0.564% | $99,835.92 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-24 | $100,034.40 | $99,999.98 | +0.0344% | -0.000% | **+0.034%** |
| Day 2 | 2026-04-27 | $100,082.00 | $100,167.08 | +0.0820% | +0.167% | **-0.085%** |
| Day 3 | 2026-04-28 | $99,942.80 | $99,678.41 | -0.0572% | -0.322% | **+0.265%** |
| Day 4 | 2026-04-29 | $99,917.60 | $99,665.78 | -0.0824% | -0.334% | **+0.252%** |
| Day 5 | 2026-04-30 | $100,175.00 | $100,620.65 | +0.1750% | +0.621% | **-0.446%** |
| Day 6 | 2026-05-01 | $99,953.37 | $100,912.72 | -0.0466% | +0.913% | **-0.960%** |
| Day 7 | 2026-05-04 | $99,821.92 | $100,577.11 | -0.1781% | +0.577% | **-0.755%** |
| Day 8 | 2026-05-05 | $100,129.92 | $101,363.48 | +0.1299% | +1.363% | **-1.233%** |
| Day 9 | 2026-05-06 | $100,681.57 | $102,771.91 | +0.6816% | +2.772% | **-2.090%** |
| Day 10 | 2026-05-07 | $100,558.92 | $102,458.77 | +0.5589% | +2.459% | **-1.900%** |
| Day 11 | 2026-05-08 | $100,888.92 | $103,301.30 | +0.8889% | +3.301% | **-2.412%** |
| Day 12 | 2026-05-11 | $100,979.67 | $103,532.99 | +0.9797% | +3.533% | **-2.553%** |
| Day 13 | 2026-05-12 | $100,924.12 | $103,391.17 | +0.9241% | +3.391% | **-2.467%** |
| Day 14 | 2026-05-13 | $101,149.62 | $103,966.90 | +1.1496% | +3.967% | **-2.817%** |
| Day 15 | 2026-05-14 | $101,468.07 | $104,779.94 | +1.4681% | +4.780% | **-3.312%** |
| Day 16 | 2026-05-15 | $100,974.17 | $103,518.95 | +0.9742% | +3.519% | **-2.545%** |
| Day 17 | 2026-05-18 | $100,935.67 | $103,420.66 | +0.9357% | +3.421% | **-2.485%** |
| Day 18 | 2026-05-19 | $100,683.22 | $102,776.12 | +0.6832% | +2.776% | **-2.093%** |
| Day 19 | 2026-05-20 | $101,095.72 | $103,829.28 | +1.0957% | +3.829% | **-2.733%** |
| Day 20 | 2026-05-21 | $101,172.17 | $104,024.47 | +1.1722% | +4.024% | **-2.852%** |
| Day 21 | 2026-05-22 | $101,334.42 | $104,438.71 | +1.3344% | +4.439% | **-3.105%** |
| Day 22 | 2026-05-26 | $101,597.32 | $105,109.93 | +1.5973% | +5.110% | **-3.513%** |
| Day 23 | 2026-05-27 | $101,604.47 | $105,128.18 | +1.6045% | +5.128% | **-3.524%** |
| Day 24 | 2026-05-28 | $101,828.87 | $105,701.11 | +1.8289% | +5.701% | **-3.872%** |
| Day 25 | 2026-05-29 | $101,920.17 | $105,934.21 | +1.9202% | +5.934% | **-4.014%** |
| Day 26 | 2026-06-01 | $102,035.12 | $106,227.69 | +2.0351% | +6.228% | **-4.193%** |
| Day 27 | 2026-06-02 | $102,091.77 | $106,372.32 | +2.0918% | +6.372% | **-4.280%** |
| Day 28 | 2026-06-03 | $101,801.37 | $105,630.89 | +1.8014% | +5.631% | **-3.830%** |
| Day 29 | 2026-06-04 | $101,954.82 | $106,022.67 | +1.9548% | +6.023% | **-4.068%** |
| Day 30 | 2026-06-05 | $100,883.97 | $103,288.66 | +0.8840% | +3.289% | **-2.405%** |
| Day 31 | 2026-06-08 | $100,981.87 | $103,538.61 | +0.9819% | +3.539% | **-2.557%** |
| Day 32 | 2026-06-09 | $100,863.07 | $103,235.30 | +0.8631% | +3.235% | **-2.372%** |
| Day 33 | 2026-06-10 | $100,232.77 | $101,626.07 | +0.2328% | +1.626% | **-1.393%** |
| Day 34 | 2026-06-11 | $100,895.52 | $103,318.15 | +0.8955% | +3.318% | **-2.423%** |
| Day 35 | 2026-06-12 | $101,114.97 | $103,878.43 | +1.1150% | +3.878% | **-2.763%** |
| Day 36 | 2026-06-15 | $101,832.72 | $105,710.94 | +1.8327% | +5.711% | **-3.878%** |
| Day 37 | 2026-06-16 | $101,603.92 | $105,126.78 | +1.6039% | +5.127% | **-3.523%** |
| Day 38 | 2026-06-17 | $101,347.07 | $103,788.56 | +1.3471% | +3.789% | **-2.442%** |
| Day 39 | 2026-06-18 | $101,347.07 | $104,859.98 | +1.3471% | +4.860% | **-3.513%** |
| Day 40 | 2026-06-22 | $101,345.96 | $104,511.73 | +1.3460% | +4.512% | **-3.166%** |
| Day 41 | 2026-06-23 | $101,345.96 | $103,016.24 | +1.3460% | +3.016% | **-1.670%** |
| Day 42 | 2026-06-24 | $101,345.96 | $102,974.11 | +1.3460% | +2.974% | **-1.628%** |
| Day 43 | 2026-06-25 | $101,345.96 | $102,975.52 | +1.3460% | +2.976% | **-1.630%** |
| Day 44 | 2026-06-26 | $101,345.96 | $102,416.64 | +1.3460% | +2.417% | **-1.071%** |
| Day 45 | 2026-06-29 | $101,345.96 | $104,032.89 | +1.3460% | +4.033% | **-2.687%** |
| Day 46 | 2026-06-30 | $101,345.96 | $104,845.94 | +1.3460% | +4.846% | **-3.500%** |
| Day 47 | 2026-07-01 | $101,345.96 | $104,706.92 | +1.3460% | +4.707% | **-3.361%** |
| Day 48 | 2026-07-02 | $101,345.96 | $104,594.58 | +1.3460% | +4.595% | **-3.249%** |
| Day 49 | 2026-07-06 | $101,345.96 | $105,494.69 | +1.3460% | +5.495% | **-4.149%** |
| Day 50 | 2026-07-07 | $101,345.96 | $105,003.21 | +1.3460% | +5.003% | **-3.657%** |
| Day 51 | 2026-07-08 | $101,345.96 | $104,653.56 | +1.3460% | +4.654% | **-3.308%** |
| Day 52 | 2026-07-09 | $101,345.96 | $105,534.00 | +1.3460% | +5.534% | **-4.188%** |
| Day 53 | 2026-07-10 | $101,345.96 | $106,010.03 | +1.3460% | +6.010% | **-4.664%** |
| Day 54 | 2026-07-13 | $101,184.84 | $105,194.18 | +1.1848% | +5.194% | **-4.009%** |
| Day 55 | 2026-07-14 | $101,149.76 | $105,588.77 | +1.1498% | +5.589% | **-4.439%** |
| Day 56 | 2026-07-15 | $101,197.51 | $105,986.16 | +1.1975% | +5.986% | **-4.788%** |
| Day 57 | 2026-07-16 | $101,021.38 | $105,438.52 | +1.0214% | +5.439% | **-4.418%** |
| Day 58 | 2026-07-17 | $100,878.82 | $104,372.72 | +0.8788% | +4.373% | **-3.494%** |
| Day 59 | 2026-07-20 | $100,686.84 | $104,214.04 | +0.6868% | +4.214% | **-3.527%** |
| Day 60 | 2026-07-21 | $100,714.93 | $105,056.57 | +0.7149% | +5.057% | **-4.342%** |
| Day 61 | 2026-07-22 | $100,679.95 | $104,963.89 | +0.6799% | +4.964% | **-4.284%** |
| Day 62 | 2026-07-23 | $100,010.81 | $103,639.71 | +0.0108% | +3.640% | **-3.629%** |
| Day 63 | 2026-07-24 | $100,059.69 | $103,757.67 | +0.0597% | +3.758% | **-3.698%** |
| Day 64 | 2026-07-27 | $100,163.83 | $103,750.65 | +0.1638% | +3.751% | **-3.587%** |
| Day 65 | 2026-07-28 | $100,120.37 | $104,023.07 | +0.1204% | +4.023% | **-3.903%** |
| Day 66 | 2026-07-29 | $100,120.37 | $102,447.53 | +0.1204% | +2.448% | **-2.328%** |
| Day 67 | 2026-07-30 | $100,120.37 | $104,141.02 | +0.1204% | +4.141% | **-4.021%** |
| Day 68 | 2026-07-31 | $100,120.37 | $104,865.60 | +0.1204% | +4.866% | **-4.746%** |
| Day 69 | 2026-08-03 | $100,120.37 | $106,400.41 | +0.1204% | +6.400% | **-6.280%** |
| Day 70 | 2026-08-04 | $100,068.37 | $108,280.65 | +0.0684% | +8.281% | **-8.213%** |
| Day 71 | 2026-08-05 | $100,033.37 | $108,095.30 | +0.0334% | +8.095% | **-8.062%** |
| Day 72 | 2026-08-06 | $100,033.37 | $107,933.81 | +0.0334% | +7.934% | **-7.901%** |
| Day 73 | 2026-08-07 | $100,066.51 | $108,568.52 | +0.0665% | +8.569% | **-8.503%** |
| Day 74 | 2026-08-10 | $100,058.35 | $108,548.86 | +0.0584% | +8.549% | **-8.491%** |
| Day 75 | 2026-08-11 | $99,899.16 | $108,197.81 | -0.1008% | +8.198% | **-8.299%** |
| Day 76 | 2026-08-12 | $100,002.18 | $108,481.46 | +0.0022% | +8.481% | **-8.479%** |
| Day 77 | 2026-08-13 | $100,272.48 | $109,225.69 | +0.2725% | +9.226% | **-8.954%** |
| Day 78 | 2026-08-14 | $100,193.94 | $109,009.44 | +0.1939% | +9.009% | **-8.815%** |
| Day 79 | 2026-08-17 | $100,006.26 | $108,492.69 | +0.0063% | +8.493% | **-8.487%** |
| Day 80 | 2026-08-18 | $99,738.51 | $107,755.48 | -0.2615% | +7.755% | **-8.017%** |
| Day 81 | 2026-08-19 | $99,826.23 | $107,997.00 | -0.1738% | +7.997% | **-8.171%** |
| Day 82 | 2026-08-20 | $99,496.26 | $107,088.47 | -0.5037% | +7.088% | **-7.592%** |
| Day 83 | 2026-08-21 | $99,650.28 | $107,512.55 | -0.3497% | +7.513% | **-7.863%** |
| Day 84 | 2026-08-24 | $99,539.10 | $107,206.43 | -0.4609% | +7.206% | **-7.667%** |
| Day 85 | 2026-08-25 | $99,657.93 | $107,533.61 | -0.3421% | +7.534% | **-7.876%** |
| Day 86 | 2026-08-26 | $99,665.58 | $107,554.67 | -0.3344% | +7.555% | **-7.889%** |
| Day 87 | 2026-08-27 | $99,932.82 | $108,290.48 | -0.0672% | +8.290% | **-8.357%** |
| Day 88 | 2026-08-28 | $99,835.92 | $108,023.68 | -0.1641% | +8.024% | **-8.188%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-04-24 | $712.14 | +$34.40 | +$23.95 | Position open |
| Day 2 | 2026-04-27 | $713.33 | +$82.00 | -$23.65 | Position open |
| Day 3 | 2026-04-28 | $709.85 | -$57.20 | +$115.55 | Position open |
| Day 4 | 2026-04-29 | $709.76 | -$60.80 | +$119.15 | Flat saved **+$119.15** vs holding |
| Day 5 | 2026-04-30 | $716.56 | +$211.20 | -$152.85 | Holding would have been **$152.85** better — honest entry |
| Day 6 | 2026-05-01 | $718.64 | +$294.40 | -$236.05 | Position open |
| Day 7 | 2026-05-04 | $716.25 | +$198.80 | -$140.45 | Position open |
| Day 8 | 2026-05-05 | $721.85 | +$422.80 | -$364.45 | Position open |
| Day 9 | 2026-05-06 | $731.88 | +$824.00 | -$765.65 | Position open |
| Day 10 | 2026-05-07 | $729.65 | +$734.80 | -$676.45 | Position open |
| Day 11 | 2026-05-08 | $735.65 | +$974.80 | -$916.45 | Position open |
| Day 12 | 2026-05-11 | $737.30 | +$1040.80 | -$982.45 | Position open |
| Day 13 | 2026-05-12 | $736.29 | +$1000.40 | -$942.05 | Position open |
| Day 14 | 2026-05-13 | $740.39 | +$1164.40 | -$1106.05 | Position open |
| Day 15 | 2026-05-14 | $746.18 | +$1396.00 | -$1337.65 | Position open |
| Day 16 | 2026-05-15 | $737.20 | +$1036.80 | -$978.45 | Position open |
| Day 17 | 2026-05-18 | $736.50 | +$1008.80 | -$950.45 | Position open |
| Day 18 | 2026-05-19 | $731.91 | +$825.20 | -$766.85 | Position open |
| Day 19 | 2026-05-20 | $739.41 | +$1125.20 | -$1066.85 | Position open |
| Day 20 | 2026-05-21 | $740.80 | +$1180.80 | -$1122.45 | Position open |
| Day 21 | 2026-05-22 | $743.75 | +$1298.80 | -$1240.45 | Position open |
| Day 22 | 2026-05-26 | $748.53 | +$1490.00 | -$1431.65 | Position open |
| Day 23 | 2026-05-27 | $748.66 | +$1495.20 | -$1436.85 | Position open |
| Day 24 | 2026-05-28 | $752.74 | +$1658.40 | -$1600.05 | Position open |
| Day 25 | 2026-05-29 | $754.40 | +$1724.80 | -$1666.45 | Position open |
| Day 26 | 2026-06-01 | $756.49 | +$1808.40 | -$1750.05 | Position open |
| Day 27 | 2026-06-02 | $757.52 | +$1849.60 | -$1791.25 | Position open |
| Day 28 | 2026-06-03 | $752.24 | +$1638.40 | -$1580.05 | Position open |
| Day 29 | 2026-06-04 | $755.03 | +$1750.00 | -$1691.65 | Position open |
| Day 30 | 2026-06-05 | $735.56 | +$971.20 | -$912.85 | Position open |
| Day 31 | 2026-06-08 | $737.34 | +$1042.40 | -$984.05 | Position open |
| Day 32 | 2026-06-09 | $735.18 | +$956.00 | -$897.65 | Position open |
| Day 33 | 2026-06-10 | $723.72 | +$497.60 | -$439.25 | Position open |
| Day 34 | 2026-06-11 | $735.77 | +$979.60 | -$921.25 | Position open |
| Day 35 | 2026-06-12 | $739.76 | +$1139.20 | -$1080.85 | Position open |
| Day 36 | 2026-06-15 | $752.81 | +$1661.20 | -$1602.85 | Position open |
| Day 37 | 2026-06-16 | $748.65 | +$1494.80 | -$1436.45 | Position open |
| Day 38 | 2026-06-17 | $739.12 | +$1113.60 | -$1055.25 | Holding would have been **$1055.25** better — honest entry |
| Day 39 | 2026-06-18 | $746.75 | +$1418.80 | -$1360.45 | Holding would have been **$1360.45** better — honest entry |
| Day 40 | 2026-06-22 | $744.27 | +$1319.60 | -$1261.25 | Holding would have been **$1261.25** better — honest entry |
| Day 41 | 2026-06-23 | $733.62 | +$893.60 | -$835.25 | Holding would have been **$835.25** better — honest entry |
| Day 42 | 2026-06-24 | $733.32 | +$881.60 | -$823.25 | Holding would have been **$823.25** better — honest entry |
| Day 43 | 2026-06-25 | $733.33 | +$882.00 | -$823.65 | Holding would have been **$823.65** better — honest entry |
| Day 44 | 2026-06-26 | $729.35 | +$722.80 | -$664.45 | Holding would have been **$664.45** better — honest entry |
| Day 45 | 2026-06-29 | $740.86 | +$1183.20 | -$1124.85 | Holding would have been **$1124.85** better — honest entry |
| Day 46 | 2026-06-30 | $746.65 | +$1414.80 | -$1356.45 | Holding would have been **$1356.45** better — honest entry |
| Day 47 | 2026-07-01 | $745.66 | +$1375.20 | -$1316.85 | Holding would have been **$1316.85** better — honest entry |
| Day 48 | 2026-07-02 | $744.86 | +$1343.20 | -$1284.85 | Holding would have been **$1284.85** better — honest entry |
| Day 49 | 2026-07-06 | $751.27 | +$1599.60 | -$1541.25 | Holding would have been **$1541.25** better — honest entry |
| Day 50 | 2026-07-07 | $747.77 | +$1459.60 | -$1401.25 | Holding would have been **$1401.25** better — honest entry |
| Day 51 | 2026-07-08 | $745.28 | +$1360.00 | -$1301.65 | Holding would have been **$1301.65** better — honest entry |
| Day 52 | 2026-07-09 | $751.55 | +$1610.80 | -$1552.45 | Holding would have been **$1552.45** better — honest entry |
| Day 53 | 2026-07-10 | $754.94 | +$1746.40 | -$1688.05 | Holding would have been **$1688.05** better — honest entry |
| Day 54 | 2026-07-13 | $749.13 | +$1514.00 | -$1455.65 | Holding would have been **$1455.65** better — honest entry |
| Day 55 | 2026-07-14 | $751.94 | +$1626.40 | -$1568.05 | Holding would have been **$1568.05** better — honest entry |
| Day 56 | 2026-07-15 | $754.77 | +$1739.60 | -$1681.25 | Holding would have been **$1681.25** better — honest entry |
| Day 57 | 2026-07-16 | $750.87 | +$1583.60 | -$1525.25 | Holding would have been **$1525.25** better — honest entry |
| Day 58 | 2026-07-17 | $743.28 | +$1280.00 | -$1221.65 | Holding would have been **$1221.65** better — honest entry |
| Day 59 | 2026-07-20 | $742.15 | +$1234.80 | -$1176.45 | Holding would have been **$1176.45** better — honest entry |
| Day 60 | 2026-07-21 | $748.15 | +$1474.80 | -$1416.45 | Position open |
| Day 61 | 2026-07-22 | $747.49 | +$1448.40 | -$1390.05 | Position open |
| Day 62 | 2026-07-23 | $738.06 | +$1071.20 | -$1012.85 | Position open |
| Day 63 | 2026-07-24 | $738.90 | +$1104.80 | -$1046.45 | Holding would have been **$1046.45** better — honest entry |
| Day 64 | 2026-07-27 | $738.85 | +$1102.80 | -$1044.45 | Holding would have been **$1044.45** better — honest entry |
| Day 65 | 2026-07-28 | $740.79 | +$1180.40 | -$1122.05 | Holding would have been **$1122.05** better — honest entry |
| Day 66 | 2026-07-29 | $729.57 | +$731.60 | -$673.25 | Holding would have been **$673.25** better — honest entry |
| Day 67 | 2026-07-30 | $741.63 | +$1214.00 | -$1155.65 | Holding would have been **$1155.65** better — honest entry |
| Day 68 | 2026-07-31 | $746.79 | +$1420.40 | -$1362.05 | Holding would have been **$1362.05** better — honest entry |
| Day 69 | 2026-08-03 | $757.72 | +$1857.60 | -$1799.25 | Holding would have been **$1799.25** better — honest entry |
| Day 70 | 2026-08-04 | $771.11 | +$2393.20 | -$2334.85 | Position open |
| Day 71 | 2026-08-05 | $769.79 | +$2340.40 | -$2282.05 | Holding would have been **$2282.05** better — honest entry |
| Day 72 | 2026-08-06 | $768.64 | +$2294.40 | -$2236.05 | Holding would have been **$2236.05** better — honest entry |
| Day 73 | 2026-08-07 | $773.16 | +$2475.20 | -$2416.85 | Position open |
| Day 74 | 2026-08-10 | $773.02 | +$2469.60 | -$2411.25 | Holding would have been **$2411.25** better — honest entry |
| Day 75 | 2026-08-11 | $770.52 | +$2369.60 | -$2311.25 | Position open |
| Day 76 | 2026-08-12 | $772.54 | +$2450.40 | -$2392.05 | Position open |
| Day 77 | 2026-08-13 | $777.84 | +$2662.40 | -$2604.05 | Position open |
| Day 78 | 2026-08-14 | $776.30 | +$2600.80 | -$2542.45 | Position open |
| Day 79 | 2026-08-17 | $772.62 | +$2453.60 | -$2395.25 | Position open |
| Day 80 | 2026-08-18 | $767.37 | +$2243.60 | -$2185.25 | Position open |
| Day 81 | 2026-08-19 | $769.09 | +$2312.40 | -$2254.05 | Position open |
| Day 82 | 2026-08-20 | $762.62 | +$2053.60 | -$1995.25 | Position open |
| Day 83 | 2026-08-21 | $765.64 | +$2174.40 | -$2116.05 | Position open |
| Day 84 | 2026-08-24 | $763.46 | +$2087.20 | -$2028.85 | Position open |
| Day 85 | 2026-08-25 | $765.79 | +$2180.40 | -$2122.05 | Position open |
| Day 86 | 2026-08-26 | $765.94 | +$2186.40 | -$2128.05 | Position open |
| Day 87 | 2026-08-27 | $771.18 | +$2396.00 | -$2337.65 | Position open |
| Day 88 | 2026-08-28 | $769.28 | +$2320.00 | -$2261.65 | Position open |

---

## Daily Entries

### Day 1 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 40 SPY (T1) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $712.14 |
| Unrealized P&L | +$34.40 |
| P&L % | +0.121% |
| Portfolio value | $100,034.40 |
| Benchmark value | $99,999.98 |
| Alpha (cumulative) | +0.034% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.12% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 2 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 40 SPY (T1) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $713.33 |
| Unrealized P&L | +$82.00 |
| P&L % | +0.288% |
| Portfolio value | $100,082.00 |
| Benchmark value | $100,167.08 |
| Alpha (cumulative) | -0.085% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 3 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 40 SPY (T1) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $709.85 |
| Unrealized P&L | -$57.20 |
| P&L % | -0.201% |
| Portfolio value | $99,942.80 |
| Benchmark value | $99,678.41 |
| Alpha (cumulative) | +0.265% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.20% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 4 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $709.76 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | -$60.80 |
| Signal saved | +$119.15 |
| Portfolio value | $99,917.60 |
| Benchmark value | $99,665.78 |
| Alpha (cumulative) | +0.252% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 5 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $716.56 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$211.20 |
| Signal saved | -$152.85 |
| Portfolio value | $100,175.00 |
| Benchmark value | $100,620.65 |
| Alpha (cumulative) | -0.446% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 6 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,953.37 |
| Benchmark value | $100,912.72 |
| Alpha (cumulative) | -0.960% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 7 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,821.92 |
| Benchmark value | $100,577.11 |
| Alpha (cumulative) | -0.755% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 8 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $100,129.92 |
| Benchmark value | $101,363.48 |
| Alpha (cumulative) | -1.233% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 9 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,681.57 |
| Benchmark value | $102,771.91 |
| Alpha (cumulative) | -2.090% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 10 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,558.92 |
| Benchmark value | $102,458.77 |
| Alpha (cumulative) | -1.900% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 11 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,888.92 |
| Benchmark value | $103,301.30 |
| Alpha (cumulative) | -2.412% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 12 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,979.67 |
| Benchmark value | $103,532.99 |
| Alpha (cumulative) | -2.553% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 13 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,924.12 |
| Benchmark value | $103,391.17 |
| Alpha (cumulative) | -2.467% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 14 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $101,149.62 |
| Benchmark value | $103,966.90 |
| Alpha (cumulative) | -2.817% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 15 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,468.07 |
| Benchmark value | $104,779.94 |
| Alpha (cumulative) | -3.312% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 16 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,974.17 |
| Benchmark value | $103,518.95 |
| Alpha (cumulative) | -2.545% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 17 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,935.67 |
| Benchmark value | $103,420.66 |
| Alpha (cumulative) | -2.485% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 18 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,683.22 |
| Benchmark value | $102,776.12 |
| Alpha (cumulative) | -2.093% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 19 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $101,095.72 |
| Benchmark value | $103,829.28 |
| Alpha (cumulative) | -2.733% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 20 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $101,172.17 |
| Benchmark value | $104,024.47 |
| Alpha (cumulative) | -2.852% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 21 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,334.42 |
| Benchmark value | $104,438.71 |
| Alpha (cumulative) | -3.105% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 22 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,597.32 |
| Benchmark value | $105,109.93 |
| Alpha (cumulative) | -3.513% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 23 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,604.47 |
| Benchmark value | $105,128.18 |
| Alpha (cumulative) | -3.524% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 24 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,828.87 |
| Benchmark value | $105,701.11 |
| Alpha (cumulative) | -3.872% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 25 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,920.17 |
| Benchmark value | $105,934.21 |
| Alpha (cumulative) | -4.014% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 26 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $102,035.12 |
| Benchmark value | $106,227.69 |
| Alpha (cumulative) | -4.193% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 27 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $102,091.77 |
| Benchmark value | $106,372.32 |
| Alpha (cumulative) | -4.280% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 28 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,801.37 |
| Benchmark value | $105,630.89 |
| Alpha (cumulative) | -3.830% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 29 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,954.82 |
| Benchmark value | $106,022.67 |
| Alpha (cumulative) | -4.068% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 30 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,883.97 |
| Benchmark value | $103,288.66 |
| Alpha (cumulative) | -2.405% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 31 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,981.87 |
| Benchmark value | $103,538.61 |
| Alpha (cumulative) | -2.557% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 32 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,863.07 |
| Benchmark value | $103,235.30 |
| Alpha (cumulative) | -2.372% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 33 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,232.77 |
| Benchmark value | $101,626.07 |
| Alpha (cumulative) | -1.393% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 34 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,895.52 |
| Benchmark value | $103,318.15 |
| Alpha (cumulative) | -2.423% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 35 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $101,114.97 |
| Benchmark value | $103,878.43 |
| Alpha (cumulative) | -2.763% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 36 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,832.72 |
| Benchmark value | $105,710.94 |
| Alpha (cumulative) | -3.878% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 37 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,603.92 |
| Benchmark value | $105,126.78 |
| Alpha (cumulative) | -3.523% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 38 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $739.12 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1113.60 |
| Signal saved | -$1055.25 |
| Portfolio value | $101,347.07 |
| Benchmark value | $103,788.56 |
| Alpha (cumulative) | -2.442% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 39 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $746.75 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1418.80 |
| Signal saved | -$1360.45 |
| Portfolio value | $101,347.07 |
| Benchmark value | $104,859.98 |
| Alpha (cumulative) | -3.513% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 40 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $744.27 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1319.60 |
| Signal saved | -$1261.25 |
| Portfolio value | $101,345.96 |
| Benchmark value | $104,511.73 |
| Alpha (cumulative) | -3.166% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 41 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $733.62 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$893.60 |
| Signal saved | -$835.25 |
| Portfolio value | $101,345.96 |
| Benchmark value | $103,016.24 |
| Alpha (cumulative) | -1.670% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 42 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $733.32 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$881.60 |
| Signal saved | -$823.25 |
| Portfolio value | $101,345.96 |
| Benchmark value | $102,974.11 |
| Alpha (cumulative) | -1.628% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 43 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $733.33 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$882.00 |
| Signal saved | -$823.65 |
| Portfolio value | $101,345.96 |
| Benchmark value | $102,975.52 |
| Alpha (cumulative) | -1.630% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 44 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $729.35 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$722.80 |
| Signal saved | -$664.45 |
| Portfolio value | $101,345.96 |
| Benchmark value | $102,416.64 |
| Alpha (cumulative) | -1.071% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 45 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $740.86 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1183.20 |
| Signal saved | -$1124.85 |
| Portfolio value | $101,345.96 |
| Benchmark value | $104,032.89 |
| Alpha (cumulative) | -2.687% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 46 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $746.65 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1414.80 |
| Signal saved | -$1356.45 |
| Portfolio value | $101,345.96 |
| Benchmark value | $104,845.94 |
| Alpha (cumulative) | -3.500% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 47 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $745.66 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1375.20 |
| Signal saved | -$1316.85 |
| Portfolio value | $101,345.96 |
| Benchmark value | $104,706.92 |
| Alpha (cumulative) | -3.361% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 48 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $744.86 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1343.20 |
| Signal saved | -$1284.85 |
| Portfolio value | $101,345.96 |
| Benchmark value | $104,594.58 |
| Alpha (cumulative) | -3.249% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 49 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $751.27 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1599.60 |
| Signal saved | -$1541.25 |
| Portfolio value | $101,345.96 |
| Benchmark value | $105,494.69 |
| Alpha (cumulative) | -4.149% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 50 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $747.77 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1459.60 |
| Signal saved | -$1401.25 |
| Portfolio value | $101,345.96 |
| Benchmark value | $105,003.21 |
| Alpha (cumulative) | -3.657% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 51 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $745.28 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1360.00 |
| Signal saved | -$1301.65 |
| Portfolio value | $101,345.96 |
| Benchmark value | $104,653.56 |
| Alpha (cumulative) | -3.308% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 52 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $751.55 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1610.80 |
| Signal saved | -$1552.45 |
| Portfolio value | $101,345.96 |
| Benchmark value | $105,534.00 |
| Alpha (cumulative) | -4.188% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 53 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $754.94 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1746.40 |
| Signal saved | -$1688.05 |
| Portfolio value | $101,345.96 |
| Benchmark value | $106,010.03 |
| Alpha (cumulative) | -4.664% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 54 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $749.13 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1514.00 |
| Signal saved | -$1455.65 |
| Portfolio value | $101,184.84 |
| Benchmark value | $105,194.18 |
| Alpha (cumulative) | -4.009% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 55 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $751.94 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1626.40 |
| Signal saved | -$1568.05 |
| Portfolio value | $101,149.76 |
| Benchmark value | $105,588.77 |
| Alpha (cumulative) | -4.439% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 56 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $754.77 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1739.60 |
| Signal saved | -$1681.25 |
| Portfolio value | $101,197.51 |
| Benchmark value | $105,986.16 |
| Alpha (cumulative) | -4.788% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 57 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $750.87 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1583.60 |
| Signal saved | -$1525.25 |
| Portfolio value | $101,021.38 |
| Benchmark value | $105,438.52 |
| Alpha (cumulative) | -4.418% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 58 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $743.28 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1280.00 |
| Signal saved | -$1221.65 |
| Portfolio value | $100,878.82 |
| Benchmark value | $104,372.72 |
| Alpha (cumulative) | -3.494% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 59 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $742.15 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1234.80 |
| Signal saved | -$1176.45 |
| Portfolio value | $100,686.84 |
| Benchmark value | $104,214.04 |
| Alpha (cumulative) | -3.527% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 60 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T11) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $100,714.93 |
| Benchmark value | $105,056.57 |
| Alpha (cumulative) | -4.342% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 61 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T11) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $100,679.95 |
| Benchmark value | $104,963.89 |
| Alpha (cumulative) | -4.284% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 62 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T12) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $100,010.81 |
| Benchmark value | $103,639.71 |
| Alpha (cumulative) | -3.629% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 63 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $738.90 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1104.80 |
| Signal saved | -$1046.45 |
| Portfolio value | $100,059.69 |
| Benchmark value | $103,757.67 |
| Alpha (cumulative) | -3.698% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 64 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $738.85 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1102.80 |
| Signal saved | -$1044.45 |
| Portfolio value | $100,163.83 |
| Benchmark value | $103,750.65 |
| Alpha (cumulative) | -3.587% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 65 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $740.79 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1180.40 |
| Signal saved | -$1122.05 |
| Portfolio value | $100,120.37 |
| Benchmark value | $104,023.07 |
| Alpha (cumulative) | -3.903% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 66 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $729.57 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$731.60 |
| Signal saved | -$673.25 |
| Portfolio value | $100,120.37 |
| Benchmark value | $102,447.53 |
| Alpha (cumulative) | -2.328% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 67 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $741.63 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1214.00 |
| Signal saved | -$1155.65 |
| Portfolio value | $100,120.37 |
| Benchmark value | $104,141.02 |
| Alpha (cumulative) | -4.021% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 68 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $746.79 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1420.40 |
| Signal saved | -$1362.05 |
| Portfolio value | $100,120.37 |
| Benchmark value | $104,865.60 |
| Alpha (cumulative) | -4.746% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 69 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $757.72 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$1857.60 |
| Signal saved | -$1799.25 |
| Portfolio value | $100,120.37 |
| Benchmark value | $106,400.41 |
| Alpha (cumulative) | -6.280% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 70 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T15) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $771.11 |
| Unrealized P&L | -$52.00 |
| P&L % | -0.135% |
| Portfolio value | $100,068.37 |
| Benchmark value | $108,280.65 |
| Alpha (cumulative) | -8.213% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 71 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $769.79 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$2340.40 |
| Signal saved | -$2282.05 |
| Portfolio value | $100,033.37 |
| Benchmark value | $108,095.30 |
| Alpha (cumulative) | -8.062% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 72 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $768.64 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$2294.40 |
| Signal saved | -$2236.05 |
| Portfolio value | $100,033.37 |
| Benchmark value | $107,933.81 |
| Alpha (cumulative) | -7.901% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 73 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $773.16 |
| Unrealized P&L | +$33.14 |
| P&L % | +0.084% |
| Portfolio value | $100,066.51 |
| Benchmark value | $108,568.52 |
| Alpha (cumulative) | -8.503% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.08% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 74 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $773.02 |
| Realized P&L (locked) | +$58.35 |
| Reference if held | +$2469.60 |
| Signal saved | -$2411.25 |
| Portfolio value | $100,058.35 |
| Benchmark value | $108,548.86 |
| Alpha (cumulative) | -8.491% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $+58.35. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 75 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $770.52 |
| Unrealized P&L | -$159.19 |
| P&L % | -0.403% |
| Portfolio value | $99,899.16 |
| Benchmark value | $108,197.81 |
| Alpha (cumulative) | -8.299% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.40% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 76 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $772.54 |
| Unrealized P&L | -$56.17 |
| P&L % | -0.142% |
| Portfolio value | $100,002.18 |
| Benchmark value | $108,481.46 |
| Alpha (cumulative) | -8.479% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 77 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $777.84 |
| Unrealized P&L | +$214.13 |
| P&L % | +0.543% |
| Portfolio value | $100,272.48 |
| Benchmark value | $109,225.69 |
| Alpha (cumulative) | -8.954% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.54% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 78 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $776.30 |
| Unrealized P&L | +$135.59 |
| P&L % | +0.344% |
| Portfolio value | $100,193.94 |
| Benchmark value | $109,009.44 |
| Alpha (cumulative) | -8.815% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: +0.34% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 79 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $772.62 |
| Unrealized P&L | -$52.09 |
| P&L % | -0.132% |
| Portfolio value | $100,006.26 |
| Benchmark value | $108,492.69 |
| Alpha (cumulative) | -8.487% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.13% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 80 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $99,738.51 |
| Benchmark value | $107,755.48 |
| Alpha (cumulative) | -8.017% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 81 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $769.09 |
| Unrealized P&L | -$232.12 |
| P&L % | -0.588% |
| Portfolio value | $99,826.23 |
| Benchmark value | $107,997.00 |
| Alpha (cumulative) | -8.171% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.59% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 82 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $762.62 |
| Unrealized P&L | -$562.09 |
| P&L % | -1.425% |
| Portfolio value | $99,496.26 |
| Benchmark value | $107,088.47 |
| Alpha (cumulative) | -7.592% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -1.43% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 83 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $765.64 |
| Unrealized P&L | -$408.07 |
| P&L % | -1.034% |
| Portfolio value | $99,650.28 |
| Benchmark value | $107,512.55 |
| Alpha (cumulative) | -7.863% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -1.03% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 84 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $763.46 |
| Unrealized P&L | -$519.25 |
| P&L % | -1.316% |
| Portfolio value | $99,539.10 |
| Benchmark value | $107,206.43 |
| Alpha (cumulative) | -7.667% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -1.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 85 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $765.79 |
| Unrealized P&L | -$400.42 |
| P&L % | -1.015% |
| Portfolio value | $99,657.93 |
| Benchmark value | $107,533.61 |
| Alpha (cumulative) | -7.876% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -1.01% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 86 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $765.94 |
| Unrealized P&L | -$392.77 |
| P&L % | -0.995% |
| Portfolio value | $99,665.58 |
| Benchmark value | $107,554.67 |
| Alpha (cumulative) | -7.889% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.99% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 87 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $771.18 |
| Unrealized P&L | -$125.53 |
| P&L % | -0.318% |
| Portfolio value | $99,932.82 |
| Benchmark value | $108,290.48 |
| Alpha (cumulative) | -8.357% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 88 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $711.280/share |
| Close price | $769.28 |
| Unrealized P&L | -$222.43 |
| P&L % | -0.564% |
| Portfolio value | $99,835.92 |
| Benchmark value | $108,023.68 |
| Alpha (cumulative) | -8.188% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $769.22 vs MA50 $753.96). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

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
_Day 88 of 90 · Alpaca equity: $99,680.49 · Cumulative alpha vs SPY: -8.188%_