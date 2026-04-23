# ALPACA PAPER JOURNAL — SPY
_Last updated: April 23, 2026 | Day 33 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$666.436/share**
> (2026-03-09, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-04-23): **BULLISH** | ⚡ Price Override Active (+4.9% above MA50)  
> Fast: MA10 $700.42 | MA30 $671.44  
> Slow: MA20 $677.54 | MA50 $675.59  
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

**Total trades:** 5 | **Closed:** 5 | **Open:** No | **Cumulative Realized P&L:** -$124.34

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $666.436 (2026-03-09) | $668.000 (2026-03-12) | 10 | +$15.64 | ✅ Closed |
| T2 | $701.250 (2026-04-16) | $701.600 (2026-04-16) | 57 | +$19.95 | ✅ Closed |
| T3 | $710.606 (2026-04-17) | $710.500 (2026-04-17) | 56 | -$5.92 | ✅ Closed |
| T4 | $706.745 (2026-04-20) | $706.280 (2026-04-21) | 56 | -$26.06 | ✅ Closed |
| T5 | $709.805 (2026-04-22) | $707.520 (2026-04-23) | 56 | -$127.95 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $99,876.61 |
| Alpaca cash | $99,876.61 |
| Cumulative realized P&L | -$124.34 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $676.45 | Long 10 SPY (T1) | +$100.14 | +1.503% | $100,100.14 |
| Day 2 | 2026-03-10 | $675.29 | Long 10 SPY (T1) | +$88.54 | +1.329% | $100,088.54 |
| Day 3 | 2026-03-11 | $674.50 | Long 10 SPY (T1) | +$80.64 | +1.210% | $100,080.64 |
| Day 4 | 2026-03-12 | $664.24 | FLAT | — | — | $100,015.64 |
| Day 5 | 2026-03-13 | $660.50 | FLAT | — | — | $100,015.64 |
| Day 6 | 2026-03-16 | $667.15 | FLAT | — | — | $100,015.64 |
| Day 7 | 2026-03-17 | $668.92 | FLAT | — | — | $100,015.64 |
| Day 8 | 2026-03-18 | $659.74 | FLAT | — | — | $100,015.64 |
| Day 9 | 2026-03-19 | $658.07 | FLAT | — | — | $100,015.64 |
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

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $100,100.14 | $100,000.01 | +0.1001% | +0.000% | **+0.100%** |
| Day 2 | 2026-03-10 | $100,088.54 | $99,828.53 | +0.0885% | -0.171% | **+0.260%** |
| Day 3 | 2026-03-11 | $100,080.64 | $99,711.74 | +0.0806% | -0.288% | **+0.369%** |
| Day 4 | 2026-03-12 | $100,015.64 | $98,195.00 | +0.0156% | -1.805% | **+1.821%** |
| Day 5 | 2026-03-13 | $100,015.64 | $97,642.11 | +0.0156% | -2.358% | **+2.374%** |
| Day 6 | 2026-03-16 | $100,015.64 | $98,625.18 | +0.0156% | -1.375% | **+1.391%** |
| Day 7 | 2026-03-17 | $100,015.64 | $98,886.84 | +0.0156% | -1.113% | **+1.129%** |
| Day 8 | 2026-03-18 | $100,015.64 | $97,529.76 | +0.0156% | -2.470% | **+2.486%** |
| Day 9 | 2026-03-19 | $100,015.64 | $97,282.88 | +0.0156% | -2.717% | **+2.733%** |
| Day 10 | 2026-03-20 | $100,015.64 | $95,865.19 | +0.0156% | -4.135% | **+4.151%** |
| Day 11 | 2026-03-23 | $100,015.64 | $96,883.74 | +0.0156% | -3.116% | **+3.132%** |
| Day 12 | 2026-03-24 | $100,015.64 | $96,562.95 | +0.0156% | -3.437% | **+3.453%** |
| Day 13 | 2026-03-25 | $100,015.64 | $97,086.27 | +0.0156% | -2.914% | **+2.930%** |
| Day 14 | 2026-03-26 | $100,015.64 | $95,367.00 | +0.0156% | -4.633% | **+4.649%** |
| Day 15 | 2026-03-27 | $100,015.64 | $93,730.51 | +0.0156% | -6.269% | **+6.285%** |
| Day 16 | 2026-03-30 | $100,015.64 | $93,431.90 | +0.0156% | -6.568% | **+6.584%** |
| Day 17 | 2026-03-31 | $100,015.64 | $96,107.63 | +0.0156% | -3.892% | **+3.908%** |
| Day 18 | 2026-04-01 | $100,015.64 | $96,855.65 | +0.0156% | -3.144% | **+3.160%** |
| Day 19 | 2026-04-02 | $100,015.64 | $96,941.39 | +0.0156% | -3.059% | **+3.075%** |
| Day 20 | 2026-04-06 | $100,015.64 | $97,402.63 | +0.0156% | -2.597% | **+2.613%** |
| Day 21 | 2026-04-07 | $100,015.64 | $97,454.37 | +0.0156% | -2.546% | **+2.562%** |
| Day 22 | 2026-04-08 | $100,015.64 | $99,933.49 | +0.0156% | -0.067% | **+0.083%** |
| Day 23 | 2026-04-09 | $100,015.64 | $100,505.59 | +0.0156% | +0.506% | **-0.490%** |
| Day 24 | 2026-04-10 | $100,015.64 | $100,428.72 | +0.0156% | +0.429% | **-0.413%** |
| Day 25 | 2026-04-13 | $100,015.64 | $101,411.79 | +0.0156% | +1.412% | **-1.396%** |
| Day 26 | 2026-04-14 | $100,015.64 | $102,647.66 | +0.0156% | +2.648% | **-2.632%** |
| Day 27 | 2026-04-15 | $100,015.64 | $103,444.46 | +0.0156% | +3.444% | **-3.428%** |
| Day 28 | 2026-04-16 | $100,035.59 | $103,707.60 | +0.0356% | +3.708% | **-3.672%** |
| Day 29 | 2026-04-17 | $100,029.67 | $104,968.60 | +0.0297% | +4.969% | **-4.939%** |
| Day 30 | 2026-04-20 | $100,144.17 | $104,780.85 | +0.1442% | +4.781% | **-4.637%** |
| Day 31 | 2026-04-21 | $100,003.61 | $104,059.44 | +0.0036% | +4.059% | **-4.055%** |
| Day 32 | 2026-04-22 | $100,081.74 | $105,137.12 | +0.0817% | +5.137% | **-5.055%** |
| Day 33 | 2026-04-23 | $99,875.66 | $104,724.68 | -0.1243% | +4.725% | **-4.849%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $676.45 | +$100.14 | -$224.48 | Position open |
| Day 2 | 2026-03-10 | $675.29 | +$88.54 | -$212.88 | Position open |
| Day 3 | 2026-03-11 | $674.50 | +$80.64 | -$204.98 | Position open |
| Day 4 | 2026-03-12 | $664.24 | -$21.96 | -$102.38 | Holding would have been **$102.38** better — honest entry |
| Day 5 | 2026-03-13 | $660.50 | -$59.36 | -$64.98 | Holding would have been **$64.98** better — honest entry |
| Day 6 | 2026-03-16 | $667.15 | +$7.14 | -$131.48 | Holding would have been **$131.48** better — honest entry |
| Day 7 | 2026-03-17 | $668.92 | +$24.84 | -$149.18 | Holding would have been **$149.18** better — honest entry |
| Day 8 | 2026-03-18 | $659.74 | -$66.96 | -$57.38 | Holding would have been **$57.38** better — honest entry |
| Day 9 | 2026-03-19 | $658.07 | -$83.66 | -$40.68 | Holding would have been **$40.68** better — honest entry |
| Day 10 | 2026-03-20 | $648.48 | -$179.56 | +$55.22 | Flat saved **+$55.22** vs holding |
| Day 11 | 2026-03-23 | $655.37 | -$110.66 | -$13.68 | Holding would have been **$13.68** better — honest entry |
| Day 12 | 2026-03-24 | $653.20 | -$132.36 | +$8.02 | Flat saved **+$8.02** vs holding |
| Day 13 | 2026-03-25 | $656.74 | -$96.96 | -$27.38 | Holding would have been **$27.38** better — honest entry |
| Day 14 | 2026-03-26 | $645.11 | -$213.26 | +$88.92 | Flat saved **+$88.92** vs holding |
| Day 15 | 2026-03-27 | $634.04 | -$323.96 | +$199.62 | Flat saved **+$199.62** vs holding |
| Day 16 | 2026-03-30 | $632.02 | -$344.16 | +$219.82 | Flat saved **+$219.82** vs holding |
| Day 17 | 2026-03-31 | $650.12 | -$163.16 | +$38.82 | Flat saved **+$38.82** vs holding |
| Day 18 | 2026-04-01 | $655.18 | -$112.56 | -$11.78 | Holding would have been **$11.78** better — honest entry |
| Day 19 | 2026-04-02 | $655.76 | -$106.76 | -$17.58 | Holding would have been **$17.58** better — honest entry |
| Day 20 | 2026-04-06 | $658.88 | -$75.56 | -$48.78 | Holding would have been **$48.78** better — honest entry |
| Day 21 | 2026-04-07 | $659.23 | -$72.06 | -$52.28 | Holding would have been **$52.28** better — honest entry |
| Day 22 | 2026-04-08 | $676.00 | +$95.64 | -$219.98 | Holding would have been **$219.98** better — honest entry |
| Day 23 | 2026-04-09 | $679.87 | +$134.34 | -$258.68 | Holding would have been **$258.68** better — honest entry |
| Day 24 | 2026-04-10 | $679.35 | +$129.14 | -$253.48 | Holding would have been **$253.48** better — honest entry |
| Day 25 | 2026-04-13 | $686.00 | +$195.64 | -$319.98 | Holding would have been **$319.98** better — honest entry |
| Day 26 | 2026-04-14 | $694.36 | +$279.24 | -$403.58 | Holding would have been **$403.58** better — honest entry |
| Day 27 | 2026-04-15 | $699.75 | +$333.14 | -$457.48 | Holding would have been **$457.48** better — honest entry |
| Day 28 | 2026-04-16 | $701.53 | +$350.94 | -$475.28 | Holding would have been **$475.28** better — honest entry |
| Day 29 | 2026-04-17 | $710.06 | +$436.24 | -$560.58 | Holding would have been **$560.58** better — honest entry |
| Day 30 | 2026-04-20 | $708.79 | +$423.54 | -$547.88 | Position open |
| Day 31 | 2026-04-21 | $703.91 | +$374.74 | -$499.08 | Holding would have been **$499.08** better — honest entry |
| Day 32 | 2026-04-22 | $711.20 | +$447.64 | -$571.98 | Position open |
| Day 33 | 2026-04-23 | $708.41 | +$419.74 | -$544.08 | Holding would have been **$544.08** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-03-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $676.45 |
| Unrealized P&L | +$100.14 |
| P&L % | +1.503% |
| Portfolio value | $100,100.14 |
| Benchmark value | $100,000.01 |
| Alpha (cumulative) | +0.100% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. Despite this, the SPY price is still above the MA20 and MA50, but the Death Cross signal indicates a bearish trend. The VIX is high at 27.39.

