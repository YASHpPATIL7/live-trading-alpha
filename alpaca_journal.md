
Mar 9  (Day 1): Trump said Iran war "pretty much complete" → market rallied
                SPY closes UP +0.71% → you enter at $678.27 on a green day

Mar 10 (Day 2): Persian Gulf strikes continue, bond yields rise → SPY -0.21%
Mar 11 (Day 3): Oil pressure persists, IEA releases reserves → SPY -0.08%
Mar 12 (Day 4): Oil hits $100/barrel, US futures falling on oil fears → SPY -1.07%

## Day 4 — March 12, 2026

- Position: Long SPY 10 shares (held)
- Entry price (Day 1): $678.27/share
- Close price (Mar 12): $669.16/share
- Shares: 10
- Capital deployed: $6,782.70 (6.78% of portfolio)
- Unrealized P&L: -$91.05
- P&L %: -1.342%
- Portfolio value: $99,908.95

- Regime call: RISK-OFF / Geopolitical shock
- Market context:
  Oil crossed $100/barrel today (WTI). S&P 500 -1.07%.
  US-Iran war continuing despite Trump's "complete" declaration Mar 9.
  Strait of Hormuz disruption → tankers halted → supply shock.
  NFP Feb came in at -92K jobs (expected +58K) — missed by 150K.
  Unemployment ticked up to 4.4%. Stagflation narrative fully active.
  Fed June cut odds collapsing. Bond yields rising.
  SPY erased all 2026 gains as of last week — currently at
  3-month lows. This is not a trending market. This is a shock market.

- Strategy note: No signal fired. No action. Holding.
  SMA crossover has zero mechanism for oil shocks or geopolitical risk.
  This is not a strategy failure — it's a regime mismatch.
  The baseline strategy was never designed to win in this environment.
  It was designed to run for 90 days and generate a verifiable record.
  Alpha-Core HMM in Week 7 classifies regimes like this and
  reduces position sizing or exits entirely when in "shock regime."
  That's the upgrade. This week is the proof of why it's needed.

- What I did today (non-Alpaca):
  Project 1: Linear Regression — RELIANCE 5y price prediction.
  Ridge vs Linear comparison. R² + RMSE + residual analysis.
  Metrics for Andrew Ng evaluation metrics — R², RMSE, confusion
  matrix, ROC/AUC, Precision/Recall/F1 — mapped to exact
  ML Specialization C1 lectures (W1, W2, W3).
  Alpaca journal automation script fixed:
  - end = today + 1 day (auto-inclusive)
  - float(entry_price.iloc[0]) fixes FutureWarning

- Key learning today:
  You entered SPY on the day Trump declared war "complete."
  The market believed him for exactly one day.
  Real trading lesson: geopolitical catalysts are not binary events.
  The HMM regime detection model needs at minimum 2 inputs
  that this strategy is blind to:
  1. Oil price level and direction (macro regime input)
  2. Credit spread (VIX proxy — fear gauge)
  Adding these as features to Alpha-Core is now in anomaly journal.

- Anomaly journal entry #002:
  SMA crossover bled -1.34% in 4 days during oil shock regime.
  Hypothesis: oil price momentum negatively correlated with
  SPY returns during geopolitical events.
  If confirmed → crude oil returns should be a feature in
  Alpha-Core's HMM state transition matrix.
  Status: Open — test in Week 7.

- Tomorrow (Day 5 — Mar 13):
  Project 2: Logistic Regression, Give Me Some Credit dataset
  AUC target 0.83, confusion matrix, ROC c

  - Automation update (Day 4 evening):
  Deployed SMA 20/50 crossover script (AlpacaDaily.py).
  First run: MA20=$682.48 < MA50=$686.92 → Death Cross confirmed.
  Position automatically closed. Now FLAT.
  Realized P&L: -$91.10
  Strategy working as designed — exits on bearish signal.
  Will re-enter when MA20 crosses above MA50 (Golden Cross).
  Next run: tomorrow after 9:30 PM IST.

