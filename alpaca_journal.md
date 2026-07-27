# ALPACA PAPER JOURNAL — SPY
_Last updated: July 27, 2026 | Day 69 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$710.606/share**
> (2026-04-17, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-07-27): **BULLISH**  
> Fast: MA10 $745.46 | MA30 $744.49  
> Slow: MA20 $746.66 | MA50 $744.08  
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

**Total trades:** 16 | **Closed:** 16 | **Open:** No | **Cumulative Realized P&L:** -$28.90

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $710.606 (2026-04-17) | $710.500 (2026-04-17) | 56 | -$5.92 | ✅ Closed |
| T2 | $706.745 (2026-04-20) | $706.280 (2026-04-21) | 56 | -$26.06 | ✅ Closed |
| T3 | $709.805 (2026-04-22) | $707.520 (2026-04-23) | 56 | -$127.95 | ✅ Closed |
| T4 | $711.277 (2026-04-24) | $709.220 (2026-04-29) | 56 | -$115.20 | ✅ Closed |
| T5 | $714.440 (2026-04-30) | $719.120 (2026-04-30) | 55 | +$257.40 | ✅ Closed |
| T6 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 55 | +$1172.07 | ✅ Closed |
| T7 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T8 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T9 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T10 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T11 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T12 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T13 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T14 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T15 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T16 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $100,008.09 |
| Alpaca cash | $100,008.09 |
| Cumulative realized P&L | -$28.90 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-17 | $708.24 | FLAT | — | — | $99,994.08 |
| Day 2 | 2026-04-20 | $706.97 | Long 56 SPY (T2) | +$12.58 | +0.032% | $100,006.66 |
| Day 3 | 2026-04-21 | $702.10 | FLAT | — | — | $99,968.02 |
| Day 4 | 2026-04-22 | $709.37 | Long 56 SPY (T3) | -$24.35 | -0.061% | $99,943.67 |
| Day 5 | 2026-04-23 | $706.59 | FLAT | — | — | $99,840.07 |
| Day 6 | 2026-04-24 | $712.14 | Long 56 SPY (T4) | +$48.32 | +0.121% | $99,888.39 |
| Day 7 | 2026-04-27 | $713.33 | Long 56 SPY (T4) | +$114.96 | +0.289% | $99,955.03 |
| Day 8 | 2026-04-28 | $709.85 | Long 56 SPY (T4) | -$79.92 | -0.201% | $99,760.15 |
| Day 9 | 2026-04-29 | $709.76 | FLAT | — | — | $99,724.87 |
| Day 10 | 2026-04-30 | $716.56 | FLAT | — | — | $99,982.27 |
| Day 11 | 2026-05-01 | $718.64 | Long 55 SPY (T6) | -$221.63 | -0.558% | $99,760.64 |
| Day 12 | 2026-05-04 | $716.25 | Long 55 SPY (T6) | -$353.08 | -0.888% | $99,629.19 |
| Day 13 | 2026-05-05 | $721.85 | Long 55 SPY (T6) | -$45.08 | -0.113% | $99,937.19 |
| Day 14 | 2026-05-06 | $731.88 | Long 55 SPY (T6) | +$506.57 | +1.274% | $100,488.84 |
| Day 15 | 2026-05-07 | $729.65 | Long 55 SPY (T6) | +$383.92 | +0.966% | $100,366.19 |
| Day 16 | 2026-05-08 | $735.65 | Long 55 SPY (T6) | +$713.92 | +1.796% | $100,696.19 |
| Day 17 | 2026-05-11 | $737.30 | Long 55 SPY (T6) | +$804.67 | +2.024% | $100,786.94 |
| Day 18 | 2026-05-12 | $736.29 | Long 55 SPY (T6) | +$749.12 | +1.885% | $100,731.39 |
| Day 19 | 2026-05-13 | $740.39 | Long 55 SPY (T6) | +$974.62 | +2.452% | $100,956.89 |
| Day 20 | 2026-05-14 | $746.18 | Long 55 SPY (T6) | +$1293.07 | +3.253% | $101,275.34 |
| Day 21 | 2026-05-15 | $737.20 | Long 55 SPY (T6) | +$799.17 | +2.011% | $100,781.44 |
| Day 22 | 2026-05-18 | $736.50 | Long 55 SPY (T6) | +$760.67 | +1.914% | $100,742.94 |
| Day 23 | 2026-05-19 | $731.91 | Long 55 SPY (T6) | +$508.22 | +1.279% | $100,490.49 |
| Day 24 | 2026-05-20 | $739.41 | Long 55 SPY (T6) | +$920.72 | +2.316% | $100,902.99 |
| Day 25 | 2026-05-21 | $740.80 | Long 55 SPY (T6) | +$997.17 | +2.509% | $100,979.44 |
| Day 26 | 2026-05-22 | $743.75 | Long 55 SPY (T6) | +$1159.42 | +2.917% | $101,141.69 |
| Day 27 | 2026-05-26 | $748.53 | Long 55 SPY (T6) | +$1422.32 | +3.578% | $101,404.59 |
| Day 28 | 2026-05-27 | $748.66 | Long 55 SPY (T6) | +$1429.47 | +3.596% | $101,411.74 |
| Day 29 | 2026-05-28 | $752.74 | Long 55 SPY (T6) | +$1653.87 | +4.161% | $101,636.14 |
| Day 30 | 2026-05-29 | $754.40 | Long 55 SPY (T6) | +$1745.17 | +4.391% | $101,727.44 |
| Day 31 | 2026-06-01 | $756.49 | Long 55 SPY (T6) | +$1860.12 | +4.680% | $101,842.39 |
| Day 32 | 2026-06-02 | $757.52 | Long 55 SPY (T6) | +$1916.77 | +4.822% | $101,899.04 |
| Day 33 | 2026-06-03 | $752.24 | Long 55 SPY (T6) | +$1626.37 | +4.092% | $101,608.64 |
| Day 34 | 2026-06-04 | $755.03 | Long 55 SPY (T6) | +$1779.82 | +4.478% | $101,762.09 |
| Day 35 | 2026-06-05 | $735.56 | Long 55 SPY (T6) | +$708.97 | +1.784% | $100,691.24 |
| Day 36 | 2026-06-08 | $737.34 | Long 55 SPY (T6) | +$806.87 | +2.030% | $100,789.14 |
| Day 37 | 2026-06-09 | $735.18 | Long 55 SPY (T6) | +$688.07 | +1.731% | $100,670.34 |
| Day 38 | 2026-06-10 | $723.72 | Long 55 SPY (T6) | +$57.77 | +0.145% | $100,040.04 |
| Day 39 | 2026-06-11 | $735.77 | Long 55 SPY (T6) | +$720.52 | +1.813% | $100,702.79 |
| Day 40 | 2026-06-12 | $739.76 | Long 55 SPY (T6) | +$939.97 | +2.365% | $100,922.24 |
| Day 41 | 2026-06-15 | $752.81 | Long 55 SPY (T6) | +$1657.72 | +4.171% | $101,639.99 |
| Day 42 | 2026-06-16 | $748.65 | Long 55 SPY (T6) | +$1428.92 | +3.595% | $101,411.19 |
| Day 43 | 2026-06-17 | $739.12 | FLAT | — | — | $101,154.34 |
| Day 44 | 2026-06-18 | $746.75 | FLAT | — | — | $101,154.34 |
| Day 45 | 2026-06-22 | $744.27 | FLAT | — | — | $101,153.23 |
| Day 46 | 2026-06-23 | $733.62 | FLAT | — | — | $101,153.23 |
| Day 47 | 2026-06-24 | $733.32 | FLAT | — | — | $101,153.23 |
| Day 48 | 2026-06-25 | $733.33 | FLAT | — | — | $101,153.23 |
| Day 49 | 2026-06-26 | $729.35 | FLAT | — | — | $101,153.23 |
| Day 50 | 2026-06-29 | $740.86 | FLAT | — | — | $101,153.23 |
| Day 51 | 2026-06-30 | $746.65 | FLAT | — | — | $101,153.23 |
| Day 52 | 2026-07-01 | $745.66 | FLAT | — | — | $101,153.23 |
| Day 53 | 2026-07-02 | $744.86 | FLAT | — | — | $101,153.23 |
| Day 54 | 2026-07-06 | $751.27 | FLAT | — | — | $101,153.23 |
| Day 55 | 2026-07-07 | $747.77 | FLAT | — | — | $101,153.23 |
| Day 56 | 2026-07-08 | $745.28 | FLAT | — | — | $101,153.23 |
| Day 57 | 2026-07-09 | $751.55 | FLAT | — | — | $101,153.23 |
| Day 58 | 2026-07-10 | $754.94 | FLAT | — | — | $101,153.23 |
| Day 59 | 2026-07-13 | $749.13 | FLAT | — | — | $100,992.11 |
| Day 60 | 2026-07-14 | $751.94 | FLAT | — | — | $100,957.03 |
| Day 61 | 2026-07-15 | $754.77 | FLAT | — | — | $101,004.78 |
| Day 62 | 2026-07-16 | $750.87 | FLAT | — | — | $100,828.65 |
| Day 63 | 2026-07-17 | $743.28 | FLAT | — | — | $100,686.09 |
| Day 64 | 2026-07-20 | $742.15 | FLAT | — | — | $100,494.11 |
| Day 65 | 2026-07-21 | $748.15 | Long 53 SPY (T14) | +$28.09 | +0.071% | $100,522.20 |
| Day 66 | 2026-07-22 | $747.49 | Long 53 SPY (T14) | -$6.89 | -0.017% | $100,487.22 |
| Day 67 | 2026-07-23 | $738.06 | Long 52 SPY (T15) | -$40.56 | -0.106% | $99,818.08 |
| Day 68 | 2026-07-24 | $738.90 | FLAT | — | — | $99,866.96 |
| Day 69 | 2026-07-27 | $738.85 | FLAT | — | — | $99,971.10 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-17 | $99,994.08 | $100,000.02 | -0.0059% | +0.000% | **-0.006%** |
| Day 2 | 2026-04-20 | $100,006.66 | $99,820.70 | +0.0067% | -0.179% | **+0.186%** |
| Day 3 | 2026-04-21 | $99,968.02 | $99,133.08 | -0.0320% | -0.867% | **+0.835%** |
| Day 4 | 2026-04-22 | $99,943.67 | $100,159.57 | -0.0563% | +0.160% | **-0.216%** |
| Day 5 | 2026-04-23 | $99,840.07 | $99,767.05 | -0.1599% | -0.233% | **+0.073%** |
| Day 6 | 2026-04-24 | $99,888.39 | $100,550.68 | -0.1116% | +0.551% | **-0.663%** |
| Day 7 | 2026-04-27 | $99,955.03 | $100,718.70 | -0.0450% | +0.719% | **-0.764%** |
| Day 8 | 2026-04-28 | $99,760.15 | $100,227.34 | -0.2399% | +0.227% | **-0.467%** |
| Day 9 | 2026-04-29 | $99,724.87 | $100,214.63 | -0.2751% | +0.215% | **-0.490%** |
| Day 10 | 2026-04-30 | $99,982.27 | $101,174.76 | -0.0177% | +1.175% | **-1.193%** |
| Day 11 | 2026-05-01 | $99,760.64 | $101,468.45 | -0.2394% | +1.468% | **-1.707%** |
| Day 12 | 2026-05-04 | $99,629.19 | $101,130.99 | -0.3708% | +1.131% | **-1.502%** |
| Day 13 | 2026-05-05 | $99,937.19 | $101,921.68 | -0.0628% | +1.922% | **-1.985%** |
| Day 14 | 2026-05-06 | $100,488.84 | $103,337.87 | +0.4888% | +3.338% | **-2.849%** |
| Day 15 | 2026-05-07 | $100,366.19 | $103,023.00 | +0.3662% | +3.023% | **-2.657%** |
| Day 16 | 2026-05-08 | $100,696.19 | $103,870.18 | +0.6962% | +3.870% | **-3.174%** |
| Day 17 | 2026-05-11 | $100,786.94 | $104,103.15 | +0.7869% | +4.103% | **-3.316%** |
| Day 18 | 2026-05-12 | $100,731.39 | $103,960.54 | +0.7314% | +3.961% | **-3.230%** |
| Day 19 | 2026-05-13 | $100,956.89 | $104,539.44 | +0.9569% | +4.539% | **-3.582%** |
| Day 20 | 2026-05-14 | $101,275.34 | $105,356.96 | +1.2753% | +5.357% | **-4.082%** |
| Day 21 | 2026-05-15 | $100,781.44 | $104,089.03 | +0.7814% | +4.089% | **-3.308%** |
| Day 22 | 2026-05-18 | $100,742.94 | $103,990.19 | +0.7429% | +3.990% | **-3.247%** |
| Day 23 | 2026-05-19 | $100,490.49 | $103,342.11 | +0.4905% | +3.342% | **-2.852%** |
| Day 24 | 2026-05-20 | $100,902.99 | $104,401.07 | +0.9030% | +4.401% | **-3.498%** |
| Day 25 | 2026-05-21 | $100,979.44 | $104,597.33 | +0.9794% | +4.597% | **-3.618%** |
| Day 26 | 2026-05-22 | $101,141.69 | $105,013.86 | +1.1417% | +5.014% | **-3.872%** |
| Day 27 | 2026-05-26 | $101,404.59 | $105,688.77 | +1.4046% | +5.689% | **-4.284%** |
| Day 28 | 2026-05-27 | $101,411.74 | $105,707.12 | +1.4117% | +5.707% | **-4.295%** |
| Day 29 | 2026-05-28 | $101,636.14 | $106,283.20 | +1.6361% | +6.283% | **-4.647%** |
| Day 30 | 2026-05-29 | $101,727.44 | $106,517.58 | +1.7274% | +6.518% | **-4.791%** |
| Day 31 | 2026-06-01 | $101,842.39 | $106,812.68 | +1.8424% | +6.813% | **-4.971%** |
| Day 32 | 2026-06-02 | $101,899.04 | $106,958.11 | +1.8990% | +6.958% | **-5.059%** |
| Day 33 | 2026-06-03 | $101,608.64 | $106,212.60 | +1.6086% | +6.213% | **-4.604%** |
| Day 34 | 2026-06-04 | $101,762.09 | $106,606.54 | +1.7621% | +6.607% | **-4.845%** |
| Day 35 | 2026-06-05 | $100,691.24 | $103,857.47 | +0.6912% | +3.857% | **-3.166%** |
| Day 36 | 2026-06-08 | $100,789.14 | $104,108.80 | +0.7891% | +4.109% | **-3.320%** |
| Day 37 | 2026-06-09 | $100,670.34 | $103,803.81 | +0.6703% | +3.804% | **-3.134%** |
| Day 38 | 2026-06-10 | $100,040.04 | $102,185.72 | +0.0400% | +2.186% | **-2.146%** |
| Day 39 | 2026-06-11 | $100,702.79 | $103,887.12 | +0.7028% | +3.887% | **-3.184%** |
| Day 40 | 2026-06-12 | $100,922.24 | $104,450.49 | +0.9222% | +4.450% | **-3.528%** |
| Day 41 | 2026-06-15 | $101,639.99 | $106,293.08 | +1.6400% | +6.293% | **-4.653%** |
| Day 42 | 2026-06-16 | $101,411.19 | $105,705.71 | +1.4112% | +5.706% | **-4.295%** |
| Day 43 | 2026-06-17 | $101,154.34 | $104,360.12 | +1.1543% | +4.360% | **-3.206%** |
| Day 44 | 2026-06-18 | $101,154.34 | $105,437.44 | +1.1543% | +5.437% | **-4.283%** |
| Day 45 | 2026-06-22 | $101,153.23 | $105,087.28 | +1.1532% | +5.087% | **-3.934%** |
| Day 46 | 2026-06-23 | $101,153.23 | $103,583.55 | +1.1532% | +3.584% | **-2.431%** |
| Day 47 | 2026-06-24 | $101,153.23 | $103,541.19 | +1.1532% | +3.541% | **-2.388%** |
| Day 48 | 2026-06-25 | $101,153.23 | $103,542.60 | +1.1532% | +3.543% | **-2.390%** |
| Day 49 | 2026-06-26 | $101,153.23 | $102,980.65 | +1.1532% | +2.981% | **-1.828%** |
| Day 50 | 2026-06-29 | $101,153.23 | $104,605.80 | +1.1532% | +4.606% | **-3.453%** |
| Day 51 | 2026-06-30 | $101,153.23 | $105,423.32 | +1.1532% | +5.423% | **-4.270%** |
| Day 52 | 2026-07-01 | $101,153.23 | $105,283.54 | +1.1532% | +5.284% | **-4.131%** |
| Day 53 | 2026-07-02 | $101,153.23 | $105,170.58 | +1.1532% | +5.171% | **-4.018%** |
| Day 54 | 2026-07-06 | $101,153.23 | $106,075.64 | +1.1532% | +6.076% | **-4.923%** |
| Day 55 | 2026-07-07 | $101,153.23 | $105,581.46 | +1.1532% | +5.581% | **-4.428%** |
| Day 56 | 2026-07-08 | $101,153.23 | $105,229.88 | +1.1532% | +5.230% | **-4.077%** |
| Day 57 | 2026-07-09 | $101,153.23 | $106,115.18 | +1.1532% | +6.115% | **-4.962%** |
| Day 58 | 2026-07-10 | $101,153.23 | $106,593.83 | +1.1532% | +6.594% | **-5.441%** |
| Day 59 | 2026-07-13 | $100,992.11 | $105,773.49 | +0.9921% | +5.773% | **-4.781%** |
| Day 60 | 2026-07-14 | $100,957.03 | $106,170.24 | +0.9570% | +6.170% | **-5.213%** |
| Day 61 | 2026-07-15 | $101,004.78 | $106,569.83 | +1.0048% | +6.570% | **-5.565%** |
| Day 62 | 2026-07-16 | $100,828.65 | $106,019.16 | +0.8286% | +6.019% | **-5.190%** |
| Day 63 | 2026-07-17 | $100,686.09 | $104,947.49 | +0.6861% | +4.947% | **-4.261%** |
| Day 64 | 2026-07-20 | $100,494.11 | $104,787.94 | +0.4941% | +4.788% | **-4.294%** |
| Day 65 | 2026-07-21 | $100,522.20 | $105,635.11 | +0.5222% | +5.635% | **-5.113%** |
| Day 66 | 2026-07-22 | $100,487.22 | $105,541.93 | +0.4872% | +5.542% | **-5.055%** |
| Day 67 | 2026-07-23 | $99,818.08 | $104,210.46 | -0.1819% | +4.210% | **-4.392%** |
| Day 68 | 2026-07-24 | $99,866.96 | $104,329.06 | -0.1330% | +4.329% | **-4.462%** |
| Day 69 | 2026-07-27 | $99,971.10 | $104,322.00 | -0.0289% | +4.322% | **-4.351%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-04-17 | $708.24 | -$132.48 | +$103.58 | Flat saved **+$103.58** vs holding |
| Day 2 | 2026-04-20 | $706.97 | -$203.60 | +$174.70 | Position open |
| Day 3 | 2026-04-21 | $702.10 | -$476.32 | +$447.42 | Flat saved **+$447.42** vs holding |
| Day 4 | 2026-04-22 | $709.37 | -$69.20 | +$40.30 | Position open |
| Day 5 | 2026-04-23 | $706.59 | -$224.88 | +$195.98 | Flat saved **+$195.98** vs holding |
| Day 6 | 2026-04-24 | $712.14 | +$85.92 | -$114.82 | Position open |
| Day 7 | 2026-04-27 | $713.33 | +$152.56 | -$181.46 | Position open |
| Day 8 | 2026-04-28 | $709.85 | -$42.32 | +$13.42 | Position open |
| Day 9 | 2026-04-29 | $709.76 | -$47.36 | +$18.46 | Flat saved **+$18.46** vs holding |
| Day 10 | 2026-04-30 | $716.56 | +$333.44 | -$362.34 | Holding would have been **$362.34** better — honest entry |
| Day 11 | 2026-05-01 | $718.64 | +$449.92 | -$478.82 | Position open |
| Day 12 | 2026-05-04 | $716.25 | +$316.08 | -$344.98 | Position open |
| Day 13 | 2026-05-05 | $721.85 | +$629.68 | -$658.58 | Position open |
| Day 14 | 2026-05-06 | $731.88 | +$1191.36 | -$1220.26 | Position open |
| Day 15 | 2026-05-07 | $729.65 | +$1066.48 | -$1095.38 | Position open |
| Day 16 | 2026-05-08 | $735.65 | +$1402.48 | -$1431.38 | Position open |
| Day 17 | 2026-05-11 | $737.30 | +$1494.88 | -$1523.78 | Position open |
| Day 18 | 2026-05-12 | $736.29 | +$1438.32 | -$1467.22 | Position open |
| Day 19 | 2026-05-13 | $740.39 | +$1667.92 | -$1696.82 | Position open |
| Day 20 | 2026-05-14 | $746.18 | +$1992.16 | -$2021.06 | Position open |
| Day 21 | 2026-05-15 | $737.20 | +$1489.28 | -$1518.18 | Position open |
| Day 22 | 2026-05-18 | $736.50 | +$1450.08 | -$1478.98 | Position open |
| Day 23 | 2026-05-19 | $731.91 | +$1193.04 | -$1221.94 | Position open |
| Day 24 | 2026-05-20 | $739.41 | +$1613.04 | -$1641.94 | Position open |
| Day 25 | 2026-05-21 | $740.80 | +$1690.88 | -$1719.78 | Position open |
| Day 26 | 2026-05-22 | $743.75 | +$1856.08 | -$1884.98 | Position open |
| Day 27 | 2026-05-26 | $748.53 | +$2123.76 | -$2152.66 | Position open |
| Day 28 | 2026-05-27 | $748.66 | +$2131.04 | -$2159.94 | Position open |
| Day 29 | 2026-05-28 | $752.74 | +$2359.52 | -$2388.42 | Position open |
| Day 30 | 2026-05-29 | $754.40 | +$2452.48 | -$2481.38 | Position open |
| Day 31 | 2026-06-01 | $756.49 | +$2569.52 | -$2598.42 | Position open |
| Day 32 | 2026-06-02 | $757.52 | +$2627.20 | -$2656.10 | Position open |
| Day 33 | 2026-06-03 | $752.24 | +$2331.52 | -$2360.42 | Position open |
| Day 34 | 2026-06-04 | $755.03 | +$2487.76 | -$2516.66 | Position open |
| Day 35 | 2026-06-05 | $735.56 | +$1397.44 | -$1426.34 | Position open |
| Day 36 | 2026-06-08 | $737.34 | +$1497.12 | -$1526.02 | Position open |
| Day 37 | 2026-06-09 | $735.18 | +$1376.16 | -$1405.06 | Position open |
| Day 38 | 2026-06-10 | $723.72 | +$734.40 | -$763.30 | Position open |
| Day 39 | 2026-06-11 | $735.77 | +$1409.20 | -$1438.10 | Position open |
| Day 40 | 2026-06-12 | $739.76 | +$1632.64 | -$1661.54 | Position open |
| Day 41 | 2026-06-15 | $752.81 | +$2363.44 | -$2392.34 | Position open |
| Day 42 | 2026-06-16 | $748.65 | +$2130.48 | -$2159.38 | Position open |
| Day 43 | 2026-06-17 | $739.12 | +$1596.80 | -$1625.70 | Holding would have been **$1625.70** better — honest entry |
| Day 44 | 2026-06-18 | $746.75 | +$2024.08 | -$2052.98 | Holding would have been **$2052.98** better — honest entry |
| Day 45 | 2026-06-22 | $744.27 | +$1885.20 | -$1914.10 | Holding would have been **$1914.10** better — honest entry |
| Day 46 | 2026-06-23 | $733.62 | +$1288.80 | -$1317.70 | Holding would have been **$1317.70** better — honest entry |
| Day 47 | 2026-06-24 | $733.32 | +$1272.00 | -$1300.90 | Holding would have been **$1300.90** better — honest entry |
| Day 48 | 2026-06-25 | $733.33 | +$1272.56 | -$1301.46 | Holding would have been **$1301.46** better — honest entry |
| Day 49 | 2026-06-26 | $729.35 | +$1049.68 | -$1078.58 | Holding would have been **$1078.58** better — honest entry |
| Day 50 | 2026-06-29 | $740.86 | +$1694.24 | -$1723.14 | Holding would have been **$1723.14** better — honest entry |
| Day 51 | 2026-06-30 | $746.65 | +$2018.48 | -$2047.38 | Holding would have been **$2047.38** better — honest entry |
| Day 52 | 2026-07-01 | $745.66 | +$1963.04 | -$1991.94 | Holding would have been **$1991.94** better — honest entry |
| Day 53 | 2026-07-02 | $744.86 | +$1918.24 | -$1947.14 | Holding would have been **$1947.14** better — honest entry |
| Day 54 | 2026-07-06 | $751.27 | +$2277.20 | -$2306.10 | Holding would have been **$2306.10** better — honest entry |
| Day 55 | 2026-07-07 | $747.77 | +$2081.20 | -$2110.10 | Holding would have been **$2110.10** better — honest entry |
| Day 56 | 2026-07-08 | $745.28 | +$1941.76 | -$1970.66 | Holding would have been **$1970.66** better — honest entry |
| Day 57 | 2026-07-09 | $751.55 | +$2292.88 | -$2321.78 | Holding would have been **$2321.78** better — honest entry |
| Day 58 | 2026-07-10 | $754.94 | +$2482.72 | -$2511.62 | Holding would have been **$2511.62** better — honest entry |
| Day 59 | 2026-07-13 | $749.13 | +$2157.36 | -$2186.26 | Holding would have been **$2186.26** better — honest entry |
| Day 60 | 2026-07-14 | $751.94 | +$2314.72 | -$2343.62 | Holding would have been **$2343.62** better — honest entry |
| Day 61 | 2026-07-15 | $754.77 | +$2473.20 | -$2502.10 | Holding would have been **$2502.10** better — honest entry |
| Day 62 | 2026-07-16 | $750.87 | +$2254.80 | -$2283.70 | Holding would have been **$2283.70** better — honest entry |
| Day 63 | 2026-07-17 | $743.28 | +$1829.76 | -$1858.66 | Holding would have been **$1858.66** better — honest entry |
| Day 64 | 2026-07-20 | $742.15 | +$1766.48 | -$1795.38 | Holding would have been **$1795.38** better — honest entry |
| Day 65 | 2026-07-21 | $748.15 | +$2102.48 | -$2131.38 | Position open |
| Day 66 | 2026-07-22 | $747.49 | +$2065.52 | -$2094.42 | Position open |
| Day 67 | 2026-07-23 | $738.06 | +$1537.44 | -$1566.34 | Position open |
| Day 68 | 2026-07-24 | $738.90 | +$1584.48 | -$1613.38 | Holding would have been **$1613.38** better — honest entry |
| Day 69 | 2026-07-27 | $738.85 | +$1581.68 | -$1610.58 | Holding would have been **$1610.58** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-04-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $708.24 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | -$132.48 |
| Signal saved | +$103.58 |
| Portfolio value | $99,994.08 |
| Benchmark value | $100,000.02 |
| Alpha (cumulative) | -0.006% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 broke above 7000, driven by a rally in tech stocks and the opening of the Strait of Hormuz. Oil prices declined, while Netflix shares plummeted. Market sentiment remains bullish.

