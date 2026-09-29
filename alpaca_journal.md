# ALPACA PAPER JOURNAL — SPY
_Last updated: September 29, 2026 | Day 56 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$751.280/share**
> (2026-07-13, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-09-29): **BULLISH**  
> Fast: MA10 $764.89 | MA30 $764.44  
> Slow: MA20 $763.93 | MA50 $760.39  
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

**Total trades:** 18 | **Closed:** 17 | **Open:** Yes | **Cumulative Realized P&L:** -$2125.75

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $751.280 (2026-07-13) | $748.240 (2026-07-13) | 53 | -$161.12 | ✅ Closed |
| T2 | $752.632 (2026-07-14) | $751.970 (2026-07-14) | 53 | -$35.08 | ✅ Closed |
| T3 | $753.599 (2026-07-15) | $754.500 (2026-07-15) | 53 | +$47.75 | ✅ Closed |
| T4 | $753.323 (2026-07-16) | $750.000 (2026-07-16) | 53 | -$176.13 | ✅ Closed |
| T5 | $745.500 (2026-07-17) | $742.860 (2026-07-17) | 54 | -$142.56 | ✅ Closed |
| T6 | $745.455 (2026-07-20) | $741.900 (2026-07-20) | 54 | -$191.98 | ✅ Closed |
| T7 | $747.620 (2026-07-21) | $735.630 (2026-07-23) | 53 | -$635.47 | ✅ Closed |
| T8 | $738.840 (2026-07-23) | $739.000 (2026-07-24) | 52 | +$8.32 | ✅ Closed |
| T9 | $737.421 (2026-07-27) | $739.350 (2026-07-27) | 54 | +$104.14 | ✅ Closed |
| T10 | $741.850 (2026-07-28) | $741.030 (2026-07-28) | 53 | -$43.46 | ✅ Closed |
| T11 | $772.150 (2026-08-04) | $770.410 (2026-08-05) | 50 | -$87.00 | ✅ Closed |
| T12 | $772.510 (2026-08-07) | $773.000 (2026-08-10) | 51 | +$24.98 | ✅ Closed |
| T13 | $773.641 (2026-08-11) | $761.630 (2026-09-01) | 51 | -$612.58 | ✅ Closed |
| T14 | $764.920 (2026-09-02) | $765.950 (2026-09-08) | 51 | +$52.53 | ✅ Closed |
| T15 | $762.999 (2026-09-09) | $757.920 (2026-09-10) | 52 | -$264.11 | ✅ Closed |
| T16 | $773.250 (2026-09-22) | $773.540 (2026-09-22) | 51 | +$14.79 | ✅ Closed |
| T17 | $768.534 (2026-09-23) | $767.970 (2026-09-23) | 51 | -$28.77 | ✅ Closed |
| T18 | $765.350 (2026-09-28) | — | 51 | — | 🟢 Open |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,017.42 |
| Alpaca cash | $60,027.40 |
| Cumulative realized P&L | -$2125.75 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-13 | $747.27 | FLAT | — | — | $99,838.88 |
| Day 2 | 2026-07-14 | $750.08 | FLAT | — | — | $99,803.80 |
| Day 3 | 2026-07-15 | $752.90 | FLAT | — | — | $99,851.55 |
| Day 4 | 2026-07-16 | $749.01 | FLAT | — | — | $99,675.42 |
| Day 5 | 2026-07-17 | $741.44 | FLAT | — | — | $99,532.86 |
| Day 6 | 2026-07-20 | $740.31 | FLAT | — | — | $99,340.88 |
| Day 7 | 2026-07-21 | $746.30 | Long 53 SPY (T7) | -$69.96 | -0.177% | $99,270.92 |
| Day 8 | 2026-07-22 | $745.64 | Long 53 SPY (T7) | -$104.94 | -0.265% | $99,235.94 |
| Day 9 | 2026-07-23 | $736.23 | Long 52 SPY (T8) | -$135.72 | -0.353% | $98,569.69 |
| Day 10 | 2026-07-24 | $737.07 | FLAT | — | — | $98,713.73 |
| Day 11 | 2026-07-27 | $737.02 | FLAT | — | — | $98,817.87 |
| Day 12 | 2026-07-28 | $738.96 | FLAT | — | — | $98,774.41 |
| Day 13 | 2026-07-29 | $727.76 | FLAT | — | — | $98,774.41 |
| Day 14 | 2026-07-30 | $739.79 | FLAT | — | — | $98,774.41 |
| Day 15 | 2026-07-31 | $744.94 | FLAT | — | — | $98,774.41 |
| Day 16 | 2026-08-03 | $755.84 | FLAT | — | — | $98,774.41 |
| Day 17 | 2026-08-04 | $769.20 | Long 50 SPY (T11) | -$147.50 | -0.382% | $98,626.91 |
| Day 18 | 2026-08-05 | $767.88 | FLAT | — | — | $98,687.41 |
| Day 19 | 2026-08-06 | $766.74 | FLAT | — | — | $98,687.41 |
| Day 20 | 2026-08-07 | $771.25 | Long 51 SPY (T12) | -$64.27 | -0.163% | $98,623.14 |
| Day 21 | 2026-08-10 | $771.11 | FLAT | — | — | $98,712.39 |
| Day 22 | 2026-08-11 | $768.61 | Long 51 SPY (T13) | -$256.60 | -0.650% | $98,455.79 |
| Day 23 | 2026-08-12 | $770.63 | Long 51 SPY (T13) | -$153.58 | -0.389% | $98,558.81 |
| Day 24 | 2026-08-13 | $775.91 | Long 51 SPY (T13) | +$115.70 | +0.293% | $98,828.09 |
| Day 25 | 2026-08-14 | $774.38 | Long 51 SPY (T13) | +$37.67 | +0.095% | $98,750.06 |
| Day 26 | 2026-08-17 | $770.71 | Long 51 SPY (T13) | -$149.50 | -0.379% | $98,562.89 |
| Day 27 | 2026-08-18 | $765.46 | Long 51 SPY (T13) | -$417.25 | -1.058% | $98,295.14 |
| Day 28 | 2026-08-19 | $767.19 | Long 51 SPY (T13) | -$329.02 | -0.834% | $98,383.37 |
| Day 29 | 2026-08-20 | $760.73 | Long 51 SPY (T13) | -$658.48 | -1.669% | $98,053.91 |
| Day 30 | 2026-08-21 | $763.74 | Long 51 SPY (T13) | -$504.97 | -1.280% | $98,207.42 |
| Day 31 | 2026-08-24 | $761.57 | Long 51 SPY (T13) | -$615.64 | -1.560% | $98,096.75 |
| Day 32 | 2026-08-25 | $763.89 | Long 51 SPY (T13) | -$497.32 | -1.260% | $98,215.07 |
| Day 33 | 2026-08-26 | $764.04 | Long 51 SPY (T13) | -$489.67 | -1.241% | $98,222.72 |
| Day 34 | 2026-08-27 | $769.27 | Long 51 SPY (T13) | -$222.94 | -0.565% | $98,489.45 |
| Day 35 | 2026-08-28 | $767.37 | Long 51 SPY (T13) | -$319.84 | -0.811% | $98,392.55 |
| Day 36 | 2026-08-31 | $764.97 | Long 51 SPY (T13) | -$442.24 | -1.121% | $98,270.15 |
| Day 37 | 2026-09-01 | $759.74 | FLAT | — | — | $98,099.81 |
| Day 38 | 2026-09-02 | $763.23 | Long 51 SPY (T14) | -$86.19 | -0.221% | $98,013.62 |
| Day 39 | 2026-09-03 | $771.20 | Long 51 SPY (T14) | +$320.28 | +0.821% | $98,420.09 |
| Day 40 | 2026-09-04 | $768.27 | Long 51 SPY (T14) | +$170.85 | +0.438% | $98,270.66 |
| Day 41 | 2026-09-08 | $764.16 | FLAT | — | — | $98,152.34 |
| Day 42 | 2026-09-09 | $760.54 | Long 52 SPY (T15) | -$127.87 | -0.322% | $98,024.47 |
| Day 43 | 2026-09-10 | $755.99 | FLAT | — | — | $97,888.23 |
| Day 44 | 2026-09-11 | $762.25 | FLAT | — | — | $97,888.23 |
| Day 45 | 2026-09-14 | $758.87 | FLAT | — | — | $97,888.23 |
| Day 46 | 2026-09-15 | $755.54 | FLAT | — | — | $97,888.23 |
| Day 47 | 2026-09-16 | $752.18 | FLAT | — | — | $97,888.23 |
| Day 48 | 2026-09-17 | $760.75 | FLAT | — | — | $97,888.23 |
| Day 49 | 2026-09-18 | $761.62 | FLAT | — | — | $97,888.23 |
| Day 50 | 2026-09-21 | $773.52 | FLAT | — | — | $97,888.23 |
| Day 51 | 2026-09-22 | $773.44 | FLAT | — | — | $97,903.02 |
| Day 52 | 2026-09-23 | $767.93 | FLAT | — | — | $97,874.25 |
| Day 53 | 2026-09-24 | $767.29 | FLAT | — | — | $97,874.25 |
| Day 54 | 2026-09-25 | $771.35 | FLAT | — | — | $97,874.25 |
| Day 55 | 2026-09-28 | $765.49 | Long 51 SPY (T18) | +$7.14 | +0.018% | $97,881.39 |
| Day 56 | 2026-09-29 | $764.48 | Long 51 SPY (T18) | -$44.37 | -0.114% | $97,829.88 |

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-07-13 | $99,838.88 | $99,999.97 | -0.1611% | -0.000% | **-0.161%** |
| Day 2 | 2026-07-14 | $99,803.80 | $100,376.01 | -0.1962% | +0.376% | **-0.572%** |
| Day 3 | 2026-07-15 | $99,851.55 | $100,753.38 | -0.1484% | +0.753% | **-0.901%** |
| Day 4 | 2026-07-16 | $99,675.42 | $100,232.82 | -0.3246% | +0.233% | **-0.558%** |
| Day 5 | 2026-07-17 | $99,532.86 | $99,219.80 | -0.4671% | -0.780% | **+0.313%** |
| Day 6 | 2026-07-20 | $99,340.88 | $99,068.58 | -0.6591% | -0.931% | **+0.272%** |
| Day 7 | 2026-07-21 | $99,270.92 | $99,870.16 | -0.7291% | -0.130% | **-0.599%** |
| Day 8 | 2026-07-22 | $99,235.94 | $99,781.84 | -0.7641% | -0.218% | **-0.546%** |
| Day 9 | 2026-07-23 | $98,569.69 | $98,522.59 | -1.4303% | -1.477% | **+0.047%** |
| Day 10 | 2026-07-24 | $98,713.73 | $98,635.00 | -1.2863% | -1.365% | **+0.079%** |
| Day 11 | 2026-07-27 | $98,817.87 | $98,628.31 | -1.1821% | -1.372% | **+0.190%** |
| Day 12 | 2026-07-28 | $98,774.41 | $98,887.92 | -1.2256% | -1.112% | **-0.114%** |
| Day 13 | 2026-07-29 | $98,774.41 | $97,389.13 | -1.2256% | -2.611% | **+1.385%** |
| Day 14 | 2026-07-30 | $98,774.41 | $98,998.99 | -1.2256% | -1.001% | **-0.225%** |
| Day 15 | 2026-07-31 | $98,774.41 | $99,688.17 | -1.2256% | -0.312% | **-0.914%** |
| Day 16 | 2026-08-03 | $98,774.41 | $101,146.81 | -1.2256% | +1.147% | **-2.373%** |
| Day 17 | 2026-08-04 | $98,626.91 | $102,934.65 | -1.3731% | +2.935% | **-4.308%** |
| Day 18 | 2026-08-05 | $98,687.41 | $102,758.01 | -1.3126% | +2.758% | **-4.071%** |
| Day 19 | 2026-08-06 | $98,687.41 | $102,605.45 | -1.3126% | +2.605% | **-3.918%** |
| Day 20 | 2026-08-07 | $98,623.14 | $103,208.98 | -1.3769% | +3.209% | **-4.586%** |
| Day 21 | 2026-08-10 | $98,712.39 | $103,190.25 | -1.2876% | +3.190% | **-4.478%** |
| Day 22 | 2026-08-11 | $98,455.79 | $102,855.70 | -1.5442% | +2.856% | **-4.400%** |
| Day 23 | 2026-08-12 | $98,558.81 | $103,126.01 | -1.4412% | +3.126% | **-4.567%** |
| Day 24 | 2026-08-13 | $98,828.09 | $103,832.59 | -1.1719% | +3.833% | **-5.005%** |
| Day 25 | 2026-08-14 | $98,750.06 | $103,627.84 | -1.2499% | +3.628% | **-4.878%** |
| Day 26 | 2026-08-17 | $98,562.89 | $103,136.72 | -1.4371% | +3.137% | **-4.574%** |
| Day 27 | 2026-08-18 | $98,295.14 | $102,434.16 | -1.7049% | +2.434% | **-4.139%** |
| Day 28 | 2026-08-19 | $98,383.37 | $102,665.67 | -1.6166% | +2.666% | **-4.283%** |
| Day 29 | 2026-08-20 | $98,053.91 | $101,801.19 | -1.9461% | +1.801% | **-3.747%** |
| Day 30 | 2026-08-21 | $98,207.42 | $102,203.99 | -1.7926% | +2.204% | **-3.997%** |
| Day 31 | 2026-08-24 | $98,096.75 | $101,913.60 | -1.9032% | +1.914% | **-3.817%** |
| Day 32 | 2026-08-25 | $98,215.07 | $102,224.07 | -1.7849% | +2.224% | **-4.009%** |
| Day 33 | 2026-08-26 | $98,222.72 | $102,244.14 | -1.7773% | +2.244% | **-4.021%** |
| Day 34 | 2026-08-27 | $98,489.45 | $102,944.02 | -1.5106% | +2.944% | **-4.455%** |
| Day 35 | 2026-08-28 | $98,392.55 | $102,689.76 | -1.6074% | +2.690% | **-4.297%** |
| Day 36 | 2026-08-31 | $98,270.15 | $102,368.59 | -1.7299% | +2.369% | **-4.099%** |
| Day 37 | 2026-09-01 | $98,099.81 | $101,668.71 | -1.9002% | +1.669% | **-3.569%** |
| Day 38 | 2026-09-02 | $98,013.62 | $102,135.74 | -1.9864% | +2.136% | **-4.122%** |
| Day 39 | 2026-09-03 | $98,420.09 | $103,202.29 | -1.5799% | +3.202% | **-4.782%** |
| Day 40 | 2026-09-04 | $98,270.66 | $102,810.20 | -1.7293% | +2.810% | **-4.539%** |
| Day 41 | 2026-09-08 | $98,152.34 | $102,260.20 | -1.8477% | +2.260% | **-4.108%** |
| Day 42 | 2026-09-09 | $98,024.47 | $101,775.77 | -1.9755% | +1.776% | **-3.752%** |
| Day 43 | 2026-09-10 | $97,888.23 | $101,166.88 | -2.1118% | +1.167% | **-3.279%** |
| Day 44 | 2026-09-11 | $97,888.23 | $102,004.60 | -2.1118% | +2.005% | **-4.117%** |
| Day 45 | 2026-09-14 | $97,888.23 | $101,552.29 | -2.1118% | +1.552% | **-3.664%** |
| Day 46 | 2026-09-15 | $97,888.23 | $101,106.67 | -2.1118% | +1.107% | **-3.219%** |
| Day 47 | 2026-09-16 | $97,888.23 | $100,657.03 | -2.1118% | +0.657% | **-2.769%** |
| Day 48 | 2026-09-17 | $97,888.23 | $101,803.87 | -2.1118% | +1.804% | **-3.916%** |
| Day 49 | 2026-09-18 | $97,888.23 | $101,920.29 | -2.1118% | +1.920% | **-4.032%** |
| Day 50 | 2026-09-21 | $97,888.23 | $103,512.76 | -2.1118% | +3.513% | **-5.625%** |
| Day 51 | 2026-09-22 | $97,903.02 | $103,502.05 | -2.0970% | +3.502% | **-5.599%** |
| Day 52 | 2026-09-23 | $97,874.25 | $102,764.70 | -2.1258% | +2.765% | **-4.891%** |
| Day 53 | 2026-09-24 | $97,874.25 | $102,679.05 | -2.1258% | +2.679% | **-4.805%** |
| Day 54 | 2026-09-25 | $97,874.25 | $103,222.37 | -2.1258% | +3.222% | **-5.348%** |
| Day 55 | 2026-09-28 | $97,881.39 | $102,438.18 | -2.1186% | +2.438% | **-4.557%** |
| Day 56 | 2026-09-29 | $97,829.88 | $102,303.02 | -2.1701% | +2.303% | **-4.473%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-07-13 | $747.27 | -$212.53 | -$1913.22 | Holding would have been **$1913.22** better — honest entry |
| Day 2 | 2026-07-14 | $750.08 | -$63.60 | -$2062.15 | Holding would have been **$2062.15** better — honest entry |
| Day 3 | 2026-07-15 | $752.90 | +$85.86 | -$2211.61 | Holding would have been **$2211.61** better — honest entry |
| Day 4 | 2026-07-16 | $749.01 | -$120.31 | -$2005.44 | Holding would have been **$2005.44** better — honest entry |
| Day 5 | 2026-07-17 | $741.44 | -$521.52 | -$1604.23 | Holding would have been **$1604.23** better — honest entry |
| Day 6 | 2026-07-20 | $740.31 | -$581.41 | -$1544.34 | Holding would have been **$1544.34** better — honest entry |
| Day 7 | 2026-07-21 | $746.30 | -$263.94 | -$1861.81 | Position open |
| Day 8 | 2026-07-22 | $745.64 | -$298.92 | -$1826.83 | Position open |
| Day 9 | 2026-07-23 | $736.23 | -$797.65 | -$1328.10 | Position open |
| Day 10 | 2026-07-24 | $737.07 | -$753.13 | -$1372.62 | Holding would have been **$1372.62** better — honest entry |
| Day 11 | 2026-07-27 | $737.02 | -$755.78 | -$1369.97 | Holding would have been **$1369.97** better — honest entry |
| Day 12 | 2026-07-28 | $738.96 | -$652.96 | -$1472.79 | Holding would have been **$1472.79** better — honest entry |
| Day 13 | 2026-07-29 | $727.76 | -$1246.56 | -$879.19 | Holding would have been **$879.19** better — honest entry |
| Day 14 | 2026-07-30 | $739.79 | -$608.97 | -$1516.78 | Holding would have been **$1516.78** better — honest entry |
| Day 15 | 2026-07-31 | $744.94 | -$336.02 | -$1789.73 | Holding would have been **$1789.73** better — honest entry |
| Day 16 | 2026-08-03 | $755.84 | +$241.68 | -$2367.43 | Holding would have been **$2367.43** better — honest entry |
| Day 17 | 2026-08-04 | $769.20 | +$949.76 | -$3075.51 | Position open |
| Day 18 | 2026-08-05 | $767.88 | +$879.80 | -$3005.55 | Holding would have been **$3005.55** better — honest entry |
| Day 19 | 2026-08-06 | $766.74 | +$819.38 | -$2945.13 | Holding would have been **$2945.13** better — honest entry |
| Day 20 | 2026-08-07 | $771.25 | +$1058.41 | -$3184.16 | Position open |
| Day 21 | 2026-08-10 | $771.11 | +$1050.99 | -$3176.74 | Holding would have been **$3176.74** better — honest entry |
| Day 22 | 2026-08-11 | $768.61 | +$918.49 | -$3044.24 | Position open |
| Day 23 | 2026-08-12 | $770.63 | +$1025.55 | -$3151.30 | Position open |
| Day 24 | 2026-08-13 | $775.91 | +$1305.39 | -$3431.14 | Position open |
| Day 25 | 2026-08-14 | $774.38 | +$1224.30 | -$3350.05 | Position open |
| Day 26 | 2026-08-17 | $770.71 | +$1029.79 | -$3155.54 | Position open |
| Day 27 | 2026-08-18 | $765.46 | +$751.54 | -$2877.29 | Position open |
| Day 28 | 2026-08-19 | $767.19 | +$843.23 | -$2968.98 | Position open |
| Day 29 | 2026-08-20 | $760.73 | +$500.85 | -$2626.60 | Position open |
| Day 30 | 2026-08-21 | $763.74 | +$660.38 | -$2786.13 | Position open |
| Day 31 | 2026-08-24 | $761.57 | +$545.37 | -$2671.12 | Position open |
| Day 32 | 2026-08-25 | $763.89 | +$668.33 | -$2794.08 | Position open |
| Day 33 | 2026-08-26 | $764.04 | +$676.28 | -$2802.03 | Position open |
| Day 34 | 2026-08-27 | $769.27 | +$953.47 | -$3079.22 | Position open |
| Day 35 | 2026-08-28 | $767.37 | +$852.77 | -$2978.52 | Position open |
| Day 36 | 2026-08-31 | $764.97 | +$725.57 | -$2851.32 | Position open |
| Day 37 | 2026-09-01 | $759.74 | +$448.38 | -$2574.13 | Holding would have been **$2574.13** better — honest entry |
| Day 38 | 2026-09-02 | $763.23 | +$633.35 | -$2759.10 | Position open |
| Day 39 | 2026-09-03 | $771.20 | +$1055.76 | -$3181.51 | Position open |
| Day 40 | 2026-09-04 | $768.27 | +$900.47 | -$3026.22 | Position open |
| Day 41 | 2026-09-08 | $764.16 | +$682.64 | -$2808.39 | Holding would have been **$2808.39** better — honest entry |
| Day 42 | 2026-09-09 | $760.54 | +$490.78 | -$2616.53 | Position open |
| Day 43 | 2026-09-10 | $755.99 | +$249.63 | -$2375.38 | Holding would have been **$2375.38** better — honest entry |
| Day 44 | 2026-09-11 | $762.25 | +$581.41 | -$2707.16 | Holding would have been **$2707.16** better — honest entry |
| Day 45 | 2026-09-14 | $758.87 | +$402.27 | -$2528.02 | Holding would have been **$2528.02** better — honest entry |
| Day 46 | 2026-09-15 | $755.54 | +$225.78 | -$2351.53 | Holding would have been **$2351.53** better — honest entry |
| Day 47 | 2026-09-16 | $752.18 | +$47.70 | -$2173.45 | Holding would have been **$2173.45** better — honest entry |
| Day 48 | 2026-09-17 | $760.75 | +$501.91 | -$2627.66 | Holding would have been **$2627.66** better — honest entry |
| Day 49 | 2026-09-18 | $761.62 | +$548.02 | -$2673.77 | Holding would have been **$2673.77** better — honest entry |
| Day 50 | 2026-09-21 | $773.52 | +$1178.72 | -$3304.47 | Holding would have been **$3304.47** better — honest entry |
| Day 51 | 2026-09-22 | $773.44 | +$1174.48 | -$3300.23 | Holding would have been **$3300.23** better — honest entry |
| Day 52 | 2026-09-23 | $767.93 | +$882.45 | -$3008.20 | Holding would have been **$3008.20** better — honest entry |
| Day 53 | 2026-09-24 | $767.29 | +$848.53 | -$2974.28 | Holding would have been **$2974.28** better — honest entry |
| Day 54 | 2026-09-25 | $771.35 | +$1063.71 | -$3189.46 | Holding would have been **$3189.46** better — honest entry |
| Day 55 | 2026-09-28 | $765.49 | +$753.13 | -$2878.88 | Position open |
| Day 56 | 2026-09-29 | $764.48 | +$699.60 | -$2825.35 | Position open |