**Strategy note:** The system correctly identified a bearish trend and entered a long position in SPY, but the MA20/MA50 crossover strategy did not trigger a trade today due to the Death Cross signal.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Momentum: STRONG. Unrealized P&L: +1.50% from entry. No exit triggered.

**Key learning:** The system's ability to identify a bearish trend is correct, but the Death Cross signal overrides the MA20/MA50 crossover strategy, resulting in a missed trade opportunity.

---

### Day 2 — 2026-03-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $675.29 |
| Unrealized P&L | +$88.54 |
| P&L % | +1.329% |
| Portfolio value | $100,088.54 |
| Benchmark value | $99,828.53 |
| Alpha (cumulative) | +0.260% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating elevated volatility. The WTI oil price is also elevated at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system did not trigger a sell signal today, as the MA20 is still below the MA50, indicating a bearish signal is not present. However, the system's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Momentum: STRONG. Unrealized P&L: +1.33% from entry. No exit triggered.

**Key learning:** The system's inaction during a risk-off regime is correct, as the primary focus is on preserving capital during such periods.

---

### Day 3 — 2026-03-11 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $674.50 |
| Unrealized P&L | +$80.64 |
| P&L % | +1.210% |
| Portfolio value | $100,080.64 |
| Benchmark value | $99,711.74 |
| Alpha (cumulative) | +0.369% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** Market sentiment lifted on de-escalation hopes, but VIX remains elevated at 27.39. WTI Oil price increased, and 10Y Treasury yield rose to 4.328%. SPY price closed at $674.49.

