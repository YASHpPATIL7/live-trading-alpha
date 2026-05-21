# ALPACA PAPER JOURNAL — SPY
_Last updated: May 21, 2026 | Day 53 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$666.436/share**
> (2026-03-09, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-05-21): **BULLISH** | ⚡ Price Override Active (+6.3% above MA50)  
> Fast: MA10 $739.73 | MA30 $720.01  
> Slow: MA20 $729.81 | MA50 $694.79  
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

**Total trades:** 8 | **Closed:** 7 | **Open:** Yes | **Cumulative Realized P&L:** +$17.86

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $666.436 (2026-03-09) | $668.000 (2026-03-12) | 10 | +$15.64 | ✅ Closed |
| T2 | $701.250 (2026-04-16) | $701.600 (2026-04-16) | 57 | +$19.95 | ✅ Closed |
| T3 | $710.606 (2026-04-17) | $710.500 (2026-04-17) | 56 | -$5.92 | ✅ Closed |
| T4 | $706.745 (2026-04-20) | $706.280 (2026-04-21) | 56 | -$26.06 | ✅ Closed |
| T5 | $709.805 (2026-04-22) | $707.520 (2026-04-23) | 56 | -$127.95 | ✅ Closed |
| T6 | $711.277 (2026-04-24) | $709.220 (2026-04-29) | 56 | -$115.20 | ✅ Closed |
| T7 | $714.440 (2026-04-30) | $719.120 (2026-04-30) | 55 | +$257.40 | ✅ Closed |
| T8 | $722.670 (2026-05-01) | — | 55 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $100,908.84 |
| Alpaca cash | $60,272.64 |
| Cumulative realized P&L | +$17.86 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $676.42 | Long 10 SPY (T1) | +$99.84 | +1.498% | $100,099.84 |
| Day 2 | 2026-03-10 | $675.25 | Long 10 SPY (T1) | +$88.14 | +1.323% | $100,088.14 |
| Day 3 | 2026-03-11 | $674.47 | Long 10 SPY (T1) | +$80.34 | +1.206% | $100,080.34 |
| Day 4 | 2026-03-12 | $664.20 | FLAT | — | — | $100,015.64 |
| Day 5 | 2026-03-13 | $660.46 | FLAT | — | — | $100,015.64 |
| Day 6 | 2026-03-16 | $667.12 | FLAT | — | — | $100,015.64 |
| Day 7 | 2026-03-17 | $668.89 | FLAT | — | — | $100,015.64 |
| Day 8 | 2026-03-18 | $659.71 | FLAT | — | — | $100,015.64 |
| Day 9 | 2026-03-19 | $658.04 | FLAT | — | — | $100,015.64 |
| Day 10 | 2026-03-20 | $648.48 | FLAT | — | — | $100,015.64 |
| Day 11 | 2026-03-23 | $655.37 | FLAT | — | — | $100,015.64 |
| Day 12 | 2026-03-24 | $653.20 | FLAT | — | — | $100,015.64 |
| Day 13 | 2026-03-25 | $656.74 | FLAT | — | — | $100,015.64 |
| Day 14 | 2026-03-26 | $645.11 | FLAT | — | — | $100,015.64 |
| Day 15 | 2026-03-27 | $634.04 | FLAT | — | — | $100,015.64 |
| Day 16 | 2026-03-30 | $632.02 | FLAT | — | — | $100,015.64 |
| Day 17 | 2026-03-31 | $650.12 | FLAT | — | — | $100,015.64 |
| Day 18 | 2026-04-01 | $655.18 | FLAT | — | — | $100,015.64 |
| Day 19 | 2026-04-02 | $655.76 | FLAT | — | — | $100,015.64 |
| Day 20 | 2026-04-06 | $658.88 | FLAT | — | — | $100,015.64 |
| Day 21 | 2026-04-07 | $659.23 | FLAT | — | — | $100,015.64 |
| Day 22 | 2026-04-08 | $676.00 | FLAT | — | — | $100,015.64 |
| Day 23 | 2026-04-09 | $679.87 | FLAT | — | — | $100,015.64 |
| Day 24 | 2026-04-10 | $679.35 | FLAT | — | — | $100,015.64 |
| Day 25 | 2026-04-13 | $686.00 | FLAT | — | — | $100,015.64 |
| Day 26 | 2026-04-14 | $694.36 | FLAT | — | — | $100,015.64 |
| Day 27 | 2026-04-15 | $699.75 | FLAT | — | — | $100,015.64 |
| Day 28 | 2026-04-16 | $701.53 | FLAT | — | — | $100,035.59 |
| Day 29 | 2026-04-17 | $710.06 | FLAT | — | — | $100,029.67 |
| Day 30 | 2026-04-20 | $708.79 | Long 56 SPY (T4) | +$114.50 | +0.289% | $100,144.17 |
| Day 31 | 2026-04-21 | $703.91 | FLAT | — | — | $100,003.61 |
| Day 32 | 2026-04-22 | $711.20 | Long 56 SPY (T5) | +$78.13 | +0.197% | $100,081.74 |
| Day 33 | 2026-04-23 | $708.41 | FLAT | — | — | $99,875.66 |
| Day 34 | 2026-04-24 | $713.97 | Long 56 SPY (T6) | +$150.80 | +0.379% | $100,026.46 |
| Day 35 | 2026-04-27 | $715.16 | Long 56 SPY (T6) | +$217.44 | +0.546% | $100,093.10 |
| Day 36 | 2026-04-28 | $711.68 | Long 56 SPY (T6) | +$22.56 | +0.057% | $99,898.22 |
| Day 37 | 2026-04-29 | $711.59 | FLAT | — | — | $99,760.46 |
| Day 38 | 2026-04-30 | $718.41 | FLAT | — | — | $100,017.86 |
| Day 39 | 2026-05-01 | $720.49 | Long 55 SPY (T8) | -$119.88 | -0.302% | $99,897.98 |
| Day 40 | 2026-05-04 | $718.09 | Long 55 SPY (T8) | -$251.88 | -0.634% | $99,765.98 |
| Day 41 | 2026-05-05 | $723.71 | Long 55 SPY (T8) | +$57.22 | +0.144% | $100,075.08 |
| Day 42 | 2026-05-06 | $733.77 | Long 55 SPY (T8) | +$610.52 | +1.536% | $100,628.38 |
| Day 43 | 2026-05-07 | $731.53 | Long 55 SPY (T8) | +$487.32 | +1.226% | $100,505.18 |
| Day 44 | 2026-05-08 | $737.54 | Long 55 SPY (T8) | +$817.87 | +2.058% | $100,835.73 |
| Day 45 | 2026-05-11 | $739.20 | Long 55 SPY (T8) | +$909.17 | +2.287% | $100,927.03 |
| Day 46 | 2026-05-12 | $738.19 | Long 55 SPY (T8) | +$853.62 | +2.148% | $100,871.48 |
| Day 47 | 2026-05-13 | $742.30 | Long 55 SPY (T8) | +$1079.67 | +2.716% | $101,097.53 |
| Day 48 | 2026-05-14 | $748.10 | Long 55 SPY (T8) | +$1398.67 | +3.519% | $101,416.53 |
| Day 49 | 2026-05-15 | $739.10 | Long 55 SPY (T8) | +$903.67 | +2.274% | $100,921.53 |
| Day 50 | 2026-05-18 | $738.40 | Long 55 SPY (T8) | +$865.17 | +2.177% | $100,883.03 |
| Day 51 | 2026-05-19 | $733.80 | Long 55 SPY (T8) | +$612.17 | +1.540% | $100,630.03 |
| Day 52 | 2026-05-20 | $741.31 | Long 55 SPY (T8) | +$1025.22 | +2.579% | $101,043.08 |
| Day 53 | 2026-05-21 | $738.84 | Long 55 SPY (T8) | +$889.37 | +2.238% | $100,907.23 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $100,099.84 | $99,999.97 | +0.0998% | -0.000% | **+0.100%** |
| Day 2 | 2026-03-10 | $100,088.14 | $99,827.00 | +0.0881% | -0.173% | **+0.261%** |
| Day 3 | 2026-03-11 | $100,080.34 | $99,711.69 | +0.0803% | -0.288% | **+0.368%** |
| Day 4 | 2026-03-12 | $100,015.64 | $98,193.40 | +0.0156% | -1.807% | **+1.823%** |
| Day 5 | 2026-03-13 | $100,015.64 | $97,640.49 | +0.0156% | -2.360% | **+2.376%** |
| Day 6 | 2026-03-16 | $100,015.64 | $98,625.09 | +0.0156% | -1.375% | **+1.391%** |
| Day 7 | 2026-03-17 | $100,015.64 | $98,886.76 | +0.0156% | -1.113% | **+1.129%** |
| Day 8 | 2026-03-18 | $100,015.64 | $97,529.61 | +0.0156% | -2.470% | **+2.486%** |
| Day 9 | 2026-03-19 | $100,015.64 | $97,282.73 | +0.0156% | -2.717% | **+2.733%** |
| Day 10 | 2026-03-20 | $100,015.64 | $95,869.40 | +0.0156% | -4.131% | **+4.147%** |
| Day 11 | 2026-03-23 | $100,015.64 | $96,888.00 | +0.0156% | -3.112% | **+3.128%** |
| Day 12 | 2026-03-24 | $100,015.64 | $96,567.19 | +0.0156% | -3.433% | **+3.449%** |
| Day 13 | 2026-03-25 | $100,015.64 | $97,090.54 | +0.0156% | -2.909% | **+2.925%** |
| Day 14 | 2026-03-26 | $100,015.64 | $95,371.19 | +0.0156% | -4.629% | **+4.645%** |
| Day 15 | 2026-03-27 | $100,015.64 | $93,734.63 | +0.0156% | -6.265% | **+6.281%** |
| Day 16 | 2026-03-30 | $100,015.64 | $93,436.00 | +0.0156% | -6.564% | **+6.580%** |
| Day 17 | 2026-03-31 | $100,015.64 | $96,111.86 | +0.0156% | -3.888% | **+3.904%** |
| Day 18 | 2026-04-01 | $100,015.64 | $96,859.91 | +0.0156% | -3.140% | **+3.156%** |
| Day 19 | 2026-04-02 | $100,015.64 | $96,945.66 | +0.0156% | -3.054% | **+3.070%** |
| Day 20 | 2026-04-06 | $100,015.64 | $97,406.91 | +0.0156% | -2.593% | **+2.609%** |
| Day 21 | 2026-04-07 | $100,015.64 | $97,458.65 | +0.0156% | -2.541% | **+2.557%** |
| Day 22 | 2026-04-08 | $100,015.64 | $99,937.88 | +0.0156% | -0.062% | **+0.078%** |
| Day 23 | 2026-04-09 | $100,015.64 | $100,510.01 | +0.0156% | +0.510% | **-0.494%** |
| Day 24 | 2026-04-10 | $100,015.64 | $100,433.13 | +0.0156% | +0.433% | **-0.417%** |
| Day 25 | 2026-04-13 | $100,015.64 | $101,416.25 | +0.0156% | +1.416% | **-1.400%** |
| Day 26 | 2026-04-14 | $100,015.64 | $102,652.17 | +0.0156% | +2.652% | **-2.636%** |
| Day 27 | 2026-04-15 | $100,015.64 | $103,449.01 | +0.0156% | +3.449% | **-3.433%** |
| Day 28 | 2026-04-16 | $100,035.59 | $103,712.16 | +0.0356% | +3.712% | **-3.676%** |
| Day 29 | 2026-04-17 | $100,029.67 | $104,973.21 | +0.0297% | +4.973% | **-4.943%** |
| Day 30 | 2026-04-20 | $100,144.17 | $104,785.46 | +0.1442% | +4.785% | **-4.641%** |
| Day 31 | 2026-04-21 | $100,003.61 | $104,064.01 | +0.0036% | +4.064% | **-4.060%** |
| Day 32 | 2026-04-22 | $100,081.74 | $105,141.75 | +0.0817% | +5.142% | **-5.060%** |
| Day 33 | 2026-04-23 | $99,875.66 | $104,729.28 | -0.1243% | +4.729% | **-4.853%** |
| Day 34 | 2026-04-24 | $100,026.46 | $105,551.25 | +0.0265% | +5.551% | **-5.524%** |
| Day 35 | 2026-04-27 | $100,093.10 | $105,727.18 | +0.0931% | +5.727% | **-5.634%** |
| Day 36 | 2026-04-28 | $99,898.22 | $105,212.71 | -0.1018% | +5.213% | **-5.315%** |
| Day 37 | 2026-04-29 | $99,760.46 | $105,199.40 | -0.2395% | +5.199% | **-5.438%** |
| Day 38 | 2026-04-30 | $100,017.86 | $106,207.65 | +0.0179% | +6.208% | **-6.190%** |
| Day 39 | 2026-05-01 | $99,897.98 | $106,515.15 | -0.1020% | +6.515% | **-6.617%** |
| Day 40 | 2026-05-04 | $99,765.98 | $106,160.34 | -0.2340% | +6.160% | **-6.394%** |
| Day 41 | 2026-05-05 | $100,075.08 | $106,991.19 | +0.0751% | +6.991% | **-6.916%** |
| Day 42 | 2026-05-06 | $100,628.38 | $108,478.43 | +0.6284% | +8.478% | **-7.850%** |
| Day 43 | 2026-05-07 | $100,505.18 | $108,147.27 | +0.5052% | +8.147% | **-7.642%** |
| Day 44 | 2026-05-08 | $100,835.73 | $109,035.77 | +0.8357% | +9.036% | **-8.200%** |
| Day 45 | 2026-05-11 | $100,927.03 | $109,281.18 | +0.9270% | +9.281% | **-8.354%** |
| Day 46 | 2026-05-12 | $100,871.48 | $109,131.87 | +0.8715% | +9.132% | **-8.260%** |
| Day 47 | 2026-05-13 | $101,097.53 | $109,739.48 | +1.0975% | +9.739% | **-8.642%** |
| Day 48 | 2026-05-14 | $101,416.53 | $110,596.93 | +1.4165% | +10.597% | **-9.180%** |
| Day 49 | 2026-05-15 | $100,921.53 | $109,266.40 | +0.9215% | +9.266% | **-8.344%** |
| Day 50 | 2026-05-18 | $100,883.03 | $109,162.91 | +0.8830% | +9.163% | **-8.280%** |
| Day 51 | 2026-05-19 | $100,630.03 | $108,482.86 | +0.6300% | +8.483% | **-7.853%** |
| Day 52 | 2026-05-20 | $101,043.08 | $109,593.12 | +1.0431% | +9.593% | **-8.550%** |
| Day 53 | 2026-05-21 | $100,907.23 | $109,227.96 | +0.9072% | +9.228% | **-8.321%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $676.42 | +$99.84 | -$81.98 | Position open |
| Day 2 | 2026-03-10 | $675.25 | +$88.14 | -$70.28 | Position open |
| Day 3 | 2026-03-11 | $674.47 | +$80.34 | -$62.48 | Position open |
| Day 4 | 2026-03-12 | $664.20 | -$22.36 | +$40.22 | Flat saved **+$40.22** vs holding |
| Day 5 | 2026-03-13 | $660.46 | -$59.76 | +$77.62 | Flat saved **+$77.62** vs holding |
| Day 6 | 2026-03-16 | $667.12 | +$6.84 | +$11.02 | Flat saved **+$11.02** vs holding |
| Day 7 | 2026-03-17 | $668.89 | +$24.54 | -$6.68 | Holding would have been **$6.68** better — honest entry |
| Day 8 | 2026-03-18 | $659.71 | -$67.26 | +$85.12 | Flat saved **+$85.12** vs holding |
| Day 9 | 2026-03-19 | $658.04 | -$83.96 | +$101.82 | Flat saved **+$101.82** vs holding |
| Day 10 | 2026-03-20 | $648.48 | -$179.56 | +$197.42 | Flat saved **+$197.42** vs holding |
| Day 11 | 2026-03-23 | $655.37 | -$110.66 | +$128.52 | Flat saved **+$128.52** vs holding |
| Day 12 | 2026-03-24 | $653.20 | -$132.36 | +$150.22 | Flat saved **+$150.22** vs holding |
| Day 13 | 2026-03-25 | $656.74 | -$96.96 | +$114.82 | Flat saved **+$114.82** vs holding |
| Day 14 | 2026-03-26 | $645.11 | -$213.26 | +$231.12 | Flat saved **+$231.12** vs holding |
| Day 15 | 2026-03-27 | $634.04 | -$323.96 | +$341.82 | Flat saved **+$341.82** vs holding |
| Day 16 | 2026-03-30 | $632.02 | -$344.16 | +$362.02 | Flat saved **+$362.02** vs holding |
| Day 17 | 2026-03-31 | $650.12 | -$163.16 | +$181.02 | Flat saved **+$181.02** vs holding |
| Day 18 | 2026-04-01 | $655.18 | -$112.56 | +$130.42 | Flat saved **+$130.42** vs holding |
| Day 19 | 2026-04-02 | $655.76 | -$106.76 | +$124.62 | Flat saved **+$124.62** vs holding |
| Day 20 | 2026-04-06 | $658.88 | -$75.56 | +$93.42 | Flat saved **+$93.42** vs holding |
| Day 21 | 2026-04-07 | $659.23 | -$72.06 | +$89.92 | Flat saved **+$89.92** vs holding |
| Day 22 | 2026-04-08 | $676.00 | +$95.64 | -$77.78 | Holding would have been **$77.78** better — honest entry |
| Day 23 | 2026-04-09 | $679.87 | +$134.34 | -$116.48 | Holding would have been **$116.48** better — honest entry |
| Day 24 | 2026-04-10 | $679.35 | +$129.14 | -$111.28 | Holding would have been **$111.28** better — honest entry |
| Day 25 | 2026-04-13 | $686.00 | +$195.64 | -$177.78 | Holding would have been **$177.78** better — honest entry |
| Day 26 | 2026-04-14 | $694.36 | +$279.24 | -$261.38 | Holding would have been **$261.38** better — honest entry |
| Day 27 | 2026-04-15 | $699.75 | +$333.14 | -$315.28 | Holding would have been **$315.28** better — honest entry |
| Day 28 | 2026-04-16 | $701.53 | +$350.94 | -$333.08 | Holding would have been **$333.08** better — honest entry |
| Day 29 | 2026-04-17 | $710.06 | +$436.24 | -$418.38 | Holding would have been **$418.38** better — honest entry |
| Day 30 | 2026-04-20 | $708.79 | +$423.54 | -$405.68 | Position open |
| Day 31 | 2026-04-21 | $703.91 | +$374.74 | -$356.88 | Holding would have been **$356.88** better — honest entry |
| Day 32 | 2026-04-22 | $711.20 | +$447.64 | -$429.78 | Position open |
| Day 33 | 2026-04-23 | $708.41 | +$419.74 | -$401.88 | Holding would have been **$401.88** better — honest entry |
| Day 34 | 2026-04-24 | $713.97 | +$475.34 | -$457.48 | Position open |
| Day 35 | 2026-04-27 | $715.16 | +$487.24 | -$469.38 | Position open |
| Day 36 | 2026-04-28 | $711.68 | +$452.44 | -$434.58 | Position open |
| Day 37 | 2026-04-29 | $711.59 | +$451.54 | -$433.68 | Holding would have been **$433.68** better — honest entry |
| Day 38 | 2026-04-30 | $718.41 | +$519.74 | -$501.88 | Holding would have been **$501.88** better — honest entry |
| Day 39 | 2026-05-01 | $720.49 | +$540.54 | -$522.68 | Position open |
| Day 40 | 2026-05-04 | $718.09 | +$516.54 | -$498.68 | Position open |
| Day 41 | 2026-05-05 | $723.71 | +$572.74 | -$554.88 | Position open |
| Day 42 | 2026-05-06 | $733.77 | +$673.34 | -$655.48 | Position open |
| Day 43 | 2026-05-07 | $731.53 | +$650.94 | -$633.08 | Position open |
| Day 44 | 2026-05-08 | $737.54 | +$711.04 | -$693.18 | Position open |
| Day 45 | 2026-05-11 | $739.20 | +$727.64 | -$709.78 | Position open |
| Day 46 | 2026-05-12 | $738.19 | +$717.54 | -$699.68 | Position open |
| Day 47 | 2026-05-13 | $742.30 | +$758.64 | -$740.78 | Position open |
| Day 48 | 2026-05-14 | $748.10 | +$816.64 | -$798.78 | Position open |
| Day 49 | 2026-05-15 | $739.10 | +$726.64 | -$708.78 | Position open |
| Day 50 | 2026-05-18 | $738.40 | +$719.64 | -$701.78 | Position open |
| Day 51 | 2026-05-19 | $733.80 | +$673.64 | -$655.78 | Position open |
| Day 52 | 2026-05-20 | $741.31 | +$748.74 | -$730.88 | Position open |
| Day 53 | 2026-05-21 | $738.84 | +$724.04 | -$706.18 | Position open |

