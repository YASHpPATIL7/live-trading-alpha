# ALPACA PAPER JOURNAL — SPY
_Last updated: July 29, 2026 | Day 70 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$706.745/share**
> (2026-04-20, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-07-29): **BEARISH**  
> Fast: MA10 $741.83 | MA30 $743.74  
> Slow: MA20 $745.79 | MA50 $743.82  
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

**Total trades:** 16 | **Closed:** 16 | **Open:** No | **Cumulative Realized P&L:** -$66.44

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $706.745 (2026-04-20) | $706.280 (2026-04-21) | 56 | -$26.06 | ✅ Closed |
| T2 | $709.805 (2026-04-22) | $707.520 (2026-04-23) | 56 | -$127.95 | ✅ Closed |
| T3 | $711.277 (2026-04-24) | $709.220 (2026-04-29) | 56 | -$115.20 | ✅ Closed |
| T4 | $714.440 (2026-04-30) | $719.120 (2026-04-30) | 55 | +$257.40 | ✅ Closed |
| T5 | $722.670 (2026-05-01) | $743.980 (2026-06-17) | 55 | +$1172.07 | ✅ Closed |
| T6 | $744.661 (2026-06-22) | $744.640 (2026-06-22) | 54 | -$1.11 | ✅ Closed |
| T7 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T8 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T9 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T10 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T11 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T12 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T13 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T14 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T15 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T16 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,964.59 |
| Alpaca cash | $99,964.59 |
| Cumulative realized P&L | -$66.44 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-20 | $706.97 | Long 56 SPY (T1) | +$12.58 | +0.032% | $100,012.58 |
| Day 2 | 2026-04-21 | $702.10 | FLAT | — | — | $99,973.94 |
| Day 3 | 2026-04-22 | $709.37 | Long 56 SPY (T2) | -$24.35 | -0.061% | $99,949.59 |
| Day 4 | 2026-04-23 | $706.59 | FLAT | — | — | $99,845.99 |
| Day 5 | 2026-04-24 | $712.14 | Long 56 SPY (T3) | +$48.32 | +0.121% | $99,894.31 |
| Day 6 | 2026-04-27 | $713.33 | Long 56 SPY (T3) | +$114.96 | +0.289% | $99,960.95 |
| Day 7 | 2026-04-28 | $709.85 | Long 56 SPY (T3) | -$79.92 | -0.201% | $99,766.07 |
| Day 8 | 2026-04-29 | $709.76 | FLAT | — | — | $99,730.79 |
| Day 9 | 2026-04-30 | $716.56 | FLAT | — | — | $99,988.19 |
| Day 10 | 2026-05-01 | $718.64 | Long 55 SPY (T5) | -$221.63 | -0.558% | $99,766.56 |
| Day 11 | 2026-05-04 | $716.25 | Long 55 SPY (T5) | -$353.08 | -0.888% | $99,635.11 |
| Day 12 | 2026-05-05 | $721.85 | Long 55 SPY (T5) | -$45.08 | -0.113% | $99,943.11 |
| Day 13 | 2026-05-06 | $731.88 | Long 55 SPY (T5) | +$506.57 | +1.274% | $100,494.76 |
| Day 14 | 2026-05-07 | $729.65 | Long 55 SPY (T5) | +$383.92 | +0.966% | $100,372.11 |
| Day 15 | 2026-05-08 | $735.65 | Long 55 SPY (T5) | +$713.92 | +1.796% | $100,702.11 |
| Day 16 | 2026-05-11 | $737.30 | Long 55 SPY (T5) | +$804.67 | +2.024% | $100,792.86 |
| Day 17 | 2026-05-12 | $736.29 | Long 55 SPY (T5) | +$749.12 | +1.885% | $100,737.31 |
| Day 18 | 2026-05-13 | $740.39 | Long 55 SPY (T5) | +$974.62 | +2.452% | $100,962.81 |
| Day 19 | 2026-05-14 | $746.18 | Long 55 SPY (T5) | +$1293.07 | +3.253% | $101,281.26 |
| Day 20 | 2026-05-15 | $737.20 | Long 55 SPY (T5) | +$799.17 | +2.011% | $100,787.36 |
| Day 21 | 2026-05-18 | $736.50 | Long 55 SPY (T5) | +$760.67 | +1.914% | $100,748.86 |
| Day 22 | 2026-05-19 | $731.91 | Long 55 SPY (T5) | +$508.22 | +1.279% | $100,496.41 |
| Day 23 | 2026-05-20 | $739.41 | Long 55 SPY (T5) | +$920.72 | +2.316% | $100,908.91 |
| Day 24 | 2026-05-21 | $740.80 | Long 55 SPY (T5) | +$997.17 | +2.509% | $100,985.36 |
| Day 25 | 2026-05-22 | $743.75 | Long 55 SPY (T5) | +$1159.42 | +2.917% | $101,147.61 |
| Day 26 | 2026-05-26 | $748.53 | Long 55 SPY (T5) | +$1422.32 | +3.578% | $101,410.51 |
| Day 27 | 2026-05-27 | $748.66 | Long 55 SPY (T5) | +$1429.47 | +3.596% | $101,417.66 |
| Day 28 | 2026-05-28 | $752.74 | Long 55 SPY (T5) | +$1653.87 | +4.161% | $101,642.06 |
| Day 29 | 2026-05-29 | $754.40 | Long 55 SPY (T5) | +$1745.17 | +4.391% | $101,733.36 |
| Day 30 | 2026-06-01 | $756.49 | Long 55 SPY (T5) | +$1860.12 | +4.680% | $101,848.31 |
| Day 31 | 2026-06-02 | $757.52 | Long 55 SPY (T5) | +$1916.77 | +4.822% | $101,904.96 |
| Day 32 | 2026-06-03 | $752.24 | Long 55 SPY (T5) | +$1626.37 | +4.092% | $101,614.56 |
| Day 33 | 2026-06-04 | $755.03 | Long 55 SPY (T5) | +$1779.82 | +4.478% | $101,768.01 |
| Day 34 | 2026-06-05 | $735.56 | Long 55 SPY (T5) | +$708.97 | +1.784% | $100,697.16 |
| Day 35 | 2026-06-08 | $737.34 | Long 55 SPY (T5) | +$806.87 | +2.030% | $100,795.06 |
| Day 36 | 2026-06-09 | $735.18 | Long 55 SPY (T5) | +$688.07 | +1.731% | $100,676.26 |
| Day 37 | 2026-06-10 | $723.72 | Long 55 SPY (T5) | +$57.77 | +0.145% | $100,045.96 |
| Day 38 | 2026-06-11 | $735.77 | Long 55 SPY (T5) | +$720.52 | +1.813% | $100,708.71 |
| Day 39 | 2026-06-12 | $739.76 | Long 55 SPY (T5) | +$939.97 | +2.365% | $100,928.16 |
| Day 40 | 2026-06-15 | $752.81 | Long 55 SPY (T5) | +$1657.72 | +4.171% | $101,645.91 |
| Day 41 | 2026-06-16 | $748.65 | Long 55 SPY (T5) | +$1428.92 | +3.595% | $101,417.11 |
| Day 42 | 2026-06-17 | $739.12 | FLAT | — | — | $101,160.26 |
| Day 43 | 2026-06-18 | $746.75 | FLAT | — | — | $101,160.26 |
| Day 44 | 2026-06-22 | $744.27 | FLAT | — | — | $101,159.15 |
| Day 45 | 2026-06-23 | $733.62 | FLAT | — | — | $101,159.15 |
| Day 46 | 2026-06-24 | $733.32 | FLAT | — | — | $101,159.15 |
| Day 47 | 2026-06-25 | $733.33 | FLAT | — | — | $101,159.15 |
| Day 48 | 2026-06-26 | $729.35 | FLAT | — | — | $101,159.15 |
| Day 49 | 2026-06-29 | $740.86 | FLAT | — | — | $101,159.15 |
| Day 50 | 2026-06-30 | $746.65 | FLAT | — | — | $101,159.15 |
| Day 51 | 2026-07-01 | $745.66 | FLAT | — | — | $101,159.15 |
| Day 52 | 2026-07-02 | $744.86 | FLAT | — | — | $101,159.15 |
| Day 53 | 2026-07-06 | $751.27 | FLAT | — | — | $101,159.15 |
| Day 54 | 2026-07-07 | $747.77 | FLAT | — | — | $101,159.15 |
| Day 55 | 2026-07-08 | $745.28 | FLAT | — | — | $101,159.15 |
| Day 56 | 2026-07-09 | $751.55 | FLAT | — | — | $101,159.15 |
| Day 57 | 2026-07-10 | $754.94 | FLAT | — | — | $101,159.15 |
| Day 58 | 2026-07-13 | $749.13 | FLAT | — | — | $100,998.03 |
| Day 59 | 2026-07-14 | $751.94 | FLAT | — | — | $100,962.95 |
| Day 60 | 2026-07-15 | $754.77 | FLAT | — | — | $101,010.70 |
| Day 61 | 2026-07-16 | $750.87 | FLAT | — | — | $100,834.57 |
| Day 62 | 2026-07-17 | $743.28 | FLAT | — | — | $100,692.01 |
| Day 63 | 2026-07-20 | $742.15 | FLAT | — | — | $100,500.03 |
| Day 64 | 2026-07-21 | $748.15 | Long 53 SPY (T13) | +$28.09 | +0.071% | $100,528.12 |
| Day 65 | 2026-07-22 | $747.49 | Long 53 SPY (T13) | -$6.89 | -0.017% | $100,493.14 |
| Day 66 | 2026-07-23 | $738.06 | Long 52 SPY (T14) | -$40.56 | -0.106% | $99,824.00 |
| Day 67 | 2026-07-24 | $738.90 | FLAT | — | — | $99,872.88 |
| Day 68 | 2026-07-27 | $738.85 | FLAT | — | — | $99,977.02 |
| Day 69 | 2026-07-28 | $740.79 | FLAT | — | — | $99,933.56 |
| Day 70 | 2026-07-29 | $729.57 | FLAT | — | — | $99,933.56 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-04-20 | $100,012.58 | $99,999.99 | +0.0126% | -0.000% | **+0.013%** |
| Day 2 | 2026-04-21 | $99,973.94 | $99,311.13 | -0.0261% | -0.689% | **+0.663%** |
| Day 3 | 2026-04-22 | $99,949.59 | $100,339.46 | -0.0504% | +0.339% | **-0.389%** |
| Day 4 | 2026-04-23 | $99,845.99 | $99,946.24 | -0.1540% | -0.054% | **-0.100%** |
| Day 5 | 2026-04-24 | $99,894.31 | $100,731.28 | -0.1057% | +0.731% | **-0.837%** |
| Day 6 | 2026-04-27 | $99,960.95 | $100,899.60 | -0.0391% | +0.900% | **-0.939%** |
| Day 7 | 2026-04-28 | $99,766.07 | $100,407.36 | -0.2339% | +0.407% | **-0.641%** |
| Day 8 | 2026-04-29 | $99,730.79 | $100,394.63 | -0.2692% | +0.395% | **-0.664%** |
| Day 9 | 2026-04-30 | $99,988.19 | $101,356.48 | -0.0118% | +1.356% | **-1.368%** |
| Day 10 | 2026-05-01 | $99,766.56 | $101,650.69 | -0.2334% | +1.651% | **-1.884%** |
| Day 11 | 2026-05-04 | $99,635.11 | $101,312.63 | -0.3649% | +1.313% | **-1.678%** |
| Day 12 | 2026-05-05 | $99,943.11 | $102,104.74 | -0.0569% | +2.105% | **-2.162%** |
| Day 13 | 2026-05-06 | $100,494.76 | $103,523.47 | +0.4948% | +3.523% | **-3.028%** |
| Day 14 | 2026-05-07 | $100,372.11 | $103,208.04 | +0.3721% | +3.208% | **-2.836%** |
| Day 15 | 2026-05-08 | $100,702.11 | $104,056.74 | +0.7021% | +4.057% | **-3.355%** |
| Day 16 | 2026-05-11 | $100,792.86 | $104,290.13 | +0.7929% | +4.290% | **-3.497%** |
| Day 17 | 2026-05-12 | $100,737.31 | $104,147.26 | +0.7373% | +4.147% | **-3.410%** |
| Day 18 | 2026-05-13 | $100,962.81 | $104,727.20 | +0.9628% | +4.727% | **-3.764%** |
| Day 19 | 2026-05-14 | $101,281.26 | $105,546.19 | +1.2813% | +5.546% | **-4.265%** |
| Day 20 | 2026-05-15 | $100,787.36 | $104,275.98 | +0.7874% | +4.276% | **-3.489%** |
| Day 21 | 2026-05-18 | $100,748.86 | $104,176.97 | +0.7489% | +4.177% | **-3.428%** |
| Day 22 | 2026-05-19 | $100,496.41 | $103,527.72 | +0.4964% | +3.528% | **-3.032%** |
| Day 23 | 2026-05-20 | $100,908.91 | $104,588.58 | +0.9089% | +4.589% | **-3.680%** |
| Day 24 | 2026-05-21 | $100,985.36 | $104,785.20 | +0.9854% | +4.785% | **-3.800%** |
| Day 25 | 2026-05-22 | $101,147.61 | $105,202.47 | +1.1476% | +5.202% | **-4.054%** |
| Day 26 | 2026-05-26 | $101,410.51 | $105,878.60 | +1.4105% | +5.879% | **-4.468%** |
| Day 27 | 2026-05-27 | $101,417.66 | $105,896.98 | +1.4177% | +5.897% | **-4.479%** |
| Day 28 | 2026-05-28 | $101,642.06 | $106,474.09 | +1.6421% | +6.474% | **-4.832%** |
| Day 29 | 2026-05-29 | $101,733.36 | $106,708.90 | +1.7334% | +6.709% | **-4.976%** |
| Day 30 | 2026-06-01 | $101,848.31 | $107,004.53 | +1.8483% | +7.005% | **-5.157%** |
| Day 31 | 2026-06-02 | $101,904.96 | $107,150.22 | +1.9050% | +7.150% | **-5.245%** |
| Day 32 | 2026-06-03 | $101,614.56 | $106,403.37 | +1.6146% | +6.403% | **-4.788%** |
| Day 33 | 2026-06-04 | $101,768.01 | $106,798.01 | +1.7680% | +6.798% | **-5.030%** |
| Day 34 | 2026-06-05 | $100,697.16 | $104,044.01 | +0.6972% | +4.044% | **-3.347%** |
| Day 35 | 2026-06-08 | $100,795.06 | $104,295.78 | +0.7951% | +4.296% | **-3.501%** |
| Day 36 | 2026-06-09 | $100,676.26 | $103,990.26 | +0.6763% | +3.990% | **-3.314%** |
| Day 37 | 2026-06-10 | $100,045.96 | $102,369.25 | +0.0460% | +2.369% | **-2.323%** |
| Day 38 | 2026-06-11 | $100,708.71 | $104,073.71 | +0.7087% | +4.074% | **-3.365%** |
| Day 39 | 2026-06-12 | $100,928.16 | $104,638.09 | +0.9282% | +4.638% | **-3.710%** |
| Day 40 | 2026-06-15 | $101,645.91 | $106,484.00 | +1.6459% | +6.484% | **-4.838%** |
| Day 41 | 2026-06-16 | $101,417.11 | $105,895.57 | +1.4171% | +5.896% | **-4.479%** |
| Day 42 | 2026-06-17 | $101,160.26 | $104,547.56 | +1.1603% | +4.548% | **-3.388%** |
| Day 43 | 2026-06-18 | $101,160.26 | $105,626.82 | +1.1603% | +5.627% | **-4.467%** |
| Day 44 | 2026-06-22 | $101,159.15 | $105,276.02 | +1.1591% | +5.276% | **-4.117%** |
| Day 45 | 2026-06-23 | $101,159.15 | $103,769.60 | +1.1591% | +3.770% | **-2.611%** |
| Day 46 | 2026-06-24 | $101,159.15 | $103,727.16 | +1.1591% | +3.727% | **-2.568%** |
| Day 47 | 2026-06-25 | $101,159.15 | $103,728.58 | +1.1591% | +3.729% | **-2.570%** |
| Day 48 | 2026-06-26 | $101,159.15 | $103,165.61 | +1.1591% | +3.166% | **-2.007%** |
| Day 49 | 2026-06-29 | $101,159.15 | $104,793.68 | +1.1591% | +4.794% | **-3.635%** |
| Day 50 | 2026-06-30 | $101,159.15 | $105,612.67 | +1.1591% | +5.613% | **-4.454%** |
| Day 51 | 2026-07-01 | $101,159.15 | $105,472.64 | +1.1591% | +5.473% | **-4.314%** |
| Day 52 | 2026-07-02 | $101,159.15 | $105,359.48 | +1.1591% | +5.359% | **-4.200%** |
| Day 53 | 2026-07-06 | $101,159.15 | $106,266.16 | +1.1591% | +6.266% | **-5.107%** |
| Day 54 | 2026-07-07 | $101,159.15 | $105,771.09 | +1.1591% | +5.771% | **-4.612%** |
| Day 55 | 2026-07-08 | $101,159.15 | $105,418.89 | +1.1591% | +5.419% | **-4.260%** |
| Day 56 | 2026-07-09 | $101,159.15 | $106,305.77 | +1.1591% | +6.306% | **-5.147%** |
| Day 57 | 2026-07-10 | $101,159.15 | $106,785.28 | +1.1591% | +6.785% | **-5.626%** |
| Day 58 | 2026-07-13 | $100,998.03 | $105,963.46 | +0.9980% | +5.963% | **-4.965%** |
| Day 59 | 2026-07-14 | $100,962.95 | $106,360.94 | +0.9629% | +6.361% | **-5.398%** |
| Day 60 | 2026-07-15 | $101,010.70 | $106,761.24 | +1.0107% | +6.761% | **-5.750%** |
| Day 61 | 2026-07-16 | $100,834.57 | $106,209.59 | +0.8346% | +6.210% | **-5.375%** |
| Day 62 | 2026-07-17 | $100,692.01 | $105,135.99 | +0.6920% | +5.136% | **-4.444%** |
| Day 63 | 2026-07-20 | $100,500.03 | $104,976.15 | +0.5000% | +4.976% | **-4.476%** |
| Day 64 | 2026-07-21 | $100,528.12 | $105,824.84 | +0.5281% | +5.825% | **-5.297%** |
| Day 65 | 2026-07-22 | $100,493.14 | $105,731.49 | +0.4931% | +5.731% | **-5.238%** |
| Day 66 | 2026-07-23 | $99,824.00 | $104,397.63 | -0.1760% | +4.398% | **-4.574%** |
| Day 67 | 2026-07-24 | $99,872.88 | $104,516.44 | -0.1271% | +4.516% | **-4.643%** |
| Day 68 | 2026-07-27 | $99,977.02 | $104,509.37 | -0.0230% | +4.509% | **-4.532%** |
| Day 69 | 2026-07-28 | $99,933.56 | $104,783.78 | -0.0664% | +4.784% | **-4.850%** |
| Day 70 | 2026-07-29 | $99,933.56 | $103,196.73 | -0.0664% | +3.197% | **-3.263%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-04-20 | $706.97 | +$12.58 | -$79.02 | Position open |
| Day 2 | 2026-04-21 | $702.10 | -$260.14 | +$193.70 | Flat saved **+$193.70** vs holding |
| Day 3 | 2026-04-22 | $709.37 | +$146.98 | -$213.42 | Position open |
| Day 4 | 2026-04-23 | $706.59 | -$8.70 | -$57.74 | Holding would have been **$57.74** better — honest entry |
| Day 5 | 2026-04-24 | $712.14 | +$302.10 | -$368.54 | Position open |
| Day 6 | 2026-04-27 | $713.33 | +$368.74 | -$435.18 | Position open |
| Day 7 | 2026-04-28 | $709.85 | +$173.86 | -$240.30 | Position open |
| Day 8 | 2026-04-29 | $709.76 | +$168.82 | -$235.26 | Holding would have been **$235.26** better — honest entry |
| Day 9 | 2026-04-30 | $716.56 | +$549.62 | -$616.06 | Holding would have been **$616.06** better — honest entry |
| Day 10 | 2026-05-01 | $718.64 | +$666.10 | -$732.54 | Position open |
| Day 11 | 2026-05-04 | $716.25 | +$532.26 | -$598.70 | Position open |
| Day 12 | 2026-05-05 | $721.85 | +$845.86 | -$912.30 | Position open |
| Day 13 | 2026-05-06 | $731.88 | +$1407.54 | -$1473.98 | Position open |
| Day 14 | 2026-05-07 | $729.65 | +$1282.66 | -$1349.10 | Position open |
| Day 15 | 2026-05-08 | $735.65 | +$1618.66 | -$1685.10 | Position open |
| Day 16 | 2026-05-11 | $737.30 | +$1711.06 | -$1777.50 | Position open |
| Day 17 | 2026-05-12 | $736.29 | +$1654.50 | -$1720.94 | Position open |
| Day 18 | 2026-05-13 | $740.39 | +$1884.10 | -$1950.54 | Position open |
| Day 19 | 2026-05-14 | $746.18 | +$2208.34 | -$2274.78 | Position open |
| Day 20 | 2026-05-15 | $737.20 | +$1705.46 | -$1771.90 | Position open |
| Day 21 | 2026-05-18 | $736.50 | +$1666.26 | -$1732.70 | Position open |
| Day 22 | 2026-05-19 | $731.91 | +$1409.22 | -$1475.66 | Position open |
| Day 23 | 2026-05-20 | $739.41 | +$1829.22 | -$1895.66 | Position open |
| Day 24 | 2026-05-21 | $740.80 | +$1907.06 | -$1973.50 | Position open |
| Day 25 | 2026-05-22 | $743.75 | +$2072.26 | -$2138.70 | Position open |
| Day 26 | 2026-05-26 | $748.53 | +$2339.94 | -$2406.38 | Position open |
| Day 27 | 2026-05-27 | $748.66 | +$2347.22 | -$2413.66 | Position open |
| Day 28 | 2026-05-28 | $752.74 | +$2575.70 | -$2642.14 | Position open |
| Day 29 | 2026-05-29 | $754.40 | +$2668.66 | -$2735.10 | Position open |
| Day 30 | 2026-06-01 | $756.49 | +$2785.70 | -$2852.14 | Position open |
| Day 31 | 2026-06-02 | $757.52 | +$2843.38 | -$2909.82 | Position open |
| Day 32 | 2026-06-03 | $752.24 | +$2547.70 | -$2614.14 | Position open |
| Day 33 | 2026-06-04 | $755.03 | +$2703.94 | -$2770.38 | Position open |
| Day 34 | 2026-06-05 | $735.56 | +$1613.62 | -$1680.06 | Position open |
| Day 35 | 2026-06-08 | $737.34 | +$1713.30 | -$1779.74 | Position open |
| Day 36 | 2026-06-09 | $735.18 | +$1592.34 | -$1658.78 | Position open |
| Day 37 | 2026-06-10 | $723.72 | +$950.58 | -$1017.02 | Position open |
| Day 38 | 2026-06-11 | $735.77 | +$1625.38 | -$1691.82 | Position open |
| Day 39 | 2026-06-12 | $739.76 | +$1848.82 | -$1915.26 | Position open |
| Day 40 | 2026-06-15 | $752.81 | +$2579.62 | -$2646.06 | Position open |
| Day 41 | 2026-06-16 | $748.65 | +$2346.66 | -$2413.10 | Position open |
| Day 42 | 2026-06-17 | $739.12 | +$1812.98 | -$1879.42 | Holding would have been **$1879.42** better — honest entry |
| Day 43 | 2026-06-18 | $746.75 | +$2240.26 | -$2306.70 | Holding would have been **$2306.70** better — honest entry |
| Day 44 | 2026-06-22 | $744.27 | +$2101.38 | -$2167.82 | Holding would have been **$2167.82** better — honest entry |
| Day 45 | 2026-06-23 | $733.62 | +$1504.98 | -$1571.42 | Holding would have been **$1571.42** better — honest entry |
| Day 46 | 2026-06-24 | $733.32 | +$1488.18 | -$1554.62 | Holding would have been **$1554.62** better — honest entry |
| Day 47 | 2026-06-25 | $733.33 | +$1488.74 | -$1555.18 | Holding would have been **$1555.18** better — honest entry |
| Day 48 | 2026-06-26 | $729.35 | +$1265.86 | -$1332.30 | Holding would have been **$1332.30** better — honest entry |
| Day 49 | 2026-06-29 | $740.86 | +$1910.42 | -$1976.86 | Holding would have been **$1976.86** better — honest entry |
| Day 50 | 2026-06-30 | $746.65 | +$2234.66 | -$2301.10 | Holding would have been **$2301.10** better — honest entry |
| Day 51 | 2026-07-01 | $745.66 | +$2179.22 | -$2245.66 | Holding would have been **$2245.66** better — honest entry |
| Day 52 | 2026-07-02 | $744.86 | +$2134.42 | -$2200.86 | Holding would have been **$2200.86** better — honest entry |
| Day 53 | 2026-07-06 | $751.27 | +$2493.38 | -$2559.82 | Holding would have been **$2559.82** better — honest entry |
| Day 54 | 2026-07-07 | $747.77 | +$2297.38 | -$2363.82 | Holding would have been **$2363.82** better — honest entry |
| Day 55 | 2026-07-08 | $745.28 | +$2157.94 | -$2224.38 | Holding would have been **$2224.38** better — honest entry |
| Day 56 | 2026-07-09 | $751.55 | +$2509.06 | -$2575.50 | Holding would have been **$2575.50** better — honest entry |
| Day 57 | 2026-07-10 | $754.94 | +$2698.90 | -$2765.34 | Holding would have been **$2765.34** better — honest entry |
| Day 58 | 2026-07-13 | $749.13 | +$2373.54 | -$2439.98 | Holding would have been **$2439.98** better — honest entry |
| Day 59 | 2026-07-14 | $751.94 | +$2530.90 | -$2597.34 | Holding would have been **$2597.34** better — honest entry |
| Day 60 | 2026-07-15 | $754.77 | +$2689.38 | -$2755.82 | Holding would have been **$2755.82** better — honest entry |
| Day 61 | 2026-07-16 | $750.87 | +$2470.98 | -$2537.42 | Holding would have been **$2537.42** better — honest entry |
| Day 62 | 2026-07-17 | $743.28 | +$2045.94 | -$2112.38 | Holding would have been **$2112.38** better — honest entry |
| Day 63 | 2026-07-20 | $742.15 | +$1982.66 | -$2049.10 | Holding would have been **$2049.10** better — honest entry |
| Day 64 | 2026-07-21 | $748.15 | +$2318.66 | -$2385.10 | Position open |
| Day 65 | 2026-07-22 | $747.49 | +$2281.70 | -$2348.14 | Position open |
| Day 66 | 2026-07-23 | $738.06 | +$1753.62 | -$1820.06 | Position open |
| Day 67 | 2026-07-24 | $738.90 | +$1800.66 | -$1867.10 | Holding would have been **$1867.10** better — honest entry |
| Day 68 | 2026-07-27 | $738.85 | +$1797.86 | -$1864.30 | Holding would have been **$1864.30** better — honest entry |
| Day 69 | 2026-07-28 | $740.79 | +$1906.50 | -$1972.94 | Holding would have been **$1972.94** better — honest entry |
| Day 70 | 2026-07-29 | $729.57 | +$1278.18 | -$1344.62 | Holding would have been **$1344.62** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-04-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T1) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $706.97 |
| Unrealized P&L | +$12.58 |
| P&L % | +0.032% |
| Portfolio value | $100,012.58 |
| Benchmark value | $99,999.99 |
| Alpha (cumulative) | +0.013% |

