# ALPACA PAPER JOURNAL — SPY
_Last updated: September 25, 2026 | Day 68 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$744.660/share**
> (2026-06-22, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-09-25): **BEARISH**  
> Fast: MA10 $763.34 | MA30 $764.88  
> Slow: MA20 $763.92 | MA50 $759.46  
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

**Total trades:** 18 | **Closed:** 18 | **Open:** No | **Cumulative Realized P&L:** -$2126.51

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $744.660 (2026-06-22) | $744.640 (2026-06-22) | 38 | -$0.76 | ✅ Closed |
| T2 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T3 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T4 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T5 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T6 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T7 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T8 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T9 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T10 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T11 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T12 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T13 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T14 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T15 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T16 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |
| T17 | $773.250 (2026-09-22) | $773.540 (2026-09-22) | 51 | +$14.79 | ✅ Closed |
| T18 | $768.534 (2026-09-23) | $767.970 (2026-09-23) | 51 | -$28.77 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,060.25 |
| Alpaca cash | $99,060.25 |
| Cumulative realized P&L | -$2126.51 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-06-22 | $742.43 | FLAT | — | — | $99,999.24 |
| Day 2 | 2026-06-23 | $731.80 | FLAT | — | — | $99,999.24 |
| Day 3 | 2026-06-24 | $731.50 | FLAT | — | — | $99,999.24 |
| Day 4 | 2026-06-25 | $731.51 | FLAT | — | — | $99,999.24 |
| Day 5 | 2026-06-26 | $727.54 | FLAT | — | — | $99,999.24 |
| Day 6 | 2026-06-29 | $739.03 | FLAT | — | — | $99,999.24 |
| Day 7 | 2026-06-30 | $744.80 | FLAT | — | — | $99,999.24 |
| Day 8 | 2026-07-01 | $743.82 | FLAT | — | — | $99,999.24 |
| Day 9 | 2026-07-02 | $743.02 | FLAT | — | — | $99,999.24 |
| Day 10 | 2026-07-06 | $749.41 | FLAT | — | — | $99,999.24 |
| Day 11 | 2026-07-07 | $745.92 | FLAT | — | — | $99,999.24 |
| Day 12 | 2026-07-08 | $743.43 | FLAT | — | — | $99,999.24 |
| Day 13 | 2026-07-09 | $749.69 | FLAT | — | — | $99,999.24 |
| Day 14 | 2026-07-10 | $753.07 | FLAT | — | — | $99,999.24 |
| Day 15 | 2026-07-13 | $747.27 | FLAT | — | — | $99,838.12 |
| Day 16 | 2026-07-14 | $750.08 | FLAT | — | — | $99,803.04 |
| Day 17 | 2026-07-15 | $752.90 | FLAT | — | — | $99,850.79 |
| Day 18 | 2026-07-16 | $749.01 | FLAT | — | — | $99,674.66 |
| Day 19 | 2026-07-17 | $741.44 | FLAT | — | — | $99,532.10 |
| Day 20 | 2026-07-20 | $740.31 | FLAT | — | — | $99,340.12 |
| Day 21 | 2026-07-21 | $746.30 | Long 53 SPY (T8) | -$69.96 | -0.177% | $99,270.16 |
| Day 22 | 2026-07-22 | $745.64 | Long 53 SPY (T8) | -$104.94 | -0.265% | $99,235.18 |
| Day 23 | 2026-07-23 | $736.23 | Long 52 SPY (T9) | -$135.72 | -0.353% | $98,568.93 |
| Day 24 | 2026-07-24 | $737.07 | FLAT | — | — | $98,712.97 |
| Day 25 | 2026-07-27 | $737.02 | FLAT | — | — | $98,817.11 |
| Day 26 | 2026-07-28 | $738.96 | FLAT | — | — | $98,773.65 |
| Day 27 | 2026-07-29 | $727.76 | FLAT | — | — | $98,773.65 |
| Day 28 | 2026-07-30 | $739.79 | FLAT | — | — | $98,773.65 |
| Day 29 | 2026-07-31 | $744.94 | FLAT | — | — | $98,773.65 |
| Day 30 | 2026-08-03 | $755.84 | FLAT | — | — | $98,773.65 |
| Day 31 | 2026-08-04 | $769.20 | Long 50 SPY (T12) | -$147.50 | -0.382% | $98,626.15 |
| Day 32 | 2026-08-05 | $767.88 | FLAT | — | — | $98,686.65 |
| Day 33 | 2026-08-06 | $766.74 | FLAT | — | — | $98,686.65 |
| Day 34 | 2026-08-07 | $771.25 | Long 51 SPY (T13) | -$64.27 | -0.163% | $98,622.38 |
| Day 35 | 2026-08-10 | $771.11 | FLAT | — | — | $98,711.63 |
| Day 36 | 2026-08-11 | $768.61 | Long 51 SPY (T14) | -$256.60 | -0.650% | $98,455.03 |
| Day 37 | 2026-08-12 | $770.63 | Long 51 SPY (T14) | -$153.58 | -0.389% | $98,558.05 |
| Day 38 | 2026-08-13 | $775.91 | Long 51 SPY (T14) | +$115.70 | +0.293% | $98,827.33 |
| Day 39 | 2026-08-14 | $774.38 | Long 51 SPY (T14) | +$37.67 | +0.095% | $98,749.30 |
| Day 40 | 2026-08-17 | $770.71 | Long 51 SPY (T14) | -$149.50 | -0.379% | $98,562.13 |
| Day 41 | 2026-08-18 | $765.46 | Long 51 SPY (T14) | -$417.25 | -1.058% | $98,294.38 |
| Day 42 | 2026-08-19 | $767.19 | Long 51 SPY (T14) | -$329.02 | -0.834% | $98,382.61 |
| Day 43 | 2026-08-20 | $760.73 | Long 51 SPY (T14) | -$658.48 | -1.669% | $98,053.15 |
| Day 44 | 2026-08-21 | $763.74 | Long 51 SPY (T14) | -$504.97 | -1.280% | $98,206.66 |
| Day 45 | 2026-08-24 | $761.57 | Long 51 SPY (T14) | -$615.64 | -1.560% | $98,095.99 |
| Day 46 | 2026-08-25 | $763.89 | Long 51 SPY (T14) | -$497.32 | -1.260% | $98,214.31 |
| Day 47 | 2026-08-26 | $764.04 | Long 51 SPY (T14) | -$489.67 | -1.241% | $98,221.96 |
| Day 48 | 2026-08-27 | $769.27 | Long 51 SPY (T14) | -$222.94 | -0.565% | $98,488.69 |
| Day 49 | 2026-08-28 | $767.37 | Long 51 SPY (T14) | -$319.84 | -0.811% | $98,391.79 |
| Day 50 | 2026-08-31 | $764.97 | Long 51 SPY (T14) | -$442.24 | -1.121% | $98,269.39 |
| Day 51 | 2026-09-01 | $759.74 | FLAT | — | — | $98,099.05 |
| Day 52 | 2026-09-02 | $763.23 | Long 51 SPY (T15) | -$86.19 | -0.221% | $98,012.86 |
| Day 53 | 2026-09-03 | $771.20 | Long 51 SPY (T15) | +$320.28 | +0.821% | $98,419.33 |
| Day 54 | 2026-09-04 | $768.27 | Long 51 SPY (T15) | +$170.85 | +0.438% | $98,269.90 |
| Day 55 | 2026-09-08 | $764.16 | FLAT | — | — | $98,151.58 |
| Day 56 | 2026-09-09 | $760.54 | Long 52 SPY (T16) | -$127.87 | -0.322% | $98,023.71 |
| Day 57 | 2026-09-10 | $755.99 | FLAT | — | — | $97,887.47 |
| Day 58 | 2026-09-11 | $762.25 | FLAT | — | — | $97,887.47 |
| Day 59 | 2026-09-14 | $758.87 | FLAT | — | — | $97,887.47 |
| Day 60 | 2026-09-15 | $755.54 | FLAT | — | — | $97,887.47 |
| Day 61 | 2026-09-16 | $752.18 | FLAT | — | — | $97,887.47 |
| Day 62 | 2026-09-17 | $760.75 | FLAT | — | — | $97,887.47 |
| Day 63 | 2026-09-18 | $761.62 | FLAT | — | — | $97,887.47 |
| Day 64 | 2026-09-21 | $773.52 | FLAT | — | — | $97,887.47 |
| Day 65 | 2026-09-22 | $773.44 | FLAT | — | — | $97,902.26 |
| Day 66 | 2026-09-23 | $767.93 | FLAT | — | — | $97,873.49 |
| Day 67 | 2026-09-24 | $767.29 | FLAT | — | — | $97,873.49 |
| Day 68 | 2026-09-25 | $771.13 | FLAT | — | — | $97,873.49 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-06-22 | $99,999.24 | $99,999.98 | -0.0008% | -0.000% | **-0.001%** |
| Day 2 | 2026-06-23 | $99,999.24 | $98,568.19 | -0.0008% | -1.432% | **+1.431%** |
| Day 3 | 2026-06-24 | $99,999.24 | $98,527.78 | -0.0008% | -1.472% | **+1.471%** |
| Day 4 | 2026-06-25 | $99,999.24 | $98,529.13 | -0.0008% | -1.471% | **+1.470%** |
| Day 5 | 2026-06-26 | $99,999.24 | $97,994.40 | -0.0008% | -2.006% | **+2.005%** |
| Day 6 | 2026-06-29 | $99,999.24 | $99,542.02 | -0.0008% | -0.458% | **+0.457%** |
| Day 7 | 2026-06-30 | $99,999.24 | $100,319.20 | -0.0008% | +0.319% | **-0.320%** |
| Day 8 | 2026-07-01 | $99,999.24 | $100,187.20 | -0.0008% | +0.187% | **-0.188%** |
| Day 9 | 2026-07-02 | $99,999.24 | $100,079.44 | -0.0008% | +0.079% | **-0.080%** |
| Day 10 | 2026-07-06 | $99,999.24 | $100,940.13 | -0.0008% | +0.940% | **-0.941%** |
| Day 11 | 2026-07-07 | $99,999.24 | $100,470.05 | -0.0008% | +0.470% | **-0.471%** |
| Day 12 | 2026-07-08 | $99,999.24 | $100,134.67 | -0.0008% | +0.135% | **-0.136%** |
| Day 13 | 2026-07-09 | $99,999.24 | $100,977.85 | -0.0008% | +0.978% | **-0.979%** |
| Day 14 | 2026-07-10 | $99,999.24 | $101,433.11 | -0.0008% | +1.433% | **-1.434%** |
| Day 15 | 2026-07-13 | $99,838.12 | $100,651.89 | -0.1619% | +0.652% | **-0.814%** |
| Day 16 | 2026-07-14 | $99,803.04 | $101,030.38 | -0.1970% | +1.030% | **-1.227%** |
| Day 17 | 2026-07-15 | $99,850.79 | $101,410.21 | -0.1492% | +1.410% | **-1.559%** |
| Day 18 | 2026-07-16 | $99,674.66 | $100,886.25 | -0.3253% | +0.886% | **-1.211%** |
| Day 19 | 2026-07-17 | $99,532.10 | $99,866.63 | -0.4679% | -0.133% | **-0.335%** |
| Day 20 | 2026-07-20 | $99,340.12 | $99,714.43 | -0.6599% | -0.286% | **-0.374%** |
| Day 21 | 2026-07-21 | $99,270.16 | $100,521.24 | -0.7298% | +0.521% | **-1.251%** |
| Day 22 | 2026-07-22 | $99,235.18 | $100,432.34 | -0.7648% | +0.432% | **-1.197%** |
| Day 23 | 2026-07-23 | $98,568.93 | $99,164.88 | -1.4311% | -0.835% | **-0.596%** |
| Day 24 | 2026-07-24 | $98,712.97 | $99,278.02 | -1.2870% | -0.722% | **-0.565%** |
| Day 25 | 2026-07-27 | $98,817.11 | $99,271.29 | -1.1829% | -0.729% | **-0.454%** |
| Day 26 | 2026-07-28 | $98,773.65 | $99,532.59 | -1.2264% | -0.467% | **-0.759%** |
| Day 27 | 2026-07-29 | $98,773.65 | $98,024.03 | -1.2264% | -1.976% | **+0.750%** |
| Day 28 | 2026-07-30 | $98,773.65 | $99,644.39 | -1.2264% | -0.356% | **-0.870%** |
| Day 29 | 2026-07-31 | $98,773.65 | $100,338.05 | -1.2264% | +0.338% | **-1.564%** |
| Day 30 | 2026-08-03 | $98,773.65 | $101,806.21 | -1.2264% | +1.806% | **-3.032%** |
| Day 31 | 2026-08-04 | $98,626.15 | $103,605.70 | -1.3739% | +3.606% | **-4.980%** |
| Day 32 | 2026-08-05 | $98,686.65 | $103,427.91 | -1.3134% | +3.428% | **-4.741%** |
| Day 33 | 2026-08-06 | $98,686.65 | $103,274.36 | -1.3134% | +3.274% | **-4.587%** |
| Day 34 | 2026-08-07 | $98,622.38 | $103,881.82 | -1.3776% | +3.882% | **-5.260%** |
| Day 35 | 2026-08-10 | $98,711.63 | $103,862.97 | -1.2884% | +3.863% | **-5.151%** |
| Day 36 | 2026-08-11 | $98,455.03 | $103,526.23 | -1.5450% | +3.526% | **-5.071%** |
| Day 37 | 2026-08-12 | $98,558.05 | $103,798.31 | -1.4419% | +3.798% | **-5.240%** |
| Day 38 | 2026-08-13 | $98,827.33 | $104,509.49 | -1.1727% | +4.509% | **-5.682%** |
| Day 39 | 2026-08-14 | $98,749.30 | $104,303.41 | -1.2507% | +4.303% | **-5.554%** |
| Day 40 | 2026-08-17 | $98,562.13 | $103,809.09 | -1.4379% | +3.809% | **-5.247%** |
| Day 41 | 2026-08-18 | $98,294.38 | $103,101.95 | -1.7056% | +3.102% | **-4.808%** |
| Day 42 | 2026-08-19 | $98,382.61 | $103,334.97 | -1.6174% | +3.335% | **-4.952%** |
| Day 43 | 2026-08-20 | $98,053.15 | $102,464.85 | -1.9469% | +2.465% | **-4.412%** |
| Day 44 | 2026-08-21 | $98,206.66 | $102,870.28 | -1.7933% | +2.870% | **-4.663%** |
| Day 45 | 2026-08-24 | $98,095.99 | $102,578.00 | -1.9040% | +2.578% | **-4.482%** |
| Day 46 | 2026-08-25 | $98,214.31 | $102,890.48 | -1.7857% | +2.890% | **-4.676%** |
| Day 47 | 2026-08-26 | $98,221.96 | $102,910.69 | -1.7780% | +2.911% | **-4.689%** |
| Day 48 | 2026-08-27 | $98,488.69 | $103,615.13 | -1.5113% | +3.615% | **-5.126%** |
| Day 49 | 2026-08-28 | $98,391.79 | $103,359.21 | -1.6082% | +3.359% | **-4.967%** |
| Day 50 | 2026-08-31 | $98,269.39 | $103,035.95 | -1.7306% | +3.036% | **-4.767%** |
| Day 51 | 2026-09-01 | $98,099.05 | $102,331.51 | -1.9009% | +2.332% | **-4.233%** |
| Day 52 | 2026-09-02 | $98,012.86 | $102,801.59 | -1.9871% | +2.802% | **-4.789%** |
| Day 53 | 2026-09-03 | $98,419.33 | $103,875.09 | -1.5807% | +3.875% | **-5.456%** |
| Day 54 | 2026-09-04 | $98,269.90 | $103,480.44 | -1.7301% | +3.480% | **-5.210%** |
| Day 55 | 2026-09-08 | $98,151.58 | $102,926.85 | -1.8484% | +2.927% | **-4.775%** |
| Day 56 | 2026-09-09 | $98,023.71 | $102,439.26 | -1.9763% | +2.439% | **-4.415%** |
| Day 57 | 2026-09-10 | $97,887.47 | $101,826.41 | -2.1125% | +1.826% | **-3.938%** |
| Day 58 | 2026-09-11 | $97,887.47 | $102,669.59 | -2.1125% | +2.670% | **-4.782%** |
| Day 59 | 2026-09-14 | $97,887.47 | $102,214.33 | -2.1125% | +2.214% | **-4.326%** |
| Day 60 | 2026-09-15 | $97,887.47 | $101,765.80 | -2.1125% | +1.766% | **-3.878%** |
| Day 61 | 2026-09-16 | $97,887.47 | $101,313.23 | -2.1125% | +1.313% | **-3.425%** |
| Day 62 | 2026-09-17 | $97,887.47 | $102,467.55 | -2.1125% | +2.468% | **-4.580%** |
| Day 63 | 2026-09-18 | $97,887.47 | $102,584.73 | -2.1125% | +2.585% | **-4.698%** |
| Day 64 | 2026-09-21 | $97,887.47 | $104,187.57 | -2.1125% | +4.188% | **-6.300%** |
| Day 65 | 2026-09-22 | $97,902.26 | $104,176.80 | -2.0977% | +4.177% | **-6.275%** |
| Day 66 | 2026-09-23 | $97,873.49 | $103,434.64 | -2.1265% | +3.435% | **-5.562%** |
| Day 67 | 2026-09-24 | $97,873.49 | $103,348.44 | -2.1265% | +3.348% | **-5.474%** |
| Day 68 | 2026-09-25 | $97,873.49 | $103,865.66 | -2.1265% | +3.866% | **-5.992%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-06-22 | $742.43 | -$84.74 | -$2041.77 | Holding would have been **$2041.77** better — honest entry |
| Day 2 | 2026-06-23 | $731.80 | -$488.68 | -$1637.83 | Holding would have been **$1637.83** better — honest entry |
| Day 3 | 2026-06-24 | $731.50 | -$500.08 | -$1626.43 | Holding would have been **$1626.43** better — honest entry |
| Day 4 | 2026-06-25 | $731.51 | -$499.70 | -$1626.81 | Holding would have been **$1626.81** better — honest entry |
| Day 5 | 2026-06-26 | $727.54 | -$650.56 | -$1475.95 | Holding would have been **$1475.95** better — honest entry |
| Day 6 | 2026-06-29 | $739.03 | -$213.94 | -$1912.57 | Holding would have been **$1912.57** better — honest entry |
| Day 7 | 2026-06-30 | $744.80 | +$5.32 | -$2131.83 | Holding would have been **$2131.83** better — honest entry |
| Day 8 | 2026-07-01 | $743.82 | -$31.92 | -$2094.59 | Holding would have been **$2094.59** better — honest entry |
| Day 9 | 2026-07-02 | $743.02 | -$62.32 | -$2064.19 | Holding would have been **$2064.19** better — honest entry |
| Day 10 | 2026-07-06 | $749.41 | +$180.50 | -$2307.01 | Holding would have been **$2307.01** better — honest entry |
| Day 11 | 2026-07-07 | $745.92 | +$47.88 | -$2174.39 | Holding would have been **$2174.39** better — honest entry |
| Day 12 | 2026-07-08 | $743.43 | -$46.74 | -$2079.77 | Holding would have been **$2079.77** better — honest entry |
| Day 13 | 2026-07-09 | $749.69 | +$191.14 | -$2317.65 | Holding would have been **$2317.65** better — honest entry |
| Day 14 | 2026-07-10 | $753.07 | +$319.58 | -$2446.09 | Holding would have been **$2446.09** better — honest entry |
| Day 15 | 2026-07-13 | $747.27 | +$99.18 | -$2225.69 | Holding would have been **$2225.69** better — honest entry |
| Day 16 | 2026-07-14 | $750.08 | +$205.96 | -$2332.47 | Holding would have been **$2332.47** better — honest entry |
| Day 17 | 2026-07-15 | $752.90 | +$313.12 | -$2439.63 | Holding would have been **$2439.63** better — honest entry |
| Day 18 | 2026-07-16 | $749.01 | +$165.30 | -$2291.81 | Holding would have been **$2291.81** better — honest entry |
| Day 19 | 2026-07-17 | $741.44 | -$122.36 | -$2004.15 | Holding would have been **$2004.15** better — honest entry |
| Day 20 | 2026-07-20 | $740.31 | -$165.30 | -$1961.21 | Holding would have been **$1961.21** better — honest entry |
| Day 21 | 2026-07-21 | $746.30 | +$62.32 | -$2188.83 | Position open |
| Day 22 | 2026-07-22 | $745.64 | +$37.24 | -$2163.75 | Position open |
| Day 23 | 2026-07-23 | $736.23 | -$320.34 | -$1806.17 | Position open |
| Day 24 | 2026-07-24 | $737.07 | -$288.42 | -$1838.09 | Holding would have been **$1838.09** better — honest entry |
| Day 25 | 2026-07-27 | $737.02 | -$290.32 | -$1836.19 | Holding would have been **$1836.19** better — honest entry |
| Day 26 | 2026-07-28 | $738.96 | -$216.60 | -$1909.91 | Holding would have been **$1909.91** better — honest entry |
| Day 27 | 2026-07-29 | $727.76 | -$642.20 | -$1484.31 | Holding would have been **$1484.31** better — honest entry |
| Day 28 | 2026-07-30 | $739.79 | -$185.06 | -$1941.45 | Holding would have been **$1941.45** better — honest entry |
| Day 29 | 2026-07-31 | $744.94 | +$10.64 | -$2137.15 | Holding would have been **$2137.15** better — honest entry |
| Day 30 | 2026-08-03 | $755.84 | +$424.84 | -$2551.35 | Holding would have been **$2551.35** better — honest entry |
| Day 31 | 2026-08-04 | $769.20 | +$932.52 | -$3059.03 | Position open |
| Day 32 | 2026-08-05 | $767.88 | +$882.36 | -$3008.87 | Holding would have been **$3008.87** better — honest entry |
| Day 33 | 2026-08-06 | $766.74 | +$839.04 | -$2965.55 | Holding would have been **$2965.55** better — honest entry |
| Day 34 | 2026-08-07 | $771.25 | +$1010.42 | -$3136.93 | Position open |
| Day 35 | 2026-08-10 | $771.11 | +$1005.10 | -$3131.61 | Holding would have been **$3131.61** better — honest entry |
| Day 36 | 2026-08-11 | $768.61 | +$910.10 | -$3036.61 | Position open |
| Day 37 | 2026-08-12 | $770.63 | +$986.86 | -$3113.37 | Position open |
| Day 38 | 2026-08-13 | $775.91 | +$1187.50 | -$3314.01 | Position open |
| Day 39 | 2026-08-14 | $774.38 | +$1129.36 | -$3255.87 | Position open |
| Day 40 | 2026-08-17 | $770.71 | +$989.90 | -$3116.41 | Position open |
| Day 41 | 2026-08-18 | $765.46 | +$790.40 | -$2916.91 | Position open |
| Day 42 | 2026-08-19 | $767.19 | +$856.14 | -$2982.65 | Position open |
| Day 43 | 2026-08-20 | $760.73 | +$610.66 | -$2737.17 | Position open |
| Day 44 | 2026-08-21 | $763.74 | +$725.04 | -$2851.55 | Position open |
| Day 45 | 2026-08-24 | $761.57 | +$642.58 | -$2769.09 | Position open |
| Day 46 | 2026-08-25 | $763.89 | +$730.74 | -$2857.25 | Position open |
| Day 47 | 2026-08-26 | $764.04 | +$736.44 | -$2862.95 | Position open |
| Day 48 | 2026-08-27 | $769.27 | +$935.18 | -$3061.69 | Position open |
| Day 49 | 2026-08-28 | $767.37 | +$862.98 | -$2989.49 | Position open |
| Day 50 | 2026-08-31 | $764.97 | +$771.78 | -$2898.29 | Position open |
| Day 51 | 2026-09-01 | $759.74 | +$573.04 | -$2699.55 | Holding would have been **$2699.55** better — honest entry |
| Day 52 | 2026-09-02 | $763.23 | +$705.66 | -$2832.17 | Position open |
| Day 53 | 2026-09-03 | $771.20 | +$1008.52 | -$3135.03 | Position open |
| Day 54 | 2026-09-04 | $768.27 | +$897.18 | -$3023.69 | Position open |
| Day 55 | 2026-09-08 | $764.16 | +$741.00 | -$2867.51 | Holding would have been **$2867.51** better — honest entry |
| Day 56 | 2026-09-09 | $760.54 | +$603.44 | -$2729.95 | Position open |
| Day 57 | 2026-09-10 | $755.99 | +$430.54 | -$2557.05 | Holding would have been **$2557.05** better — honest entry |
| Day 58 | 2026-09-11 | $762.25 | +$668.42 | -$2794.93 | Holding would have been **$2794.93** better — honest entry |
| Day 59 | 2026-09-14 | $758.87 | +$539.98 | -$2666.49 | Holding would have been **$2666.49** better — honest entry |
| Day 60 | 2026-09-15 | $755.54 | +$413.44 | -$2539.95 | Holding would have been **$2539.95** better — honest entry |
| Day 61 | 2026-09-16 | $752.18 | +$285.76 | -$2412.27 | Holding would have been **$2412.27** better — honest entry |
| Day 62 | 2026-09-17 | $760.75 | +$611.42 | -$2737.93 | Holding would have been **$2737.93** better — honest entry |
| Day 63 | 2026-09-18 | $761.62 | +$644.48 | -$2770.99 | Holding would have been **$2770.99** better — honest entry |
| Day 64 | 2026-09-21 | $773.52 | +$1096.68 | -$3223.19 | Holding would have been **$3223.19** better — honest entry |
| Day 65 | 2026-09-22 | $773.44 | +$1093.64 | -$3220.15 | Holding would have been **$3220.15** better — honest entry |
| Day 66 | 2026-09-23 | $767.93 | +$884.26 | -$3010.77 | Holding would have been **$3010.77** better — honest entry |
| Day 67 | 2026-09-24 | $767.29 | +$859.94 | -$2986.45 | Holding would have been **$2986.45** better — honest entry |
| Day 68 | 2026-09-25 | $771.13 | +$1005.86 | -$3132.37 | Holding would have been **$3132.37** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-06-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $742.43 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$84.74 |
| Signal saved | -$2041.77 |
| Portfolio value | $99,999.24 |
| Benchmark value | $99,999.98 |
| Alpha (cumulative) | -0.001% |