---

## Daily Entries

### Day 1 — 2026-07-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $747.27 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$212.53 |
| Signal saved | -$1913.22 |
| Portfolio value | $99,838.88 |
| Benchmark value | $99,999.97 |
| Alpha (cumulative) | -0.161% |

**Regime call:** BULL

**Market context:** The market experienced a bullish day with a strong close, despite the Nasdaq dropping amid U.S.-Iran strikes. The VIX remains relatively low at 16.24. Oil prices also remained steady at $74.79 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The fast signal remained bullish with a strong momentum.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold through market volatility and maintain a bullish stance is a testament to the effectiveness of the dual-timeframe strategy in capturing market trends.

---

### Day 2 — 2026-07-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $750.08 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$63.60 |
| Signal saved | -$2062.15 |
| Portfolio value | $99,803.80 |
| Benchmark value | $100,376.01 |
| Alpha (cumulative) | -0.572% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell, while ETFs rose ahead of testimony. The VIX index remained relatively low at 16.45. Oil prices were steady at $78.7 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bullish fast signal (MA10/MA30 golden cross), with the slow filter regime remaining in a bullish context.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to lock in a positive P&L of $1027.70 underscores the importance of discipline in exiting positions on strong bullish signals.

---

### Day 3 — 2026-07-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $752.90 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$85.86 |
| Signal saved | -$2211.61 |
| Portfolio value | $99,851.55 |
| Benchmark value | $100,753.38 |
| Alpha (cumulative) | -0.901% |