## Day 5 — March 13, 2026

- Position: FLAT (SMA crossover exited on Mar 12 evening)
- Entry price (Day 1): $678.27/share
- Close price (Mar 13): $662.29/share
- Shares: 0 (position closed by signal)
- Realized P&L: -$91.05 (locked in on Mar 12 exit)
- Portfolio value: $99,908.95

- Regime call: BEARISH — confirmed
- Market context:
  SPY hit $661.36 intraday — 1-month low, erasing all 2026 gains.
  S&P 500 now 100% bearish per Ichimoku cloud analysis —
  two consecutive closes below the cloud confirmed downtrend.
  Put/call ratio on SPY options: 52% puts vs 48% calls —
  institutional hedging accelerating.
  Iran war continuing. Oil above $100. Stagflation narrative
  fully priced in. Fed rate cut odds for June near zero.
  Trump made ambiguous "war over soon" comment — brief
  intraday spike then immediate reversal. Market doesn't
  believe the headline anymore.

- Strategy note:
  SMA crossover correctly exited on Mar 12 before today's
  further -0.56% drop. If I had held manually: -$159.80 loss.
  By following the signal: realized only -$91.05.
  Signal saved $68.75 vs emotional holding.
  This is why process beats gut feeling.
  Currently FLAT — waiting for MA20 > MA50 re-entry signal.
  No Golden Cross in sight given current tape.

- What I did today (non-Alpaca):
  Project 2: Logistic Regression — Give Me Some Credit dataset.
  AUC achieved: target 0.83.
  Confusion matrix, ROC curve, Precision/Recall/F1 complete.
  Key finding: lowered threshold (0.5 → 0.3) improved Recall
  at cost of Precision — correct trade-off for credit risk
  (missing a real default costs more than a false alarm).
  DSA: Two Sum ✅, Best Time to Buy/Sell Stock ✅,
  Contains Duplicate ✅ — 3 problems done.
  Projects 1 + 2 pushed to GitHub with READMEs + AIWORKFLOW.md.

- Key learning today:
  The signal exited before the bottom. That's not luck.
  That's the system doing exactly what it was designed to do.
  The lesson: trust the process even when it feels wrong.
  On Mar 12 at 8 PM IST when signal said SELL, position was
  only -$91. Holding felt tempting. Signal was right.
  Today would have been -$159.80.

- Anomaly journal entry #003:
  Trump geopolitical headline caused intraday spike then reversal.
  Market is discounting presidential statements on war status.
  This is a regime property — news credibility decay.
  Hypothesis: sentiment signal (FinBERT on presidential statements)
  + volume spike = false breakout detector.
  Alpha-Core Week 7: add FinBERT news gate for geopolitical events.
  Status: Open.

- Tomorrow (Day 6 — Mar 16, Monday):
  Run AlpacaDaily.py after 9:30 PM IST.
  Project 3: Decision Tree — BUY/HOLD/SELL signals.
  Week 2 begins: XGBoost, LSTM Nifty Forecaster, K-Means dashboard.

---

## Day 6 — March 16, 2026

- Position: FLAT (no re-entry signal fired)
- Entry price (Day 1): $678.27/share
- Close price (Mar 16): $668.86/share
- Shares: 0
- Unrealized P&L on original entry (reference only): -$94.10
- Realized P&L (locked): -$91.05
- Portfolio value: $99,908.95

- Regime call: BEARISH with bounce — not confirmed reversal
- Market context:
  SPY recovered from $661.36 low (Mar 13) to $668.86 today.
  +1.0% bounce on Mar 16 — triggered by Trump comment
  that Iran war "will be over very soon."
  Technical analysts flagging: bounce expected but not sustainable.
  Resistance at $672x — any close above that level needed
  to start calling this a reversal vs a dead-cat bounce.
  S&P 500 still below 200-day SMA. Weekly chart still bearish.
  Goldman Sachs maintained year-end target of 7,600 —
  but that's a Dec 2026 view, not a March view.
  MACD and Stochastic RSI both deeply bearish on weekly chart.
  Next support zone if bounce fails: $640–650 range.