**Strategy note:** The system exited the position due to a bear regime, as confirmed by the slow MA20/MA50 crossover. A bullish fast signal was generated, but the system prioritized the slow regime filter.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter is more important than the fast signal in determining position entry and exit decisions.

---

### Day 2 — 2026-04-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T2) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $706.97 |
| Unrealized P&L | +$12.58 |
| P&L % | +0.032% |
| Portfolio value | $100,006.66 |
| Benchmark value | $99,820.70 |
| Alpha (cumulative) | +0.186% |

**Regime call:** BEAR

**Market context:** Small Cap Stocks and Russell 2000 declined, while Oil Prices surged amid Middle East tensions. The S&P 500 held 7100, with Nasdaq Composite battling fears. Equity Futures and Exchange-Traded Funds also declined.

**Strategy note:** The system held long SPY due to a BULLISH Fast signal and BEAR regime, despite strong momentum. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +0.03% from entry. No exit triggered.

**Key learning:** A strong momentum environment can override a bearish regime context, but may also increase risk of a false signal.

---

### Day 3 — 2026-04-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $702.10 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | -$476.32 |
| Signal saved | +$447.42 |
| Portfolio value | $99,968.02 |
| Benchmark value | $99,133.08 |
| Alpha (cumulative) | +0.835% |