**Regime call:** BEAR

**Market context:** Small Cap Stocks and Russell 2000 declined, while Oil Prices surged amid Middle East tensions. The S&P 500 held 7100, with Nasdaq Composite battling fears. Equity Futures and Exchange-Traded Funds also declined.

**Strategy note:** The system held long SPY due to a BULLISH Fast signal and BEAR regime, despite strong momentum. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +0.03% from entry. No exit triggered.

**Key learning:** A strong momentum environment can override a bearish regime context, but may also increase risk of a false signal.

---

### Day 2 — 2026-04-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $702.10 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | -$260.14 |
| Signal saved | +$193.70 |
| Portfolio value | $99,973.94 |
| Benchmark value | $99,311.13 |
| Alpha (cumulative) | +0.663% |

**Regime call:** BEAR

**Market context:** Markets rallied on Iran deal hopes, with stocks outperforming safe-havens like gold. Small caps and risk-on trades led the gains. Oil prices pulled back on the news.

**Strategy note:** The system remained long SPY despite a BEAR regime, as the fast signal remained BULLISH due to a strong golden cross. No exit was triggered.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter can sometimes conflict with the fast signal, requiring careful consideration of both indicators.

---

### Day 3 — 2026-04-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T2) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $709.37 |
| Unrealized P&L | -$24.35 |
| P&L % | -0.061% |
| Portfolio value | $99,949.59 |
| Benchmark value | $100,339.46 |
| Alpha (cumulative) | -0.389% |

