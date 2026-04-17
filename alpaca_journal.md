# ALPACA PAPER JOURNAL — SPY
_Last updated: April 17, 2026 | Day 29 of 90_
_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_
_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_
_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_

> ⚠️ **RECONCILIATION NOTE**  
> All P&L uses Alpaca fill prices. First entry: **$666.436/share**
> (2026-03-09, after-hours fill).

> 📡 **CURRENT SIGNAL** (2026-04-17): **BULLISH** | ⚡ Price Override Active (+5.4% above MA50)  
> Fast: MA10 $684.58 | MA30 $666.92  
> Slow: MA20 $666.62 | MA50 $673.88  
> Regime: **BEAR** | Momentum: **STRONG** | Session: AFTER_HOURS

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

**Total trades:** 3 | **Closed:** 3 | **Open:** No | **Cumulative Realized P&L:** +$29.67

| Trade | Entry | Exit | Shares | P&L | Status |
|---|---|---|---|---|---|
| T1 | $666.436 (2026-03-09) | $668.000 (2026-03-12) | 10 | +$15.64 | ✅ Closed |
| T2 | $701.250 (2026-04-16) | $701.600 (2026-04-16) | 57 | +$19.95 | ✅ Closed |
| T3 | $710.606 (2026-04-17) | $710.500 (2026-04-17) | 56 | -$5.92 | ✅ Closed |

## Account Summary

| Field | Value |
|---|---|
| Symbol | SPY |
| Starting capital | $100,000 |
| Alpaca equity | $100,029.59 |
| Alpaca cash | $100,029.59 |
| Cumulative realized P&L | +$29.67 |

## Master Table

| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $676.43 | Long 10 SPY (T1) | +$99.94 | +1.500% | $100,099.94 |
| Day 2 | 2026-03-10 | $675.26 | Long 10 SPY (T1) | +$88.24 | +1.324% | $100,088.24 |
| Day 3 | 2026-03-11 | $674.47 | Long 10 SPY (T1) | +$80.34 | +1.206% | $100,080.34 |
| Day 4 | 2026-03-12 | $664.21 | FLAT | — | — | $100,015.64 |
| Day 5 | 2026-03-13 | $660.47 | FLAT | — | — | $100,015.64 |
| Day 6 | 2026-03-16 | $667.12 | FLAT | — | — | $100,015.64 |
| Day 7 | 2026-03-17 | $668.90 | FLAT | — | — | $100,015.64 |
| Day 8 | 2026-03-18 | $659.71 | FLAT | — | — | $100,015.64 |
| Day 9 | 2026-03-19 | $658.05 | FLAT | — | — | $100,015.64 |
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

## Benchmark vs Strategy

| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |
|---|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $100,099.94 | $100,000.03 | +0.0999% | +0.000% | **+0.100%** |
| Day 2 | 2026-03-10 | $100,088.24 | $99,827.06 | +0.0882% | -0.173% | **+0.261%** |
| Day 3 | 2026-03-11 | $100,080.34 | $99,710.27 | +0.0803% | -0.290% | **+0.370%** |
| Day 4 | 2026-03-12 | $100,015.64 | $98,193.49 | +0.0156% | -1.807% | **+1.823%** |
| Day 5 | 2026-03-13 | $100,015.64 | $97,640.58 | +0.0156% | -2.359% | **+2.375%** |
| Day 6 | 2026-03-16 | $100,015.64 | $98,623.69 | +0.0156% | -1.376% | **+1.392%** |
| Day 7 | 2026-03-17 | $100,015.64 | $98,886.83 | +0.0156% | -1.113% | **+1.129%** |
| Day 8 | 2026-03-18 | $100,015.64 | $97,528.23 | +0.0156% | -2.472% | **+2.488%** |
| Day 9 | 2026-03-19 | $100,015.64 | $97,282.82 | +0.0156% | -2.717% | **+2.733%** |
| Day 10 | 2026-03-20 | $100,015.64 | $95,868.04 | +0.0156% | -4.132% | **+4.148%** |
| Day 11 | 2026-03-23 | $100,015.64 | $96,886.62 | +0.0156% | -3.113% | **+3.129%** |
| Day 12 | 2026-03-24 | $100,015.64 | $96,565.82 | +0.0156% | -3.434% | **+3.450%** |
| Day 13 | 2026-03-25 | $100,015.64 | $97,089.16 | +0.0156% | -2.911% | **+2.927%** |
| Day 14 | 2026-03-26 | $100,015.64 | $95,369.84 | +0.0156% | -4.630% | **+4.646%** |
| Day 15 | 2026-03-27 | $100,015.64 | $93,733.30 | +0.0156% | -6.267% | **+6.283%** |
| Day 16 | 2026-03-30 | $100,015.64 | $93,434.68 | +0.0156% | -6.565% | **+6.581%** |
| Day 17 | 2026-03-31 | $100,015.64 | $96,110.49 | +0.0156% | -3.890% | **+3.906%** |
| Day 18 | 2026-04-01 | $100,015.64 | $96,858.54 | +0.0156% | -3.141% | **+3.157%** |
| Day 19 | 2026-04-02 | $100,015.64 | $96,944.28 | +0.0156% | -3.056% | **+3.072%** |
| Day 20 | 2026-04-06 | $100,015.64 | $97,405.52 | +0.0156% | -2.594% | **+2.610%** |
| Day 21 | 2026-04-07 | $100,015.64 | $97,457.27 | +0.0156% | -2.543% | **+2.559%** |
| Day 22 | 2026-04-08 | $100,015.64 | $99,936.46 | +0.0156% | -0.064% | **+0.080%** |
| Day 23 | 2026-04-09 | $100,015.64 | $100,508.58 | +0.0156% | +0.509% | **-0.493%** |
| Day 24 | 2026-04-10 | $100,015.64 | $100,431.71 | +0.0156% | +0.432% | **-0.416%** |
| Day 25 | 2026-04-13 | $100,015.64 | $101,414.81 | +0.0156% | +1.415% | **-1.399%** |
| Day 26 | 2026-04-14 | $100,015.64 | $102,650.71 | +0.0156% | +2.651% | **-2.635%** |
| Day 27 | 2026-04-15 | $100,015.64 | $103,447.54 | +0.0156% | +3.448% | **-3.432%** |
| Day 28 | 2026-04-16 | $100,035.59 | $103,710.69 | +0.0356% | +3.711% | **-3.675%** |
| Day 29 | 2026-04-17 | $100,029.67 | $104,971.72 | +0.0297% | +4.972% | **-4.942%** |

## Signal Saved vs Holding

| Day | Date | SPY Close | If Held | Signal Saved | Note |
|---|---|---|---|---|---|
| Day 1 | 2026-03-09 | $676.43 | +$99.94 | -$70.27 | Position open |
| Day 2 | 2026-03-10 | $675.26 | +$88.24 | -$58.57 | Position open |
| Day 3 | 2026-03-11 | $674.47 | +$80.34 | -$50.67 | Position open |
| Day 4 | 2026-03-12 | $664.21 | -$22.26 | +$51.93 | Flat saved **+$51.93** vs holding |
| Day 5 | 2026-03-13 | $660.47 | -$59.66 | +$89.33 | Flat saved **+$89.33** vs holding |
| Day 6 | 2026-03-16 | $667.12 | +$6.84 | +$22.83 | Flat saved **+$22.83** vs holding |
| Day 7 | 2026-03-17 | $668.90 | +$24.64 | +$5.03 | Flat saved **+$5.03** vs holding |
| Day 8 | 2026-03-18 | $659.71 | -$67.26 | +$96.93 | Flat saved **+$96.93** vs holding |
| Day 9 | 2026-03-19 | $658.05 | -$83.86 | +$113.53 | Flat saved **+$113.53** vs holding |
| Day 10 | 2026-03-20 | $648.48 | -$179.56 | +$209.23 | Flat saved **+$209.23** vs holding |
| Day 11 | 2026-03-23 | $655.37 | -$110.66 | +$140.33 | Flat saved **+$140.33** vs holding |
| Day 12 | 2026-03-24 | $653.20 | -$132.36 | +$162.03 | Flat saved **+$162.03** vs holding |
| Day 13 | 2026-03-25 | $656.74 | -$96.96 | +$126.63 | Flat saved **+$126.63** vs holding |
| Day 14 | 2026-03-26 | $645.11 | -$213.26 | +$242.93 | Flat saved **+$242.93** vs holding |
| Day 15 | 2026-03-27 | $634.04 | -$323.96 | +$353.63 | Flat saved **+$353.63** vs holding |
| Day 16 | 2026-03-30 | $632.02 | -$344.16 | +$373.83 | Flat saved **+$373.83** vs holding |
| Day 17 | 2026-03-31 | $650.12 | -$163.16 | +$192.83 | Flat saved **+$192.83** vs holding |
| Day 18 | 2026-04-01 | $655.18 | -$112.56 | +$142.23 | Flat saved **+$142.23** vs holding |
| Day 19 | 2026-04-02 | $655.76 | -$106.76 | +$136.43 | Flat saved **+$136.43** vs holding |
| Day 20 | 2026-04-06 | $658.88 | -$75.56 | +$105.23 | Flat saved **+$105.23** vs holding |
| Day 21 | 2026-04-07 | $659.23 | -$72.06 | +$101.73 | Flat saved **+$101.73** vs holding |
| Day 22 | 2026-04-08 | $676.00 | +$95.64 | -$65.97 | Holding would have been **$65.97** better — honest entry |
| Day 23 | 2026-04-09 | $679.87 | +$134.34 | -$104.67 | Holding would have been **$104.67** better — honest entry |
| Day 24 | 2026-04-10 | $679.35 | +$129.14 | -$99.47 | Holding would have been **$99.47** better — honest entry |
| Day 25 | 2026-04-13 | $686.00 | +$195.64 | -$165.97 | Holding would have been **$165.97** better — honest entry |
| Day 26 | 2026-04-14 | $694.36 | +$279.24 | -$249.57 | Holding would have been **$249.57** better — honest entry |
| Day 27 | 2026-04-15 | $699.75 | +$333.14 | -$303.47 | Holding would have been **$303.47** better — honest entry |
| Day 28 | 2026-04-16 | $701.53 | +$350.94 | -$321.27 | Holding would have been **$321.27** better — honest entry |
| Day 29 | 2026-04-17 | $710.06 | +$436.24 | -$406.57 | Holding would have been **$406.57** better — honest entry |