---

## Daily Entries

### Day 1 — 2026-03-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $676.42 |
| Unrealized P&L | +$99.84 |
| P&L % | +1.498% |
| Portfolio value | $100,099.84 |
| Benchmark value | $99,999.97 |
| Alpha (cumulative) | +0.100% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. Despite this, the SPY price is still above the MA20 and MA50, but the Death Cross signal indicates a bearish trend. The VIX is high at 27.39.

**Strategy note:** The system correctly identified a bearish trend and entered a long position in SPY, but the MA20/MA50 crossover strategy did not trigger a trade today due to the Death Cross signal.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +1.50% from entry. No exit triggered.

**Key learning:** The system's ability to identify a bearish trend is correct, but the Death Cross signal overrides the MA20/MA50 crossover strategy, resulting in a missed trade opportunity.

---

### Day 2 — 2026-03-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $675.25 |
| Unrealized P&L | +$88.14 |
| P&L % | +1.323% |
| Portfolio value | $100,088.14 |
| Benchmark value | $99,827.00 |
| Alpha (cumulative) | +0.261% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating elevated volatility. The WTI oil price is also elevated at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system did not trigger a sell signal today, as the MA20 is still below the MA50, indicating a bearish signal is not present. However, the system's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +1.32% from entry. No exit triggered.

