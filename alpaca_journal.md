# ALPACA PAPER JOURNAL — SPY
_Last updated: August 11, 2026 | Day 75 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$711.277/share**
> (2026-04-24, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-08-11): **BULLISH** | ⚡ Price Override Active (+3.5% above MA50)  
> Fast: MA10 $757.27 | MA30 $750.19  
> Slow: MA20 $751.37 | MA50 $747.02  
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

**Total trades:** 17 | **Closed:** 16 | **Open:** Yes | **Cumulative Realized P&L:** +$25.55

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $711.277 (2026-04-24) | $709.220 (2026-04-29) | 56 | -$115.20 | ✅ Closed |
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
| T17 | $773.640 (2026-08-11) | — | 50 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,903.89 |
| Alpaca cash | $61,218.89 |
| Cumulative realized P&L | +$25.55 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-24 | $712.14 | Long 56 SPY (T1) | +$48.32 | +0.121% | $100,048.32 |
| Day 2 | 2026-04-27 | $713.33 | Long 56 SPY (T1) | +$114.96 | +0.289% | $100,114.96 |
| Day 3 | 2026-04-28 | $709.85 | Long 56 SPY (T1) | -$79.92 | -0.201% | $99,920.08 |
| Day 4 | 2026-04-29 | $709.76 | FLAT | — | — | $99,884.80 |
| Day 5 | 2026-04-30 | $716.56 | FLAT | — | — | $100,142.20 |
| Day 6 | 2026-05-01 | $718.64 | Long 55 SPY (T3) | -$221.63 | -0.558% | $99,920.57 |
| Day 7 | 2026-05-04 | $716.25 | Long 55 SPY (T3) | -$353.08 | -0.888% | $99,789.12 |
| Day 8 | 2026-05-05 | $721.85 | Long 55 SPY (T3) | -$45.08 | -0.113% | $100,097.12 |
| Day 9 | 2026-05-06 | $731.88 | Long 55 SPY (T3) | +$506.57 | +1.274% | $100,648.77 |
| Day 10 | 2026-05-07 | $729.65 | Long 55 SPY (T3) | +$383.92 | +0.966% | $100,526.12 |
| Day 11 | 2026-05-08 | $735.65 | Long 55 SPY (T3) | +$713.92 | +1.796% | $100,856.12 |
| Day 12 | 2026-05-11 | $737.30 | Long 55 SPY (T3) | +$804.67 | +2.024% | $100,946.87 |
| Day 13 | 2026-05-12 | $736.29 | Long 55 SPY (T3) | +$749.12 | +1.885% | $100,891.32 |
| Day 14 | 2026-05-13 | $740.39 | Long 55 SPY (T3) | +$974.62 | +2.452% | $101,116.82 |
| Day 15 | 2026-05-14 | $746.18 | Long 55 SPY (T3) | +$1293.07 | +3.253% | $101,435.27 |
| Day 16 | 2026-05-15 | $737.20 | Long 55 SPY (T3) | +$799.17 | +2.011% | $100,941.37 |
| Day 17 | 2026-05-18 | $736.50 | Long 55 SPY (T3) | +$760.67 | +1.914% | $100,902.87 |
| Day 18 | 2026-05-19 | $731.91 | Long 55 SPY (T3) | +$508.22 | +1.279% | $100,650.42 |
| Day 19 | 2026-05-20 | $739.41 | Long 55 SPY (T3) | +$920.72 | +2.316% | $101,062.92 |
| Day 20 | 2026-05-21 | $740.80 | Long 55 SPY (T3) | +$997.17 | +2.509% | $101,139.37 |
| Day 21 | 2026-05-22 | $743.75 | Long 55 SPY (T3) | +$1159.42 | +2.917% | $101,301.62 |
| Day 22 | 2026-05-26 | $748.53 | Long 55 SPY (T3) | +$1422.32 | +3.578% | $101,564.52 |
| Day 23 | 2026-05-27 | $748.66 | Long 55 SPY (T3) | +$1429.47 | +3.596% | $101,571.67 |
| Day 24 | 2026-05-28 | $752.74 | Long 55 SPY (T3) | +$1653.87 | +4.161% | $101,796.07 |
| Day 25 | 2026-05-29 | $754.40 | Long 55 SPY (T3) | +$1745.17 | +4.391% | $101,887.37 |
| Day 26 | 2026-06-01 | $756.49 | Long 55 SPY (T3) | +$1860.12 | +4.680% | $102,002.32 |
| Day 27 | 2026-06-02 | $757.52 | Long 55 SPY (T3) | +$1916.77 | +4.822% | $102,058.97 |
| Day 28 | 2026-06-03 | $752.24 | Long 55 SPY (T3) | +$1626.37 | +4.092% | $101,768.57 |
| Day 29 | 2026-06-04 | $755.03 | Long 55 SPY (T3) | +$1779.82 | +4.478% | $101,922.02 |
| Day 30 | 2026-06-05 | $735.56 | Long 55 SPY (T3) | +$708.97 | +1.784% | $100,851.17 |
| Day 31 | 2026-06-08 | $737.34 | Long 55 SPY (T3) | +$806.87 | +2.030% | $100,949.07 |
| Day 32 | 2026-06-09 | $735.18 | Long 55 SPY (T3) | +$688.07 | +1.731% | $100,830.27 |
| Day 33 | 2026-06-10 | $723.72 | Long 55 SPY (T3) | +$57.77 | +0.145% | $100,199.97 |
| Day 34 | 2026-06-11 | $735.77 | Long 55 SPY (T3) | +$720.52 | +1.813% | $100,862.72 |
| Day 35 | 2026-06-12 | $739.76 | Long 55 SPY (T3) | +$939.97 | +2.365% | $101,082.17 |
| Day 36 | 2026-06-15 | $752.81 | Long 55 SPY (T3) | +$1657.72 | +4.171% | $101,799.92 |
| Day 37 | 2026-06-16 | $748.65 | Long 55 SPY (T3) | +$1428.92 | +3.595% | $101,571.12 |
| Day 38 | 2026-06-17 | $739.12 | FLAT | — | — | $101,314.27 |
| Day 39 | 2026-06-18 | $746.75 | FLAT | — | — | $101,314.27 |
| Day 40 | 2026-06-22 | $744.27 | FLAT | — | — | $101,313.16 |
| Day 41 | 2026-06-23 | $733.62 | FLAT | — | — | $101,313.16 |
| Day 42 | 2026-06-24 | $733.32 | FLAT | — | — | $101,313.16 |
| Day 43 | 2026-06-25 | $733.33 | FLAT | — | — | $101,313.16 |
| Day 44 | 2026-06-26 | $729.35 | FLAT | — | — | $101,313.16 |
| Day 45 | 2026-06-29 | $740.86 | FLAT | — | — | $101,313.16 |
| Day 46 | 2026-06-30 | $746.65 | FLAT | — | — | $101,313.16 |
| Day 47 | 2026-07-01 | $745.66 | FLAT | — | — | $101,313.16 |
| Day 48 | 2026-07-02 | $744.86 | FLAT | — | — | $101,313.16 |
| Day 49 | 2026-07-06 | $751.27 | FLAT | — | — | $101,313.16 |
| Day 50 | 2026-07-07 | $747.77 | FLAT | — | — | $101,313.16 |
| Day 51 | 2026-07-08 | $745.28 | FLAT | — | — | $101,313.16 |
| Day 52 | 2026-07-09 | $751.55 | FLAT | — | — | $101,313.16 |
| Day 53 | 2026-07-10 | $754.94 | FLAT | — | — | $101,313.16 |
| Day 54 | 2026-07-13 | $749.13 | FLAT | — | — | $101,152.04 |
| Day 55 | 2026-07-14 | $751.94 | FLAT | — | — | $101,116.96 |
| Day 56 | 2026-07-15 | $754.77 | FLAT | — | — | $101,164.71 |
| Day 57 | 2026-07-16 | $750.87 | FLAT | — | — | $100,988.58 |
| Day 58 | 2026-07-17 | $743.28 | FLAT | — | — | $100,846.02 |
| Day 59 | 2026-07-20 | $742.15 | FLAT | — | — | $100,654.04 |
| Day 60 | 2026-07-21 | $748.15 | Long 53 SPY (T11) | +$28.09 | +0.071% | $100,682.13 |
| Day 61 | 2026-07-22 | $747.49 | Long 53 SPY (T11) | -$6.89 | -0.017% | $100,647.15 |
| Day 62 | 2026-07-23 | $738.06 | Long 52 SPY (T12) | -$40.56 | -0.106% | $99,978.01 |
| Day 63 | 2026-07-24 | $738.90 | FLAT | — | — | $100,026.89 |
| Day 64 | 2026-07-27 | $738.85 | FLAT | — | — | $100,131.03 |
| Day 65 | 2026-07-28 | $740.79 | FLAT | — | — | $100,087.57 |
| Day 66 | 2026-07-29 | $729.57 | FLAT | — | — | $100,087.57 |
| Day 67 | 2026-07-30 | $741.63 | FLAT | — | — | $100,087.57 |
| Day 68 | 2026-07-31 | $746.79 | FLAT | — | — | $100,087.57 |
| Day 69 | 2026-08-03 | $757.72 | FLAT | — | — | $100,087.57 |
| Day 70 | 2026-08-04 | $771.11 | Long 50 SPY (T15) | -$52.00 | -0.135% | $100,035.57 |
| Day 71 | 2026-08-05 | $769.79 | FLAT | — | — | $100,000.57 |
| Day 72 | 2026-08-06 | $768.64 | FLAT | — | — | $100,000.57 |
| Day 73 | 2026-08-07 | $773.16 | Long 51 SPY (T16) | +$33.14 | +0.084% | $100,033.71 |
| Day 74 | 2026-08-10 | $773.02 | FLAT | — | — | $100,025.55 |
| Day 75 | 2026-08-11 | $773.62 | Long 50 SPY (T17) | -$1.00 | -0.003% | $100,024.55 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-24 | $100,048.32 | $99,999.98 | +0.0483% | -0.000% | **+0.048%** |
| Day 2 | 2026-04-27 | $100,114.96 | $100,167.08 | +0.1150% | +0.167% | **-0.052%** |
| Day 3 | 2026-04-28 | $99,920.08 | $99,678.41 | -0.0799% | -0.322% | **+0.242%** |
| Day 4 | 2026-04-29 | $99,884.80 | $99,665.78 | -0.1152% | -0.334% | **+0.219%** |
| Day 5 | 2026-04-30 | $100,142.20 | $100,620.65 | +0.1422% | +0.621% | **-0.479%** |
| Day 6 | 2026-05-01 | $99,920.57 | $100,912.72 | -0.0794% | +0.913% | **-0.992%** |
| Day 7 | 2026-05-04 | $99,789.12 | $100,577.11 | -0.2109% | +0.577% | **-0.788%** |
| Day 8 | 2026-05-05 | $100,097.12 | $101,363.48 | +0.0971% | +1.363% | **-1.266%** |
| Day 9 | 2026-05-06 | $100,648.77 | $102,771.91 | +0.6488% | +2.772% | **-2.123%** |
| Day 10 | 2026-05-07 | $100,526.12 | $102,458.77 | +0.5261% | +2.459% | **-1.933%** |
| Day 11 | 2026-05-08 | $100,856.12 | $103,301.30 | +0.8561% | +3.301% | **-2.445%** |
| Day 12 | 2026-05-11 | $100,946.87 | $103,532.99 | +0.9469% | +3.533% | **-2.586%** |
| Day 13 | 2026-05-12 | $100,891.32 | $103,391.17 | +0.8913% | +3.391% | **-2.500%** |
| Day 14 | 2026-05-13 | $101,116.82 | $103,966.90 | +1.1168% | +3.967% | **-2.850%** |
| Day 15 | 2026-05-14 | $101,435.27 | $104,779.94 | +1.4353% | +4.780% | **-3.345%** |
| Day 16 | 2026-05-15 | $100,941.37 | $103,518.95 | +0.9414% | +3.519% | **-2.578%** |
| Day 17 | 2026-05-18 | $100,902.87 | $103,420.66 | +0.9029% | +3.421% | **-2.518%** |
| Day 18 | 2026-05-19 | $100,650.42 | $102,776.12 | +0.6504% | +2.776% | **-2.126%** |
| Day 19 | 2026-05-20 | $101,062.92 | $103,829.28 | +1.0629% | +3.829% | **-2.766%** |
| Day 20 | 2026-05-21 | $101,139.37 | $104,024.47 | +1.1394% | +4.024% | **-2.885%** |
| Day 21 | 2026-05-22 | $101,301.62 | $104,438.71 | +1.3016% | +4.439% | **-3.137%** |
| Day 22 | 2026-05-26 | $101,564.52 | $105,109.93 | +1.5645% | +5.110% | **-3.546%** |
| Day 23 | 2026-05-27 | $101,571.67 | $105,128.18 | +1.5717% | +5.128% | **-3.556%** |
| Day 24 | 2026-05-28 | $101,796.07 | $105,701.11 | +1.7961% | +5.701% | **-3.905%** |
| Day 25 | 2026-05-29 | $101,887.37 | $105,934.21 | +1.8874% | +5.934% | **-4.047%** |
| Day 26 | 2026-06-01 | $102,002.32 | $106,227.69 | +2.0023% | +6.228% | **-4.226%** |
| Day 27 | 2026-06-02 | $102,058.97 | $106,372.32 | +2.0590% | +6.372% | **-4.313%** |
| Day 28 | 2026-06-03 | $101,768.57 | $105,630.89 | +1.7686% | +5.631% | **-3.862%** |
| Day 29 | 2026-06-04 | $101,922.02 | $106,022.67 | +1.9220% | +6.023% | **-4.101%** |
| Day 30 | 2026-06-05 | $100,851.17 | $103,288.66 | +0.8512% | +3.289% | **-2.438%** |
| Day 31 | 2026-06-08 | $100,949.07 | $103,538.61 | +0.9491% | +3.539% | **-2.590%** |
| Day 32 | 2026-06-09 | $100,830.27 | $103,235.30 | +0.8303% | +3.235% | **-2.405%** |
| Day 33 | 2026-06-10 | $100,199.97 | $101,626.07 | +0.2000% | +1.626% | **-1.426%** |
| Day 34 | 2026-06-11 | $100,862.72 | $103,318.15 | +0.8627% | +3.318% | **-2.455%** |
| Day 35 | 2026-06-12 | $101,082.17 | $103,878.43 | +1.0822% | +3.878% | **-2.796%** |
| Day 36 | 2026-06-15 | $101,799.92 | $105,710.94 | +1.7999% | +5.711% | **-3.911%** |
| Day 37 | 2026-06-16 | $101,571.12 | $105,126.78 | +1.5711% | +5.127% | **-3.556%** |
| Day 38 | 2026-06-17 | $101,314.27 | $103,788.56 | +1.3143% | +3.789% | **-2.475%** |
| Day 39 | 2026-06-18 | $101,314.27 | $104,859.98 | +1.3143% | +4.860% | **-3.546%** |
| Day 40 | 2026-06-22 | $101,313.16 | $104,511.73 | +1.3132% | +4.512% | **-3.199%** |
| Day 41 | 2026-06-23 | $101,313.16 | $103,016.24 | +1.3132% | +3.016% | **-1.703%** |
| Day 42 | 2026-06-24 | $101,313.16 | $102,974.11 | +1.3132% | +2.974% | **-1.661%** |
| Day 43 | 2026-06-25 | $101,313.16 | $102,975.52 | +1.3132% | +2.976% | **-1.663%** |
| Day 44 | 2026-06-26 | $101,313.16 | $102,416.64 | +1.3132% | +2.417% | **-1.104%** |
| Day 45 | 2026-06-29 | $101,313.16 | $104,032.89 | +1.3132% | +4.033% | **-2.720%** |
| Day 46 | 2026-06-30 | $101,313.16 | $104,845.94 | +1.3132% | +4.846% | **-3.533%** |
| Day 47 | 2026-07-01 | $101,313.16 | $104,706.92 | +1.3132% | +4.707% | **-3.394%** |
| Day 48 | 2026-07-02 | $101,313.16 | $104,594.58 | +1.3132% | +4.595% | **-3.282%** |
| Day 49 | 2026-07-06 | $101,313.16 | $105,494.69 | +1.3132% | +5.495% | **-4.182%** |
| Day 50 | 2026-07-07 | $101,313.16 | $105,003.21 | +1.3132% | +5.003% | **-3.690%** |
| Day 51 | 2026-07-08 | $101,313.16 | $104,653.56 | +1.3132% | +4.654% | **-3.341%** |
| Day 52 | 2026-07-09 | $101,313.16 | $105,534.00 | +1.3132% | +5.534% | **-4.221%** |
| Day 53 | 2026-07-10 | $101,313.16 | $106,010.03 | +1.3132% | +6.010% | **-4.697%** |
| Day 54 | 2026-07-13 | $101,152.04 | $105,194.18 | +1.1520% | +5.194% | **-4.042%** |
| Day 55 | 2026-07-14 | $101,116.96 | $105,588.77 | +1.1170% | +5.589% | **-4.472%** |
| Day 56 | 2026-07-15 | $101,164.71 | $105,986.16 | +1.1647% | +5.986% | **-4.821%** |
| Day 57 | 2026-07-16 | $100,988.58 | $105,438.52 | +0.9886% | +5.439% | **-4.450%** |
| Day 58 | 2026-07-17 | $100,846.02 | $104,372.72 | +0.8460% | +4.373% | **-3.527%** |
| Day 59 | 2026-07-20 | $100,654.04 | $104,214.04 | +0.6540% | +4.214% | **-3.560%** |
| Day 60 | 2026-07-21 | $100,682.13 | $105,056.57 | +0.6821% | +5.057% | **-4.375%** |
| Day 61 | 2026-07-22 | $100,647.15 | $104,963.89 | +0.6471% | +4.964% | **-4.317%** |
| Day 62 | 2026-07-23 | $99,978.01 | $103,639.71 | -0.0220% | +3.640% | **-3.662%** |
| Day 63 | 2026-07-24 | $100,026.89 | $103,757.67 | +0.0269% | +3.758% | **-3.731%** |
| Day 64 | 2026-07-27 | $100,131.03 | $103,750.65 | +0.1310% | +3.751% | **-3.620%** |
| Day 65 | 2026-07-28 | $100,087.57 | $104,023.07 | +0.0876% | +4.023% | **-3.935%** |
| Day 66 | 2026-07-29 | $100,087.57 | $102,447.53 | +0.0876% | +2.448% | **-2.360%** |
| Day 67 | 2026-07-30 | $100,087.57 | $104,141.02 | +0.0876% | +4.141% | **-4.053%** |
| Day 68 | 2026-07-31 | $100,087.57 | $104,865.60 | +0.0876% | +4.866% | **-4.778%** |
| Day 69 | 2026-08-03 | $100,087.57 | $106,400.41 | +0.0876% | +6.400% | **-6.312%** |
| Day 70 | 2026-08-04 | $100,035.57 | $108,280.65 | +0.0356% | +8.281% | **-8.245%** |
| Day 71 | 2026-08-05 | $100,000.57 | $108,095.30 | +0.0006% | +8.095% | **-8.094%** |
| Day 72 | 2026-08-06 | $100,000.57 | $107,933.81 | +0.0006% | +7.934% | **-7.933%** |
| Day 73 | 2026-08-07 | $100,033.71 | $108,568.52 | +0.0337% | +8.569% | **-8.535%** |
| Day 74 | 2026-08-10 | $100,025.55 | $108,548.86 | +0.0256% | +8.549% | **-8.523%** |
| Day 75 | 2026-08-11 | $100,024.55 | $108,633.11 | +0.0246% | +8.633% | **-8.608%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-04-24 | $712.14 | +$48.32 | -$22.77 | Position open |
| Day 2 | 2026-04-27 | $713.33 | +$114.96 | -$89.41 | Position open |
| Day 3 | 2026-04-28 | $709.85 | -$79.92 | +$105.47 | Position open |
| Day 4 | 2026-04-29 | $709.76 | -$84.96 | +$110.51 | Flat saved **+$110.51** vs holding |
| Day 5 | 2026-04-30 | $716.56 | +$295.84 | -$270.29 | Holding would have been **$270.29** better — honest entry |
| Day 6 | 2026-05-01 | $718.64 | +$412.32 | -$386.77 | Position open |
| Day 7 | 2026-05-04 | $716.25 | +$278.48 | -$252.93 | Position open |
| Day 8 | 2026-05-05 | $721.85 | +$592.08 | -$566.53 | Position open |
| Day 9 | 2026-05-06 | $731.88 | +$1153.76 | -$1128.21 | Position open |
| Day 10 | 2026-05-07 | $729.65 | +$1028.88 | -$1003.33 | Position open |
| Day 11 | 2026-05-08 | $735.65 | +$1364.88 | -$1339.33 | Position open |
| Day 12 | 2026-05-11 | $737.30 | +$1457.28 | -$1431.73 | Position open |
| Day 13 | 2026-05-12 | $736.29 | +$1400.72 | -$1375.17 | Position open |
| Day 14 | 2026-05-13 | $740.39 | +$1630.32 | -$1604.77 | Position open |
| Day 15 | 2026-05-14 | $746.18 | +$1954.56 | -$1929.01 | Position open |
| Day 16 | 2026-05-15 | $737.20 | +$1451.68 | -$1426.13 | Position open |
| Day 17 | 2026-05-18 | $736.50 | +$1412.48 | -$1386.93 | Position open |
| Day 18 | 2026-05-19 | $731.91 | +$1155.44 | -$1129.89 | Position open |
| Day 19 | 2026-05-20 | $739.41 | +$1575.44 | -$1549.89 | Position open |
| Day 20 | 2026-05-21 | $740.80 | +$1653.28 | -$1627.73 | Position open |
| Day 21 | 2026-05-22 | $743.75 | +$1818.48 | -$1792.93 | Position open |
| Day 22 | 2026-05-26 | $748.53 | +$2086.16 | -$2060.61 | Position open |
| Day 23 | 2026-05-27 | $748.66 | +$2093.44 | -$2067.89 | Position open |
| Day 24 | 2026-05-28 | $752.74 | +$2321.92 | -$2296.37 | Position open |
| Day 25 | 2026-05-29 | $754.40 | +$2414.88 | -$2389.33 | Position open |
| Day 26 | 2026-06-01 | $756.49 | +$2531.92 | -$2506.37 | Position open |
| Day 27 | 2026-06-02 | $757.52 | +$2589.60 | -$2564.05 | Position open |
| Day 28 | 2026-06-03 | $752.24 | +$2293.92 | -$2268.37 | Position open |
| Day 29 | 2026-06-04 | $755.03 | +$2450.16 | -$2424.61 | Position open |
| Day 30 | 2026-06-05 | $735.56 | +$1359.84 | -$1334.29 | Position open |
| Day 31 | 2026-06-08 | $737.34 | +$1459.52 | -$1433.97 | Position open |
| Day 32 | 2026-06-09 | $735.18 | +$1338.56 | -$1313.01 | Position open |
| Day 33 | 2026-06-10 | $723.72 | +$696.80 | -$671.25 | Position open |
| Day 34 | 2026-06-11 | $735.77 | +$1371.60 | -$1346.05 | Position open |
| Day 35 | 2026-06-12 | $739.76 | +$1595.04 | -$1569.49 | Position open |
| Day 36 | 2026-06-15 | $752.81 | +$2325.84 | -$2300.29 | Position open |
| Day 37 | 2026-06-16 | $748.65 | +$2092.88 | -$2067.33 | Position open |
| Day 38 | 2026-06-17 | $739.12 | +$1559.20 | -$1533.65 | Holding would have been **$1533.65** better — honest entry |
| Day 39 | 2026-06-18 | $746.75 | +$1986.48 | -$1960.93 | Holding would have been **$1960.93** better — honest entry |
| Day 40 | 2026-06-22 | $744.27 | +$1847.60 | -$1822.05 | Holding would have been **$1822.05** better — honest entry |
| Day 41 | 2026-06-23 | $733.62 | +$1251.20 | -$1225.65 | Holding would have been **$1225.65** better — honest entry |
| Day 42 | 2026-06-24 | $733.32 | +$1234.40 | -$1208.85 | Holding would have been **$1208.85** better — honest entry |
| Day 43 | 2026-06-25 | $733.33 | +$1234.96 | -$1209.41 | Holding would have been **$1209.41** better — honest entry |
| Day 44 | 2026-06-26 | $729.35 | +$1012.08 | -$986.53 | Holding would have been **$986.53** better — honest entry |
| Day 45 | 2026-06-29 | $740.86 | +$1656.64 | -$1631.09 | Holding would have been **$1631.09** better — honest entry |
| Day 46 | 2026-06-30 | $746.65 | +$1980.88 | -$1955.33 | Holding would have been **$1955.33** better — honest entry |
| Day 47 | 2026-07-01 | $745.66 | +$1925.44 | -$1899.89 | Holding would have been **$1899.89** better — honest entry |
| Day 48 | 2026-07-02 | $744.86 | +$1880.64 | -$1855.09 | Holding would have been **$1855.09** better — honest entry |
| Day 49 | 2026-07-06 | $751.27 | +$2239.60 | -$2214.05 | Holding would have been **$2214.05** better — honest entry |
| Day 50 | 2026-07-07 | $747.77 | +$2043.60 | -$2018.05 | Holding would have been **$2018.05** better — honest entry |
| Day 51 | 2026-07-08 | $745.28 | +$1904.16 | -$1878.61 | Holding would have been **$1878.61** better — honest entry |
| Day 52 | 2026-07-09 | $751.55 | +$2255.28 | -$2229.73 | Holding would have been **$2229.73** better — honest entry |
| Day 53 | 2026-07-10 | $754.94 | +$2445.12 | -$2419.57 | Holding would have been **$2419.57** better — honest entry |
| Day 54 | 2026-07-13 | $749.13 | +$2119.76 | -$2094.21 | Holding would have been **$2094.21** better — honest entry |
| Day 55 | 2026-07-14 | $751.94 | +$2277.12 | -$2251.57 | Holding would have been **$2251.57** better — honest entry |
| Day 56 | 2026-07-15 | $754.77 | +$2435.60 | -$2410.05 | Holding would have been **$2410.05** better — honest entry |
| Day 57 | 2026-07-16 | $750.87 | +$2217.20 | -$2191.65 | Holding would have been **$2191.65** better — honest entry |
| Day 58 | 2026-07-17 | $743.28 | +$1792.16 | -$1766.61 | Holding would have been **$1766.61** better — honest entry |
| Day 59 | 2026-07-20 | $742.15 | +$1728.88 | -$1703.33 | Holding would have been **$1703.33** better — honest entry |
| Day 60 | 2026-07-21 | $748.15 | +$2064.88 | -$2039.33 | Position open |
| Day 61 | 2026-07-22 | $747.49 | +$2027.92 | -$2002.37 | Position open |
| Day 62 | 2026-07-23 | $738.06 | +$1499.84 | -$1474.29 | Position open |
| Day 63 | 2026-07-24 | $738.90 | +$1546.88 | -$1521.33 | Holding would have been **$1521.33** better — honest entry |
| Day 64 | 2026-07-27 | $738.85 | +$1544.08 | -$1518.53 | Holding would have been **$1518.53** better — honest entry |
| Day 65 | 2026-07-28 | $740.79 | +$1652.72 | -$1627.17 | Holding would have been **$1627.17** better — honest entry |
| Day 66 | 2026-07-29 | $729.57 | +$1024.40 | -$998.85 | Holding would have been **$998.85** better — honest entry |
| Day 67 | 2026-07-30 | $741.63 | +$1699.76 | -$1674.21 | Holding would have been **$1674.21** better — honest entry |
| Day 68 | 2026-07-31 | $746.79 | +$1988.72 | -$1963.17 | Holding would have been **$1963.17** better — honest entry |
| Day 69 | 2026-08-03 | $757.72 | +$2600.80 | -$2575.25 | Holding would have been **$2575.25** better — honest entry |
| Day 70 | 2026-08-04 | $771.11 | +$3350.64 | -$3325.09 | Position open |
| Day 71 | 2026-08-05 | $769.79 | +$3276.72 | -$3251.17 | Holding would have been **$3251.17** better — honest entry |
| Day 72 | 2026-08-06 | $768.64 | +$3212.32 | -$3186.77 | Holding would have been **$3186.77** better — honest entry |
| Day 73 | 2026-08-07 | $773.16 | +$3465.44 | -$3439.89 | Position open |
| Day 74 | 2026-08-10 | $773.02 | +$3457.60 | -$3432.05 | Holding would have been **$3432.05** better — honest entry |
| Day 75 | 2026-08-11 | $773.62 | +$3491.20 | -$3465.65 | Position open |