**Regime call:** BULL

**Market context:** Markets remain in a recovery phase with the VIX at 17.3, and oil prices stable at $73.41 per barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with the fast MAs showing a golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime can override a bearish momentum environment, but still requires careful monitoring.

---

### Day 2 — 2026-06-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $731.80 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$488.68 |
| Signal saved | -$1637.83 |
| Portfolio value | $99,999.24 |
| Benchmark value | $98,568.19 |
| Alpha (cumulative) | +1.431% |

**Regime call:** Consolidation

**Market context:** Markets were mixed today, with slight dips in tech shares, but overall remaining in a bull regime. The VIX index remains relatively low at 19.49. Oil prices are steady at $72.99 per barrel.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime context (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of both short-term and long-term signals.

---

### Day 3 — 2026-06-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $731.50 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$500.08 |
| Signal saved | -$1626.43 |
| Portfolio value | $99,999.24 |
| Benchmark value | $98,527.78 |
| Alpha (cumulative) | +1.471% |

**Regime call:** BULL

**Market context:** US-Iran tensions eased, boosting futures, while VIX remained relatively low at 18.29. Rivian's decline weighed on sentiment, but the market context remains bullish.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50 crossover).

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish regime context, leading to a position exit.

---

### Day 4 — 2026-06-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $731.51 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$499.70 |
| Signal saved | -$1626.81 |
| Portfolio value | $99,999.24 |
| Benchmark value | $98,529.13 |
| Alpha (cumulative) | +1.470% |

**Regime call:** Bullish Regime

**Market context:** Markets were up pre-bell on Thursday, driven by investors' enthusiasm for AI growth themes and reduced Middle East risks. The S&P 500 ETF with a 20% yield outperformed most covered call ETFs. The VIX index remained relatively low at 18.75.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bullish regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal in a bullish regime led to a profitable exit, highlighting the importance of regime context in the dual-timeframe strategy.

---

### Day 5 — 2026-06-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $727.54 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$650.56 |
| Signal saved | -$1475.95 |
| Portfolio value | $99,999.24 |
| Benchmark value | $97,994.40 |
| Alpha (cumulative) | +2.005% |

**Regime call:** RISK-ON

**Market context:** Global investors shifted focus from Middle East to Technology Stocks, causing ETFs and equity futures to decline. Market sentiment remains uncertain with weak momentum and a bearish fast signal. VIX remains elevated at 19.06.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) in a bull regime. Monitoring for re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 6 — 2026-06-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $739.03 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$213.94 |
| Signal saved | -$1912.57 |
| Portfolio value | $99,999.24 |
| Benchmark value | $99,542.02 |
| Alpha (cumulative) | +0.457% |