**Regime call:** BULL

**Market context:** The market rallied on cool inflation data, with the Dow climbing and the SPY closing at $753.43. Economic reports and earnings releases also contributed to the positive sentiment.

**Strategy note:** The system held a long position in SPY, as the fast signal remained BULLISH with a fast golden cross and the slow filter regime confirmed as BULL. The system did not exit the position today.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions, including the regime filter, is crucial in maintaining its performance.

---

### Day 4 — 2026-07-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $749.01 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$120.31 |
| Signal saved | -$2005.44 |
| Portfolio value | $99,675.42 |
| Benchmark value | $100,232.82 |
| Alpha (cumulative) | -0.558% |

**Regime call:** Consolidation

**Market context:** The market saw a mixed day with the Nasdaq sliding due to tech stocks, while the VIX remained relatively low at 15.87. Oil prices were steady at $79.72 per barrel and the 10Y Treasury yield held at 4.59%. The SPY price closed at $753.01.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position and lock in a profit is a key component of its overall success.

---

### Day 5 — 2026-07-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $741.44 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$521.52 |
| Signal saved | -$1604.23 |
| Portfolio value | $99,532.86 |
| Benchmark value | $99,219.80 |
| Alpha (cumulative) | +0.313% |

**Regime call:** Consolidation