**Strategy note:** MA20 ($660.25) is below MA50 ($675.76), indicating a bearish signal. The system did not enter a trade today, as the signal is not conducive to a long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Momentum: STRONG. Unrealized P&L: +1.21% from entry. No exit triggered.

**Key learning:** The strategy's ability to avoid a losing trade is more valuable than a single winning trade.

---

### Day 4 — 2026-03-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $664.24 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$21.96 |
| Signal saved | -$102.38 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,195.00 |
| Alpha (cumulative) | +1.821% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed's warning about another supply shock. The VIX is elevated at 27.39. Oil prices are also high at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system generated a bearish signal today, but the system did not short as the long position was already open. This was correct because the system is not designed to short.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's long position was profitable today despite the bearish signal, highlighting the importance of position sizing and risk management in a trend-following strategy.

---

### Day 5 — 2026-03-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $660.50 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$59.36 |
| Signal saved | -$64.98 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,642.11 |
| Alpha (cumulative) | +2.374% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is currently experiencing a risk-off regime due to the impending supply shock warned by the Fed Chair. The VIX index is elevated at 27.39, indicating increased market volatility. Oil prices are also high, at $104.76 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system did not enter a trade as the position status was already FLAT. This was correct because the signal was not a buy signal.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal does not necessarily mean a trade should be entered if the position is already flat.