**Regime call:** Consolidation

**Market context:** The S&P 500 closed at $738.53, with VIX at 17.84 and 10Y Treasury yield at 4.38%. Market headlines pointed to emerging headwinds and renewed US-Iran diplomacy hopes.

**Strategy note:** The system exited the position on a bearish fast signal, with MA10 crossing below MA30, and is now monitoring for re-entry on a next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in gains on a bearish signal highlights the importance of discipline in adhering to the dual-timeframe strategy.

---

### Day 7 — 2026-06-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $744.80 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$5.32 |
| Signal saved | -$2131.83 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,319.20 |
| Alpha (cumulative) | -0.320% |

**Regime call:** Consolidation

**Market context:** The Nasdaq tested a critical level, and equity futures retreated ahead of high-stakes US-Iran talks. The S&P 500 and Nasdaq ended the quarter higher, while the Dow was driven by Alphabet's debut. The VIX remained relatively low at 16.85.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position correctly in a bull regime highlights the importance of the slow filter in preventing false signals.

---

### Day 8 — 2026-07-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $743.82 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$31.92 |
| Signal saved | -$2094.59 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,187.20 |
| Alpha (cumulative) | -0.188% |

**Regime call:** Consolidation

**Market context:** The market experienced a low-volatility day with the VIX at 16.11, while the WTI Oil price remained relatively stable at $68.15. The 10Y Treasury yield also remained steady at 4.46%. The SPY price closed at $748.85 after a day of mixed headlines.