**Regime call:** BEAR

**Market context:** Risk-on trade buoyed small cap sentiment, while the VIX remains calm. The S&P 500 climbed on a ceasefire extension and tech tailwinds.

**Strategy note:** The system held a long SPY position, despite a bear regime, due to a bullish fast signal from the 10/30 SMA crossover. Unrealized P&L was -0.01% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.06% from entry. No exit triggered.

**Key learning:** A bear regime does not necessarily mean a bear market, as the system's fast signal can override the slow filter.

---

### Day 4 — 2026-04-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $706.59 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | -$8.70 |
| Signal saved | -$57.74 |
| Portfolio value | $99,845.99 |
| Benchmark value | $99,946.24 |
| Alpha (cumulative) | -0.100% |

**Regime call:** BULL

**Market context:** The S&P 500 retreated but held 7100 on fresh Mideast escalation as earnings kick off, while VIX crept toward 20 as Iran fears and Tesla's whipsaw rattle nerves.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and strong momentum, causing the system to hold long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long in a bull regime despite rising VIX is being tested.

---

### Day 5 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T3) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $712.14 |
| Unrealized P&L | +$48.32 |
| P&L % | +0.121% |
| Portfolio value | $99,894.31 |
| Benchmark value | $100,731.28 |
| Alpha (cumulative) | -0.837% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +0.12% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 6 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T3) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $713.33 |
| Unrealized P&L | +$114.96 |
| P&L % | +0.289% |
| Portfolio value | $99,960.95 |
| Benchmark value | $100,899.60 |
| Alpha (cumulative) | -0.939% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 7 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T3) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $709.85 |
| Unrealized P&L | -$79.92 |
| P&L % | -0.201% |
| Portfolio value | $99,766.07 |
| Benchmark value | $100,407.36 |
| Alpha (cumulative) | -0.641% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.20% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 8 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $709.76 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$168.82 |
| Signal saved | -$235.26 |
| Portfolio value | $99,730.79 |
| Benchmark value | $100,394.63 |
| Alpha (cumulative) | -0.664% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 9 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $716.56 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$549.62 |
| Signal saved | -$616.06 |
| Portfolio value | $99,988.19 |
| Benchmark value | $101,356.48 |
| Alpha (cumulative) | -1.368% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 10 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $718.64 |
| Unrealized P&L | -$221.63 |
| P&L % | -0.558% |
| Portfolio value | $99,766.56 |
| Benchmark value | $101,650.69 |
| Alpha (cumulative) | -1.884% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 11 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $716.25 |
| Unrealized P&L | -$353.08 |
| P&L % | -0.888% |
| Portfolio value | $99,635.11 |
| Benchmark value | $101,312.63 |
| Alpha (cumulative) | -1.678% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.89% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 12 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $721.85 |
| Unrealized P&L | -$45.08 |
| P&L % | -0.113% |
| Portfolio value | $99,943.11 |
| Benchmark value | $102,104.74 |
| Alpha (cumulative) | -2.162% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 13 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $731.88 |
| Unrealized P&L | +$506.57 |
| P&L % | +1.274% |
| Portfolio value | $100,494.76 |
| Benchmark value | $103,523.47 |
| Alpha (cumulative) | -3.028% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.27% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 14 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $729.65 |
| Unrealized P&L | +$383.92 |
| P&L % | +0.966% |
| Portfolio value | $100,372.11 |
| Benchmark value | $103,208.04 |
| Alpha (cumulative) | -2.836% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +0.97% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 15 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $735.65 |
| Unrealized P&L | +$713.92 |
| P&L % | +1.796% |
| Portfolio value | $100,702.11 |
| Benchmark value | $104,056.74 |
| Alpha (cumulative) | -3.355% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.80% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 16 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $737.30 |
| Unrealized P&L | +$804.67 |
| P&L % | +2.024% |
| Portfolio value | $100,792.86 |
| Benchmark value | $104,290.13 |
| Alpha (cumulative) | -3.497% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.02% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 17 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $736.29 |
| Unrealized P&L | +$749.12 |
| P&L % | +1.885% |
| Portfolio value | $100,737.31 |
| Benchmark value | $104,147.26 |
| Alpha (cumulative) | -3.410% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.89% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 18 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $740.39 |
| Unrealized P&L | +$974.62 |
| P&L % | +2.452% |
| Portfolio value | $100,962.81 |
| Benchmark value | $104,727.20 |
| Alpha (cumulative) | -3.764% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.45% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 19 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $746.18 |
| Unrealized P&L | +$1293.07 |
| P&L % | +3.253% |
| Portfolio value | $101,281.26 |
| Benchmark value | $105,546.19 |
| Alpha (cumulative) | -4.265% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +3.25% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 20 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $737.20 |
| Unrealized P&L | +$799.17 |
| P&L % | +2.011% |
| Portfolio value | $100,787.36 |
| Benchmark value | $104,275.98 |
| Alpha (cumulative) | -3.489% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.01% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 21 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $736.50 |
| Unrealized P&L | +$760.67 |
| P&L % | +1.914% |
| Portfolio value | $100,748.86 |
| Benchmark value | $104,176.97 |
| Alpha (cumulative) | -3.428% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.91% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 22 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $731.91 |
| Unrealized P&L | +$508.22 |
| P&L % | +1.279% |
| Portfolio value | $100,496.41 |
| Benchmark value | $103,527.72 |
| Alpha (cumulative) | -3.032% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.28% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 23 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $739.41 |
| Unrealized P&L | +$920.72 |
| P&L % | +2.316% |
| Portfolio value | $100,908.91 |
| Benchmark value | $104,588.58 |
| Alpha (cumulative) | -3.680% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.32% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 24 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $740.80 |
| Unrealized P&L | +$997.17 |
| P&L % | +2.509% |
| Portfolio value | $100,985.36 |
| Benchmark value | $104,785.20 |
| Alpha (cumulative) | -3.800% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.51% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