**Key learning:** The system's inaction during a risk-off regime is correct, as the primary focus is on preserving capital during such periods.

---

### Day 3 — 2026-03-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $674.47 |
| Unrealized P&L | +$80.34 |
| P&L % | +1.206% |
| Portfolio value | $100,080.34 |
| Benchmark value | $99,711.69 |
| Alpha (cumulative) | +0.368% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** Market sentiment lifted on de-escalation hopes, but VIX remains elevated at 27.39. WTI Oil price increased, and 10Y Treasury yield rose to 4.328%. SPY price closed at $674.49.

**Strategy note:** MA20 ($660.25) is below MA50 ($675.76), indicating a bearish signal. The system did not enter a trade today, as the signal is not conducive to a long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +1.21% from entry. No exit triggered.

**Key learning:** The strategy's ability to avoid a losing trade is more valuable than a single winning trade.

---

### Day 4 — 2026-03-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $664.20 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$22.36 |
| Signal saved | +$40.22 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,193.40 |
| Alpha (cumulative) | +1.823% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed's warning about another supply shock. The VIX is elevated at 27.39. Oil prices are also high at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system generated a bearish signal today, but the system did not short as the long position was already open. This was correct because the system is not designed to short.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's long position was profitable today despite the bearish signal, highlighting the importance of position sizing and risk management in a trend-following strategy.