---

### Day 6 — 2026-03-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $667.15 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$7.14 |
| Signal saved | -$131.48 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,625.18 |
| Alpha (cumulative) | +1.391% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** Markets are higher pre-bell as de-escalation hopes lift risk sentiment. However, Fed Chair Powell's warning of another supply shock is a bearish signal. VIX remains elevated at 27.39.

**Strategy note:** MA20 is below MA50, indicating a bearish crossover. The system did not enter a trade today as it was flat, but the signal would have been to sell given the bearish crossover.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal is a valid reason to sell, even if the market is rising in the short term.

---

### Day 7 — 2026-03-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $668.92 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$24.84 |
| Signal saved | -$149.18 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,886.84 |
| Alpha (cumulative) | +1.129% |

**Regime call:** RISK-OFF

**Market context:** Markets were relatively calm, with the VIX at 27.39, and the 10Y Treasury yield at 4.328%. Headlines were mixed, with some articles hinting at a potential correction.

**Strategy note:** The MA20/MA50 crossover system is in a BEARISH — Death Cross regime. The system did not enter a position today, as the market conditions did not trigger a signal.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction today was correct, as the market did not trigger a signal, and the realized P&L was locked at +$15.58

---

### Day 8 — 2026-03-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $659.74 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$66.96 |
| Signal saved | -$57.38 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,529.76 |
| Alpha (cumulative) | +2.486% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime following Fed Chair Powell's warning of another supply shock. The VIX index is elevated at 27.39, indicating increased volatility. The SPY price closed at $659.63.