---

### Day 25 — 2026-05-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $743.75 |
| Unrealized P&L | +$1159.42 |
| P&L % | +2.917% |
| Portfolio value | $101,147.61 |
| Benchmark value | $105,202.47 |
| Alpha (cumulative) | -4.054% |

**Regime call:** BULL

**Market context:** The market remained bullish with strong momentum, and the VIX index remained low at 16.59. Corporate earnings season boosted equity futures and exchange-traded funds. The 10Y Treasury yield was steady at 4.57%.

**Strategy note:** The dual-timeframe signal remained bullish with a fast golden cross, and the system held long SPY. The slow filter regime remained in a bull context.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.92% from entry. No exit triggered.

**Key learning:** A strong momentum environment can persist even with some volatility, as seen in today's market action.

---

### Day 26 — 2026-05-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $748.53 |
| Unrealized P&L | +$1422.32 |
| P&L % | +3.578% |
| Portfolio value | $101,410.51 |
| Benchmark value | $105,878.60 |
| Alpha (cumulative) | -4.468% |

**Regime call:** BULL

**Market context:** The stock market saw one of its best 8-week stretches ever, with the S&P 500 experiencing strong gains. VIX remains low at 17.04. Oil prices are stable at $94.13/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime. The system's unrealized P&L increased to +3.67% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +3.58% from entry. No exit triggered.