- Strategy note:
  MA20 = $682.48, MA50 = $686.92 as of last check.
  Both MAs above current price → still in Death Cross territory.
  No re-entry signal fired. FLAT is correct positioning.
  Today's bounce (+$6.57 from Friday) does NOT flip the signal.
  The MA cross needs sustained price recovery over several days
  to bring MA20 back above MA50.
  Estimated re-entry: not before late March at earliest
  given current trajectory.

- What I did today (non-Alpaca):
  Week 2 begins.
  AlpacaDaily.py run — confirmed FLAT, no signal.
  Journal entries Days 5-6 written and committed.
  Caught up on all outstanding journal entries.

- Key learning today:
  One green day in a downtrend is not a reversal.
  The difference between a bounce and a reversal:
  → Bounce: price recovers but MAs still point down
  → Reversal: price AND MAs both turn upward
  The strategy waits for the MA confirmation, not the price move.
  This prevents re-entering too early into a bear trap.

- Tomorrow (Day 7 — Mar 17):
  Run AlpacaDaily.py after 9:30 PM IST.
  Project 3: Decision Tree — BUY/HOLD/SELL (if not done today).
  Project 4: Random Forest — ensemble improvement DT→RF.
  Push to GitHub with READMEs + AIWORKFLOW.md.

## Day 7 — March 17, 2026 (Monday)

- Position: FLAT (SMA crossover exited Mar 12)
- Entry price (Day 1 reference): $678.27/share
- Close price (Mar 17): $670.79/share
- Unrealized P&L (reference only): -$74.80
- Realized P&L (locked): -$91.05 (exited Mar 12)
- Portfolio value: $99,925.20

- Regime call: CAUTIOUS — dead cat bounce, not confirmed reversal
- Market context:
  SPY +$1.76 (+0.26%) on the day. Modest green session.
  Oil pulled back slightly from $100 → markets exhaled briefly.
  S&P 500 rose 0.7% in early trading — "strongest session since
  conflict began" per market commentary.
  However: oil back above $95 by afternoon → gains faded.
  Fed meeting March 18-19 looming. No one expects a cut.
  10-year Treasury yield sitting at 4.20% — still elevated.
  Technology stocks (Nvidia) led gains. Jensen Huang announced
  $1 trillion in Blackwell + Vera Rubin orders — doubled YoY.
  Gold at $5,019. Bitcoin -$980. Risk-off under the surface.

- Strategy note:
  MA20 still below MA50. Death Cross intact. No re-entry signal.
  One green day in a downtrend ≠ reversal. Strategy correctly flat.
  Holding cash while everyone tries to call the bottom.
  This is the hardest part of rule-based trading — doing nothing
  feels wrong. The model says doing nothing is right.

- What I did today:
  AlpacaDaily.py run — FLAT confirmed, no signal.
  Journal catch-up in progress.

- Key learning today:
  Technology can rally during a geopolitical/oil shock if
  the catalyst is company-specific (Nvidia orders).
  Macro bears and sector bulls can coexist.
  A diversified portfolio would have partially hedged this.
  Pure SPY = full beta exposure to the macro shock with
  no offset from tech alpha. Lesson for Alpha-Core: sector
  weighting matters, not just regime state.

---

## Day 8 — March 18, 2026 (Wednesday)

- Position: FLAT
- Entry price (Day 1 reference): $678.27/share
- Close price (Mar 18): $661.43/share
- Unrealized P&L (reference): -$168.40 (-2.483%)
- Realized P&L (locked): -$91.05
- Portfolio value: $99,831.60