**Market context:** Markets traded in a relatively calm manner, with the SPY closing at $745.72. The VIX index remained at 18.07, indicating a stable market environment. Chipmaker stocks retreated, contributing to a decline in equity futures.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position, locking in a realized P&L of $+864.24. The system is now waiting for the next fast golden cross to re-enter the market.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management strategy effectively locked in profits during a period of market consolidation.

---

### Day 6 — 2026-07-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $740.31 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$581.41 |
| Signal saved | -$1544.34 |
| Portfolio value | $99,340.88 |
| Benchmark value | $99,068.58 |
| Alpha (cumulative) | +0.272% |

**Regime call:** BULL

**Market context:** Market futures edged higher ahead of key earnings reports, despite Middle East tensions. The dollar's weakness was a topic of discussion, but its impact on social security checks was highlighted. Momentum in the S&P 500 was weak.

**Strategy note:** The system held long SPY, with a bullish fast signal and a bull regime. The slow filter's MA20 and MA50 remained in a bullish alignment.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum environment can persist even as the market edges higher, highlighting the importance of regime context in trading decisions.

---

### Day 7 — 2026-07-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T7) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $746.30 |
| Unrealized P&L | -$69.96 |
| P&L % | -0.177% |
| Portfolio value | $99,270.92 |
| Benchmark value | $99,870.16 |
| Alpha (cumulative) | -0.599% |