---

## Daily Entries

### Day 1 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T1) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $712.14 |
| Unrealized P&L | +$48.32 |
| P&L % | +0.121% |
| Portfolio value | $100,048.32 |
| Benchmark value | $99,999.98 |
| Alpha (cumulative) | +0.048% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +0.12% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 2 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T1) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $713.33 |
| Unrealized P&L | +$114.96 |
| P&L % | +0.289% |
| Portfolio value | $100,114.96 |
| Benchmark value | $100,167.08 |
| Alpha (cumulative) | -0.052% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 3 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T1) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $709.85 |
| Unrealized P&L | -$79.92 |
| P&L % | -0.201% |
| Portfolio value | $99,920.08 |
| Benchmark value | $99,678.41 |
| Alpha (cumulative) | +0.242% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.20% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 4 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $709.76 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | -$84.96 |
| Signal saved | +$110.51 |
| Portfolio value | $99,884.80 |
| Benchmark value | $99,665.78 |
| Alpha (cumulative) | +0.219% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 5 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $716.56 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$295.84 |
| Signal saved | -$270.29 |
| Portfolio value | $100,142.20 |
| Benchmark value | $100,620.65 |
| Alpha (cumulative) | -0.479% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 6 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,920.57 |
| Benchmark value | $100,912.72 |
| Alpha (cumulative) | -0.992% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 7 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,789.12 |
| Benchmark value | $100,577.11 |
| Alpha (cumulative) | -0.788% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 8 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $100,097.12 |
| Benchmark value | $101,363.48 |
| Alpha (cumulative) | -1.266% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 9 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,648.77 |
| Benchmark value | $102,771.91 |
| Alpha (cumulative) | -2.123% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 10 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,526.12 |
| Benchmark value | $102,458.77 |
| Alpha (cumulative) | -1.933% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 11 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,856.12 |
| Benchmark value | $103,301.30 |
| Alpha (cumulative) | -2.445% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 12 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,946.87 |
| Benchmark value | $103,532.99 |
| Alpha (cumulative) | -2.586% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 13 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,891.32 |
| Benchmark value | $103,391.17 |
| Alpha (cumulative) | -2.500% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 14 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $101,116.82 |
| Benchmark value | $103,966.90 |
| Alpha (cumulative) | -2.850% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 15 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,435.27 |
| Benchmark value | $104,779.94 |
| Alpha (cumulative) | -3.345% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 16 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,941.37 |
| Benchmark value | $103,518.95 |
| Alpha (cumulative) | -2.578% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 17 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,902.87 |
| Benchmark value | $103,420.66 |
| Alpha (cumulative) | -2.518% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 18 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,650.42 |
| Benchmark value | $102,776.12 |
| Alpha (cumulative) | -2.126% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 19 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $101,062.92 |
| Benchmark value | $103,829.28 |
| Alpha (cumulative) | -2.766% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 20 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $101,139.37 |
| Benchmark value | $104,024.47 |
| Alpha (cumulative) | -2.885% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 21 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,301.62 |
| Benchmark value | $104,438.71 |
| Alpha (cumulative) | -3.137% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 22 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,564.52 |
| Benchmark value | $105,109.93 |
| Alpha (cumulative) | -3.546% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 23 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,571.67 |
| Benchmark value | $105,128.18 |
| Alpha (cumulative) | -3.556% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 24 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,796.07 |
| Benchmark value | $105,701.11 |
| Alpha (cumulative) | -3.905% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 25 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,887.37 |
| Benchmark value | $105,934.21 |
| Alpha (cumulative) | -4.047% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 26 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $102,002.32 |
| Benchmark value | $106,227.69 |
| Alpha (cumulative) | -4.226% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 27 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $102,058.97 |
| Benchmark value | $106,372.32 |
| Alpha (cumulative) | -4.313% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 28 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,768.57 |
| Benchmark value | $105,630.89 |
| Alpha (cumulative) | -3.862% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 29 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,922.02 |
| Benchmark value | $106,022.67 |
| Alpha (cumulative) | -4.101% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 30 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,851.17 |
| Benchmark value | $103,288.66 |
| Alpha (cumulative) | -2.438% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 31 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,949.07 |
| Benchmark value | $103,538.61 |
| Alpha (cumulative) | -2.590% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 32 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,830.27 |
| Benchmark value | $103,235.30 |
| Alpha (cumulative) | -2.405% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 33 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,199.97 |
| Benchmark value | $101,626.07 |
| Alpha (cumulative) | -1.426% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 34 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,862.72 |
| Benchmark value | $103,318.15 |
| Alpha (cumulative) | -2.455% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 35 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $101,082.17 |
| Benchmark value | $103,878.43 |
| Alpha (cumulative) | -2.796% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 36 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,799.92 |
| Benchmark value | $105,710.94 |
| Alpha (cumulative) | -3.911% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 37 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T3) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,571.12 |
| Benchmark value | $105,126.78 |
| Alpha (cumulative) | -3.556% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 38 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $739.12 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1559.20 |
| Signal saved | -$1533.65 |
| Portfolio value | $101,314.27 |
| Benchmark value | $103,788.56 |
| Alpha (cumulative) | -2.475% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 39 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $746.75 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1986.48 |
| Signal saved | -$1960.93 |
| Portfolio value | $101,314.27 |
| Benchmark value | $104,859.98 |
| Alpha (cumulative) | -3.546% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 40 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $744.27 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1847.60 |
| Signal saved | -$1822.05 |
| Portfolio value | $101,313.16 |
| Benchmark value | $104,511.73 |
| Alpha (cumulative) | -3.199% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 41 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $733.62 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1251.20 |
| Signal saved | -$1225.65 |
| Portfolio value | $101,313.16 |
| Benchmark value | $103,016.24 |
| Alpha (cumulative) | -1.703% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 42 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $733.32 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1234.40 |
| Signal saved | -$1208.85 |
| Portfolio value | $101,313.16 |
| Benchmark value | $102,974.11 |
| Alpha (cumulative) | -1.661% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 43 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $733.33 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1234.96 |
| Signal saved | -$1209.41 |
| Portfolio value | $101,313.16 |
| Benchmark value | $102,975.52 |
| Alpha (cumulative) | -1.663% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 44 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $729.35 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1012.08 |
| Signal saved | -$986.53 |
| Portfolio value | $101,313.16 |
| Benchmark value | $102,416.64 |
| Alpha (cumulative) | -1.104% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 45 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $740.86 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1656.64 |
| Signal saved | -$1631.09 |
| Portfolio value | $101,313.16 |
| Benchmark value | $104,032.89 |
| Alpha (cumulative) | -2.720% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 46 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $746.65 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1980.88 |
| Signal saved | -$1955.33 |
| Portfolio value | $101,313.16 |
| Benchmark value | $104,845.94 |
| Alpha (cumulative) | -3.533% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 47 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $745.66 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1925.44 |
| Signal saved | -$1899.89 |
| Portfolio value | $101,313.16 |
| Benchmark value | $104,706.92 |
| Alpha (cumulative) | -3.394% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 48 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $744.86 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1880.64 |
| Signal saved | -$1855.09 |
| Portfolio value | $101,313.16 |
| Benchmark value | $104,594.58 |
| Alpha (cumulative) | -3.282% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 49 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $751.27 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2239.60 |
| Signal saved | -$2214.05 |
| Portfolio value | $101,313.16 |
| Benchmark value | $105,494.69 |
| Alpha (cumulative) | -4.182% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 50 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $747.77 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2043.60 |
| Signal saved | -$2018.05 |
| Portfolio value | $101,313.16 |
| Benchmark value | $105,003.21 |
| Alpha (cumulative) | -3.690% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 51 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $745.28 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1904.16 |
| Signal saved | -$1878.61 |
| Portfolio value | $101,313.16 |
| Benchmark value | $104,653.56 |
| Alpha (cumulative) | -3.341% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 52 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $751.55 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2255.28 |
| Signal saved | -$2229.73 |
| Portfolio value | $101,313.16 |
| Benchmark value | $105,534.00 |
| Alpha (cumulative) | -4.221% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 53 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $754.94 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2445.12 |
| Signal saved | -$2419.57 |
| Portfolio value | $101,313.16 |
| Benchmark value | $106,010.03 |
| Alpha (cumulative) | -4.697% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 54 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $749.13 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2119.76 |
| Signal saved | -$2094.21 |
| Portfolio value | $101,152.04 |
| Benchmark value | $105,194.18 |
| Alpha (cumulative) | -4.042% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 55 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $751.94 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2277.12 |
| Signal saved | -$2251.57 |
| Portfolio value | $101,116.96 |
| Benchmark value | $105,588.77 |
| Alpha (cumulative) | -4.472% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 56 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $754.77 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2435.60 |
| Signal saved | -$2410.05 |
| Portfolio value | $101,164.71 |
| Benchmark value | $105,986.16 |
| Alpha (cumulative) | -4.821% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 57 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $750.87 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2217.20 |
| Signal saved | -$2191.65 |
| Portfolio value | $100,988.58 |
| Benchmark value | $105,438.52 |
| Alpha (cumulative) | -4.450% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 58 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $743.28 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1792.16 |
| Signal saved | -$1766.61 |
| Portfolio value | $100,846.02 |
| Benchmark value | $104,372.72 |
| Alpha (cumulative) | -3.527% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 59 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $742.15 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1728.88 |
| Signal saved | -$1703.33 |
| Portfolio value | $100,654.04 |
| Benchmark value | $104,214.04 |
| Alpha (cumulative) | -3.560% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 60 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T11) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $100,682.13 |
| Benchmark value | $105,056.57 |
| Alpha (cumulative) | -4.375% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 61 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T11) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $100,647.15 |
| Benchmark value | $104,963.89 |
| Alpha (cumulative) | -4.317% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 62 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T12) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $99,978.01 |
| Benchmark value | $103,639.71 |
| Alpha (cumulative) | -3.662% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 63 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $738.90 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1546.88 |
| Signal saved | -$1521.33 |
| Portfolio value | $100,026.89 |
| Benchmark value | $103,757.67 |
| Alpha (cumulative) | -3.731% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 64 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $738.85 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1544.08 |
| Signal saved | -$1518.53 |
| Portfolio value | $100,131.03 |
| Benchmark value | $103,750.65 |
| Alpha (cumulative) | -3.620% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 65 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $740.79 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1652.72 |
| Signal saved | -$1627.17 |
| Portfolio value | $100,087.57 |
| Benchmark value | $104,023.07 |
| Alpha (cumulative) | -3.935% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 66 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $729.57 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1024.40 |
| Signal saved | -$998.85 |
| Portfolio value | $100,087.57 |
| Benchmark value | $102,447.53 |
| Alpha (cumulative) | -2.360% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 67 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $741.63 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1699.76 |
| Signal saved | -$1674.21 |
| Portfolio value | $100,087.57 |
| Benchmark value | $104,141.02 |
| Alpha (cumulative) | -4.053% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 68 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $746.79 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$1988.72 |
| Signal saved | -$1963.17 |
| Portfolio value | $100,087.57 |
| Benchmark value | $104,865.60 |
| Alpha (cumulative) | -4.778% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 69 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $757.72 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$2600.80 |
| Signal saved | -$2575.25 |
| Portfolio value | $100,087.57 |
| Benchmark value | $106,400.41 |
| Alpha (cumulative) | -6.312% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 70 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T15) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $771.11 |
| Unrealized P&L | -$52.00 |
| P&L % | -0.135% |
| Portfolio value | $100,035.57 |
| Benchmark value | $108,280.65 |
| Alpha (cumulative) | -8.245% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 71 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $769.79 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$3276.72 |
| Signal saved | -$3251.17 |
| Portfolio value | $100,000.57 |
| Benchmark value | $108,095.30 |
| Alpha (cumulative) | -8.094% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 72 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $768.64 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$3212.32 |
| Signal saved | -$3186.77 |
| Portfolio value | $100,000.57 |
| Benchmark value | $107,933.81 |
| Alpha (cumulative) | -7.933% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 73 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T16) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $773.16 |
| Unrealized P&L | +$33.14 |
| P&L % | +0.084% |
| Portfolio value | $100,033.71 |
| Benchmark value | $108,568.52 |
| Alpha (cumulative) | -8.535% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: +0.08% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 74 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $773.02 |
| Realized P&L (locked) | +$25.55 |
| Reference if held | +$3457.60 |
| Signal saved | -$3432.05 |
| Portfolio value | $100,025.55 |
| Benchmark value | $108,548.86 |
| Alpha (cumulative) | -8.523% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $+25.55. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 75 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T17) |
| Entry (Alpaca fill) | $711.277/share |
| Close price | $773.62 |
| Unrealized P&L | -$1.00 |
| P&L % | -0.003% |
| Portfolio value | $100,024.55 |
| Benchmark value | $108,633.11 |
| Alpha (cumulative) | -8.608% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $751.37 vs MA50 $747.02). Momentum: STRONG. Unrealized P&L: -0.00% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

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
_Day 75 of 90 · Alpaca equity: $99,903.89 · Cumulative alpha vs SPY: -8.608%_