- Regime call: RISK-OFF / Hawkish Fed + Oil shock compounding
- Market context:
  FOMC decision day. Fed held rates at 3.5–3.75%. No cut.
  Powell's statement: "limited progress on taming inflation,
  uncertainties from Iran conflict driving oil higher,
  no signal of imminent rate ease." Exactly the worst outcome.
  S&P 500 dropped -1.36% to 6,624.70. Dow -768 points (-1.63%).
  Nasdaq -1.46%. All major indices closed down over -1%.
  Middle East attacks targeted energy infrastructure directly —
  oil spiked on supply disruption fears.
  PPI (producer prices) came in hotter than expected.
  Three simultaneous headwinds: oil up, rates sticky, PPI hot.
  This is the stagflation trifecta. Market had no defence.

- Strategy note:
  Signal still FLAT. Correct.
  If position had been held from Day 1: -$168.40 today.
  Actual realized loss: -$91.05.
  Signal has now saved $77.35 vs a hold-and-hope approach.
  The cost of being flat = missing any future recovery.
  The benefit of being flat = not losing more in drawdown.
  For a 90-day process-building exercise, flat is exactly right.

- Anomaly journal entry #004:
  Fed hawkishness + oil shock = compounding negative event.
  Neither alone would cause -1.36% in a day.
  The interaction between macro regime inputs is non-linear.
  HMM in Alpha-Core Week 7 needs at minimum 3 state inputs:
  1. Oil price direction (energy shock proxy)
  2. Fed stance delta (hawkish/neutral/dovish shift)
  3. Credit spreads / VIX level (fear gauge)
  When all three align bearish → risk of -1%+ day is high.
  Status: Open — formalise as feature set in Week 7.

- Key learning today:
  The Fed is trapped. Cut rates → inflation + oil = worse inflation.
  Hold rates → growth slows, market re-rates lower.
  This is a regime the SMA crossover was never designed for.
  It's also a regime the market hasn't priced correctly yet.
  When the Fed is trapped, downside risk is asymmetric.

---

## Day 9 — March 19, 2026 (Thursday)

- Position: FLAT
- Entry price (Day 1 reference): $678.27/share
- Close price (Mar 19): $659.80/share
- Unrealized P&L (reference): -$184.70 (-2.723%)
- Realized P&L (locked): -$91.05
- Portfolio value: $99,815.30

- Regime call: BEARISH — four-month lows, no floor found
- Market context:
  SPY hit four-month lows. S&P 500 threatening to breach
  recent support. Middle East attacks continued to target
  energy infrastructure. Oil supply chain disruption = structural,
  not temporary. Market beginning to price in extended conflict.
  Stocks "down again, threatening lows" per Schwab morning note.
  10-year Treasury yield rose to 4.30% (+4bps) — bond market
  agrees with the bearish equity narrative.
  USD Index flat at 100.01. Gold elevated. Risk-off confirmed.

- Strategy note:
  Day 9. SPY is -$18.47 from entry. Portfolio at $99,815.
  If held entire time: -$184.70 unrealized loss.
  Actual locked loss: -$91.05 (exited on signal Mar 12).
  Signal has now saved $93.65 vs a passive hold.
  That's 1.38% of the original deployed capital saved
  by following a simple rule-based exit. No emotion.
  No "it'll come back." Just the signal.
  This is the 90-day record being built in real time.
  At job interview: "My model exited before the Fed shock
  and saved 51% of the unrealized drawdown. Here's the log."

- What I did today:
  AlpacaDaily.py run — FLAT, no signal.
  Journal Days 7-9 written and committed.
  FutureWarning in AlpacaDaily.py — fix below.

- Key learning today:
  -$184.70 vs -$91.05. That's not luck. That's process.
  The signal exited on a Death Cross. Death Cross fired
  before: the Fed meeting, the energy infrastructure attack,
  the four-month low. The MA system isn't smart.
  It doesn't know about Powell. It doesn't know about oil.
  It just knows price structure. And price structure warned first.
  This is why technical signals exist — they encode fear
  before the fundamental news arrives on your screen.

- Tomorrow (Day 10 — Mar 20):
  AlpacaDaily.py run after 1:30 AM IST.
  Projects 3-4 (Decision Tree + Random Forest) if not complete.
  Push GitHub commits. Journal Day 10.