**Regime call:** Recovery Rally

**Market context:** Markets rose pre-bell Tuesday, driven by a semiconductor recovery and countering Iran jitters. The Nasdaq and S&P 500 futures rallied, with big tech earnings drawing focus. The VIX remained relatively low at 17.41.

**Strategy note:** The system exited the position, locking in a $+529.70 realized P&L, due to a bullish fast signal (MA10/MA30) in a BULL regime (MA20/MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.18% from entry. No exit triggered.

**Key learning:** A weak momentum reading occurred despite a bullish fast signal, highlighting the importance of monitoring momentum in conjunction with dual-timeframe signals.

---

### Day 8 — 2026-07-22 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 53 SPY (T7) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $745.64 |
| Unrealized P&L | -$104.94 |
| P&L % | -0.265% |
| Portfolio value | $99,235.94 |
| Benchmark value | $99,781.84 |
| Alpha (cumulative) | -0.546% |

**Regime call:** BULL

**Market context:** Markets opened lower but ended with modest gains, with SPY closing at $748.84. The VIX index remained relatively low at 16.99. Major tech earnings are expected ahead of the bell.

**Strategy note:** The system held long SPY as the fast signal remained BULLISH and the regime context remained in a BULL market, with the slow MAs (MA20 vs MA50) confirming this regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.27% from entry. No exit triggered.

**Key learning:** The system's ability to ride the recovery rally and hold onto gains is being tested, highlighting the importance of regime context in strategy decision-making.

---

### Day 9 — 2026-07-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 52 SPY (T8) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $736.23 |
| Unrealized P&L | -$135.72 |
| P&L % | -0.353% |
| Portfolio value | $98,569.69 |
| Benchmark value | $98,522.59 |
| Alpha (cumulative) | +0.047% |

**Regime call:** BULL

**Market context:** Markets declined today amidst a tech sell-off, with major indices futures falling. Major news included earnings from Tesla and Alphabet, reviving fears about AI spending. The VIX index rose to 19.83.

**Strategy note:** The dual-timeframe SMA crossover system exited the position due to a bullish fast signal (MA10 > MA30), while the slow filter remained in a bull regime (MA20 > MA50).

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.35% from entry. No exit triggered.

**Key learning:** The system's ability to exit positions in line with the slow filter's regime context helped mitigate losses, but a re-entry on the next fast golden cross may be needed to recapture gains.

---

### Day 10 — 2026-07-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $737.07 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$753.13 |
| Signal saved | -$1372.62 |
| Portfolio value | $98,713.73 |
| Benchmark value | $98,635.00 |
| Alpha (cumulative) | +0.079% |

**Regime call:** BULL

**Market context:** US stocks and equity futures rose pre-bell amid new US tariffs, while VIX remained relatively low at 18.19. Oil prices were stable at $89.8/barrel. The 10Y Treasury yield held steady at 4.67%.

**Strategy note:** The dual-timeframe signal remained BULLISH, with a Fast Golden Cross and a BULL regime from the Slow MAs. The system held long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading does not necessarily lead to a short-term reversal, especially when the regime remains BULL.

---

### Day 11 — 2026-07-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $737.02 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$755.78 |
| Signal saved | -$1369.97 |
| Portfolio value | $98,817.87 |
| Benchmark value | $98,628.31 |
| Alpha (cumulative) | +0.190% |

**Regime call:** Consolidation

**Market context:** Oil prices fell, easing fears ahead of the Fed meeting and big tech earnings. Equities futures rose, with the Nasdaq, S&P 500, and Dow futures increasing. Market news focused on ETFs, equity futures, and S&P 500 performance.

**Strategy note:** The system exited the position due to a bullish fast signal (MA10/MA30 golden cross) in a bull regime (MA20/MA50). The system is now monitoring for a re-entry on the next fast golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to adapt to changing market conditions and regimes is crucial in avoiding losses and capturing opportunities.

---

### Day 12 — 2026-07-28 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $738.96 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$652.96 |
| Signal saved | -$1472.79 |
| Portfolio value | $98,774.41 |
| Benchmark value | $98,887.92 |
| Alpha (cumulative) | -0.114% |

**Regime call:** BULL

**Market context:** Markets were mixed ahead of the Fed decision, with semiconductor stocks under pressure. The VIX remained relatively low at 18.06. The 10Y Treasury yield held steady at 4.59%.

**Strategy note:** The dual-timeframe SMA crossover strategy held long SPY, with a bullish fast signal and a bullish regime context. The system did not trigger an exit.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A weak momentum reading in a bullish regime context may signal a potential consolidation phase.

---

### Day 13 — 2026-07-29 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $727.76 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$1246.56 |
| Signal saved | -$879.19 |
| Portfolio value | $98,774.41 |
| Benchmark value | $97,389.13 |
| Alpha (cumulative) | +1.385% |

**Regime call:** Consolidation

**Market context:** The market headlines were mixed with some sectors performing well, while others struggled. The VIX index remained relatively low at 19.84. The 10Y Treasury yield remained steady at 4.63%.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime. The slow filter (MA20/MA50) remains in a bull regime.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit positions in bearish regimes is crucial in maintaining overall performance.

---

### Day 14 — 2026-07-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $739.79 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$608.97 |
| Signal saved | -$1516.78 |
| Portfolio value | $98,774.41 |
| Benchmark value | $98,998.99 |
| Alpha (cumulative) | -0.225% |

**Regime call:** Consolidation

**Market context:** The market was relatively calm with no major catalysts, and the VIX remained low at 19.05. Nvidia and AMD stocks were in the news, but their performance did not significantly impact the overall market. The 10Y Treasury yield was steady at 4.68%.

**Strategy note:** The system exited the position due to a bearish fast signal, with the MA10 crossing below the MA30. The slow filter remained in a bull regime, but the system prioritized the fast signal for entry and exit decisions.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's reliance on the fast signal led to a loss, highlighting the importance of considering the regime context in high-impact decisions.

---

### Day 15 — 2026-07-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $744.94 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | -$336.02 |
| Signal saved | -$1789.73 |
| Portfolio value | $98,774.41 |
| Benchmark value | $99,688.17 |
| Alpha (cumulative) | -0.914% |

**Regime call:** Consolidation

**Market context:** The market ended the week on a mixed note, with ETFs and equity futures higher pre-bell Friday, but the S&P 500 and Nasdaq ended the best day in a month on the previous day.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 death cross) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to exit a position in a bull regime highlights the importance of maintaining a regime-aware strategy.