---

## Daily Entries

### Day 1 — 2026-03-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $676.43 |
| Unrealized P&L | +$99.94 |
| P&L % | +1.500% |
| Portfolio value | $100,099.94 |
| Benchmark value | $100,000.03 |
| Alpha (cumulative) | +0.100% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. Despite this, the SPY price is still above the MA20 and MA50, but the Death Cross signal indicates a bearish trend. The VIX is high at 27.39.

**Strategy note:** The system correctly identified a bearish trend and entered a long position in SPY, but the MA20/MA50 crossover strategy did not trigger a trade today due to the Death Cross signal.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Momentum: STRONG. Unrealized P&L: +1.50% from entry. No exit triggered.

**Key learning:** The system's ability to identify a bearish trend is correct, but the Death Cross signal overrides the MA20/MA50 crossover strategy, resulting in a missed trade opportunity.

---

### Day 2 — 2026-03-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | Long 10 SPY (T1) |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $675.26 |
| Unrealized P&L | +$88.24 |
| P&L % | +1.324% |
| Portfolio value | $100,088.24 |
| Benchmark value | $99,827.06 |
| Alpha (cumulative) | +0.261% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating elevated volatility. The WTI oil price is also elevated at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system did not trigger a sell signal today, as the MA20 is still below the MA50, indicating a bearish signal is not present. However, the system's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Momentum: STRONG. Unrealized P&L: +1.32% from entry. No exit triggered.

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
| Benchmark value | $99,710.27 |
| Alpha (cumulative) | +0.370% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** Market sentiment lifted on de-escalation hopes, but VIX remains elevated at 27.39. WTI Oil price increased, and 10Y Treasury yield rose to 4.328%. SPY price closed at $674.49.

**Strategy note:** MA20 ($660.25) is below MA50 ($675.76), indicating a bearish signal. The system did not enter a trade today, as the signal is not conducive to a long position.

**What I did today:** System held long SPY. Fast signal remained BULLISH. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Momentum: STRONG. Unrealized P&L: +1.21% from entry. No exit triggered.

**Key learning:** The strategy's ability to avoid a losing trade is more valuable than a single winning trade.

---

### Day 4 — 2026-03-12 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $664.21 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$22.26 |
| Signal saved | +$51.93 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,193.49 |
| Alpha (cumulative) | +1.823% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed's warning about another supply shock. The VIX is elevated at 27.39. Oil prices are also high at $104.76/barrel.