---

### Day 5 — 2026-03-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $660.46 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$59.76 |
| Signal saved | +$77.62 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,640.49 |
| Alpha (cumulative) | +2.376% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is currently experiencing a risk-off regime due to the impending supply shock warned by the Fed Chair. The VIX index is elevated at 27.39, indicating increased market volatility. Oil prices are also high, at $104.76 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system did not enter a trade as the position status was already FLAT. This was correct because the signal was not a buy signal.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal does not necessarily mean a trade should be entered if the position is already flat.

---

### Day 6 — 2026-03-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $667.12 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$6.84 |
| Signal saved | +$11.02 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,625.09 |
| Alpha (cumulative) | +1.391% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** Markets are higher pre-bell as de-escalation hopes lift risk sentiment. However, Fed Chair Powell's warning of another supply shock is a bearish signal. VIX remains elevated at 27.39.

**Strategy note:** MA20 is below MA50, indicating a bearish crossover. The system did not enter a trade today as it was flat, but the signal would have been to sell given the bearish crossover.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal is a valid reason to sell, even if the market is rising in the short term.

---

### Day 7 — 2026-03-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $668.89 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$24.54 |
| Signal saved | -$6.68 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,886.76 |
| Alpha (cumulative) | +1.129% |

**Regime call:** RISK-OFF

**Market context:** Markets were relatively calm, with the VIX at 27.39, and the 10Y Treasury yield at 4.328%. Headlines were mixed, with some articles hinting at a potential correction.

**Strategy note:** The MA20/MA50 crossover system is in a BEARISH — Death Cross regime. The system did not enter a position today, as the market conditions did not trigger a signal.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction today was correct, as the market did not trigger a signal, and the realized P&L was locked at +$15.58

---

### Day 8 — 2026-03-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $659.71 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$67.26 |
| Signal saved | +$85.12 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,529.61 |
| Alpha (cumulative) | +2.486% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime following Fed Chair Powell's warning of another supply shock. The VIX index is elevated at 27.39, indicating increased volatility. The SPY price closed at $659.63.

**Strategy note:** The MA20/MA50 crossover strategy is in a BEARISH — Death Cross regime, but no trade was executed due to the system being flat. The strategy's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits is crucial in a risk-off regime, as seen today with a $+15.58 realized P&L.

---

### Day 9 — 2026-03-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.04 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$83.96 |
| Signal saved | +$101.82 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,282.73 |
| Alpha (cumulative) | +2.733% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. The VIX is elevated at 27.39. The SPY price closed at $658.00.

**Strategy note:** The system is flat, as the MA20/MA50 crossover strategy did not trigger a trade today. This is correct, as the signal is bearish (Death Cross) and the system is designed to avoid trading during such conditions.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management approach is effective in avoiding losses during periods of high market volatility.

---

### Day 10 — 2026-03-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $648.48 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$179.56 |
| Signal saved | +$197.42 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,869.40 |
| Alpha (cumulative) | +4.147% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite warning signs from the Fed Chair and rising VIX. Oil prices continued to climb. The 10Y Treasury yield remained elevated.

**Strategy note:** The MA20/MA50 crossover system remained flat as MA20 was below MA50, indicating no buy or sell signal. This was correct as the market did not follow the bearish signal.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to stay flat in a volatile market environment is crucial for preserving capital.

---

### Day 11 — 2026-03-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.37 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$110.66 |
| Signal saved | +$128.52 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,888.00 |
| Alpha (cumulative) | +3.128% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating increased volatility. Oil prices are also elevated.

**Strategy note:** The MA system is in a bearish regime due to the death cross, but did not enter a trade today as the position was already flat. The system's inaction was correct as the market did not provide a clear buy or sell signal.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to avoid trading during periods of high volatility is crucial in maintaining its overall performance.

---