**Strategy note:** The system exited the position based on a bearish fast signal (MA10/MA30 death cross) and a bull regime (MA20/MA50), resulting in a realized P&L of $+1188.82.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market regimes and signals is crucial in maximizing returns and minimizing losses.

---

### Day 9 — 2026-07-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $743.02 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$62.32 |
| Signal saved | -$2064.19 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,079.44 |
| Alpha (cumulative) | -0.080% |

**Regime call:** Consolidation

**Market context:** Markets were relatively subdued today, with the S&P 500 futures mixed ahead of the June jobs report. Analysts' warnings about popular income ETFs and Goldman's strategist's comments on Europe's performance were among the notable headlines. The VIX index remained relatively low at 16.66.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime (MA20/MA50 crossover). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a clear understanding of the market's regime context.

---

### Day 10 — 2026-07-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $749.41 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$180.50 |
| Signal saved | -$2307.01 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,940.13 |
| Alpha (cumulative) | -0.941% |

**Regime call:** Consolidation

**Market context:** Markets were muted ahead of a quiet week, with equity futures mixed and ETFs higher. Chip stocks rebounded, contributing to the positive sentiment. Investors await the release of Fed minutes.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a $+1188.82 realized P&L.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can override a bullish slow regime, leading to profitable exits.

---

