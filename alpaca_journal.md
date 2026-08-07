# ALPACA PAPER JOURNAL — SPY
_Last updated: August 07, 2026 | Day 75 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$709.805/share**
> (2026-04-22, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-08-07): **BULLISH** | ⚡ Price Override Active (+3.6% above MA50)  
> Fast: MA10 $753.87 | MA30 $748.73  
> Slow: MA20 $750.17 | MA50 $746.61  
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

**Total trades:** 17 | **Closed:** 16 | **Open:** Yes | **Cumulative Realized P&L:** -$127.38

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $709.805 (2026-04-22) | $707.520 (2026-04-23) | 56 | -$127.95 | ✅ Closed |
| T2 | $711.277 (2026-04-24) | $709.220 (2026-04-29) | 56 | -$115.20 | ✅ Closed |
| T3 | $714.440 (2026-04-30) | $719.120 (2026-04-30) | 55 | +$257.40 | ✅ Closed |
| T4 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 55 | +$1172.07 | ✅ Closed |
| T5 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T6 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T7 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T8 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T9 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T10 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T11 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T12 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T13 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T14 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T15 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T16 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T17 | $772.510 (2026-08-07) | — | 51 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,901.23 |
| Alpaca cash | $60,478.74 |
| Cumulative realized P&L | -$127.38 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-22 | $709.37 | Long 56 SPY (T1) | -$24.35 | -0.061% | $99,975.65 |
| Day 2 | 2026-04-23 | $706.59 | FLAT | — | — | $99,872.05 |
| Day 3 | 2026-04-24 | $712.14 | Long 56 SPY (T2) | +$48.32 | +0.121% | $99,920.37 |
| Day 4 | 2026-04-27 | $713.33 | Long 56 SPY (T2) | +$114.96 | +0.289% | $99,987.01 |
| Day 5 | 2026-04-28 | $709.85 | Long 56 SPY (T2) | -$79.92 | -0.201% | $99,792.13 |
| Day 6 | 2026-04-29 | $709.76 | FLAT | — | — | $99,756.85 |
| Day 7 | 2026-04-30 | $716.56 | FLAT | — | — | $100,014.25 |
| Day 8 | 2026-05-01 | $718.64 | Long 55 SPY (T4) | -$221.63 | -0.558% | $99,792.62 |
| Day 9 | 2026-05-04 | $716.25 | Long 55 SPY (T4) | -$353.08 | -0.888% | $99,661.17 |
| Day 10 | 2026-05-05 | $721.85 | Long 55 SPY (T4) | -$45.08 | -0.113% | $99,969.17 |
| Day 11 | 2026-05-06 | $731.88 | Long 55 SPY (T4) | +$506.57 | +1.274% | $100,520.82 |
| Day 12 | 2026-05-07 | $729.65 | Long 55 SPY (T4) | +$383.92 | +0.966% | $100,398.17 |
| Day 13 | 2026-05-08 | $735.65 | Long 55 SPY (T4) | +$713.92 | +1.796% | $100,728.17 |
| Day 14 | 2026-05-11 | $737.30 | Long 55 SPY (T4) | +$804.67 | +2.024% | $100,818.92 |
| Day 15 | 2026-05-12 | $736.29 | Long 55 SPY (T4) | +$749.12 | +1.885% | $100,763.37 |
| Day 16 | 2026-05-13 | $740.39 | Long 55 SPY (T4) | +$974.62 | +2.452% | $100,988.87 |
| Day 17 | 2026-05-14 | $746.18 | Long 55 SPY (T4) | +$1293.07 | +3.253% | $101,307.32 |
| Day 18 | 2026-05-15 | $737.20 | Long 55 SPY (T4) | +$799.17 | +2.011% | $100,813.42 |
| Day 19 | 2026-05-18 | $736.50 | Long 55 SPY (T4) | +$760.67 | +1.914% | $100,774.92 |
| Day 20 | 2026-05-19 | $731.91 | Long 55 SPY (T4) | +$508.22 | +1.279% | $100,522.47 |
| Day 21 | 2026-05-20 | $739.41 | Long 55 SPY (T4) | +$920.72 | +2.316% | $100,934.97 |
| Day 22 | 2026-05-21 | $740.80 | Long 55 SPY (T4) | +$997.17 | +2.509% | $101,011.42 |
| Day 23 | 2026-05-22 | $743.75 | Long 55 SPY (T4) | +$1159.42 | +2.917% | $101,173.67 |
| Day 24 | 2026-05-26 | $748.53 | Long 55 SPY (T4) | +$1422.32 | +3.578% | $101,436.57 |
| Day 25 | 2026-05-27 | $748.66 | Long 55 SPY (T4) | +$1429.47 | +3.596% | $101,443.72 |
| Day 26 | 2026-05-28 | $752.74 | Long 55 SPY (T4) | +$1653.87 | +4.161% | $101,668.12 |
| Day 27 | 2026-05-29 | $754.40 | Long 55 SPY (T4) | +$1745.17 | +4.391% | $101,759.42 |
| Day 28 | 2026-06-01 | $756.49 | Long 55 SPY (T4) | +$1860.12 | +4.680% | $101,874.37 |
| Day 29 | 2026-06-02 | $757.52 | Long 55 SPY (T4) | +$1916.77 | +4.822% | $101,931.02 |
| Day 30 | 2026-06-03 | $752.24 | Long 55 SPY (T4) | +$1626.37 | +4.092% | $101,640.62 |
| Day 31 | 2026-06-04 | $755.03 | Long 55 SPY (T4) | +$1779.82 | +4.478% | $101,794.07 |
| Day 32 | 2026-06-05 | $735.56 | Long 55 SPY (T4) | +$708.97 | +1.784% | $100,723.22 |
| Day 33 | 2026-06-08 | $737.34 | Long 55 SPY (T4) | +$806.87 | +2.030% | $100,821.12 |
| Day 34 | 2026-06-09 | $735.18 | Long 55 SPY (T4) | +$688.07 | +1.731% | $100,702.32 |
| Day 35 | 2026-06-10 | $723.72 | Long 55 SPY (T4) | +$57.77 | +0.145% | $100,072.02 |
| Day 36 | 2026-06-11 | $735.77 | Long 55 SPY (T4) | +$720.52 | +1.813% | $100,734.77 |
| Day 37 | 2026-06-12 | $739.76 | Long 55 SPY (T4) | +$939.97 | +2.365% | $100,954.22 |
| Day 38 | 2026-06-15 | $752.81 | Long 55 SPY (T4) | +$1657.72 | +4.171% | $101,671.97 |
| Day 39 | 2026-06-16 | $748.65 | Long 55 SPY (T4) | +$1428.92 | +3.595% | $101,443.17 |
| Day 40 | 2026-06-17 | $739.12 | FLAT | — | — | $101,186.32 |
| Day 41 | 2026-06-18 | $746.75 | FLAT | — | — | $101,186.32 |
| Day 42 | 2026-06-22 | $744.27 | FLAT | — | — | $101,185.21 |
| Day 43 | 2026-06-23 | $733.62 | FLAT | — | — | $101,185.21 |
| Day 44 | 2026-06-24 | $733.32 | FLAT | — | — | $101,185.21 |
| Day 45 | 2026-06-25 | $733.33 | FLAT | — | — | $101,185.21 |
| Day 46 | 2026-06-26 | $729.35 | FLAT | — | — | $101,185.21 |
| Day 47 | 2026-06-29 | $740.86 | FLAT | — | — | $101,185.21 |
| Day 48 | 2026-06-30 | $746.65 | FLAT | — | — | $101,185.21 |
| Day 49 | 2026-07-01 | $745.66 | FLAT | — | — | $101,185.21 |
| Day 50 | 2026-07-02 | $744.86 | FLAT | — | — | $101,185.21 |
| Day 51 | 2026-07-06 | $751.27 | FLAT | — | — | $101,185.21 |
| Day 52 | 2026-07-07 | $747.77 | FLAT | — | — | $101,185.21 |
| Day 53 | 2026-07-08 | $745.28 | FLAT | — | — | $101,185.21 |
| Day 54 | 2026-07-09 | $751.55 | FLAT | — | — | $101,185.21 |
| Day 55 | 2026-07-10 | $754.94 | FLAT | — | — | $101,185.21 |
| Day 56 | 2026-07-13 | $749.13 | FLAT | — | — | $101,024.09 |
| Day 57 | 2026-07-14 | $751.94 | FLAT | — | — | $100,989.01 |
| Day 58 | 2026-07-15 | $754.77 | FLAT | — | — | $101,036.76 |
| Day 59 | 2026-07-16 | $750.87 | FLAT | — | — | $100,860.63 |
| Day 60 | 2026-07-17 | $743.28 | FLAT | — | — | $100,718.07 |
| Day 61 | 2026-07-20 | $742.15 | FLAT | — | — | $100,526.09 |
| Day 62 | 2026-07-21 | $748.15 | Long 53 SPY (T12) | +$28.09 | +0.071% | $100,554.18 |
| Day 63 | 2026-07-22 | $747.49 | Long 53 SPY (T12) | -$6.89 | -0.017% | $100,519.20 |
| Day 64 | 2026-07-23 | $738.06 | Long 52 SPY (T13) | -$40.56 | -0.106% | $99,850.06 |
| Day 65 | 2026-07-24 | $738.90 | FLAT | — | — | $99,898.94 |
| Day 66 | 2026-07-27 | $738.85 | FLAT | — | — | $100,003.08 |
| Day 67 | 2026-07-28 | $740.79 | FLAT | — | — | $99,959.62 |
| Day 68 | 2026-07-29 | $729.57 | FLAT | — | — | $99,959.62 |
| Day 69 | 2026-07-30 | $741.63 | FLAT | — | — | $99,959.62 |
| Day 70 | 2026-07-31 | $746.79 | FLAT | — | — | $99,959.62 |
| Day 71 | 2026-08-03 | $757.72 | FLAT | — | — | $99,959.62 |
| Day 72 | 2026-08-04 | $771.11 | Long 50 SPY (T16) | -$52.00 | -0.135% | $99,907.62 |
| Day 73 | 2026-08-05 | $769.79 | FLAT | — | — | $99,872.62 |
| Day 74 | 2026-08-06 | $768.64 | FLAT | — | — | $99,872.62 |
| Day 75 | 2026-08-07 | $773.16 | Long 51 SPY (T17) | +$33.14 | +0.084% | $99,905.76 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-22 | $99,975.65 | $100,000.03 | -0.0244% | +0.000% | **-0.024%** |
| Day 2 | 2026-04-23 | $99,872.05 | $99,608.13 | -0.1279% | -0.392% | **+0.264%** |
| Day 3 | 2026-04-24 | $99,920.37 | $100,390.52 | -0.0796% | +0.391% | **-0.471%** |
| Day 4 | 2026-04-27 | $99,987.01 | $100,558.27 | -0.0130% | +0.558% | **-0.571%** |
| Day 5 | 2026-04-28 | $99,792.13 | $100,067.70 | -0.2079% | +0.068% | **-0.276%** |
| Day 6 | 2026-04-29 | $99,756.85 | $100,055.01 | -0.2431% | +0.055% | **-0.298%** |
| Day 7 | 2026-04-30 | $100,014.25 | $101,013.61 | +0.0142% | +1.014% | **-1.000%** |
| Day 8 | 2026-05-01 | $99,792.62 | $101,306.82 | -0.2074% | +1.307% | **-1.514%** |
| Day 9 | 2026-05-04 | $99,661.17 | $100,969.91 | -0.3388% | +0.970% | **-1.309%** |
| Day 10 | 2026-05-05 | $99,969.17 | $101,759.34 | -0.0308% | +1.759% | **-1.790%** |
| Day 11 | 2026-05-06 | $100,520.82 | $103,173.27 | +0.5208% | +3.173% | **-2.652%** |
| Day 12 | 2026-05-07 | $100,398.17 | $102,858.91 | +0.3982% | +2.859% | **-2.461%** |
| Day 13 | 2026-05-08 | $100,728.17 | $103,704.73 | +0.7282% | +3.705% | **-2.977%** |
| Day 14 | 2026-05-11 | $100,818.92 | $103,937.33 | +0.8189% | +3.937% | **-3.118%** |
| Day 15 | 2026-05-12 | $100,763.37 | $103,794.95 | +0.7634% | +3.795% | **-3.032%** |
| Day 16 | 2026-05-13 | $100,988.87 | $104,372.93 | +0.9889% | +4.373% | **-3.384%** |
| Day 17 | 2026-05-14 | $101,307.32 | $105,189.14 | +1.3073% | +5.189% | **-3.882%** |
| Day 18 | 2026-05-15 | $100,813.42 | $103,923.23 | +0.8134% | +3.923% | **-3.110%** |
| Day 19 | 2026-05-18 | $100,774.92 | $103,824.55 | +0.7749% | +3.825% | **-3.050%** |
| Day 20 | 2026-05-19 | $100,522.47 | $103,177.50 | +0.5225% | +3.177% | **-2.654%** |
| Day 21 | 2026-05-20 | $100,934.97 | $104,234.78 | +0.9350% | +4.235% | **-3.300%** |
| Day 22 | 2026-05-21 | $101,011.42 | $104,430.72 | +1.0114% | +4.431% | **-3.420%** |
| Day 23 | 2026-05-22 | $101,173.67 | $104,846.59 | +1.1737% | +4.847% | **-3.673%** |
| Day 24 | 2026-05-26 | $101,436.57 | $105,520.42 | +1.4366% | +5.520% | **-4.083%** |
| Day 25 | 2026-05-27 | $101,443.72 | $105,538.75 | +1.4437% | +5.539% | **-4.095%** |
| Day 26 | 2026-05-28 | $101,668.12 | $106,113.91 | +1.6681% | +6.114% | **-4.446%** |
| Day 27 | 2026-05-29 | $101,759.42 | $106,347.92 | +1.7594% | +6.348% | **-4.589%** |
| Day 28 | 2026-06-01 | $101,874.37 | $106,642.55 | +1.8744% | +6.643% | **-4.769%** |
| Day 29 | 2026-06-02 | $101,931.02 | $106,787.75 | +1.9310% | +6.788% | **-4.857%** |
| Day 30 | 2026-06-03 | $101,640.62 | $106,043.42 | +1.6406% | +6.043% | **-4.402%** |
| Day 31 | 2026-06-04 | $101,794.07 | $106,436.73 | +1.7941% | +6.437% | **-4.643%** |
| Day 32 | 2026-06-05 | $100,723.22 | $103,692.04 | +0.7232% | +3.692% | **-2.969%** |
| Day 33 | 2026-06-08 | $100,821.12 | $103,942.97 | +0.8211% | +3.943% | **-3.122%** |
| Day 34 | 2026-06-09 | $100,702.32 | $103,638.47 | +0.7023% | +3.638% | **-2.936%** |
| Day 35 | 2026-06-10 | $100,072.02 | $102,022.95 | +0.0720% | +2.023% | **-1.951%** |
| Day 36 | 2026-06-11 | $100,734.77 | $103,721.64 | +0.7348% | +3.722% | **-2.987%** |
| Day 37 | 2026-06-12 | $100,954.22 | $104,284.12 | +0.9542% | +4.284% | **-3.330%** |
| Day 38 | 2026-06-15 | $101,671.97 | $106,123.78 | +1.6720% | +6.124% | **-4.452%** |
| Day 39 | 2026-06-16 | $101,443.17 | $105,537.34 | +1.4432% | +5.537% | **-4.094%** |
| Day 40 | 2026-06-17 | $101,186.32 | $104,193.89 | +1.1863% | +4.194% | **-3.008%** |
| Day 41 | 2026-06-18 | $101,186.32 | $105,269.50 | +1.1863% | +5.270% | **-4.084%** |
| Day 42 | 2026-06-22 | $101,185.21 | $104,919.89 | +1.1852% | +4.920% | **-3.735%** |
| Day 43 | 2026-06-23 | $101,185.21 | $103,418.56 | +1.1852% | +3.419% | **-2.234%** |
| Day 44 | 2026-06-24 | $101,185.21 | $103,376.27 | +1.1852% | +3.376% | **-2.191%** |
| Day 45 | 2026-06-25 | $101,185.21 | $103,377.68 | +1.1852% | +3.378% | **-2.193%** |
| Day 46 | 2026-06-26 | $101,185.21 | $102,816.62 | +1.1852% | +2.817% | **-1.632%** |
| Day 47 | 2026-06-29 | $101,185.21 | $104,439.18 | +1.1852% | +4.439% | **-3.254%** |
| Day 48 | 2026-06-30 | $101,185.21 | $105,255.40 | +1.1852% | +5.255% | **-4.070%** |
| Day 49 | 2026-07-01 | $101,185.21 | $105,115.84 | +1.1852% | +5.116% | **-3.931%** |
| Day 50 | 2026-07-02 | $101,185.21 | $105,003.06 | +1.1852% | +5.003% | **-3.818%** |
| Day 51 | 2026-07-06 | $101,185.21 | $105,906.68 | +1.1852% | +5.907% | **-4.722%** |
| Day 52 | 2026-07-07 | $101,185.21 | $105,413.29 | +1.1852% | +5.413% | **-4.228%** |
| Day 53 | 2026-07-08 | $101,185.21 | $105,062.27 | +1.1852% | +5.062% | **-3.877%** |
| Day 54 | 2026-07-09 | $101,185.21 | $105,946.15 | +1.1852% | +5.946% | **-4.761%** |
| Day 55 | 2026-07-10 | $101,185.21 | $106,424.04 | +1.1852% | +6.424% | **-5.239%** |
| Day 56 | 2026-07-13 | $101,024.09 | $105,605.01 | +1.0241% | +5.605% | **-4.581%** |
| Day 57 | 2026-07-14 | $100,989.01 | $106,001.13 | +0.9890% | +6.001% | **-5.012%** |
| Day 58 | 2026-07-15 | $101,036.76 | $106,400.08 | +1.0368% | +6.400% | **-5.363%** |
| Day 59 | 2026-07-16 | $100,860.63 | $105,850.29 | +0.8606% | +5.850% | **-4.989%** |
| Day 60 | 2026-07-17 | $100,718.07 | $104,780.33 | +0.7181% | +4.780% | **-4.062%** |
| Day 61 | 2026-07-20 | $100,526.09 | $104,621.03 | +0.5261% | +4.621% | **-4.095%** |
| Day 62 | 2026-07-21 | $100,554.18 | $105,466.86 | +0.5542% | +5.467% | **-4.913%** |
| Day 63 | 2026-07-22 | $100,519.20 | $105,373.81 | +0.5192% | +5.374% | **-4.855%** |
| Day 64 | 2026-07-23 | $99,850.06 | $104,044.47 | -0.1499% | +4.044% | **-4.194%** |
| Day 65 | 2026-07-24 | $99,898.94 | $104,162.88 | -0.1011% | +4.163% | **-4.264%** |
| Day 66 | 2026-07-27 | $100,003.08 | $104,155.83 | +0.0031% | +4.156% | **-4.153%** |
| Day 67 | 2026-07-28 | $99,959.62 | $104,429.31 | -0.0404% | +4.429% | **-4.469%** |
| Day 68 | 2026-07-29 | $99,959.62 | $102,847.63 | -0.0404% | +2.848% | **-2.888%** |
| Day 69 | 2026-07-30 | $99,959.62 | $104,547.73 | -0.0404% | +4.548% | **-4.588%** |
| Day 70 | 2026-07-31 | $99,959.62 | $105,275.14 | -0.0404% | +5.275% | **-5.315%** |
| Day 71 | 2026-08-03 | $99,959.62 | $106,815.94 | -0.0404% | +6.816% | **-6.856%** |
| Day 72 | 2026-08-04 | $99,907.62 | $108,703.53 | -0.0924% | +8.704% | **-8.796%** |
| Day 73 | 2026-08-05 | $99,872.62 | $108,517.45 | -0.1274% | +8.517% | **-8.644%** |
| Day 74 | 2026-08-06 | $99,872.62 | $108,355.33 | -0.1274% | +8.355% | **-8.482%** |
| Day 75 | 2026-08-07 | $99,905.76 | $108,992.52 | -0.0942% | +8.993% | **-9.087%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-04-22 | $709.37 | -$24.35 | -$103.03 | Position open |
| Day 2 | 2026-04-23 | $706.59 | -$180.03 | +$52.65 | Flat saved **+$52.65** vs holding |
| Day 3 | 2026-04-24 | $712.14 | +$130.77 | -$258.15 | Position open |
| Day 4 | 2026-04-27 | $713.33 | +$197.41 | -$324.79 | Position open |
| Day 5 | 2026-04-28 | $709.85 | +$2.53 | -$129.91 | Position open |
| Day 6 | 2026-04-29 | $709.76 | -$2.51 | -$124.87 | Holding would have been **$124.87** better — honest entry |
| Day 7 | 2026-04-30 | $716.56 | +$378.29 | -$505.67 | Holding would have been **$505.67** better — honest entry |
| Day 8 | 2026-05-01 | $718.64 | +$494.77 | -$622.15 | Position open |
| Day 9 | 2026-05-04 | $716.25 | +$360.93 | -$488.31 | Position open |
| Day 10 | 2026-05-05 | $721.85 | +$674.53 | -$801.91 | Position open |
| Day 11 | 2026-05-06 | $731.88 | +$1236.21 | -$1363.59 | Position open |
| Day 12 | 2026-05-07 | $729.65 | +$1111.33 | -$1238.71 | Position open |
| Day 13 | 2026-05-08 | $735.65 | +$1447.33 | -$1574.71 | Position open |
| Day 14 | 2026-05-11 | $737.30 | +$1539.73 | -$1667.11 | Position open |
| Day 15 | 2026-05-12 | $736.29 | +$1483.17 | -$1610.55 | Position open |
| Day 16 | 2026-05-13 | $740.39 | +$1712.77 | -$1840.15 | Position open |
| Day 17 | 2026-05-14 | $746.18 | +$2037.01 | -$2164.39 | Position open |
| Day 18 | 2026-05-15 | $737.20 | +$1534.13 | -$1661.51 | Position open |
| Day 19 | 2026-05-18 | $736.50 | +$1494.93 | -$1622.31 | Position open |
| Day 20 | 2026-05-19 | $731.91 | +$1237.89 | -$1365.27 | Position open |
| Day 21 | 2026-05-20 | $739.41 | +$1657.89 | -$1785.27 | Position open |
| Day 22 | 2026-05-21 | $740.80 | +$1735.73 | -$1863.11 | Position open |
| Day 23 | 2026-05-22 | $743.75 | +$1900.93 | -$2028.31 | Position open |
| Day 24 | 2026-05-26 | $748.53 | +$2168.61 | -$2295.99 | Position open |
| Day 25 | 2026-05-27 | $748.66 | +$2175.89 | -$2303.27 | Position open |
| Day 26 | 2026-05-28 | $752.74 | +$2404.37 | -$2531.75 | Position open |
| Day 27 | 2026-05-29 | $754.40 | +$2497.33 | -$2624.71 | Position open |
| Day 28 | 2026-06-01 | $756.49 | +$2614.37 | -$2741.75 | Position open |
| Day 29 | 2026-06-02 | $757.52 | +$2672.05 | -$2799.43 | Position open |
| Day 30 | 2026-06-03 | $752.24 | +$2376.37 | -$2503.75 | Position open |
| Day 31 | 2026-06-04 | $755.03 | +$2532.61 | -$2659.99 | Position open |
| Day 32 | 2026-06-05 | $735.56 | +$1442.29 | -$1569.67 | Position open |
| Day 33 | 2026-06-08 | $737.34 | +$1541.97 | -$1669.35 | Position open |
| Day 34 | 2026-06-09 | $735.18 | +$1421.01 | -$1548.39 | Position open |
| Day 35 | 2026-06-10 | $723.72 | +$779.25 | -$906.63 | Position open |
| Day 36 | 2026-06-11 | $735.77 | +$1454.05 | -$1581.43 | Position open |
| Day 37 | 2026-06-12 | $739.76 | +$1677.49 | -$1804.87 | Position open |
| Day 38 | 2026-06-15 | $752.81 | +$2408.29 | -$2535.67 | Position open |
| Day 39 | 2026-06-16 | $748.65 | +$2175.33 | -$2302.71 | Position open |
| Day 40 | 2026-06-17 | $739.12 | +$1641.65 | -$1769.03 | Holding would have been **$1769.03** better — honest entry |
| Day 41 | 2026-06-18 | $746.75 | +$2068.93 | -$2196.31 | Holding would have been **$2196.31** better — honest entry |
| Day 42 | 2026-06-22 | $744.27 | +$1930.05 | -$2057.43 | Holding would have been **$2057.43** better — honest entry |
| Day 43 | 2026-06-23 | $733.62 | +$1333.65 | -$1461.03 | Holding would have been **$1461.03** better — honest entry |
| Day 44 | 2026-06-24 | $733.32 | +$1316.85 | -$1444.23 | Holding would have been **$1444.23** better — honest entry |
| Day 45 | 2026-06-25 | $733.33 | +$1317.41 | -$1444.79 | Holding would have been **$1444.79** better — honest entry |
| Day 46 | 2026-06-26 | $729.35 | +$1094.53 | -$1221.91 | Holding would have been **$1221.91** better — honest entry |
| Day 47 | 2026-06-29 | $740.86 | +$1739.09 | -$1866.47 | Holding would have been **$1866.47** better — honest entry |
| Day 48 | 2026-06-30 | $746.65 | +$2063.33 | -$2190.71 | Holding would have been **$2190.71** better — honest entry |
| Day 49 | 2026-07-01 | $745.66 | +$2007.89 | -$2135.27 | Holding would have been **$2135.27** better — honest entry |
| Day 50 | 2026-07-02 | $744.86 | +$1963.09 | -$2090.47 | Holding would have been **$2090.47** better — honest entry |
| Day 51 | 2026-07-06 | $751.27 | +$2322.05 | -$2449.43 | Holding would have been **$2449.43** better — honest entry |
| Day 52 | 2026-07-07 | $747.77 | +$2126.05 | -$2253.43 | Holding would have been **$2253.43** better — honest entry |
| Day 53 | 2026-07-08 | $745.28 | +$1986.61 | -$2113.99 | Holding would have been **$2113.99** better — honest entry |
| Day 54 | 2026-07-09 | $751.55 | +$2337.73 | -$2465.11 | Holding would have been **$2465.11** better — honest entry |
| Day 55 | 2026-07-10 | $754.94 | +$2527.57 | -$2654.95 | Holding would have been **$2654.95** better — honest entry |
| Day 56 | 2026-07-13 | $749.13 | +$2202.21 | -$2329.59 | Holding would have been **$2329.59** better — honest entry |
| Day 57 | 2026-07-14 | $751.94 | +$2359.57 | -$2486.95 | Holding would have been **$2486.95** better — honest entry |
| Day 58 | 2026-07-15 | $754.77 | +$2518.05 | -$2645.43 | Holding would have been **$2645.43** better — honest entry |
| Day 59 | 2026-07-16 | $750.87 | +$2299.65 | -$2427.03 | Holding would have been **$2427.03** better — honest entry |
| Day 60 | 2026-07-17 | $743.28 | +$1874.61 | -$2001.99 | Holding would have been **$2001.99** better — honest entry |
| Day 61 | 2026-07-20 | $742.15 | +$1811.33 | -$1938.71 | Holding would have been **$1938.71** better — honest entry |
| Day 62 | 2026-07-21 | $748.15 | +$2147.33 | -$2274.71 | Position open |
| Day 63 | 2026-07-22 | $747.49 | +$2110.37 | -$2237.75 | Position open |
| Day 64 | 2026-07-23 | $738.06 | +$1582.29 | -$1709.67 | Position open |
| Day 65 | 2026-07-24 | $738.90 | +$1629.33 | -$1756.71 | Holding would have been **$1756.71** better — honest entry |
| Day 66 | 2026-07-27 | $738.85 | +$1626.53 | -$1753.91 | Holding would have been **$1753.91** better — honest entry |
| Day 67 | 2026-07-28 | $740.79 | +$1735.17 | -$1862.55 | Holding would have been **$1862.55** better — honest entry |
| Day 68 | 2026-07-29 | $729.57 | +$1106.85 | -$1234.23 | Holding would have been **$1234.23** better — honest entry |
| Day 69 | 2026-07-30 | $741.63 | +$1782.21 | -$1909.59 | Holding would have been **$1909.59** better — honest entry |
| Day 70 | 2026-07-31 | $746.79 | +$2071.17 | -$2198.55 | Holding would have been **$2198.55** better — honest entry |
| Day 71 | 2026-08-03 | $757.72 | +$2683.25 | -$2810.63 | Holding would have been **$2810.63** better — honest entry |
| Day 72 | 2026-08-04 | $771.11 | +$3433.09 | -$3560.47 | Position open |
| Day 73 | 2026-08-05 | $769.79 | +$3359.17 | -$3486.55 | Holding would have been **$3486.55** better — honest entry |
| Day 74 | 2026-08-06 | $768.64 | +$3294.77 | -$3422.15 | Holding would have been **$3422.15** better — honest entry |
| Day 75 | 2026-08-07 | $773.16 | +$3547.89 | -$3675.27 | Position open |