---

### Day 16 — 2026-08-03 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $755.84 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$241.68 |
| Signal saved | -$2367.43 |
| Portfolio value | $98,774.41 |
| Benchmark value | $101,146.81 |
| Alpha (cumulative) | -2.373% |

**Regime call:** Consolidation

**Market context:** US-Iran truce hopes lifted equity futures and ETFs, but market headlines were mixed with some cautionary notes on the economy.

**Strategy note:** The dual-timeframe SMA crossover strategy exited the position due to a bearish fast signal (MA10 < MA30) in a bull regime (MA20 > MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a bullish signal, and the system's ability to adapt to changing market conditions is crucial.

---

### Day 17 — 2026-08-04 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 50 SPY (T11) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $769.20 |
| Unrealized P&L | -$147.50 |
| P&L % | -0.382% |
| Portfolio value | $98,626.91 |
| Benchmark value | $102,934.65 |
| Alpha (cumulative) | -4.308% |

**Regime call:** Consolidation

**Market context:** Markets were relatively calm with VIX at 16.21, while WTI Oil held steady at $75.31. The 10Y Treasury yield remained at 4.63%. Headlines were mixed, with some stocks experiencing significant price movements.

**Strategy note:** The system exited the position due to a bearish fast signal (MA10/MA30 crossover) in a bull regime, locking in a realized P&L of $-66.44.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** The system's ability to exit the position before further losses highlights the importance of timely risk management in a dual-timeframe strategy.

---

### Day 18 — 2026-08-05 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $767.88 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$879.80 |
| Signal saved | -$3005.55 |
| Portfolio value | $98,687.41 |
| Benchmark value | $102,758.01 |
| Alpha (cumulative) | -4.071% |

**Regime call:** BULL

**Market context:** US stock futures were flat after S&P500 and Dow ended at record highs on strong earnings and easing geopolitical concerns. VIX remained low at 16.32. Oil price was stable at $75.25/barrel.

**Strategy note:** The dual-timeframe signal remained BULLISH with a Fast Golden Cross, and the system held long SPY. The slow filter regime remained BULL.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong momentum environment can mask underlying regime shifts, highlighting the importance of both fast and slow signals in a dual-timeframe strategy.

---

### Day 19 — 2026-08-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $766.74 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$819.38 |
| Signal saved | -$2945.13 |
| Portfolio value | $98,687.41 |
| Benchmark value | $102,605.45 |
| Alpha (cumulative) | -3.918% |

**Regime call:** BULL

**Market context:** Markets ended lower amid Hormuz uncertainty and awaited jobs data to judge Fed rate course. SPY fell $58.81 from its previous close. VIX remained relatively low at 15.15.

**Strategy note:** The system exited the position based on a bullish fast signal (MA10/MA30) and a BULL regime context (MA20/MA50).

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A strong bull regime does not guarantee a successful trade, as the system still experienced a loss.

---

### Day 20 — 2026-08-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T12) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $771.25 |
| Unrealized P&L | -$64.27 |
| P&L % | -0.163% |
| Portfolio value | $98,623.14 |
| Benchmark value | $103,208.98 |
| Alpha (cumulative) | -4.586% |

**Regime call:** BULL

**Market context:** Markets traded higher pre-bell Friday amid strong tech results, with ETFs and equity futures also rising. VIX remained relatively low at 14.89. Oil prices were stable at $77.41 per barrel.

**Strategy note:** The system held long SPY due to a bullish dual-timeframe signal, with MA10 crossing above MA30 and a strong bull regime. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.16% from entry. No exit triggered.

**Key learning:** The system remains in a bull regime but has yet to generate significant alpha, highlighting the need for further refinement in the strategy.

---

### Day 21 — 2026-08-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $771.11 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$1050.99 |
| Signal saved | -$3176.74 |
| Portfolio value | $98,712.39 |
| Benchmark value | $103,190.25 |
| Alpha (cumulative) | -4.478% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Monday as oil prices rose, while the S&P 500 companies' second-quarter profit boomed. The VIX remained relatively low at 15.24. Oil prices continued to rise, reaching $80.36 per barrel.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bullish regime context. The slow filter MA20 MA50 also confirmed the bullish regime.

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to capture a strong rally is dependent on its ability to correctly identify the regime context.

---

### Day 22 — 2026-08-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $768.61 |
| Unrealized P&L | -$256.60 |
| P&L % | -0.650% |
| Portfolio value | $98,455.79 |
| Benchmark value | $102,855.70 |
| Alpha (cumulative) | -4.400% |

**Regime call:** BULL

**Market context:** Equity futures were mixed pre-bell Tuesday amid stalled US-Iran talks, while exchange-traded funds were higher. The VIX remained relatively low at 15.4. Oil prices were stable at $82.0/barrel.

**Strategy note:** The system held long SPY based on a bullish fast signal and a bull regime, with strong momentum. No exit was triggered today.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.65% from entry. No exit triggered.

**Key learning:** A strong bull regime and momentum can lead to prolonged periods of sideways or slightly upward movement, making it essential to set realistic expectations for returns.

---

### Day 23 — 2026-08-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $770.63 |
| Unrealized P&L | -$153.58 |
| P&L % | -0.389% |
| Portfolio value | $98,558.81 |
| Benchmark value | $103,126.01 |
| Alpha (cumulative) | -4.567% |

**Regime call:** BULL

**Market context:** Markets continued their upward trend with the S&P 500 closing at $772.04, driven by tech gains and in-line consumer inflation data. The VIX index remained relatively low at 14.83. Oil prices also remained stable at $82.68 per barrel.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, with the fast signal remaining bullish due to a golden cross. The slow filter regime remained in a bull context, with MA20 above MA50.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.39% from entry. No exit triggered.

**Key learning:** The system's unrealized P&L remains negative, highlighting the need for improved entry timing and risk management.

---

### Day 24 — 2026-08-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $775.91 |
| Unrealized P&L | +$115.70 |
| P&L % | +0.293% |
| Portfolio value | $98,828.09 |
| Benchmark value | $103,832.59 |
| Alpha (cumulative) | -5.005% |

**Regime call:** BULL

**Market context:** US stocks rose, with the SPY trading higher. Producer inflation data was released, and exchange-traded funds and equity futures were higher pre-bell. The VIX remained relatively low at 14.74.

**Strategy note:** The system held long SPY due to a bullish fast signal and a bull regime, with the slow MA20 crossing above MA50. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong bull regime can persist even with a relatively low VIX, as seen in today's market action.

---

### Day 25 — 2026-08-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $774.38 |
| Unrealized P&L | +$37.67 |
| P&L % | +0.095% |
| Portfolio value | $98,750.06 |
| Benchmark value | $103,627.84 |
| Alpha (cumulative) | -4.878% |

**Regime call:** BULL

**Market context:** Wall Street's riskiest trades are back on top, and ETFs are higher, while equity futures are mixed, amid retail sales data. The Average Social Security Check gets a raise every January, but a $500,000 portfolio’s ‘paycheck’ doesn’t. The 10Y Treasury yield remains at 4.66%.

**Strategy note:** The system held long SPY, with a BULLISH fast signal and a BULL regime, and saw an unrealized P&L of +0.49% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: +0.10% from entry. No exit triggered.

**Key learning:** The system remains in a BULL regime, but the strong momentum and bullish fast signal suggest caution is warranted.

---

### Day 26 — 2026-08-17

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $770.71 |
| Unrealized P&L | -$149.50 |
| P&L % | -0.379% |
| Portfolio value | $98,562.89 |
| Benchmark value | $103,136.72 |
| Alpha (cumulative) | -4.574% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.38% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 27 — 2026-08-18

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $765.46 |
| Unrealized P&L | -$417.25 |
| P&L % | -1.058% |
| Portfolio value | $98,295.14 |
| Benchmark value | $102,434.16 |
| Alpha (cumulative) | -4.139% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.06% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 28 — 2026-08-19

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $767.19 |
| Unrealized P&L | -$329.02 |
| P&L % | -0.834% |
| Portfolio value | $98,383.37 |
| Benchmark value | $102,665.67 |
| Alpha (cumulative) | -4.283% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.83% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 29 — 2026-08-20

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $760.73 |
| Unrealized P&L | -$658.48 |
| P&L % | -1.669% |
| Portfolio value | $98,053.91 |
| Benchmark value | $101,801.19 |
| Alpha (cumulative) | -3.747% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.67% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 30 — 2026-08-21

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $763.74 |
| Unrealized P&L | -$504.97 |
| P&L % | -1.280% |
| Portfolio value | $98,207.42 |
| Benchmark value | $102,203.99 |
| Alpha (cumulative) | -3.997% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.28% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 31 — 2026-08-24

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $761.57 |
| Unrealized P&L | -$615.64 |
| P&L % | -1.560% |
| Portfolio value | $98,096.75 |
| Benchmark value | $101,913.60 |
| Alpha (cumulative) | -3.817% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 32 — 2026-08-25

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $763.89 |
| Unrealized P&L | -$497.32 |
| P&L % | -1.260% |
| Portfolio value | $98,215.07 |
| Benchmark value | $102,224.07 |
| Alpha (cumulative) | -4.009% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.26% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 33 — 2026-08-26

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $764.04 |
| Unrealized P&L | -$489.67 |
| P&L % | -1.241% |
| Portfolio value | $98,222.72 |
| Benchmark value | $102,244.14 |
| Alpha (cumulative) | -4.021% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.24% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 34 — 2026-08-27

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $769.27 |
| Unrealized P&L | -$222.94 |
| P&L % | -0.565% |
| Portfolio value | $98,489.45 |
| Benchmark value | $102,944.02 |
| Alpha (cumulative) | -4.455% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.56% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 35 — 2026-08-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $767.37 |
| Unrealized P&L | -$319.84 |
| P&L % | -0.811% |
| Portfolio value | $98,392.55 |
| Benchmark value | $102,689.76 |
| Alpha (cumulative) | -4.297% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.81% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 36 — 2026-08-31

| Field | Value |
|---|---|
| Position | Long 51 SPY (T13) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $764.97 |
| Unrealized P&L | -$442.24 |
| P&L % | -1.121% |
| Portfolio value | $98,270.15 |
| Benchmark value | $102,368.59 |
| Alpha (cumulative) | -4.099% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -1.12% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 37 — 2026-09-01

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $759.74 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$448.38 |
| Signal saved | -$2574.13 |
| Portfolio value | $98,099.81 |
| Benchmark value | $101,668.71 |
| Alpha (cumulative) | -3.569% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 38 — 2026-09-02

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $763.23 |
| Unrealized P&L | -$86.19 |
| P&L % | -0.221% |
| Portfolio value | $98,013.62 |
| Benchmark value | $102,135.74 |
| Alpha (cumulative) | -4.122% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.22% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 39 — 2026-09-03

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $771.20 |
| Unrealized P&L | +$320.28 |
| P&L % | +0.821% |
| Portfolio value | $98,420.09 |
| Benchmark value | $103,202.29 |
| Alpha (cumulative) | -4.782% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: +0.82% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 40 — 2026-09-04

| Field | Value |
|---|---|
| Position | Long 51 SPY (T14) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $768.27 |
| Unrealized P&L | +$170.85 |
| P&L % | +0.438% |
| Portfolio value | $98,270.66 |
| Benchmark value | $102,810.20 |
| Alpha (cumulative) | -4.539% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: +0.44% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 41 — 2026-09-08

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $764.16 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$682.64 |
| Signal saved | -$2808.39 |
| Portfolio value | $98,152.34 |
| Benchmark value | $102,260.20 |
| Alpha (cumulative) | -4.108% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 42 — 2026-09-09

| Field | Value |
|---|---|
| Position | Long 52 SPY (T15) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $760.54 |
| Unrealized P&L | -$127.87 |
| P&L % | -0.322% |
| Portfolio value | $98,024.47 |
| Benchmark value | $101,775.77 |
| Alpha (cumulative) | -3.752% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.32% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 43 — 2026-09-10

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $755.99 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$249.63 |
| Signal saved | -$2375.38 |
| Portfolio value | $97,888.23 |
| Benchmark value | $101,166.88 |
| Alpha (cumulative) | -3.279% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 44 — 2026-09-11

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $762.25 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$581.41 |
| Signal saved | -$2707.16 |
| Portfolio value | $97,888.23 |
| Benchmark value | $102,004.60 |
| Alpha (cumulative) | -4.117% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 45 — 2026-09-14

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $758.87 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$402.27 |
| Signal saved | -$2528.02 |
| Portfolio value | $97,888.23 |
| Benchmark value | $101,552.29 |
| Alpha (cumulative) | -3.664% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 46 — 2026-09-15

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $755.54 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$225.78 |
| Signal saved | -$2351.53 |
| Portfolio value | $97,888.23 |
| Benchmark value | $101,106.67 |
| Alpha (cumulative) | -3.219% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 47 — 2026-09-16

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $752.18 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$47.70 |
| Signal saved | -$2173.45 |
| Portfolio value | $97,888.23 |
| Benchmark value | $100,657.03 |
| Alpha (cumulative) | -2.769% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 48 — 2026-09-17

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $760.75 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$501.91 |
| Signal saved | -$2627.66 |
| Portfolio value | $97,888.23 |
| Benchmark value | $101,803.87 |
| Alpha (cumulative) | -3.916% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 49 — 2026-09-18

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $761.62 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$548.02 |
| Signal saved | -$2673.77 |
| Portfolio value | $97,888.23 |
| Benchmark value | $101,920.29 |
| Alpha (cumulative) | -4.032% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 50 — 2026-09-21

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $773.52 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$1178.72 |
| Signal saved | -$3304.47 |
| Portfolio value | $97,888.23 |
| Benchmark value | $103,512.76 |
| Alpha (cumulative) | -5.625% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 51 — 2026-09-22

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $773.44 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$1174.48 |
| Signal saved | -$3300.23 |
| Portfolio value | $97,903.02 |
| Benchmark value | $103,502.05 |
| Alpha (cumulative) | -5.599% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 52 — 2026-09-23

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $767.93 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$882.45 |
| Signal saved | -$3008.20 |
| Portfolio value | $97,874.25 |
| Benchmark value | $102,764.70 |
| Alpha (cumulative) | -4.891% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 53 — 2026-09-24

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $767.29 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$848.53 |
| Signal saved | -$2974.28 |
| Portfolio value | $97,874.25 |
| Benchmark value | $102,679.05 |
| Alpha (cumulative) | -4.805% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 54 — 2026-09-25

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $771.35 |
| Realized P&L (locked) | -$2125.75 |
| Reference if held | +$1063.71 |
| Signal saved | -$3189.46 |
| Portfolio value | $97,874.25 |
| Benchmark value | $103,222.37 |
| Alpha (cumulative) | -5.348% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System exited the position. Realized P&L locked at $-2125.75. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** _fill in_

---

### Day 55 — 2026-09-28

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $765.49 |
| Unrealized P&L | +$7.14 |
| P&L % | +0.018% |
| Portfolio value | $97,881.39 |
| Benchmark value | $102,438.18 |
| Alpha (cumulative) | -4.557% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: +0.02% from entry. No exit triggered.

**Key learning:** _fill in_

---

### Day 56 — 2026-09-29

| Field | Value |
|---|---|
| Position | Long 51 SPY (T18) |
| Entry (Alpaca fill) | $751.280/share |
| Close price | $764.48 |
| Unrealized P&L | -$44.37 |
| P&L % | -0.114% |
| Portfolio value | $97,829.88 |
| Benchmark value | $102,303.02 |
| Alpha (cumulative) | -4.473% |

**Regime call:** _fill in_

**Market context:** _fill in_

**Strategy note:** _fill in_

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $763.93 vs MA50 $760.39). Momentum: STRONG. Unrealized P&L: -0.11% from entry. No exit triggered.

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
_Day 56 of 90 · Alpaca equity: $99,017.42 · Cumulative alpha vs SPY: -4.473%_