### Day 11 — 2026-07-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $745.92 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$47.88 |
| Signal saved | -$2174.39 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,470.05 |
| Alpha (cumulative) | -0.471% |

**Regime call:** Recovery Rally

**Market context:** The Nasdaq sank as Samsung tumbled, while equity futures were mixed amid caution over the chip sector outlook. The VIX index remained relatively low at 16.25. Oil prices were steady at $70.51 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (Fast Death Cross), while the slow filter indicated a bullish regime. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bullish regime, highlighting the importance of monitoring multiple timeframes and signals.

---

### Day 12 — 2026-07-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $743.43 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$46.74 |
| Signal saved | -$2079.77 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,134.67 |
| Alpha (cumulative) | -0.136% |

**Regime call:** Consolidation

**Market context:** The stock market reacted to unstable peace talks and Trump's comments on Iran, causing a drop in the Dow. Oil prices remained relatively stable. The VIX index rose slightly.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross). The regime remains BULL, as the slow MAs (MA20/MA50) indicate.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in profits during a bearish signal is crucial to maintaining overall performance.

---

### Day 13 — 2026-07-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $749.69 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$191.14 |
| Signal saved | -$2317.65 |
| Portfolio value | $99,999.24 |
| Benchmark value | $100,977.85 |
| Alpha (cumulative) | -0.979% |