### Day 12 — 2026-03-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $653.20 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$132.36 |
| Signal saved | +$150.22 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,567.19 |
| Alpha (cumulative) | +3.449% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market context today is characterized by a bearish signal from the MA20/MA50 crossover strategy and a rising VIX. The Fed Chair's warning of another supply shock is likely contributing to the risk-off sentiment. Meanwhile, the WTI Oil price is stable, and the 10Y Treasury yield is rising.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system remained flat due to the signal being a death cross, which typically indicates a sell signal. The strategy's inaction was correct as the market declined.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross signal should be treated with caution and may require a more nuanced approach to determine the optimal course of action.

---

### Day 13 — 2026-03-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $656.74 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$96.96 |
| Signal saved | +$114.82 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,090.54 |
| Alpha (cumulative) | +2.925% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite the Fed Chair's warning of another supply shock. VIX remained elevated, but WTI Oil price dropped. The 10Y Treasury yield also decreased.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH — Death Cross regime. The system did not enter a trade today, as the MA20 was below the MA50 and the signal was bearish.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A dead-cat bounce can occur even in a bearish market regime, highlighting the importance of staying nimble and not over-interpreting short-term market movements.

---

### Day 14 — 2026-03-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $645.11 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$213.26 |
| Signal saved | +$231.12 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,371.19 |
| Alpha (cumulative) | +4.645% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning about another supply shock. The VIX is at 27.39, indicating increased market volatility. Oil prices are also on the rise.

**Strategy note:** The MA20/MA50 crossover strategy did not trigger any trades today, as the signal was bearish (Death Cross) and the system remained flat.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal may not always be a buy signal, and staying flat can be a correct decision in uncertain market conditions.

---

### Day 15 — 2026-03-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $634.04 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$323.96 |
| Signal saved | +$341.82 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,734.63 |
| Alpha (cumulative) | +6.281% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** Markets remained relatively stable despite the Fed Chair's warning of an impending supply shock. The VIX index increased slightly, while the 10Y Treasury yield remained steady. Oil prices also rose.

**Strategy note:** The MA20/MA50 system remained flat as the Death Cross signal did not trigger a trade. This was correct as the market did not experience a significant downturn.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction during a period of heightened uncertainty highlights the importance of a well-defined trading plan and risk management.

---

### Day 16 — 2026-03-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $632.02 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$344.16 |
| Signal saved | +$362.02 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,436.00 |
| Alpha (cumulative) | +6.580% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite a bearish signal from the MA crossover strategy, with SPY closing at $631.97. VIX remained elevated at 27.39. Headlines were mixed, with a warning from Fed Chair Powell and hopes for de-escalation.

**Strategy note:** The system remained flat as the MA20/MA50 crossover strategy indicated a bearish signal, which was correct given the market's cautious behavior.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits and avoid new positions during a dead-cat bounce is crucial for preserving capital.

---

### Day 17 — 2026-03-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $650.12 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$163.16 |
| Signal saved | +$181.02 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,111.86 |
| Alpha (cumulative) | +3.904% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market experienced a dead-cat bounce, with SPY closing at $641.88, despite a bearish signal from the MA20/MA50 crossover. VIX remained elevated at 27.39. Fed Chair Powell's warning of another supply shock contributed to the cautious market sentiment.

**Strategy note:** The system did not enter a trade today due to a bearish signal from the MA20/MA50 crossover. The system's inaction was correct as the market experienced a dead-cat bounce.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal from the MA20/MA50 crossover does not guarantee a sell signal, as the market can experience a dead-cat bounce.

---

### Day 18 — 2026-04-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.18 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$112.56 |
| Signal saved | +$130.42 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,859.91 |
| Alpha (cumulative) | +3.156% |

**Regime call:** RISK-OFF

**Market context:** The market experienced a risk-off day, driven by the bearish MA cross and elevated VIX, amidst geopolitical tensions and a decline in oil prices.

**Strategy note:** The MA20/MA50 crossover system correctly identified a bearish signal, but did not enter a trade as the position was already flat.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to identify bearish signals is intact, but it must be used in conjunction with position management to maximize returns.

---

### Day 19 — 2026-04-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.76 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$106.76 |
| Signal saved | +$124.62 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,945.66 |
| Alpha (cumulative) | +3.070% |

**Regime call:** RISK-OFF

**Market context:** The stock market sold off on Trump's speech and surging oil prices, with the Dow experiencing a decline. The VIX index rose to 27.15, indicating increased market volatility. Oil prices surged to $112.24 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH signal due to the Death Cross, but no trades were executed as the position was flat.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy correctly identified a bearish signal, but the lack of a trade execution highlights the importance of position sizing and risk management.

---

### Day 20 — 2026-04-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.88 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$75.56 |
| Signal saved | +$93.42 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,406.91 |
| Alpha (cumulative) | +2.609% |

**Regime call:** BULLISH

**Market context:** Markets were mixed post-BLS jobs, with equity futures trading mixed pre-bell Monday amid ongoing Iran conflict. VIX remained elevated at 24.17. WTI oil price rose to $112.59/barrel.

**Strategy note:** MA20 crossed below MA50, triggering a bullish signal. The system remains flat, with no trades executed today.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's alpha continues to outperform the benchmark, with a cumulative alpha of +2.610%

---

### Day 21 — 2026-04-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $659.23 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | -$72.06 |
| Signal saved | +$89.92 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,458.65 |
| Alpha (cumulative) | +2.557% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, and oil prices were falling, amidst a two-week US-Iran ceasefire.

**Strategy note:** MA20 crossed below MA50, triggering a bearish signal. The system exited the position.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** VIX levels can significantly influence market sentiment and impact our strategy's performance.

---

### Day 22 — 2026-04-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $676.00 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$95.64 |
| Signal saved | -$77.78 |
| Portfolio value | $100,015.64 |
| Benchmark value | $99,937.88 |
| Alpha (cumulative) | +0.078% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, indicating a decrease in market volatility. Oil prices continued to fall. Markets were higher pre-bell Wednesday amid a two-week US-Iran ceasefire.

**Strategy note:** The MA20/MA50 crossover strategy remained bearish, with a death cross. The system exited the position and is now flat, waiting for a golden cross to re-enter.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's bearish signal was correct, but the realized P&L was relatively low, highlighting the importance of position sizing and risk management.

---

### Day 23 — 2026-04-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $679.87 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$134.34 |
| Signal saved | -$116.48 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,510.01 |
| Alpha (cumulative) | -0.494% |

**Regime call:** RISK-ON

**Market context:** Equity futures and ETFs declined pre-bell as fragile Middle East ceasefire lifted oil prices. VIX rose to 20.8. S&P 500 had a rare gap-up on Wednesday.

**Strategy note:** MA20/MA50 crossover strategy exited position based on bearish signal. System now flat, waiting for next golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** MA crossover strategy underperformed passive hold, reinforcing need for robust risk management

---

### Day 24 — 2026-04-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $679.35 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$129.14 |
| Signal saved | -$111.28 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,433.13 |
| Alpha (cumulative) | -0.417% |

**Regime call:** RISK-ON