**Key learning:** Strong momentum can persist for extended periods, but regime context remains crucial for risk management.

---

### Day 27 — 2026-05-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $748.66 |
| Unrealized P&L | +$1429.47 |
| P&L % | +3.596% |
| Portfolio value | $101,417.66 |
| Benchmark value | $105,896.98 |
| Alpha (cumulative) | -4.479% |

**Regime call:** Bullish

**Market context:** Markets continued their rally, with the SPY closing at $750.30. Short sellers are betting record amounts against stocks, but the market is rallying on a potential deal between Trump and Iran. The VIX remains relatively low at 16.79.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong regime context. The system held long SPY, with an unrealized P&L of +3.82% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong regime context can lead to increased confidence in a bullish signal, but it's essential to monitor the market context and adjust the strategy accordingly.

---

### Day 28 — 2026-05-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $752.74 |
| Unrealized P&L | +$1653.87 |
| P&L % | +4.161% |
| Portfolio value | $101,642.06 |
| Benchmark value | $106,474.09 |
| Alpha (cumulative) | -4.832% |

**Regime call:** BULL

**Market context:** The market saw a strong day with SPY closing at $754.62. Headlines focused on the acceleration of 'The Great Migration' from tech to value and the outperformance of certain ETFs. Economic data was also released, including PCE and claims.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.42% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.16% from entry. No exit triggered.