**Regime call:** BEAR

**Market context:** Markets rallied on Iran deal hopes, with stocks outperforming safe-havens like gold. Small caps and risk-on trades led the gains. Oil prices pulled back on the news.

**Strategy note:** The system remained long SPY despite a BEAR regime, as the fast signal remained BULLISH due to a strong golden cross. No exit was triggered.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter can sometimes conflict with the fast signal, requiring careful consideration of both indicators.

---

### Day 4 — 2026-04-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T3) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $709.37 |
| Unrealized P&L | -$24.35 |
| P&L % | -0.061% |
| Portfolio value | $99,943.67 |
| Benchmark value | $100,159.57 |
| Alpha (cumulative) | -0.216% |

**Regime call:** BEAR

**Market context:** Risk-on trade buoyed small cap sentiment, while the VIX remains calm. The S&P 500 climbed on a ceasefire extension and tech tailwinds.

**Strategy note:** The system held a long SPY position, despite a bear regime, due to a bullish fast signal from the 10/30 SMA crossover. Unrealized P&L was -0.01% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.06% from entry. No exit triggered.

**Key learning:** A bear regime does not necessarily mean a bear market, as the system's fast signal can override the slow filter.

---

### Day 5 — 2026-04-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $706.59 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | -$224.88 |
| Signal saved | +$195.98 |
| Portfolio value | $99,840.07 |
| Benchmark value | $99,767.05 |
| Alpha (cumulative) | +0.073% |