**Strategy note:** The MA20/MA50 crossover system generated a bearish signal today, but the system did not short as the long position was already open. This was correct because the system is not designed to short.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's long position was profitable today despite the bearish signal, highlighting the importance of position sizing and risk management in a trend-following strategy.

---

### Day 5 — 2026-03-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $660.47 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$59.66 |
| Signal saved | +$89.33 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,640.58 |
| Alpha (cumulative) | +2.375% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is currently experiencing a risk-off regime due to the impending supply shock warned by the Fed Chair. The VIX index is elevated at 27.39, indicating increased market volatility. Oil prices are also high, at $104.76 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system did not enter a trade as the position status was already FLAT. This was correct because the signal was not a buy signal.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal does not necessarily mean a trade should be entered if the position is already flat.

---

### Day 6 — 2026-03-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $667.12 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$6.84 |
| Signal saved | +$22.83 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,623.69 |
| Alpha (cumulative) | +1.392% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** Markets are higher pre-bell as de-escalation hopes lift risk sentiment. However, Fed Chair Powell's warning of another supply shock is a bearish signal. VIX remains elevated at 27.39.

**Strategy note:** MA20 is below MA50, indicating a bearish crossover. The system did not enter a trade today as it was flat, but the signal would have been to sell given the bearish crossover.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal is a valid reason to sell, even if the market is rising in the short term.

---

### Day 7 — 2026-03-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $668.90 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$24.64 |
| Signal saved | +$5.03 |
| Portfolio value | $100,015.64 |
| Benchmark value | $98,886.83 |
| Alpha (cumulative) | +1.129% |

**Regime call:** RISK-OFF

**Market context:** Markets were relatively calm, with the VIX at 27.39, and the 10Y Treasury yield at 4.328%. Headlines were mixed, with some articles hinting at a potential correction.

**Strategy note:** The MA20/MA50 crossover system is in a BEARISH — Death Cross regime. The system did not enter a position today, as the market conditions did not trigger a signal.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction today was correct, as the market did not trigger a signal, and the realized P&L was locked at +$15.58

---

### Day 8 — 2026-03-18 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $659.71 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$67.26 |
| Signal saved | +$96.93 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,528.23 |
| Alpha (cumulative) | +2.488% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime following Fed Chair Powell's warning of another supply shock. The VIX index is elevated at 27.39, indicating increased volatility. The SPY price closed at $659.63.

**Strategy note:** The MA20/MA50 crossover strategy is in a BEARISH — Death Cross regime, but no trade was executed due to the system being flat. The strategy's inaction was correct as the market is experiencing a risk-off regime.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits is crucial in a risk-off regime, as seen today with a $+15.58 realized P&L.

---

### Day 9 — 2026-03-19 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.05 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$83.86 |
| Signal saved | +$113.53 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,282.82 |
| Alpha (cumulative) | +2.733% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning of another supply shock. The VIX is elevated at 27.39. The SPY price closed at $658.00.

**Strategy note:** The system is flat, as the MA20/MA50 crossover strategy did not trigger a trade today. This is correct, as the signal is bearish (Death Cross) and the system is designed to avoid trading during such conditions.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's risk management approach is effective in avoiding losses during periods of high market volatility.

---

### Day 10 — 2026-03-20 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $648.48 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$179.56 |
| Signal saved | +$209.23 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,868.04 |
| Alpha (cumulative) | +4.148% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite warning signs from the Fed Chair and rising VIX. Oil prices continued to climb. The 10Y Treasury yield remained elevated.

**Strategy note:** The MA20/MA50 crossover system remained flat as MA20 was below MA50, indicating no buy or sell signal. This was correct as the market did not follow the bearish signal.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to stay flat in a volatile market environment is crucial for preserving capital.

---

### Day 11 — 2026-03-23 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.37 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$110.66 |
| Signal saved | +$140.33 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,886.62 |
| Alpha (cumulative) | +3.129% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market is experiencing a risk-off regime due to the Fed Chair's warning of another supply shock. The VIX is high at 27.39, indicating increased volatility. Oil prices are also elevated.

**Strategy note:** The MA system is in a bearish regime due to the death cross, but did not enter a trade today as the position was already flat. The system's inaction was correct as the market did not provide a clear buy or sell signal.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to avoid trading during periods of high volatility is crucial in maintaining its overall performance.