---

## Daily Entries

### Day 1 — 2026-04-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T1) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $709.37 |
| Unrealized P&L | -$24.35 |
| P&L % | -0.061% |
| Portfolio value | $99,975.65 |
| Benchmark value | $100,000.03 |
| Alpha (cumulative) | -0.024% |

**Regime call:** BEAR

**Market context:** Risk-on trade buoyed small cap sentiment, while the VIX remains calm. The S&P 500 climbed on a ceasefire extension and tech tailwinds.

**Strategy note:** The system held a long SPY position, despite a bear regime, due to a bullish fast signal from the 10/30 SMA crossover. Unrealized P&L was -0.01% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.06% from entry. No exit triggered.

**Key learning:** A bear regime does not necessarily mean a bear market, as the system's fast signal can override the slow filter.

---

### Day 2 — 2026-04-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $706.59 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | -$180.03 |
| Signal saved | +$52.65 |
| Portfolio value | $99,872.05 |
| Benchmark value | $99,608.13 |
| Alpha (cumulative) | +0.264% |

**Regime call:** BULL

**Market context:** The S&P 500 retreated but held 7100 on fresh Mideast escalation as earnings kick off, while VIX crept toward 20 as Iran fears and Tesla's whipsaw rattle nerves.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and strong momentum, causing the system to hold long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long in a bull regime despite rising VIX is being tested.