**Regime call:** BULL

**Market context:** The S&P 500 retreated but held 7100 on fresh Mideast escalation as earnings kick off, while VIX crept toward 20 as Iran fears and Tesla's whipsaw rattle nerves.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and strong momentum, causing the system to hold long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long in a bull regime despite rising VIX is being tested.

---

### Day 6 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T4) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $712.14 |
| Unrealized P&L | +$48.32 |
| P&L % | +0.121% |
| Portfolio value | $99,888.39 |
| Benchmark value | $100,550.68 |
| Alpha (cumulative) | -0.663% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +0.12% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 7 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T4) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $713.33 |
| Unrealized P&L | +$114.96 |
| P&L % | +0.289% |
| Portfolio value | $99,955.03 |
| Benchmark value | $100,718.70 |
| Alpha (cumulative) | -0.764% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 8 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T4) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $709.85 |
| Unrealized P&L | -$79.92 |
| P&L % | -0.201% |
| Portfolio value | $99,760.15 |
| Benchmark value | $100,227.34 |
| Alpha (cumulative) | -0.467% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.20% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 9 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $709.76 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | -$47.36 |
| Signal saved | +$18.46 |
| Portfolio value | $99,724.87 |
| Benchmark value | $100,214.63 |
| Alpha (cumulative) | -0.490% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 10 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $716.56 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$333.44 |
| Signal saved | -$362.34 |
| Portfolio value | $99,982.27 |
| Benchmark value | $101,174.76 |
| Alpha (cumulative) | -1.193% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 11 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,760.64 |
| Benchmark value | $101,468.45 |
| Alpha (cumulative) | -1.707% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 12 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,629.19 |
| Benchmark value | $101,130.99 |
| Alpha (cumulative) | -1.502% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 13 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $99,937.19 |
| Benchmark value | $101,921.68 |
| Alpha (cumulative) | -1.985% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 14 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,488.84 |
| Benchmark value | $103,337.87 |
| Alpha (cumulative) | -2.849% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 15 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,366.19 |
| Benchmark value | $103,023.00 |
| Alpha (cumulative) | -2.657% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 16 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,696.19 |
| Benchmark value | $103,870.18 |
| Alpha (cumulative) | -3.174% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 17 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,786.94 |
| Benchmark value | $104,103.15 |
| Alpha (cumulative) | -3.316% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 18 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,731.39 |
| Benchmark value | $103,960.54 |
| Alpha (cumulative) | -3.230% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 19 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $100,956.89 |
| Benchmark value | $104,539.44 |
| Alpha (cumulative) | -3.582% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 20 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,275.34 |
| Benchmark value | $105,356.96 |
| Alpha (cumulative) | -4.082% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 21 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,781.44 |
| Benchmark value | $104,089.03 |
| Alpha (cumulative) | -3.308% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 22 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,742.94 |
| Benchmark value | $103,990.19 |
| Alpha (cumulative) | -3.247% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 23 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,490.49 |
| Benchmark value | $103,342.11 |
| Alpha (cumulative) | -2.852% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 24 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $100,902.99 |
| Benchmark value | $104,401.07 |
| Alpha (cumulative) | -3.498% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 25 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $100,979.44 |
| Benchmark value | $104,597.33 |
| Alpha (cumulative) | -3.618% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 26 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,141.69 |
| Benchmark value | $105,013.86 |
| Alpha (cumulative) | -3.872% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 27 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,404.59 |
| Benchmark value | $105,688.77 |
| Alpha (cumulative) | -4.284% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 28 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,411.74 |
| Benchmark value | $105,707.12 |
| Alpha (cumulative) | -4.295% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 29 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,636.14 |
| Benchmark value | $106,283.20 |
| Alpha (cumulative) | -4.647% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 30 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,727.44 |
| Benchmark value | $106,517.58 |
| Alpha (cumulative) | -4.791% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 31 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $101,842.39 |
| Benchmark value | $106,812.68 |
| Alpha (cumulative) | -4.971% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 32 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $101,899.04 |
| Benchmark value | $106,958.11 |
| Alpha (cumulative) | -5.059% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 33 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,608.64 |
| Benchmark value | $106,212.60 |
| Alpha (cumulative) | -4.604% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 34 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,762.09 |
| Benchmark value | $106,606.54 |
| Alpha (cumulative) | -4.845% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 35 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,691.24 |
| Benchmark value | $103,857.47 |
| Alpha (cumulative) | -3.166% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 36 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,789.14 |
| Benchmark value | $104,108.80 |
| Alpha (cumulative) | -3.320% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 37 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,670.34 |
| Benchmark value | $103,803.81 |
| Alpha (cumulative) | -3.134% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 38 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,040.04 |
| Benchmark value | $102,185.72 |
| Alpha (cumulative) | -2.146% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 39 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,702.79 |
| Benchmark value | $103,887.12 |
| Alpha (cumulative) | -3.184% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 40 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $100,922.24 |
| Benchmark value | $104,450.49 |
| Alpha (cumulative) | -3.528% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 41 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,639.99 |
| Benchmark value | $106,293.08 |
| Alpha (cumulative) | -4.653% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 42 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T6) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,411.19 |
| Benchmark value | $105,705.71 |
| Alpha (cumulative) | -4.295% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 43 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $739.12 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1596.80 |
| Signal saved | -$1625.70 |
| Portfolio value | $101,154.34 |
| Benchmark value | $104,360.12 |
| Alpha (cumulative) | -3.206% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 44 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $746.75 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2024.08 |
| Signal saved | -$2052.98 |
| Portfolio value | $101,154.34 |
| Benchmark value | $105,437.44 |
| Alpha (cumulative) | -4.283% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 45 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $744.27 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1885.20 |
| Signal saved | -$1914.10 |
| Portfolio value | $101,153.23 |
| Benchmark value | $105,087.28 |
| Alpha (cumulative) | -3.934% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 46 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $733.62 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1288.80 |
| Signal saved | -$1317.70 |
| Portfolio value | $101,153.23 |
| Benchmark value | $103,583.55 |
| Alpha (cumulative) | -2.431% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 47 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $733.32 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1272.00 |
| Signal saved | -$1300.90 |
| Portfolio value | $101,153.23 |
| Benchmark value | $103,541.19 |
| Alpha (cumulative) | -2.388% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 48 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $733.33 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1272.56 |
| Signal saved | -$1301.46 |
| Portfolio value | $101,153.23 |
| Benchmark value | $103,542.60 |
| Alpha (cumulative) | -2.390% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 49 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $729.35 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1049.68 |
| Signal saved | -$1078.58 |
| Portfolio value | $101,153.23 |
| Benchmark value | $102,980.65 |
| Alpha (cumulative) | -1.828% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 50 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $740.86 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1694.24 |
| Signal saved | -$1723.14 |
| Portfolio value | $101,153.23 |
| Benchmark value | $104,605.80 |
| Alpha (cumulative) | -3.453% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 51 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $746.65 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2018.48 |
| Signal saved | -$2047.38 |
| Portfolio value | $101,153.23 |
| Benchmark value | $105,423.32 |
| Alpha (cumulative) | -4.270% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 52 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $745.66 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1963.04 |
| Signal saved | -$1991.94 |
| Portfolio value | $101,153.23 |
| Benchmark value | $105,283.54 |
| Alpha (cumulative) | -4.131% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 53 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $744.86 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1918.24 |
| Signal saved | -$1947.14 |
| Portfolio value | $101,153.23 |
| Benchmark value | $105,170.58 |
| Alpha (cumulative) | -4.018% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 54 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $751.27 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2277.20 |
| Signal saved | -$2306.10 |
| Portfolio value | $101,153.23 |
| Benchmark value | $106,075.64 |
| Alpha (cumulative) | -4.923% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 55 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $747.77 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2081.20 |
| Signal saved | -$2110.10 |
| Portfolio value | $101,153.23 |
| Benchmark value | $105,581.46 |
| Alpha (cumulative) | -4.428% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 56 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $745.28 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1941.76 |
| Signal saved | -$1970.66 |
| Portfolio value | $101,153.23 |
| Benchmark value | $105,229.88 |
| Alpha (cumulative) | -4.077% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 57 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $751.55 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2292.88 |
| Signal saved | -$2321.78 |
| Portfolio value | $101,153.23 |
| Benchmark value | $106,115.18 |
| Alpha (cumulative) | -4.962% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 58 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $754.94 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2482.72 |
| Signal saved | -$2511.62 |
| Portfolio value | $101,153.23 |
| Benchmark value | $106,593.83 |
| Alpha (cumulative) | -5.441% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 59 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $749.13 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2157.36 |
| Signal saved | -$2186.26 |
| Portfolio value | $100,992.11 |
| Benchmark value | $105,773.49 |
| Alpha (cumulative) | -4.781% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 60 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $751.94 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2314.72 |
| Signal saved | -$2343.62 |
| Portfolio value | $100,957.03 |
| Benchmark value | $106,170.24 |
| Alpha (cumulative) | -5.213% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 61 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $754.77 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2473.20 |
| Signal saved | -$2502.10 |
| Portfolio value | $101,004.78 |
| Benchmark value | $106,569.83 |
| Alpha (cumulative) | -5.565% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 62 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $750.87 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$2254.80 |
| Signal saved | -$2283.70 |
| Portfolio value | $100,828.65 |
| Benchmark value | $106,019.16 |
| Alpha (cumulative) | -5.190% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 63 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $743.28 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1829.76 |
| Signal saved | -$1858.66 |
| Portfolio value | $100,686.09 |
| Benchmark value | $104,947.49 |
| Alpha (cumulative) | -4.261% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 64 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $742.15 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1766.48 |
| Signal saved | -$1795.38 |
| Portfolio value | $100,494.11 |
| Benchmark value | $104,787.94 |
| Alpha (cumulative) | -4.294% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 65 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T14) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $100,522.20 |
| Benchmark value | $105,635.11 |
| Alpha (cumulative) | -5.113% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 66 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T14) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $100,487.22 |
| Benchmark value | $105,541.93 |
| Alpha (cumulative) | -5.055% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 67 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T15) |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $99,818.08 |
| Benchmark value | $104,210.46 |
| Alpha (cumulative) | -4.392% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 68 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $738.90 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1584.48 |
| Signal saved | -$1613.38 |
| Portfolio value | $99,866.96 |
| Benchmark value | $104,329.06 |
| Alpha (cumulative) | -4.462% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 69 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $710.606/share |
| Close price | $738.85 |
| Realized P&L (locked) | -$28.90 |
| Reference if held | +$1581.68 |
| Signal saved | -$1610.58 |
| Portfolio value | $99,971.10 |
| Benchmark value | $104,322.00 |
| Alpha (cumulative) | -4.351% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-28.90. Regime: BULL (MA20 $746.66 vs MA50 $744.08). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

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
_Day 69 of 90 · Alpaca equity: $100,008.09 · Cumulative alpha vs SPY: -4.351%_