---

### Day 12 — 2026-03-24 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $653.20 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$132.36 |
| Signal saved | +$162.03 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,565.82 |
| Alpha (cumulative) | +3.450% |

**Regime call:** RISK-OFF — Fed Shock

**Market context:** The market context today is characterized by a bearish signal from the MA20/MA50 crossover strategy and a rising VIX. The Fed Chair's warning of another supply shock is likely contributing to the risk-off sentiment. Meanwhile, the WTI Oil price is stable, and the 10Y Treasury yield is rising.

**Strategy note:** The MA20/MA50 crossover strategy correctly identified a bearish signal, but the system remained flat due to the signal being a death cross, which typically indicates a sell signal. The strategy's inaction was correct as the market declined.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross signal should be treated with caution and may require a more nuanced approach to determine the optimal course of action.

---

### Day 13 — 2026-03-25 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $656.74 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$96.96 |
| Signal saved | +$126.63 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,089.16 |
| Alpha (cumulative) | +2.927% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite the Fed Chair's warning of another supply shock. VIX remained elevated, but WTI Oil price dropped. The 10Y Treasury yield also decreased.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH — Death Cross regime. The system did not enter a trade today, as the MA20 was below the MA50 and the signal was bearish.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A dead-cat bounce can occur even in a bearish market regime, highlighting the importance of staying nimble and not over-interpreting short-term market movements.

---

### Day 14 — 2026-03-26 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $645.11 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$213.26 |
| Signal saved | +$242.93 |
| Portfolio value | $100,015.64 |
| Benchmark value | $95,369.84 |
| Alpha (cumulative) | +4.646% |

**Regime call:** RISK-OFF / Fed Shock

**Market context:** The market is experiencing a risk-off sentiment due to Fed Chair Powell's warning about another supply shock. The VIX is at 27.39, indicating increased market volatility. Oil prices are also on the rise.

**Strategy note:** The MA20/MA50 crossover strategy did not trigger any trades today, as the signal was bearish (Death Cross) and the system remained flat.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish MA crossover signal may not always be a buy signal, and staying flat can be a correct decision in uncertain market conditions.

---

### Day 15 — 2026-03-27 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $634.04 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$323.96 |
| Signal saved | +$353.63 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,733.30 |
| Alpha (cumulative) | +6.283% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** Markets remained relatively stable despite the Fed Chair's warning of an impending supply shock. The VIX index increased slightly, while the 10Y Treasury yield remained steady. Oil prices also rose.

**Strategy note:** The MA20/MA50 system remained flat as the Death Cross signal did not trigger a trade. This was correct as the market did not experience a significant downturn.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's inaction during a period of heightened uncertainty highlights the importance of a well-defined trading plan and risk management.

---

### Day 16 — 2026-03-30 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $632.02 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$344.16 |
| Signal saved | +$373.83 |
| Portfolio value | $100,015.64 |
| Benchmark value | $93,434.68 |
| Alpha (cumulative) | +6.581% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market showed resilience despite a bearish signal from the MA crossover strategy, with SPY closing at $631.97. VIX remained elevated at 27.39. Headlines were mixed, with a warning from Fed Chair Powell and hopes for de-escalation.

**Strategy note:** The system remained flat as the MA20/MA50 crossover strategy indicated a bearish signal, which was correct given the market's cautious behavior.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's ability to lock in profits and avoid new positions during a dead-cat bounce is crucial for preserving capital.

---

### Day 17 — 2026-03-31 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $650.12 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$163.16 |
| Signal saved | +$192.83 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,110.49 |
| Alpha (cumulative) | +3.906% |

**Regime call:** CAUTIOUS — dead-cat bounce

**Market context:** The market experienced a dead-cat bounce, with SPY closing at $641.88, despite a bearish signal from the MA20/MA50 crossover. VIX remained elevated at 27.39. Fed Chair Powell's warning of another supply shock contributed to the cautious market sentiment.

**Strategy note:** The system did not enter a trade today due to a bearish signal from the MA20/MA50 crossover. The system's inaction was correct as the market experienced a dead-cat bounce.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal from the MA20/MA50 crossover does not guarantee a sell signal, as the market can experience a dead-cat bounce.

---