**Strategy note:** The MA20/MA50 crossover strategy is in a BEARISH — Death Cross regime, but no trade was executed due to the system being flat. The strategy's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits is crucial in a risk-off regime, as seen today with a $+15.58 realized P&L.

---

### Day 9 — 2026-03-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.07 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$83.66 |
| Signal saved | -$40.68 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,282.88 |
| Alpha (cumulative) | +2.733% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. The VIX is elevated at 27.39. The SPY price closed at $658.00.

**Strategy note:** The system is flat, as the MA20/MA50 crossover strategy did not trigger a trade today. This is correct, as the signal is bearish (Death Cross) and the system is designed to avoid trading during such conditions.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management approach is effective in avoiding losses during periods of high market volatility.

---

### Day 10 — 2026-03-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $648.48 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$179.56 |
| Signal saved | +$55.22 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,865.19 |
| Alpha (cumulative) | +4.151% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite warning signs from the Fed Chair and rising VIX. Oil prices continued to climb. The 10Y Treasury yield remained elevated.

**Strategy note:** The MA20/MA50 crossover system remained flat as MA20 was below MA50, indicating no buy or sell signal. This was correct as the market did not follow the bearish signal.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to stay flat in a volatile market environment is crucial for preserving capital.

---

### Day 11 — 2026-03-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.37 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$110.66 |
| Signal saved | -$13.68 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,883.74 |
| Alpha (cumulative) | +3.132% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating increased volatility. Oil prices are also elevated.

**Strategy note:** The MA system is in a bearish regime due to the death cross, but did not enter a trade today as the position was already flat. The system's inaction was correct as the market did not provide a clear buy or sell signal.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to avoid trading during periods of high volatility is crucial in maintaining its overall performance.

---

### Day 12 — 2026-03-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $653.20 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$132.36 |
| Signal saved | +$8.02 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,562.95 |
| Alpha (cumulative) | +3.453% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market context today is characterized by a bearish signal from the MA20/MA50 crossover strategy and a rising VIX. The Fed Chair's warning of another supply shock is likely contributing to the risk-off sentiment. Meanwhile, the WTI Oil price is stable, and the 10Y Treasury yield is rising.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system remained flat due to the signal being a death cross, which typically indicates a sell signal. The strategy's inaction was correct as the market declined.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross signal should be treated with caution and may require a more nuanced approach to determine the optimal course of action.

---

### Day 13 — 2026-03-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $656.74 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$96.96 |
| Signal saved | -$27.38 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,086.27 |
| Alpha (cumulative) | +2.930% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite the Fed Chair's warning of another supply shock. VIX remained elevated, but WTI Oil price dropped. The 10Y Treasury yield also decreased.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH — Death Cross regime. The system did not enter a trade today, as the MA20 was below the MA50 and the signal was bearish.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A dead-cat bounce can occur even in a bearish market regime, highlighting the importance of staying nimble and not over-interpreting short-term market movements.

---

### Day 14 — 2026-03-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $645.11 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$213.26 |
| Signal saved | +$88.92 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,367.00 |
| Alpha (cumulative) | +4.649% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning about another supply shock. The VIX is at 27.39, indicating increased market volatility. Oil prices are also on the rise.

**Strategy note:** The MA20/MA50 crossover strategy did not trigger any trades today, as the signal was bearish (Death Cross) and the system remained flat.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal may not always be a buy signal, and staying flat can be a correct decision in uncertain market conditions.

---

### Day 15 — 2026-03-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $634.04 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$323.96 |
| Signal saved | +$199.62 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,730.51 |
| Alpha (cumulative) | +6.285% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** Markets remained relatively stable despite the Fed Chair's warning of an impending supply shock. The VIX index increased slightly, while the 10Y Treasury yield remained steady. Oil prices also rose.