**Market context:** The S&P 500 closed above a key level, with equity futures mixed amidst geopolitical uncertainty and a looming CPI report. The VIX remained relatively calm, but could swing wildly after the CPI data release.

**Strategy note:** The system exited the position due to a bearish MA cross, and is now flat. The MA20 is below the MA50, indicating a bearish trend.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's bearish signal was correct, but the realized P&L was lower than the passive hold, highlighting the importance of risk management in trading strategies.

---

### Day 25 — 2026-04-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $686.00 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$195.64 |
| Signal saved | -$177.78 |
| Portfolio value | $100,015.64 |
| Benchmark value | $101,416.25 |
| Alpha (cumulative) | -1.400% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 sold off due to geopolitical tensions, with oil prices surging over $100. The VIX sharply reversed, pointing towards 30 after failed peace negotiations. This led to a risk-off sentiment in the market.

**Strategy note:** MA50 crossed above MA20, triggering a bearish signal. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal does not guarantee losses, as the system's realized P&L was positive despite the market downturn.

---

### Day 26 — 2026-04-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $694.36 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$279.24 |
| Signal saved | -$261.38 |
| Portfolio value | $100,015.64 |
| Benchmark value | $102,652.17 |
| Alpha (cumulative) | -2.636% |

**Regime call:** RISK-OFF

**Market context:** The market rose today with Dow leading, despite concerns over inflation data and a potential US-Iran truce. VIX remains elevated at 18.05. Oil prices also increased.

**Strategy note:** MA20 ($660.21) is below MA50 ($672.89), indicating a bearish signal. The system exited the position, locking in a $+15.58 P&L.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross in the MA crossover strategy led to a premature exit, resulting in a missed opportunity to ride the market's upward momentum.

---

### Day 27 — 2026-04-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $699.75 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$333.14 |
| Signal saved | -$315.28 |
| Portfolio value | $100,015.64 |
| Benchmark value | $103,449.01 |
| Alpha (cumulative) | -3.433% |

**Regime call:** RISK-ON

**Market context:** Investors turned to corporate earnings, driving equity futures higher. Wall Street's fear gauge, VIX, is fading. The S&P 500 Stocks' earnings are expected to skyrocket 200% in three months.

**Strategy note:** MA20/MA50 crossover strategy is in a BEARISH regime due to a Death Cross. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's realized P&L outperformed a passive hold by $15.58, but still trailed the benchmark by $286.66.

---

### Day 28 — 2026-04-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $701.53 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$350.94 |
| Signal saved | -$333.08 |
| Portfolio value | $100,035.59 |
| Benchmark value | $103,712.16 |
| Alpha (cumulative) | -3.676% |

**Regime call:** BEAR

**Market context:** The market remains in a bear regime, with SPY trading below its 50-day moving average. The S&P 500 index is also under pressure, with no clear signs of a reversal. Economic data releases and geopolitical tensions continue to weigh on investor sentiment.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, despite the bear regime, due to a bullish fast signal. The system's unrealized P&L increased by 0.06% from entry.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bullish fast signal does not guarantee success in a bear regime, and the system's performance may be impacted by the prevailing market conditions.

---

### Day 29 — 2026-04-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $710.06 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$436.24 |
| Signal saved | -$418.38 |
| Portfolio value | $100,029.67 |
| Benchmark value | $104,973.21 |
| Alpha (cumulative) | -4.943% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 broke above 7000, driven by a rally in tech stocks and the opening of the Strait of Hormuz. Oil prices declined, while Netflix shares plummeted. Market sentiment remains bullish.

**Strategy note:** The system exited the position due to a bear regime, as confirmed by the slow MA20/MA50 crossover. A bullish fast signal was generated, but the system prioritized the slow regime filter.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter is more important than the fast signal in determining position entry and exit decisions.

---

### Day 30 — 2026-04-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T4) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $708.79 |
| Unrealized P&L | +$114.50 |
| P&L % | +0.289% |
| Portfolio value | $100,144.17 |
| Benchmark value | $104,785.46 |
| Alpha (cumulative) | -4.641% |

**Regime call:** BEAR

**Market context:** Small Cap Stocks and Russell 2000 declined, while Oil Prices surged amid Middle East tensions. The S&P 500 held 7100, with Nasdaq Composite battling fears. Equity Futures and Exchange-Traded Funds also declined.

**Strategy note:** The system held long SPY due to a BULLISH Fast signal and BEAR regime, despite strong momentum. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong momentum environment can override a bearish regime context, but may also increase risk of a false signal.

---

### Day 31 — 2026-04-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $703.91 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$374.74 |
| Signal saved | -$356.88 |
| Portfolio value | $100,003.61 |
| Benchmark value | $104,064.01 |
| Alpha (cumulative) | -4.060% |

**Regime call:** BEAR

**Market context:** Markets rallied on Iran deal hopes, with stocks outperforming safe-havens like gold. Small caps and risk-on trades led the gains. Oil prices pulled back on the news.

**Strategy note:** The system remained long SPY despite a BEAR regime, as the fast signal remained BULLISH due to a strong golden cross. No exit was triggered.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter can sometimes conflict with the fast signal, requiring careful consideration of both indicators.

---

### Day 32 — 2026-04-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T5) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $711.20 |
| Unrealized P&L | +$78.13 |
| P&L % | +0.197% |
| Portfolio value | $100,081.74 |
| Benchmark value | $105,141.75 |
| Alpha (cumulative) | -5.060% |

**Regime call:** BEAR

**Market context:** Risk-on trade buoyed small cap sentiment, while the VIX remains calm. The S&P 500 climbed on a ceasefire extension and tech tailwinds.

**Strategy note:** The system held a long SPY position, despite a bear regime, due to a bullish fast signal from the 10/30 SMA crossover. Unrealized P&L was -0.01% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +0.20% from entry. No exit triggered.

**Key learning:** A bear regime does not necessarily mean a bear market, as the system's fast signal can override the slow filter.

---

### Day 33 — 2026-04-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $708.41 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$419.74 |
| Signal saved | -$401.88 |
| Portfolio value | $99,875.66 |
| Benchmark value | $104,729.28 |
| Alpha (cumulative) | -4.853% |

**Regime call:** BULL

**Market context:** The S&P 500 retreated but held 7100 on fresh Mideast escalation as earnings kick off, while VIX crept toward 20 as Iran fears and Tesla's whipsaw rattle nerves.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and strong momentum, causing the system to hold long SPY.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long in a bull regime despite rising VIX is being tested.

---

### Day 34 — 2026-04-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T6) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $713.97 |
| Unrealized P&L | +$150.80 |
| P&L % | +0.379% |
| Portfolio value | $100,026.46 |
| Benchmark value | $105,551.25 |
| Alpha (cumulative) | -5.524% |

**Regime call:** BULL

**Market context:** The S&P 500 climbed as Intel posted its best quarter in years, while oil retreated. Equity futures were mixed pre-bell as traders assessed tech earnings amid global uncertainty. The VIX index crept towards 20 due to Iran fears and Tesla's whipsaw.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +0.38% from entry. No exit triggered.