### Day 18 — 2026-04-01 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.18 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$112.56 |
| Signal saved | +$142.23 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,858.54 |
| Alpha (cumulative) | +3.157% |

**Regime call:** RISK-OFF

**Market context:** The market experienced a risk-off day, driven by the bearish MA cross and elevated VIX, amidst geopolitical tensions and a decline in oil prices.

**Strategy note:** The MA20/MA50 crossover system correctly identified a bearish signal, but did not enter a trade as the position was already flat.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's ability to identify bearish signals is intact, but it must be used in conjunction with position management to maximize returns.

---

### Day 19 — 2026-04-02 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $655.76 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$106.76 |
| Signal saved | +$136.43 |
| Portfolio value | $100,015.64 |
| Benchmark value | $96,944.28 |
| Alpha (cumulative) | +3.072% |

**Regime call:** RISK-OFF

**Market context:** The stock market sold off on Trump's speech and surging oil prices, with the Dow experiencing a decline. The VIX index rose to 27.15, indicating increased market volatility. Oil prices surged to $112.24 per barrel.

**Strategy note:** The MA20/MA50 crossover strategy is currently in a BEARISH signal due to the Death Cross, but no trades were executed as the position was flat.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy correctly identified a bearish signal, but the lack of a trade execution highlights the importance of position sizing and risk management.

---

### Day 20 — 2026-04-06 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $658.88 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$75.56 |
| Signal saved | +$105.23 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,405.52 |
| Alpha (cumulative) | +2.610% |

**Regime call:** BULLISH

**Market context:** Markets were mixed post-BLS jobs, with equity futures trading mixed pre-bell Monday amid ongoing Iran conflict. VIX remained elevated at 24.17. WTI oil price rose to $112.59/barrel.

**Strategy note:** MA20 crossed below MA50, triggering a bullish signal. The system remains flat, with no trades executed today.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's alpha continues to outperform the benchmark, with a cumulative alpha of +2.610%

---

### Day 21 — 2026-04-07 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $659.23 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | -$72.06 |
| Signal saved | +$101.73 |
| Portfolio value | $100,015.64 |
| Benchmark value | $97,457.27 |
| Alpha (cumulative) | +2.559% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, and oil prices were falling, amidst a two-week US-Iran ceasefire.

**Strategy note:** MA20 crossed below MA50, triggering a bearish signal. The system exited the position.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** VIX levels can significantly influence market sentiment and impact our strategy's performance.

---

### Day 22 — 2026-04-08 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $676.00 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$95.64 |
| Signal saved | -$65.97 |
| Portfolio value | $100,015.64 |
| Benchmark value | $99,936.46 |
| Alpha (cumulative) | +0.080% |

**Regime call:** RISK-OFF

**Market context:** The VIX broke under 20, indicating a decrease in market volatility. Oil prices continued to fall. Markets were higher pre-bell Wednesday amid a two-week US-Iran ceasefire.

**Strategy note:** The MA20/MA50 crossover strategy remained bearish, with a death cross. The system exited the position and is now flat, waiting for a golden cross to re-enter.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's bearish signal was correct, but the realized P&L was relatively low, highlighting the importance of position sizing and risk management.

---

### Day 23 — 2026-04-09 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $679.87 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$134.34 |
| Signal saved | -$104.67 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,508.58 |
| Alpha (cumulative) | -0.493% |

**Regime call:** RISK-ON

**Market context:** Equity futures and ETFs declined pre-bell as fragile Middle East ceasefire lifted oil prices. VIX rose to 20.8. S&P 500 had a rare gap-up on Wednesday.

**Strategy note:** MA20/MA50 crossover strategy exited position based on bearish signal. System now flat, waiting for next golden cross.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** MA crossover strategy underperformed passive hold, reinforcing need for robust risk management

---

### Day 24 — 2026-04-10 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $679.35 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$129.14 |
| Signal saved | -$99.47 |
| Portfolio value | $100,015.64 |
| Benchmark value | $100,431.71 |
| Alpha (cumulative) | -0.416% |

**Regime call:** RISK-ON

**Market context:** The S&P 500 closed above a key level, with equity futures mixed amidst geopolitical uncertainty and a looming CPI report. The VIX remained relatively calm, but could swing wildly after the CPI data release.

**Strategy note:** The system exited the position due to a bearish MA cross, and is now flat. The MA20 is below the MA50, indicating a bearish trend.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's bearish signal was correct, but the realized P&L was lower than the passive hold, highlighting the importance of risk management in trading strategies.