**Regime call:** Consolidation

**Market context:** Markets traded mixed with equity futures and chip stocks rebounding. The VIX index remained relatively low at 16.14. Oil prices were steady at $72.09 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position as the fast signal turned bearish with a death cross. The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit the position in time resulted in a significant realized P&L of $+1188.82.

---

### Day 14 — 2026-07-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $753.07 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$319.58 |
| Signal saved | -$2446.09 |
| Portfolio value | $99,999.24 |
| Benchmark value | $101,433.11 |
| Alpha (cumulative) | -1.434% |

**Regime call:** Consolidation

**Market context:** US-Iran tensions weighed on markets, while Q2 earnings season is approaching. Equity futures and ETFs were mixed, with precious metals ETFs performing well. VIX remained relatively low at 15.5.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 Death Cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish fast signal can occur even in a bull regime, emphasizing the importance of considering multiple timeframes in trading decisions.

---

### Day 15 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $747.27 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$99.18 |
| Signal saved | -$2225.69 |
| Portfolio value | $99,838.12 |
| Benchmark value | $100,651.89 |
| Alpha (cumulative) | -0.814% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 16 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $750.08 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$205.96 |
| Signal saved | -$2332.47 |
| Portfolio value | $99,803.04 |
| Benchmark value | $101,030.38 |
| Alpha (cumulative) | -1.227% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 17 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $752.90 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$313.12 |
| Signal saved | -$2439.63 |
| Portfolio value | $99,850.79 |
| Benchmark value | $101,410.21 |
| Alpha (cumulative) | -1.559% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 18 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$165.30 |
| Signal saved | -$2291.81 |
| Portfolio value | $99,674.66 |
| Benchmark value | $100,886.25 |
| Alpha (cumulative) | -1.211% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 19 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$122.36 |
| Signal saved | -$2004.15 |
| Portfolio value | $99,532.10 |
| Benchmark value | $99,866.63 |
| Alpha (cumulative) | -0.335% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 20 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$165.30 |
| Signal saved | -$1961.21 |
| Portfolio value | $99,340.12 |
| Benchmark value | $99,714.43 |
| Alpha (cumulative) | -0.374% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 21 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T8) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,270.16 |
| Benchmark value | $100,521.24 |
| Alpha (cumulative) | -1.251% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 22 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T8) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,235.18 |
| Benchmark value | $100,432.34 |
| Alpha (cumulative) | -1.197% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 23 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T9) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,568.93 |
| Benchmark value | $99,164.88 |
| Alpha (cumulative) | -0.596% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 24 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$288.42 |
| Signal saved | -$1838.09 |
| Portfolio value | $98,712.97 |
| Benchmark value | $99,278.02 |
| Alpha (cumulative) | -0.565% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 25 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$290.32 |
| Signal saved | -$1836.19 |
| Portfolio value | $98,817.11 |
| Benchmark value | $99,271.29 |
| Alpha (cumulative) | -0.454% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 26 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$216.60 |
| Signal saved | -$1909.91 |
| Portfolio value | $98,773.65 |
| Benchmark value | $99,532.59 |
| Alpha (cumulative) | -0.759% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 27 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$642.20 |
| Signal saved | -$1484.31 |
| Portfolio value | $98,773.65 |
| Benchmark value | $98,024.03 |
| Alpha (cumulative) | +0.750% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 28 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | -$185.06 |
| Signal saved | -$1941.45 |
| Portfolio value | $98,773.65 |
| Benchmark value | $99,644.39 |
| Alpha (cumulative) | -0.870% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 29 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$10.64 |
| Signal saved | -$2137.15 |
| Portfolio value | $98,773.65 |
| Benchmark value | $100,338.05 |
| Alpha (cumulative) | -1.564% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 30 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$424.84 |
| Signal saved | -$2551.35 |
| Portfolio value | $98,773.65 |
| Benchmark value | $101,806.21 |
| Alpha (cumulative) | -3.032% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 31 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T12) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,626.15 |
| Benchmark value | $103,605.70 |
| Alpha (cumulative) | -4.980% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 32 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$882.36 |
| Signal saved | -$3008.87 |
| Portfolio value | $98,686.65 |
| Benchmark value | $103,427.91 |
| Alpha (cumulative) | -4.741% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 33 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$839.04 |
| Signal saved | -$2965.55 |
| Portfolio value | $98,686.65 |
| Benchmark value | $103,274.36 |
| Alpha (cumulative) | -4.587% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 34 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,622.38 |
| Benchmark value | $103,881.82 |
| Alpha (cumulative) | -5.260% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 35 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$1005.10 |
| Signal saved | -$3131.61 |
| Portfolio value | $98,711.63 |
| Benchmark value | $103,862.97 |
| Alpha (cumulative) | -5.151% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 36 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,455.03 |
| Benchmark value | $103,526.23 |
| Alpha (cumulative) | -5.071% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 37 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,558.05 |
| Benchmark value | $103,798.31 |
| Alpha (cumulative) | -5.240% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 38 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $98,827.33 |
| Benchmark value | $104,509.49 |
| Alpha (cumulative) | -5.682% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 39 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $98,749.30 |
| Benchmark value | $104,303.41 |
| Alpha (cumulative) | -5.554% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 40 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,562.13 |
| Benchmark value | $103,809.09 |
| Alpha (cumulative) | -5.247% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 41 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,294.38 |
| Benchmark value | $103,101.95 |
| Alpha (cumulative) | -4.808% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 42 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,382.61 |
| Benchmark value | $103,334.97 |
| Alpha (cumulative) | -4.952% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 43 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,053.15 |
| Benchmark value | $102,464.85 |
| Alpha (cumulative) | -4.412% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 44 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,206.66 |
| Benchmark value | $102,870.28 |
| Alpha (cumulative) | -4.663% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 45 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,095.99 |
| Benchmark value | $102,578.00 |
| Alpha (cumulative) | -4.482% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 46 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,214.31 |
| Benchmark value | $102,890.48 |
| Alpha (cumulative) | -4.676% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 47 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,221.96 |
| Benchmark value | $102,910.69 |
| Alpha (cumulative) | -4.689% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 48 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,488.69 |
| Benchmark value | $103,615.13 |
| Alpha (cumulative) | -5.126% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 49 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,391.79 |
| Benchmark value | $103,359.21 |
| Alpha (cumulative) | -4.967% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 50 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,269.39 |
| Benchmark value | $103,035.95 |
| Alpha (cumulative) | -4.767% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$573.04 |
| Signal saved | -$2699.55 |
| Portfolio value | $98,099.05 |
| Benchmark value | $102,331.51 |
| Alpha (cumulative) | -4.233% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,012.86 |
| Benchmark value | $102,801.59 |
| Alpha (cumulative) | -4.789% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,419.33 |
| Benchmark value | $103,875.09 |
| Alpha (cumulative) | -5.456% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T15) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,269.90 |
| Benchmark value | $103,480.44 |
| Alpha (cumulative) | -5.210% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 55 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$741.00 |
| Signal saved | -$2867.51 |
| Portfolio value | $98,151.58 |
| Benchmark value | $102,926.85 |
| Alpha (cumulative) | -4.775% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 56 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T16) |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,023.71 |
| Benchmark value | $102,439.26 |
| Alpha (cumulative) | -4.415% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BEARISH. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Momentum: RECOVERING. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 57 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$430.54 |
| Signal saved | -$2557.05 |
| Portfolio value | $97,887.47 |
| Benchmark value | $101,826.41 |
| Alpha (cumulative) | -3.938% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 58 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$668.42 |
| Signal saved | -$2794.93 |
| Portfolio value | $97,887.47 |
| Benchmark value | $102,669.59 |
| Alpha (cumulative) | -4.782% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 59 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$539.98 |
| Signal saved | -$2666.49 |
| Portfolio value | $97,887.47 |
| Benchmark value | $102,214.33 |
| Alpha (cumulative) | -4.326% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 60 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$413.44 |
| Signal saved | -$2539.95 |
| Portfolio value | $97,887.47 |
| Benchmark value | $101,765.80 |
| Alpha (cumulative) | -3.878% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 61 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$285.76 |
| Signal saved | -$2412.27 |
| Portfolio value | $97,887.47 |
| Benchmark value | $101,313.23 |
| Alpha (cumulative) | -3.425% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 62 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$611.42 |
| Signal saved | -$2737.93 |
| Portfolio value | $97,887.47 |
| Benchmark value | $102,467.55 |
| Alpha (cumulative) | -4.580% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 63 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$644.48 |
| Signal saved | -$2770.99 |
| Portfolio value | $97,887.47 |
| Benchmark value | $102,584.73 |
| Alpha (cumulative) | -4.698% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 64 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$1096.68 |
| Signal saved | -$3223.19 |
| Portfolio value | $97,887.47 |
| Benchmark value | $104,187.57 |
| Alpha (cumulative) | -6.300% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 65 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$1093.64 |
| Signal saved | -$3220.15 |
| Portfolio value | $97,902.26 |
| Benchmark value | $104,176.80 |
| Alpha (cumulative) | -6.275% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 66 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$884.26 |
| Signal saved | -$3010.77 |
| Portfolio value | $97,873.49 |
| Benchmark value | $103,434.64 |
| Alpha (cumulative) | -5.562% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 67 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$859.94 |
| Signal saved | -$2986.45 |
| Portfolio value | $97,873.49 |
| Benchmark value | $103,348.44 |
| Alpha (cumulative) | -5.474% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 68 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $744.660/share |
| Close price | $771.13 |
| Realized P&L (locked) | -$2126.51 |
| Reference if held | +$1005.86 |
| Signal saved | -$3132.37 |
| Portfolio value | $97,873.49 |
| Benchmark value | $103,865.66 |
| Alpha (cumulative) | -5.992% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2126.51. Regime: BULL (MA20 $763.92 vs MA50 $759.46). Fast signal (MA10/MA30): bearish. Monitoring for re-entry on next fast golden cross.

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
_Day 68 of 90 · Alpaca equity: $99,060.25 · Cumulative alpha vs SPY: -5.992%_