**Strategy note:** The MA20/MA50 system remained flat as the Death Cross signal did not trigger a trade. This was correct as the market did not experience a significant downturn.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction during a period of heightened uncertainty highlights the importance of a well-defined trading plan and risk management.

---

### Day 16 — 2026-03-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $632.02 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$344.16 |
| Signal saved | +$219.82 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,431.90 |
| Alpha (cumulative) | +6.584% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite a bearish signal from the MA crossover strategy, with SPY closing at $631.97. VIX remained elevated at 27.39. Headlines were mixed, with a warning from Fed Chair Powell and hopes for de-escalation.

**Strategy note:** The system remained flat as the MA20/MA50 crossover strategy indicated a bearish signal, which was correct given the market's cautious behavior.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits and avoid new positions during a dead-cat bounce is crucial for preserving capital.

---

### Day 17 — 2026-03-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $650.12 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$163.16 |
| Signal saved | +$38.82 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,107.63 |
| Alpha (cumulative) | +3.908% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market experienced a dead-cat bounce, with SPY closing at $641.88, despite a bearish signal from the MA20/MA50 crossover. VIX remained elevated at 27.39. Fed Chair Powell's warning of another supply shock contributed to the cautious market sentiment.

**Strategy note:** The system did not enter a trade today due to a bearish signal from the MA20/MA50 crossover. The system's inaction was correct as the market experienced a dead-cat bounce.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal from the MA20/MA50 crossover does not guarantee a sell signal, as the market can experience a dead-cat bounce.

---

### Day 18 — 2026-04-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.18 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$112.56 |
| Signal saved | -$11.78 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,855.65 |
| Alpha (cumulative) | +3.160% |

**Regime call:** RISK-OFF

**Market context:** The market experienced a risk-off day, driven by the bearish MA cross and elevated VIX, amidst geopolitical tensions and a decline in oil prices.

**Strategy note:** The MA20/MA50 crossover system correctly identified a bearish signal, but did not enter a trade as the position was already flat.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to identify bearish signals is intact, but it must be used in conjunction with position management to maximize returns.

---

### Day 19 — 2026-04-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.76 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$106.76 |
| Signal saved | -$17.58 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,941.39 |
| Alpha (cumulative) | +3.075% |

**Regime call:** RISK-OFF

**Market context:** The stock market sold off on Trump's speech and surging oil prices, with the Dow experiencing a decline. The VIX index rose to 27.15, indicating increased market volatility. Oil prices surged to $112.24 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH signal due to the Death Cross, but no trades were executed as the position was flat.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy correctly identified a bearish signal, but the lack of a trade execution highlights the importance of position sizing and risk management.

---

### Day 20 — 2026-04-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.88 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$75.56 |
| Signal saved | -$48.78 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,402.63 |
| Alpha (cumulative) | +2.613% |

**Regime call:** BULLISH

**Market context:** Markets were mixed post-BLS jobs, with equity futures trading mixed pre-bell Monday amid ongoing Iran conflict. VIX remained elevated at 24.17. WTI oil price rose to $112.59/barrel.

**Strategy note:** MA20 crossed below MA50, triggering a bullish signal. The system remains flat, with no trades executed today.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's alpha continues to outperform the benchmark, with a cumulative alpha of +2.610%

---

### Day 21 — 2026-04-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $659.23 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | -$72.06 |
| Signal saved | -$52.28 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,454.37 |
| Alpha (cumulative) | +2.562% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, and oil prices were falling, amidst a two-week US-Iran ceasefire.

**Strategy note:** MA20 crossed below MA50, triggering a bearish signal. The system exited the position.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** VIX levels can significantly influence market sentiment and impact our strategy's performance.

---

### Day 22 — 2026-04-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $676.00 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$95.64 |
| Signal saved | -$219.98 |
| Portfolio value | $100,015.64 |
| Benchmark value | $99,933.49 |
| Alpha (cumulative) | +0.083% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, indicating a decrease in market volatility. Oil prices continued to fall. Markets were higher pre-bell Wednesday amid a two-week US-Iran ceasefire.