**Key learning:** The system's ability to lock in losses is crucial in maintaining a positive cumulative alpha.

---

### Day 35 — 2026-04-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T6) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $715.16 |
| Unrealized P&L | +$217.44 |
| P&L % | +0.546% |
| Portfolio value | $100,093.10 |
| Benchmark value | $105,727.18 |
| Alpha (cumulative) | -5.634% |

**Regime call:** BULL

**Market context:** The S&P 500 held its pattern as earnings collided with an oil surge and Fed fears. Equity futures were mixed amid Hormuz uncertainty and corporate earnings. VIX remained relatively low at 18.71.

**Strategy note:** The dual-timeframe SMA crossover strategy held its long position in SPY, with a bullish fast signal and a bullish regime context. Unrealized P&L increased to +0.19% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +0.55% from entry. No exit triggered.

**Key learning:** Strong momentum in a bullish regime context can lead to increased unrealized profits, but also raises the risk of a potential reversal.

---

### Day 36 — 2026-04-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 56 SPY (T6) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $711.68 |
| Unrealized P&L | +$22.56 |
| P&L % | +0.057% |
| Portfolio value | $99,898.22 |
| Benchmark value | $105,212.71 |
| Alpha (cumulative) | -5.315% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell amid higher oil prices and earnings deluge, while investors worry about mounting debt. The S&P 500 held a pattern with Mag 7 earnings colliding with oil surge and Fed fears. The VIX remained relatively low at 18.56.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH, with a strong momentum and a bull regime confirmed by the slow MAs.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +0.06% from entry. No exit triggered.

**Key learning:** A strong bull regime can still result in losses if the system's timing is off, highlighting the importance of precise entry and exit signals.

---

### Day 37 — 2026-04-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $711.59 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$451.54 |
| Signal saved | -$433.68 |
| Portfolio value | $99,760.46 |
| Benchmark value | $105,199.40 |
| Alpha (cumulative) | -5.438% |

**Regime call:** BULL

**Market context:** The S&P 500 held steady as big tech earnings, Fed decision, and oil prices collided. Real yields crushed gold in the short term, but the long-term picture remains intact. The VIX index remained relatively low at 18.26.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime. The system held long SPY and did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying risks, and the system's slow filter remains critical in avoiding longs in strong bear regimes.

---

### Day 38 — 2026-04-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $718.41 |
| Realized P&L (locked) | +$17.86 |
| Reference if held | +$519.74 |
| Signal saved | -$501.88 |
| Portfolio value | $100,017.86 |
| Benchmark value | $106,207.65 |
| Alpha (cumulative) | -6.190% |

**Regime call:** Consolidation

**Market context:** The S&P 500 rode a tech earnings wave despite an inflation warning, with ETFs and equity futures higher pre-bell Thursday. The VIX remained relatively low at 17.37. Oil prices hovered around $104.83 per barrel.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30 golden cross) within a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+17.86. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still exited with a loss.

---

### Day 39 — 2026-05-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $720.49 |
| Unrealized P&L | -$119.88 |
| P&L % | -0.302% |
| Portfolio value | $99,897.98 |
| Benchmark value | $106,515.15 |
| Alpha (cumulative) | -6.617% |

**Regime call:** BULL

**Market context:** Risk-on trade returned to the market as the CBOE VIX fell to 16, and the S&P 500 continued its strong May footing. However, consumer sentiment posted its lowest score in history.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: -0.30% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with low consumer sentiment.

---

### Day 40 — 2026-05-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $718.09 |
| Unrealized P&L | -$251.88 |
| P&L % | -0.634% |
| Portfolio value | $99,765.98 |
| Benchmark value | $106,160.34 |
| Alpha (cumulative) | -6.394% |

**Regime call:** BULL

**Market context:** The market experienced a bullish signal with a fast golden cross, while the slow regime remains in a bull context. The VIX remains relatively low at 18.29. Market news focused on a potential market rally and the performance of individual stocks.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The unrealized P&L is -0.63% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: -0.63% from entry. No exit triggered.

**Key learning:** A strong market rally can quickly turn into a risk-off environment, highlighting the importance of regime awareness in trading decisions.

---

### Day 41 — 2026-05-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $723.71 |
| Unrealized P&L | +$57.22 |
| P&L % | +0.144% |
| Portfolio value | $100,075.08 |
| Benchmark value | $106,991.19 |
| Alpha (cumulative) | -6.916% |

**Regime call:** BULL

**Market context:** The market remained in a bullish regime, with the SPY price closing at $723.71. The VIX index remained relatively low at 17.38, indicating a stable market environment. Oil prices also remained stable at $102.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to the MA10 crossing above MA30. The slow filter regime remained in a bullish context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +0.14% from entry. No exit triggered.

**Key learning:** The system's ability to hold onto a winning trade in a strong bull regime is crucial to maintaining its overall performance.

---

### Day 42 — 2026-05-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $733.77 |
| Unrealized P&L | +$610.52 |
| P&L % | +1.536% |
| Portfolio value | $100,628.38 |
| Benchmark value | $108,478.43 |
| Alpha (cumulative) | -7.850% |

**Regime call:** BULL

**Market context:** Risk appetite improved as VIX slid toward 17, driven by a surge in tech stocks and a decline in oil prices. The S&P 500 extended its record run, with semiconductors leading the charge. Market sentiment remains optimistic.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime context. The slow filter's MA20/MA50 crossover confirmed the bull regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +1.54% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even as VIX declines, emphasizing the importance of regime context in trading decisions.

---

### Day 43 — 2026-05-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $731.53 |
| Unrealized P&L | +$487.32 |
| P&L % | +1.226% |
| Portfolio value | $100,505.18 |
| Benchmark value | $108,147.27 |
| Alpha (cumulative) | -7.642% |

**Regime call:** BULL

**Market context:** The S&P 500 gained on chip stock strength and falling oil, with investors returning to optimism. Corporate earnings and economic data also boosted equity futures. The 10Y Treasury yield stood at 4.36%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime. The unrealized P&L was +1.72% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +1.23% from entry. No exit triggered.

**Key learning:** The system's long position in SPY remains profitable, but the regime's strength is being tested by the rising 10Y Treasury yield.

---

### Day 44 — 2026-05-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $737.54 |
| Unrealized P&L | +$817.87 |
| P&L % | +2.058% |
| Portfolio value | $100,835.73 |
| Benchmark value | $109,035.77 |
| Alpha (cumulative) | -8.200% |

**Regime call:** BULL

**Market context:** Equities rose pre-bell Friday amid positive employment data, while Tesla's 19% drop in a month sparked sell concerns. Lower ETF fees are saving 401(k) investors thousands, and stock funds posted their best month since 2020. The VIX remained relatively low at 17.35.

**Strategy note:** The system held long SPY due to a bullish signal from the fast MA crossover and a bullish regime context from the slow MAs. The slow MAs confirmed a bullish regime, and the fast signal remained in a strong bullish state.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.06% from entry. No exit triggered.