---

### Day 3 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T2) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $712.14 |
| Unrealized P&L | +$48.32 |
| P&L % | +0.121% |
| Portfolio value | $99,920.37 |
| Benchmark value | $100,390.52 |
| Alpha (cumulative) | -0.471% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +0.12% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 4 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T2) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $713.33 |
| Unrealized P&L | +$114.96 |
| P&L % | +0.289% |
| Portfolio value | $99,987.01 |
| Benchmark value | $100,558.27 |
| Alpha (cumulative) | -0.571% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 5 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T2) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $709.85 |
| Unrealized P&L | -$79.92 |
| P&L % | -0.201% |
| Portfolio value | $99,792.13 |
| Benchmark value | $100,067.70 |
| Alpha (cumulative) | -0.276% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.20% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 6 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $709.76 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | -$2.51 |
| Signal saved | -$124.87 |
| Portfolio value | $99,756.85 |
| Benchmark value | $100,055.01 |
| Alpha (cumulative) | -0.298% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 7 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $716.56 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$378.29 |
| Signal saved | -$505.67 |
| Portfolio value | $100,014.25 |
| Benchmark value | $101,013.61 |
| Alpha (cumulative) | -1.000% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 8 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,792.62 |
| Benchmark value | $101,306.82 |
| Alpha (cumulative) | -1.514% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 9 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,661.17 |
| Benchmark value | $100,969.91 |
| Alpha (cumulative) | -1.309% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 10 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $99,969.17 |
| Benchmark value | $101,759.34 |
| Alpha (cumulative) | -1.790% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 11 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,520.82 |
| Benchmark value | $103,173.27 |
| Alpha (cumulative) | -2.652% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 12 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,398.17 |
| Benchmark value | $102,858.91 |
| Alpha (cumulative) | -2.461% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 13 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,728.17 |
| Benchmark value | $103,704.73 |
| Alpha (cumulative) | -2.977% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 14 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,818.92 |
| Benchmark value | $103,937.33 |
| Alpha (cumulative) | -3.118% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 15 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,763.37 |
| Benchmark value | $103,794.95 |
| Alpha (cumulative) | -3.032% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 16 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $100,988.87 |
| Benchmark value | $104,372.93 |
| Alpha (cumulative) | -3.384% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 17 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,307.32 |
| Benchmark value | $105,189.14 |
| Alpha (cumulative) | -3.882% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 18 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,813.42 |
| Benchmark value | $103,923.23 |
| Alpha (cumulative) | -3.110% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 19 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,774.92 |
| Benchmark value | $103,824.55 |
| Alpha (cumulative) | -3.050% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 20 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,522.47 |
| Benchmark value | $103,177.50 |
| Alpha (cumulative) | -2.654% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 21 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $100,934.97 |
| Benchmark value | $104,234.78 |
| Alpha (cumulative) | -3.300% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 22 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $101,011.42 |
| Benchmark value | $104,430.72 |
| Alpha (cumulative) | -3.420% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 23 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,173.67 |
| Benchmark value | $104,846.59 |
| Alpha (cumulative) | -3.673% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 24 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,436.57 |
| Benchmark value | $105,520.42 |
| Alpha (cumulative) | -4.083% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 25 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,443.72 |
| Benchmark value | $105,538.75 |
| Alpha (cumulative) | -4.095% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 26 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,668.12 |
| Benchmark value | $106,113.91 |
| Alpha (cumulative) | -4.446% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 27 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,759.42 |
| Benchmark value | $106,347.92 |
| Alpha (cumulative) | -4.589% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 28 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $101,874.37 |
| Benchmark value | $106,642.55 |
| Alpha (cumulative) | -4.769% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 29 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $101,931.02 |
| Benchmark value | $106,787.75 |
| Alpha (cumulative) | -4.857% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 30 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,640.62 |
| Benchmark value | $106,043.42 |
| Alpha (cumulative) | -4.402% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 31 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,794.07 |
| Benchmark value | $106,436.73 |
| Alpha (cumulative) | -4.643% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 32 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,723.22 |
| Benchmark value | $103,692.04 |
| Alpha (cumulative) | -2.969% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 33 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,821.12 |
| Benchmark value | $103,942.97 |
| Alpha (cumulative) | -3.122% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 34 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,702.32 |
| Benchmark value | $103,638.47 |
| Alpha (cumulative) | -2.936% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 35 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,072.02 |
| Benchmark value | $102,022.95 |
| Alpha (cumulative) | -1.951% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 36 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,734.77 |
| Benchmark value | $103,721.64 |
| Alpha (cumulative) | -2.987% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 37 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $100,954.22 |
| Benchmark value | $104,284.12 |
| Alpha (cumulative) | -3.330% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 38 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,671.97 |
| Benchmark value | $106,123.78 |
| Alpha (cumulative) | -4.452% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 39 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T4) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,443.17 |
| Benchmark value | $105,537.34 |
| Alpha (cumulative) | -4.094% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 40 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $739.12 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1641.65 |
| Signal saved | -$1769.03 |
| Portfolio value | $101,186.32 |
| Benchmark value | $104,193.89 |
| Alpha (cumulative) | -3.008% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 41 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $746.75 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2068.93 |
| Signal saved | -$2196.31 |
| Portfolio value | $101,186.32 |
| Benchmark value | $105,269.50 |
| Alpha (cumulative) | -4.084% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 42 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $744.27 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1930.05 |
| Signal saved | -$2057.43 |
| Portfolio value | $101,185.21 |
| Benchmark value | $104,919.89 |
| Alpha (cumulative) | -3.735% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 43 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $733.62 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1333.65 |
| Signal saved | -$1461.03 |
| Portfolio value | $101,185.21 |
| Benchmark value | $103,418.56 |
| Alpha (cumulative) | -2.234% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 44 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $733.32 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1316.85 |
| Signal saved | -$1444.23 |
| Portfolio value | $101,185.21 |
| Benchmark value | $103,376.27 |
| Alpha (cumulative) | -2.191% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 45 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $733.33 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1317.41 |
| Signal saved | -$1444.79 |
| Portfolio value | $101,185.21 |
| Benchmark value | $103,377.68 |
| Alpha (cumulative) | -2.193% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 46 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $729.35 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1094.53 |
| Signal saved | -$1221.91 |
| Portfolio value | $101,185.21 |
| Benchmark value | $102,816.62 |
| Alpha (cumulative) | -1.632% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 47 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $740.86 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1739.09 |
| Signal saved | -$1866.47 |
| Portfolio value | $101,185.21 |
| Benchmark value | $104,439.18 |
| Alpha (cumulative) | -3.254% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 48 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $746.65 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2063.33 |
| Signal saved | -$2190.71 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,255.40 |
| Alpha (cumulative) | -4.070% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 49 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $745.66 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2007.89 |
| Signal saved | -$2135.27 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,115.84 |
| Alpha (cumulative) | -3.931% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 50 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $744.86 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1963.09 |
| Signal saved | -$2090.47 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,003.06 |
| Alpha (cumulative) | -3.818% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 51 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $751.27 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2322.05 |
| Signal saved | -$2449.43 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,906.68 |
| Alpha (cumulative) | -4.722% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 52 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $747.77 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2126.05 |
| Signal saved | -$2253.43 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,413.29 |
| Alpha (cumulative) | -4.228% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 53 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $745.28 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1986.61 |
| Signal saved | -$2113.99 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,062.27 |
| Alpha (cumulative) | -3.877% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 54 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $751.55 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2337.73 |
| Signal saved | -$2465.11 |
| Portfolio value | $101,185.21 |
| Benchmark value | $105,946.15 |
| Alpha (cumulative) | -4.761% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 55 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $754.94 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2527.57 |
| Signal saved | -$2654.95 |
| Portfolio value | $101,185.21 |
| Benchmark value | $106,424.04 |
| Alpha (cumulative) | -5.239% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 56 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $749.13 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2202.21 |
| Signal saved | -$2329.59 |
| Portfolio value | $101,024.09 |
| Benchmark value | $105,605.01 |
| Alpha (cumulative) | -4.581% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 57 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $751.94 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2359.57 |
| Signal saved | -$2486.95 |
| Portfolio value | $100,989.01 |
| Benchmark value | $106,001.13 |
| Alpha (cumulative) | -5.012% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 58 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $754.77 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2518.05 |
| Signal saved | -$2645.43 |
| Portfolio value | $101,036.76 |
| Benchmark value | $106,400.08 |
| Alpha (cumulative) | -5.363% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 59 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $750.87 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2299.65 |
| Signal saved | -$2427.03 |
| Portfolio value | $100,860.63 |
| Benchmark value | $105,850.29 |
| Alpha (cumulative) | -4.989% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 60 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $743.28 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1874.61 |
| Signal saved | -$2001.99 |
| Portfolio value | $100,718.07 |
| Benchmark value | $104,780.33 |
| Alpha (cumulative) | -4.062% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 61 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $742.15 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1811.33 |
| Signal saved | -$1938.71 |
| Portfolio value | $100,526.09 |
| Benchmark value | $104,621.03 |
| Alpha (cumulative) | -4.095% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 62 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T12) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $100,554.18 |
| Benchmark value | $105,466.86 |
| Alpha (cumulative) | -4.913% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 63 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T12) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $100,519.20 |
| Benchmark value | $105,373.81 |
| Alpha (cumulative) | -4.855% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 64 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T13) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $99,850.06 |
| Benchmark value | $104,044.47 |
| Alpha (cumulative) | -4.194% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 65 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $738.90 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1629.33 |
| Signal saved | -$1756.71 |
| Portfolio value | $99,898.94 |
| Benchmark value | $104,162.88 |
| Alpha (cumulative) | -4.264% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 66 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $738.85 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1626.53 |
| Signal saved | -$1753.91 |
| Portfolio value | $100,003.08 |
| Benchmark value | $104,155.83 |
| Alpha (cumulative) | -4.153% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 67 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $740.79 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1735.17 |
| Signal saved | -$1862.55 |
| Portfolio value | $99,959.62 |
| Benchmark value | $104,429.31 |
| Alpha (cumulative) | -4.469% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 68 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $729.57 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1106.85 |
| Signal saved | -$1234.23 |
| Portfolio value | $99,959.62 |
| Benchmark value | $102,847.63 |
| Alpha (cumulative) | -2.888% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 69 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $741.63 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$1782.21 |
| Signal saved | -$1909.59 |
| Portfolio value | $99,959.62 |
| Benchmark value | $104,547.73 |
| Alpha (cumulative) | -4.588% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 70 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $746.79 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2071.17 |
| Signal saved | -$2198.55 |
| Portfolio value | $99,959.62 |
| Benchmark value | $105,275.14 |
| Alpha (cumulative) | -5.315% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 71 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $757.72 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$2683.25 |
| Signal saved | -$2810.63 |
| Portfolio value | $99,959.62 |
| Benchmark value | $106,815.94 |
| Alpha (cumulative) | -6.856% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 72 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T16) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $771.11 |
| Unrealized P&L | -$52.00 |
| P&L % | -0.135% |
| Portfolio value | $99,907.62 |
| Benchmark value | $108,703.53 |
| Alpha (cumulative) | -8.796% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: -0.14% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 73 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $769.79 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$3359.17 |
| Signal saved | -$3486.55 |
| Portfolio value | $99,872.62 |
| Benchmark value | $108,517.45 |
| Alpha (cumulative) | -8.644% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 74 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $768.64 |
| Realized P&L (locked) | -$127.38 |
| Reference if held | +$3294.77 |
| Signal saved | -$3422.15 |
| Portfolio value | $99,872.62 |
| Benchmark value | $108,355.33 |
| Alpha (cumulative) | -8.482% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-127.38. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 75 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T17) |
| Entry (Alpaca fill) | $709.805/share |
| Close price | $773.16 |
| Unrealized P&L | +$33.14 |
| P&L % | +0.084% |
| Portfolio value | $99,905.76 |
| Benchmark value | $108,992.52 |
| Alpha (cumulative) | -9.087% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $750.17 vs MA50 $746.61). Momentum: STRONG. Unrealized P&L: +0.08% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

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
_Day 75 of 90 · Alpaca equity: $99,901.23 · Cumulative alpha vs SPY: -9.087%_