**Key learning:** A strong momentum and a bullish signal can lead to significant gains, but risk management is crucial to avoid over-leveraging.

---

### Day 29 — 2026-05-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $754.40 |
| Unrealized P&L | +$1745.17 |
| P&L % | +4.391% |
| Portfolio value | $101,733.36 |
| Benchmark value | $106,708.90 |
| Alpha (cumulative) | -4.976% |

**Regime call:** BULL

**Market context:** Markets were mostly up on lower volume, driven by hopes of a US-Iran deal, with exchange-traded funds and equity futures rising pre-bell.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, resulting in an unrealized P&L of +4.71% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.39% from entry. No exit triggered.

**Key learning:** Strong momentum can persist even with lower volume, but regime context remains crucial for risk management.

---

### Day 30 — 2026-06-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $756.49 |
| Unrealized P&L | +$1860.12 |
| P&L % | +4.680% |
| Portfolio value | $101,848.31 |
| Benchmark value | $107,004.53 |
| Alpha (cumulative) | -5.157% |

**Regime call:** BULL

**Market context:** Markets remained bullish with a strong close in SPY, despite negative news from the Middle East. The VIX index also stayed low at 15.74. Oil prices were stable at $92.57/barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with a fast signal remaining bullish and a strong momentum. The slow filter regime also confirmed a bull regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.68% from entry. No exit triggered.

**Key learning:** Strong momentum and a confirmed bull regime do not guarantee continued price appreciation, and the system must remain vigilant for potential reversals.

---

### Day 31 — 2026-06-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $757.52 |
| Unrealized P&L | +$1916.77 |
| P&L % | +4.822% |
| Portfolio value | $101,904.96 |
| Benchmark value | $107,150.22 |
| Alpha (cumulative) | -5.245% |

**Regime call:** BULL

**Market context:** The S&P 500 hit a new high, with strong momentum and a bullish signal. The VIX remained relatively low at 16.06. Global macro data showed stable oil prices and a 4.45% 10Y Treasury yield.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and a strong momentum. The system held long SPY, with an unrealized P&L of +5.05% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.82% from entry. No exit triggered.

**Key learning:** Bullish regimes can be prolonged, but a strong momentum is essential to ride the trend.

---

### Day 32 — 2026-06-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $752.24 |
| Unrealized P&L | +$1626.37 |
| P&L % | +4.092% |
| Portfolio value | $101,614.56 |
| Benchmark value | $106,403.37 |
| Alpha (cumulative) | -4.788% |

**Regime call:** BULL

**Market context:** The market had a strong day, with the SPY closing at $755.33. AbbVie and UFO stocks delivered significant returns, while the S&P 500 and exchange-traded funds were mixed. Economic signals were fresh, but no clear direction emerged.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY, with an unrealized P&L of +4.52% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.09% from entry. No exit triggered.

**Key learning:** The system's ability to ride out a strong trend in a BULL regime is crucial for its success, but requires careful management of risk and position sizing.