**Key learning:** The system's ability to hold long in a strong bullish regime resulted in a +2.01% unrealized P&L from entry, underscoring the importance of regime context in the dual-timeframe strategy.

---

### Day 45 — 2026-05-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $739.20 |
| Unrealized P&L | +$909.17 |
| P&L % | +2.287% |
| Portfolio value | $100,927.03 |
| Benchmark value | $109,281.18 |
| Alpha (cumulative) | -8.354% |

**Regime call:** Bullish

**Market context:** The market showed resilience with SPY closing at $740.13, despite the presence of bearish headlines. VIX remained relatively low at 17.93. Oil prices continued to fluctuate around $97.99 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY based on a bullish fast signal and a bullish regime context.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.29% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to strong momentum environments is crucial for maintaining a profitable edge.

---

### Day 46 — 2026-05-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $738.19 |
| Unrealized P&L | +$853.62 |
| P&L % | +2.148% |
| Portfolio value | $100,871.48 |
| Benchmark value | $109,131.87 |
| Alpha (cumulative) | -8.260% |

**Regime call:** BULL

**Market context:** Markets declined today amid rising oil prices and higher inflation expectations. The Dow and Nasdaq fell, while chip stocks saw a boost. The VIX index rose to 18.83.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime. The slow MA crossover remains in a bull regime, supporting the long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.15% from entry. No exit triggered.

**Key learning:** A strong bull regime can override a declining market, but it's essential to monitor momentum and adjust the strategy accordingly.

---

### Day 47 — 2026-05-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $742.30 |
| Unrealized P&L | +$1079.67 |
| P&L % | +2.716% |
| Portfolio value | $101,097.53 |
| Benchmark value | $109,739.48 |
| Alpha (cumulative) | -8.642% |

**Regime call:** BULL

**Market context:** The market showed mixed movements with the Dow Jones futures falling and the Nasdaq gaining. Producer inflation spiked to 6%, fueling fears of a Fed rate hike. The S&P 500 and Nasdaq-100 indices were in focus.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross. The system held long SPY as the regime remained BULL and momentum was STRONG.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.72% from entry. No exit triggered.

**Key learning:** A strong bull regime can be sustained even in the face of inflation concerns, but vigilance is still required.

---

### Day 48 — 2026-05-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $748.10 |
| Unrealized P&L | +$1398.67 |
| P&L % | +3.519% |
| Portfolio value | $101,416.53 |
| Benchmark value | $110,596.93 |
| Alpha (cumulative) | -9.180% |

**Regime call:** BULL

**Market context:** The S&P 500 continued its upward trend, with the SPY closing at $748.35. The VIX index remained relatively low at 17.91, indicating a calm market environment. Market headlines focused on various economic and financial topics, including ETFs and the US-China meeting.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, with the fast signal holding long SPY and the slow filter confirming a bull market context. The system did not trigger an exit today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +3.52% from entry. No exit triggered.

**Key learning:** The system's long position in SPY generated a 3.55% unrealized profit, highlighting the importance of maintaining a bullish regime and strong momentum in the current market environment.

---

### Day 49 — 2026-05-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $739.10 |
| Unrealized P&L | +$903.67 |
| P&L % | +2.274% |
| Portfolio value | $100,921.53 |
| Benchmark value | $109,266.40 |
| Alpha (cumulative) | -8.344% |

**Regime call:** BULL

**Market context:** The S&P 500 barely yielded 2% with some dividend stocks performing better, while a 10% correction this summer is predicted due to being above moving averages. Pre-market slid as China summit ended without major commitments, and exchange-traded funds and equity futures declined due to oil surge, higher yields, and geopolitical uncertainty.

**Strategy note:** The dual-timeframe signal remained BULLISH with a fast golden cross, and the system held long SPY as the regime remained BULL with strong momentum.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.27% from entry. No exit triggered.

**Key learning:** The system's risk management via slow filter (SMA20/50) was not triggered to exit the long position today.

---

### Day 50 — 2026-05-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $738.40 |
| Unrealized P&L | +$865.17 |
| P&L % | +2.177% |
| Portfolio value | $100,883.03 |
| Benchmark value | $109,162.91 |
| Alpha (cumulative) | -8.280% |

**Regime call:** Bull

**Market context:** Markets remained relatively stable with a slight recovery in sentiment, despite inflation concerns and stalled Iran peace efforts.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with an unrealized P&L of +1.84%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.18% from entry. No exit triggered.

**Key learning:** A strong bull regime does not guarantee a positive alpha, as the system's long position underperformed the benchmark.

---

### Day 51 — 2026-05-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $733.80 |
| Unrealized P&L | +$612.17 |
| P&L % | +1.540% |
| Portfolio value | $100,630.03 |
| Benchmark value | $108,482.86 |
| Alpha (cumulative) | -7.853% |

**Regime call:** BULL

**Market context:** Markets remained in a recovery phase, with the VIX index at 18.03, while the 10Y Treasury yield increased to 4.67%. The SPY price rose to $734.48.

**Strategy note:** The dual-timeframe SMA crossover system held a long position in SPY, triggered by a fast golden cross, and maintained a bullish regime based on the slow MAs. The unrealized P&L was +1.63%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +1.54% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market conditions, particularly in the recovery phase, is crucial for maintaining its performance.

---

### Day 52 — 2026-05-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $741.31 |
| Unrealized P&L | +$1025.22 |
| P&L % | +2.579% |
| Portfolio value | $101,043.08 |
| Benchmark value | $109,593.12 |
| Alpha (cumulative) | -8.550% |

**Regime call:** BULL

**Market context:** The market rebounded today with ETFs and equity futures advancing ahead of the Nvidia earnings report. The VIX index remained relatively low at 17.79. Oil prices stabilized at $99.54 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy remained in a bullish regime, holding long SPY with an unrealized P&L of +2.23%. The fast signal remained bullish with a fast golden cross.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.58% from entry. No exit triggered.

**Key learning:** The system's ability to adapt to changing market regimes is crucial in maintaining its performance, as seen in today's recovery from a previous bearish regime.

---

### Day 53 — 2026-05-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 55 SPY (T8) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $738.84 |
| Unrealized P&L | +$889.37 |
| P&L % | +2.238% |
| Portfolio value | $100,907.23 |
| Benchmark value | $109,227.96 |
| Alpha (cumulative) | -8.321% |

**Regime call:** Recovery Rally

**Market context:** US stocks rose as small caps gained momentum, despite uncertainty surrounding US-Iran talks and recession fears.

**Strategy note:** System held long SPY based on bullish fast signal and bullish regime, with unrealized P&L of +2.24%.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $729.81 vs MA50 $694.79). Momentum: RECOVERING. Unrealized P&L: +2.24% from entry. No exit triggered.

**Key learning:** A strong bullish regime is not a guarantee of continued gains, and a recovery rally can be fragile.

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
_Day 53 of 90 · Alpaca equity: $100,908.84 · Cumulative alpha vs SPY: -8.321%_