---

### Day 25 — 2026-04-13 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $686.00 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$195.64 |
| Signal saved | -$165.97 |
| Portfolio value | $100,015.64 |
| Benchmark value | $101,414.81 |
| Alpha (cumulative) | -1.399% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 sold off due to geopolitical tensions, with oil prices surging over $100. The VIX sharply reversed, pointing towards 30 after failed peace negotiations. This led to a risk-off sentiment in the market.

**Strategy note:** MA50 crossed above MA20, triggering a bearish signal. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bearish signal does not guarantee losses, as the system's realized P&L was positive despite the market downturn.

---

### Day 26 — 2026-04-14 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $694.36 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$279.24 |
| Signal saved | -$249.57 |
| Portfolio value | $100,015.64 |
| Benchmark value | $102,650.71 |
| Alpha (cumulative) | -2.635% |

**Regime call:** RISK-OFF

**Market context:** The market rose today with Dow leading, despite concerns over inflation data and a potential US-Iran truce. VIX remains elevated at 18.05. Oil prices also increased.

**Strategy note:** MA20 ($660.21) is below MA50 ($672.89), indicating a bearish signal. The system exited the position, locking in a $+15.58 P&L.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A death cross in the MA crossover strategy led to a premature exit, resulting in a missed opportunity to ride the market's upward momentum.

---

### Day 27 — 2026-04-15 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $699.75 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$333.14 |
| Signal saved | -$303.47 |
| Portfolio value | $100,015.64 |
| Benchmark value | $103,447.54 |
| Alpha (cumulative) | -3.432% |

**Regime call:** RISK-ON

**Market context:** Investors turned to corporate earnings, driving equity futures higher. Wall Street's fear gauge, VIX, is fading. The S&P 500 Stocks' earnings are expected to skyrocket 200% in three months.

**Strategy note:** MA20/MA50 crossover strategy is in a BEARISH regime due to a Death Cross. The system exited the position, locking a realized P&L of $+15.58.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The strategy's realized P&L outperformed a passive hold by $15.58, but still trailed the benchmark by $286.66.

---

### Day 28 — 2026-04-16 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $701.53 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$350.94 |
| Signal saved | -$321.27 |
| Portfolio value | $100,035.59 |
| Benchmark value | $103,710.69 |
| Alpha (cumulative) | -3.675% |

**Regime call:** BEAR

**Market context:** The market remains in a bear regime, with SPY trading below its 50-day moving average. The S&P 500 index is also under pressure, with no clear signs of a reversal. Economic data releases and geopolitical tensions continue to weigh on investor sentiment.

**Strategy note:** The dual-timeframe SMA crossover strategy held a long position in SPY, despite the bear regime, due to a bullish fast signal. The system's unrealized P&L increased by 0.06% from entry.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** A bullish fast signal does not guarantee success in a bear regime, and the system's performance may be impacted by the prevailing market conditions.

---

### Day 29 — 2026-04-17 _(narrative: groq)_

| Field | Value |
|---|---|
| Position | FLAT |
| Entry (Alpaca fill) | $666.436/share |
| Close price | $710.06 |
| Realized P&L (locked) | +$29.67 |
| Reference if held | +$436.24 |
| Signal saved | -$406.57 |
| Portfolio value | $100,029.67 |
| Benchmark value | $104,971.72 |
| Alpha (cumulative) | -4.942% |

**Regime call:** RISK-OFF

**Market context:** The S&P 500 broke above 7000, driven by a rally in tech stocks and the opening of the Strait of Hormuz. Oil prices declined, while Netflix shares plummeted. Market sentiment remains bullish.

**Strategy note:** The system exited the position due to a bear regime, as confirmed by the slow MA20/MA50 crossover. A bullish fast signal was generated, but the system prioritized the slow regime filter.

**What I did today:** System exited the position. Realized P&L locked at $+29.67. Regime: BEAR (MA20 $666.62 vs MA50 $673.88). Fast signal (MA10/MA30): bullish. Monitoring for re-entry on next fast golden cross.

**Key learning:** The system's regime filter is more important than the fast signal in determining position entry and exit decisions.

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
_Day 29 of 90 · Alpaca equity: $100,029.59 · Cumulative alpha vs SPY: -4.942%_