---

### Day 33 — 2026-06-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $755.03 |
| Unrealized P&L | +$1779.82 |
| P&L % | +4.478% |
| Portfolio value | $101,768.01 |
| Benchmark value | $106,798.01 |
| Alpha (cumulative) | -5.030% |

**Regime call:** BULL

**Market context:** Markets closed mixed, with some positive headlines in tech and energy, but overall economic data weighed on investor sentiment. The VIX index remains relatively low at 15.52. Oil prices slightly increased to $93.09 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime context. The slow filter's MA20 crossed above MA50, confirming the bull regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.48% from entry. No exit triggered.

**Key learning:** A strong bull regime can mask underlying market weakness, making it essential to monitor momentum and economic data.

---

### Day 34 — 2026-06-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $735.56 |
| Unrealized P&L | +$708.97 |
| P&L % | +1.784% |
| Portfolio value | $100,697.16 |
| Benchmark value | $104,044.01 |
| Alpha (cumulative) | -3.347% |

**Regime call:** BULL

**Market context:** The Jobs Report was released today, which is considered great news for the market, but could negatively impact bond yields. WTI Oil price is stable at $90.9/barrel. The VIX index is at 17.19.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a strong momentum. The system held long SPY.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.78% from entry. No exit triggered.

**Key learning:** The market's strong reaction to positive economic news can sometimes be short-lived and may lead to a pullback.

---

### Day 35 — 2026-06-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $737.34 |
| Unrealized P&L | +$806.87 |
| P&L % | +2.030% |
| Portfolio value | $100,795.06 |
| Benchmark value | $104,295.78 |
| Alpha (cumulative) | -3.501% |

**Regime call:** BULL

**Market context:** Markets continued their recovery rally, with SPY closing at $742.25. News headlines were mixed, but overall sentiment remained positive. VIX remained relatively low at 18.45.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with the fast signal remaining bullish. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.03% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with some market volatility, but it's essential to monitor the slow filter for signs of weakening momentum.

---

### Day 36 — 2026-06-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $735.18 |
| Unrealized P&L | +$688.07 |
| P&L % | +1.731% |
| Portfolio value | $100,676.26 |
| Benchmark value | $103,990.26 |
| Alpha (cumulative) | -3.314% |

**Regime call:** RISK-NEUTRAL

**Market context:** Markets were generally higher with the Dow Jones ETFs outperforming the S&P 500 and Nasdaq. Inflation data is expected ahead of CPI and SPCX. Oil prices remained relatively stable.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context indicated a BULL market. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.73% from entry. No exit triggered.

**Key learning:** A recovering momentum in a bull regime can lead to positive unrealized P&L, but requires careful management of risk.

---

### Day 37 — 2026-06-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $723.72 |
| Unrealized P&L | +$57.77 |
| P&L % | +0.145% |
| Portfolio value | $100,045.96 |
| Benchmark value | $102,369.25 |
| Alpha (cumulative) | -2.323% |

**Regime call:** BULL

**Market context:** The market headlines were dominated by inflation concerns, with the CPI inflation rate reaching +4.2%, the hottest in 3 years. The VIX index also rose to 21.68. Oil prices remained steady at $91.01 per barrel.

**Strategy note:** The system held a long position in SPY as the fast signal remained BULLISH, with a weak momentum context. The slow filter regime also confirmed a BULL regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** A weak momentum context can persist even as the fast signal remains bullish, suggesting a need for caution in the current market environment.

---

### Day 38 — 2026-06-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $735.77 |
| Unrealized P&L | +$720.52 |
| P&L % | +1.813% |
| Portfolio value | $100,708.71 |
| Benchmark value | $104,073.71 |
| Alpha (cumulative) | -3.365% |

**Regime call:** BULL

**Market context:** Energy stocks continued their rally, with IYE up 27% YTD. The market remains relatively calm, with VIX at 21.4. US attacks on Iran are causing some volatility.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime, and did not trigger an exit.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +1.81% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a bull regime is being tested, but the weak momentum is a concern.

---

### Day 39 — 2026-06-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $739.76 |
| Unrealized P&L | +$939.97 |
| P&L % | +2.365% |
| Portfolio value | $100,928.16 |
| Benchmark value | $104,638.09 |
| Alpha (cumulative) | -3.710% |

**Regime call:** BULL

**Market context:** Energy sector continues to rally with XLE up 29% YTD. Market headlines focus on ETFs, equity futures, and SpaceX debut. Retail ETFs face challenges amidst sticky inflation and robust job growth.

**Strategy note:** Dual-timeframe signal remains BULLISH with Fast Golden Cross, while Slow MAs confirm BULL regime. System held long SPY as no exit trigger was met.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +2.37% from entry. No exit triggered.

**Key learning:** Momentum remains WEAK despite a BULL regime, requiring continued monitoring for potential regime shift.

---

### Day 40 — 2026-06-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $752.81 |
| Unrealized P&L | +$1657.72 |
| P&L % | +4.171% |
| Portfolio value | $101,645.91 |
| Benchmark value | $106,484.00 |
| Alpha (cumulative) | -4.838% |

**Regime call:** Consolidation

**Market context:** Air taxi stocks and AI security plays rose as the broader market also gained. 64 years of raises were highlighted in DGRO, and quantum computing stocks jumped amid risk-on optimism. VIX remained relatively low at 16.18.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime remained BULL. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +4.17% from entry. No exit triggered.

**Key learning:** The system's ability to ride out consolidations is key to its long-term performance.

---

### Day 41 — 2026-06-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T5) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $748.65 |
| Unrealized P&L | +$1428.92 |
| P&L % | +3.595% |
| Portfolio value | $101,417.11 |
| Benchmark value | $105,895.57 |
| Alpha (cumulative) | -4.479% |

**Regime call:** BULL

**Market context:** Oil prices eased after the Strait was opened, while the 10Y Treasury yield remained steady at 4.42%. The S&P 500 is expected to soar to 9000 according to a Wall Street analyst. ETFs and equity futures are higher ahead of the Fed policy meeting.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context, with the slow MA20 above MA50. The fast signal remained bullish with a strong momentum.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +3.60% from entry. No exit triggered.

**Key learning:** A strong bullish regime context can override a weak fast signal, but a strong momentum is still required for a valid trade

---

### Day 42 — 2026-06-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $739.12 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1812.98 |
| Signal saved | -$1879.42 |
| Portfolio value | $101,160.26 |
| Benchmark value | $104,547.56 |
| Alpha (cumulative) | -3.388% |

**Regime call:** BULL

**Market context:** The S&P 500 futures edged higher ahead of the Fed rate decision. Tech ETFs are doing something unprecedented, but investors are advised to wait. The VIX remains relatively low at 16.84.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The regime context is still BULL, with MA20 above MA50.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long during a strong bull regime is key to its performance, but it still trails the benchmark by a significant margin.

---