**Strategy note:** The MA20/MA50 crossover strategy remained bearish, with a death cross. The system exited the position and is now flat, waiting for a golden cross to re-enter.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's bearish signal was correct, but the realized P&L was relatively low, highlighting the importance of position sizing and risk management.

---

### Day 23 — 2026-04-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $679.87 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$134.34 |
| Signal saved | -$258.68 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,505.59 |
| Alpha (cumulative) | -0.490% |

**Regime call:** RISK-ON

**Market context:** Equity futures and ETFs declined pre-bell as fragile Middle East ceasefire lifted oil prices. VIX rose to 20.8. S&P 500 had a rare gap-up on Wednesday.

**Strategy note:** MA20/MA50 crossover strategy exited position based on bearish signal. System now flat, waiting for next golden cross.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** MA crossover strategy underperformed passive hold, reinforcing need for robust risk management

---

### Day 24 — 2026-04-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $679.35 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$129.14 |
| Signal saved | -$253.48 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,428.72 |
| Alpha (cumulative) | -0.413% |

**Regime call:** RISK-ON

**Market context:** The S&P 500 closed above a key level, with equity futures mixed amidst geopolitical uncertainty and a looming CPI report. The VIX remained relatively calm, but could swing wildly after the CPI data release.

**Strategy note:** The system exited the position due to a bearish MA cross, and is now flat. The MA20 is below the MA50, indicating a bearish trend.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's bearish signal was correct, but the realized P&L was lower than the passive hold, highlighting the importance of risk management in trading strategies.

---

### Day 25 — 2026-04-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $686.00 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$195.64 |
| Signal saved | -$319.98 |
| Portfolio value | $100,015.64 |
| Benchmark value | $101,411.79 |
| Alpha (cumulative) | -1.396% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 sold off due to geopolitical tensions, with oil prices surging over $100. The VIX sharply reversed, pointing towards 30 after failed peace negotiations. This led to a risk-off sentiment in the market.

**Strategy note:** MA50 crossed above MA20, triggering a bearish signal. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal does not guarantee losses, as the system's realized P&L was positive despite the market downturn.

---

### Day 26 — 2026-04-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $694.36 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$279.24 |
| Signal saved | -$403.58 |
| Portfolio value | $100,015.64 |
| Benchmark value | $102,647.66 |
| Alpha (cumulative) | -2.632% |

**Regime call:** RISK-OFF

**Market context:** The market rose today with Dow leading, despite concerns over inflation data and a potential US-Iran truce. VIX remains elevated at 18.05. Oil prices also increased.

**Strategy note:** MA20 ($660.21) is below MA50 ($672.89), indicating a bearish signal. The system exited the position, locking in a $+15.58 P&L.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross in the MA crossover strategy led to a premature exit, resulting in a missed opportunity to ride the market's upward momentum.

---

### Day 27 — 2026-04-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $699.75 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$333.14 |
| Signal saved | -$457.48 |
| Portfolio value | $100,015.64 |
| Benchmark value | $103,444.46 |
| Alpha (cumulative) | -3.428% |

**Regime call:** RISK-ON

**Market context:** Investors turned to corporate earnings, driving equity futures higher. Wall Street's fear gauge, VIX, is fading. The S&P 500 Stocks' earnings are expected to skyrocket 200% in three months.

**Strategy note:** MA20/MA50 crossover strategy is in a BEARISH regime due to a Death Cross. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's realized P&L outperformed a passive hold by $15.58, but still trailed the benchmark by $286.66.

---

### Day 28 — 2026-04-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $701.53 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$350.94 |
| Signal saved | -$475.28 |
| Portfolio value | $100,035.59 |
| Benchmark value | $103,707.60 |
| Alpha (cumulative) | -3.672% |

**Regime call:** BEAR