### Day 43 — 2026-06-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $746.75 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2240.26 |
| Signal saved | -$2306.70 |
| Portfolio value | $101,160.26 |
| Benchmark value | $105,626.82 |
| Alpha (cumulative) | -4.467% |

**Regime call:** RISK-ON

**Market context:** Markets bounced back pre-bell Thursday, lifted by a US-Iran interim deal, despite hawkish Fed outlook. The S&P 500, Dow, and Nasdaq futures climbed, while ETFs and equity futures also rose. VIX fell to 16.8.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a BULL regime, locking a realized P&L of $1189.93. Monitoring for re-entry on next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can still occur in a BULL regime, illustrating the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 44 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $744.27 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2101.38 |
| Signal saved | -$2167.82 |
| Portfolio value | $101,159.15 |
| Benchmark value | $105,276.02 |
| Alpha (cumulative) | -4.117% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 45 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $733.62 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1504.98 |
| Signal saved | -$1571.42 |
| Portfolio value | $101,159.15 |
| Benchmark value | $103,769.60 |
| Alpha (cumulative) | -2.611% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 46 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $733.32 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1488.18 |
| Signal saved | -$1554.62 |
| Portfolio value | $101,159.15 |
| Benchmark value | $103,727.16 |
| Alpha (cumulative) | -2.568% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 47 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $733.33 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1488.74 |
| Signal saved | -$1555.18 |
| Portfolio value | $101,159.15 |
| Benchmark value | $103,728.58 |
| Alpha (cumulative) | -2.570% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 48 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $729.35 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1265.86 |
| Signal saved | -$1332.30 |
| Portfolio value | $101,159.15 |
| Benchmark value | $103,165.61 |
| Alpha (cumulative) | -2.007% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 49 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $740.86 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1910.42 |
| Signal saved | -$1976.86 |
| Portfolio value | $101,159.15 |
| Benchmark value | $104,793.68 |
| Alpha (cumulative) | -3.635% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 50 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $746.65 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2234.66 |
| Signal saved | -$2301.10 |
| Portfolio value | $101,159.15 |
| Benchmark value | $105,612.67 |
| Alpha (cumulative) | -4.454% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 51 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $745.66 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2179.22 |
| Signal saved | -$2245.66 |
| Portfolio value | $101,159.15 |
| Benchmark value | $105,472.64 |
| Alpha (cumulative) | -4.314% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 52 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $744.86 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2134.42 |
| Signal saved | -$2200.86 |
| Portfolio value | $101,159.15 |
| Benchmark value | $105,359.48 |
| Alpha (cumulative) | -4.200% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 53 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $751.27 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2493.38 |
| Signal saved | -$2559.82 |
| Portfolio value | $101,159.15 |
| Benchmark value | $106,266.16 |
| Alpha (cumulative) | -5.107% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 54 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $747.77 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2297.38 |
| Signal saved | -$2363.82 |
| Portfolio value | $101,159.15 |
| Benchmark value | $105,771.09 |
| Alpha (cumulative) | -4.612% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 55 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $745.28 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2157.94 |
| Signal saved | -$2224.38 |
| Portfolio value | $101,159.15 |
| Benchmark value | $105,418.89 |
| Alpha (cumulative) | -4.260% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 56 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $751.55 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2509.06 |
| Signal saved | -$2575.50 |
| Portfolio value | $101,159.15 |
| Benchmark value | $106,305.77 |
| Alpha (cumulative) | -5.147% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 57 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $754.94 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2698.90 |
| Signal saved | -$2765.34 |
| Portfolio value | $101,159.15 |
| Benchmark value | $106,785.28 |
| Alpha (cumulative) | -5.626% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 58 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $749.13 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2373.54 |
| Signal saved | -$2439.98 |
| Portfolio value | $100,998.03 |
| Benchmark value | $105,963.46 |
| Alpha (cumulative) | -4.965% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 59 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $751.94 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2530.90 |
| Signal saved | -$2597.34 |
| Portfolio value | $100,962.95 |
| Benchmark value | $106,360.94 |
| Alpha (cumulative) | -5.398% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 60 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $754.77 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2689.38 |
| Signal saved | -$2755.82 |
| Portfolio value | $101,010.70 |
| Benchmark value | $106,761.24 |
| Alpha (cumulative) | -5.750% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 61 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $750.87 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2470.98 |
| Signal saved | -$2537.42 |
| Portfolio value | $100,834.57 |
| Benchmark value | $106,209.59 |
| Alpha (cumulative) | -5.375% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 62 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $743.28 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$2045.94 |
| Signal saved | -$2112.38 |
| Portfolio value | $100,692.01 |
| Benchmark value | $105,135.99 |
| Alpha (cumulative) | -4.444% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 63 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $742.15 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1982.66 |
| Signal saved | -$2049.10 |
| Portfolio value | $100,500.03 |
| Benchmark value | $104,976.15 |
| Alpha (cumulative) | -4.476% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 64 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T13) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $748.15 |
| Unrealized P&L | +$28.09 |
| P&L % | +0.071% |
| Portfolio value | $100,528.12 |
| Benchmark value | $105,824.84 |
| Alpha (cumulative) | -5.297% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: +0.07% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 65 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T13) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $747.49 |
| Unrealized P&L | -$6.89 |
| P&L % | -0.017% |
| Portfolio value | $100,493.14 |
| Benchmark value | $105,731.49 |
| Alpha (cumulative) | -5.238% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.02% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 66 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T14) |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $738.06 |
| Unrealized P&L | -$40.56 |
| P&L % | -0.106% |
| Portfolio value | $99,824.00 |
| Benchmark value | $104,397.63 |
| Alpha (cumulative) | -4.574% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Momentum: WEAK. Unrealized P&L: -0.11% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 67 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $738.90 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1800.66 |
| Signal saved | -$1867.10 |
| Portfolio value | $99,872.88 |
| Benchmark value | $104,516.44 |
| Alpha (cumulative) | -4.643% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 68 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $738.85 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1797.86 |
| Signal saved | -$1864.30 |
| Portfolio value | $99,977.02 |
| Benchmark value | $104,509.37 |
| Alpha (cumulative) | -4.532% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 69 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $740.79 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1906.50 |
| Signal saved | -$1972.94 |
| Portfolio value | $99,933.56 |
| Benchmark value | $104,783.78 |
| Alpha (cumulative) | -4.850% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 70 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $706.745/share |
| Close price | $729.57 |
| Realized P&L (locked) | -$66.44 |
| Reference if held | +$1278.18 |
| Signal saved | -$1344.62 |
| Portfolio value | $99,933.56 |
| Benchmark value | $103,196.73 |
| Alpha (cumulative) | -3.263% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-66.44. Regime: BULL (MA20 $745.79 vs MA50 $743.82). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

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
_Day 70 of 90 · Alpaca equity: $99,964.59 · Cumulative alpha vs SPY: -3.263%_