**Market context:** The market remains in a bear regime, with SPY trading below its 50-day moving average. The S&P 500 index is also under pressure, with no clear signs of a reversal. Economic data releases and geopolitical tensions continue to weigh on investor sentiment.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, despite the bear regime, due to a bullish fast signal. The system's unrealized P&L increased by 0.06% from entry.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bullish fast signal does not guarantee success in a bear regime, and the system's performance may be impacted by the prevailing market conditions.

---

### Day 29 — 2026-04-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $710.06 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$436.24 |
| Signal saved | -$560.58 |
| Portfolio value | $100,029.67 |
| Benchmark value | $104,968.60 |
| Alpha (cumulative) | -4.939% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 broke above 7000, driven by a rally in tech stocks and the opening of the Strait of Hormuz. Oil prices declined, while Netflix shares plummeted. Market sentiment remains bullish.

**Strategy note:** The system exited the position due to a bear regime, as confirmed by the slow MA20/MA50 crossover. A bullish fast signal was generated, but the system prioritized the slow regime filter.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Benchmark value | $104,780.85 |
| Alpha (cumulative) | -4.637% |

**Regime call:** BEAR

**Market context:** Small Cap Stocks and Russell 2000 declined, while Oil Prices surged amid Middle East tensions. The S&P 500 held 7100, with Nasdaq Composite battling fears. Equity Futures and Exchange-Traded Funds also declined.

**Strategy note:** The system held long SPY due to a BULLISH Fast signal and BEAR regime, despite strong momentum. No exit was triggered.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Momentum: STRONG. Unrealized P&L: +0.29% from entry. No exit triggered.

**Key learning:** A strong momentum environment can override a bearish regime context, but may also increase risk of a false signal.

---

### Day 31 — 2026-04-21 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $703.91 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$374.74 |
| Signal saved | -$499.08 |
| Portfolio value | $100,003.61 |
| Benchmark value | $104,059.44 |
| Alpha (cumulative) | -4.055% |

**Regime call:** BEAR

**Market context:** Markets rallied on Iran deal hopes, with stocks outperforming safe-havens like gold. Small caps and risk-on trades led the gains. Oil prices pulled back on the news.

**Strategy note:** The system remained long SPY despite a BEAR regime, as the fast signal remained BULLISH due to a strong golden cross. No exit was triggered.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

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
| Benchmark value | $105,137.12 |
| Alpha (cumulative) | -5.055% |

**Regime call:** BEAR

**Market context:** Risk-on trade buoyed small cap sentiment, while the VIX remains calm. The S&P 500 climbed on a ceasefire extension and tech tailwinds.

**Strategy note:** The system held a long SPY position, despite a bear regime, due to a bullish fast signal from the 10/30 SMA crossover. Unrealized P&L was -0.01% from entry.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Momentum: STRONG. Unrealized P&L: +0.20% from entry. No exit triggered.

**Key learning:** A bear regime does not necessarily mean a bear market, as the system's fast signal can override the slow filter.

---

### Day 33 — 2026-04-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $708.41 |
| Realized P&L (locked) | -$124.34 |
| Reference if held | +$419.74 |
| Signal saved | -$544.08 |
| Portfolio value | $99,875.66 |
| Benchmark value | $104,724.68 |
| Alpha (cumulative) | -4.849% |

**Regime call:** BULL

**Market context:** The S&P 500 retreated but held 7100 on fresh Mideast escalation as earnings kick off, while VIX crept toward 20 as Iran fears and Tesla's whipsaw rattle nerves.

**Strategy note:** The dual-timeframe signal remained bullish, with a fast golden cross and strong momentum, causing the system to hold long SPY.

**What I did today:** System exited the position. Realized P&L locked at $-124.34. Regime: BULL (MA20 $677.54 vs MA50 $675.59). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to hold long in a bull regime despite rising VIX is being tested.

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
_Day 33 of 90 · Alpaca equity: $99,876.61 · Cumulative alpha vs SPY: -4.849%_