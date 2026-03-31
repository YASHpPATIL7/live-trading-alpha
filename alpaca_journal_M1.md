======================================================================
ALPACA PAPER JOURNAL — SPY
SOURCE OF TRUTH: Alpaca fills only. No yfinance prices used for P&L.
======================================================================
⚠️  RECONCILIATION NOTE (added retroactively):
    Days 1–4 narrative entries were originally written using
    $678.27 as entry price (Day 1 yfinance close — incorrect).
    Actual Alpaca fill: $666.436/share (after-hours, Mar 9).
    All P&L figures below use $666.436 as entry.
    Close prices use yfinance EOD via automated script.
======================================================================

Actual Entry:         $666.436/share  (Alpaca fill, Mar 9 after-hours)
Actual Exit:          $667.994/share  (Alpaca fill, Mar 13 premarket)
Realized P&L:         +$15.58  (+0.023% on $100k portfolio)
Exit reason:          MA20 crossed below MA50 — Death Cross (Mar 12 detection)
Shares:               10 SPY
Capital deployed:     $6,664.36  (6.66% of portfolio)

======================================================================
MASTER TABLE
======================================================================
          Date  SPY_Close       Status  Unrealized_PnL  PnL_Pct  Portfolio_Value
Day 1   Mar 09     676.42  Long 10 SPY          +99.84   +0.100%       100,099.84
Day 2   Mar 10     675.34  Long 10 SPY          +89.04   +0.089%       100,089.04
Day 3   Mar 11     674.49  Long 10 SPY          +80.54   +0.081%       100,080.54
Day 4   Mar 12     664.25  Long 10 SPY          -21.86   -0.022%        99,978.14
Day 5   Mar 13     660.49         FLAT            0.00    0.000%       100,015.58 ← exit filled
Day 6   Mar 16     667.21         FLAT            0.00    0.000%       100,015.58
Day 7   Mar 17     668.96         FLAT            0.00    0.000%       100,015.58
Day 8   Mar 18     659.63         FLAT            0.00    0.000%       100,015.58
Day 9   Mar 19     658.00         FLAT            0.00    0.000%       100,015.58
Day 10  Mar 20     648.57         FLAT            0.00    0.000%       100,015.58
Day 11  Mar 23     655.41         FLAT            0.00    0.000%       100,015.58

======================================================================
BENCHMARK vs STRATEGY (SPY buy-and-hold from Day 1 close $676.42)
Benchmark shares: 147.84
======================================================================
          Strategy_Value  Benchmark_Value  Strategy_Return  Benchmark_Return  Alpha
Day 1         100,099.84       100,000.00           +0.100%           +0.000%  +0.100%
Day 2         100,089.04        99,840.34           +0.089%           -0.160%  +0.249%
Day 3         100,080.54        99,714.67           +0.081%           -0.285%  +0.366%
Day 4          99,978.14        98,200.82           -0.022%           -1.799%  +1.777%
Day 5         100,015.58        97,644.95           +0.016%           -2.355%  +2.371%
Day 6         100,015.58        98,638.42           +0.016%           -1.362%  +1.378%
Day 7         100,015.58        98,897.13           +0.016%           -1.103%  +1.119%
Day 8         100,015.58        97,517.81           +0.016%           -2.482%  +2.498%
Day 9         100,015.58        97,276.84           +0.016%           -2.723%  +2.739%
Day 10        100,015.58        95,882.74           +0.016%           -4.117%  +4.133%
Day 11        100,015.58        96,893.94           +0.016%           -3.106%  +3.122%

======================================================================
SIGNAL SAVED — Reference only (what unrealized P&L would be if held)
======================================================================
          SPY_Close  IfHeld_PnL  Signal_Saved  Note
Day 1        676.42      +99.84        -84.26  Holding better (still long, no comparison yet)
Day 2        675.34      +89.04        -73.46  Holding better
Day 3        674.49      +80.54        -64.96  Holding better
Day 4        664.25      -21.86        +37.44  Signal better — exit signalled this evening
Day 5        660.49      -59.46        +75.04  Signal better — exit filled at $667.994
Day 6        667.21       +7.74         +7.84  ← SPY bounced, holding briefly better on paper
Day 7        668.96      +25.24         -9.66  ← SPY bounced further — holding would've been
                                               $9.66 better on this day. Honest entry.
Day 8        659.63      -68.06        +83.64  Signal better — Fed shock hit
Day 9        658.00      -84.36        +99.94  Signal better — new lows
Day 10       648.57     -178.66       +194.24  Signal better — SPY continues lower
Day 11       655.41     -110.26       +125.84  Signal better — still well below entry


======================================================================
## Day 1 — March 9, 2026 (Monday)
======================================================================
- Position:              Long 10 SPY
- Actual entry fill:     $666.436/share  (Alpaca, after-hours Mar 9)
  ⚠️  Note: Signal triggered at close. Order filled after-hours at
      $666.436, not at the $676.42 closing price. This is the
      after-hours gap problem documented in Error 006.
- Close price (Mar 9):   $676.42
- Shares:                10
- Capital deployed:      $6,664.36  (6.66% of portfolio)
- Unrealized P&L:        +$99.84  (vs close)
- P&L %:                 +0.100%
- Portfolio value:       $100,099.84

- Regime call:           RISK-ON / Geopolitical relief
- Market context:
  Trump said Iran war "pretty much complete" → market rallied.
  SPY closes UP +0.71%. System enters on green day.
  Entry is after-hours at $666.436 — $9.98 below the close.
  This is the first lesson: after-hours fills vs close prices.

- Strategy note:
  SMA crossover fired. Entry executed. Process begins.
  Note for backtest: entry price = $666.436, not $676.42.

======================================================================
## Day 2 — March 10, 2026 (Tuesday)
======================================================================
- Position:              Long 10 SPY (held)
- Entry price:           $666.436/share
- Close price (Mar 10):  $675.34
- Shares:                10
- Unrealized P&L:        +$89.04
- P&L %:                 +0.089%
- Portfolio value:       $100,089.04
- Benchmark (if B&H):    $99,840.34  |  Alpha today: +0.249%

- Regime call:           CAUTIOUS — first cracks appearing
- Market context:
  Persian Gulf strikes continue. Bond yields rise. SPY -0.21%.
  Still long. Still positive. Signal says hold.

======================================================================
## Day 3 — March 11, 2026 (Wednesday)
======================================================================
- Position:              Long 10 SPY (held)
- Entry price:           $666.436/share
- Close price (Mar 11):  $674.49
- Unrealized P&L:        +$80.54
- P&L %:                 +0.081%
- Portfolio value:       $100,080.54
- Benchmark (if B&H):    $99,714.67  |  Alpha today: +0.366%

- Regime call:           CAUTIOUS — oil pressure building
- Market context:
  IEA releases reserves. Oil pressure persists. SPY -0.08%.
  Position still positive. Trend weakening but MA not crossed.
  No action. Correct.

======================================================================
## Day 4 — March 12, 2026 (Thursday)
======================================================================
- Position:              Long 10 SPY (held through close, exited same evening)
- Entry price:           $666.436/share
- Close price (Mar 12):  $664.25
- Shares:                10
- Capital deployed:      $6,664.36
- Unrealized P&L:        -$21.86  (at close)
- P&L %:                 -0.022%
- Portfolio value:       $99,978.14  (at close, before exit fill)
- Benchmark (if B&H):    $98,200.82  |  Alpha today: +1.777%

- Regime call:           RISK-OFF / Geopolitical shock
- Market context:
  Oil crossed $100/barrel. S&P 500 -1.07%.
  US-Iran war continuing. Strait of Hormuz disruption.
  NFP Feb: -92K jobs (expected +58K). Missed by 150K.
  Unemployment ticked to 4.4%. Stagflation narrative active.
  Fed June cut odds collapsing. Bond yields rising.
  SPY erased all 2026 gains. Three-month lows.
  This is not a trending market — it's a shock market.

- Strategy note:
  No signal at open or during session. Held through close.
  SMA crossover has zero mechanism for oil shocks or
  geopolitical events. This is not a failure — it's a regime
  mismatch. The strategy was designed to run 90 days and
  generate a verifiable record. Alpha-Core Week 7 classifies
  regimes like this and exits during "shock regime."
  This week is the proof of why that upgrade is needed.

- Evening (9:31 PM IST / post-close EST):
  AlpacaDaily.py deployed and run for first time.
  MA20 = $682.48, MA50 = $686.92 → MA20 < MA50.
  DEATH CROSS detected. SELL signal generated.
  Sell order placed (limit, extended_hours=True).
  ⚠️  Earlier draft noted "Realized P&L: -$91.10" — this was
      wrong. It used $678.27 as entry (Day 1 yfinance close).
      Actual fill happened next session. See Day 5.

- What I did today:
  Project 1: Linear Regression — RELIANCE 5y price prediction.
  Ridge vs Linear comparison. R² + RMSE + residual analysis.
  Metrics mapped: R², RMSE, ROC/AUC, Precision/Recall/F1
  → mapped to Andrew Ng ML Specialization C1 lectures (W1-W3).
  Alpaca journal automation script fixed:
  → end = today + 1 day (auto-inclusive)
  → float(entry_price.iloc[0]) fixes FutureWarning

- Key learning today:
  Entered SPY on the day Trump declared war "complete."
  Market believed him for exactly one day.
  Real lesson: geopolitical catalysts are not binary events.
  HMM regime model needs at minimum 2 inputs this strategy
  is blind to:
  1. Oil price level and direction (macro regime input)
  2. Credit spread / VIX (fear gauge)

- Anomaly journal entry #002:
  SMA crossover in unrealized drawdown during oil shock.
  Hypothesis: oil price momentum negatively correlated with
  SPY returns during geopolitical events.
  → crude oil returns should be a feature in HMM state matrix.
  Status: Open — test in Week 7.

======================================================================
## Day 5 — March 13, 2026 (Friday)
======================================================================
- Position:              FLAT (sell order from Day 4 evening filled)
- Entry price:           $666.436/share
- Exit fill price:       $667.994/share  (Alpaca, premarket Mar 13)
- Close price (Mar 13):  $660.49
- Shares at exit:        10
- Realized P&L:          +$15.58  (+0.023%)
  Calculation: ($667.994 − $666.436) × 10 = +$15.58
- Portfolio value:       $100,015.58  ← Alpaca source of truth
- Benchmark (if B&H):   $97,644.95  |  Alpha: +2.371%

- Exit note:
  Sell order was placed as limit/extended-hours on Day 4 evening.
  Fill of $667.994 occurred in premarket Mar 13 — significantly
  above the Day 5 close of $660.49. The system exited at a
  better price than end-of-day, before the day's decline.
  If held to close: unrealized = (660.49 - 666.436) × 10 = -$59.46
  Signal saved vs holding to close: +$15.58 − (−$59.46) = +$75.04

- Regime call:           BEARISH — confirmed
- Market context:
  SPY hit $661.36 intraday — 1-month low, erasing all 2026 gains.
  S&P 500 100% bearish per Ichimoku — two consecutive closes
  below the cloud confirm downtrend.
  Put/call ratio: 52% puts / 48% calls — institutional hedging.
  Iran war continuing. Oil above $100. Stagflation priced in.
  Fed rate cut odds for June near zero.
  Trump made ambiguous "war over soon" comment — brief intraday
  spike then immediate reversal. Market no longer believes it.

- Strategy note:
  Exit filled at $667.994 before today's further -0.56% decline.
  Signal detected Death Cross on Day 4, executed on Day 5.
  Doing nothing after this exit is the correct position.
  No Golden Cross in sight given current tape.
  Waiting for MA20 > MA50.

- Key learning today:
  Trust the process even when it feels wrong.
  On Day 4 evening the position was only -$21.86 unrealized.
  Holding felt tempting. The signal was right.
  Today's close: $660.49. Holding would be -$59.46.
  Process beats gut feeling.

- What I did today:
  Project 2: Logistic Regression — Give Me Some Credit dataset.
  AUC achieved: 0.83.
  Confusion matrix, ROC curve, Precision/Recall/F1 complete.
  Key finding: threshold 0.5 → 0.3 improved Recall at cost of
  Precision — correct for credit risk (missing real default
  costs more than a false alarm).
  DSA: Two Sum ✅, Best Time to Buy/Sell Stock ✅,
  Contains Duplicate ✅ — 3 problems.
  Projects 1 + 2 pushed to GitHub with READMEs + AIWORKFLOW.md.

- Anomaly journal entry #003:
  Trump geopolitical headline → intraday spike then reversal.
  Market discounting presidential statements on war status.
  This is a regime property — news credibility decay.
  Hypothesis: FinBERT on presidential statements + volume spike
  = false breakout detector.
  Alpha-Core Week 7: add FinBERT news gate for geopolitical events.
  Status: Open.

======================================================================
## Day 6 — March 16, 2026 (Monday)
======================================================================
- Position:              FLAT
- Entry price ref:       $666.436/share
- Close price (Mar 16):  $667.21
- Realized P&L (locked): +$15.58
- Portfolio value:       $100,015.58
- Benchmark (if B&H):   $98,638.42  |  Alpha: +1.378%
- Reference (if held):  (667.21 − 666.436) × 10 = +$7.74
  Note: SPY bounced today. If still holding, unrealized would
  be +$7.74 — less than our locked +$15.58. FLAT still better.

- Regime call:           BEARISH with bounce — not confirmed reversal
- Market context:
  SPY recovered from $661.36 (Mar 13 low) to $667.21.
  +1.0% bounce triggered by Trump comment: "war will be over soon."
  Resistance at $672 — close above that level needed to call
  reversal vs dead-cat bounce.
  S&P 500 still below 200-day SMA. Weekly chart still bearish.
  MACD + Stochastic RSI both deeply bearish on weekly.
  Goldman maintained year-end 7,600 target (Dec 2026 view, not now).
  Next support if bounce fails: $640–650.

- Strategy note:
  MA20 = $682.48, MA50 = $686.92. Death Cross intact.
  One green day in a downtrend ≠ reversal.
  Re-entry needs sustained price recovery over several sessions
  to bring MA20 back above MA50.
  Estimated re-entry: not before late March at earliest.

- Key learning today:
  One green day in a downtrend is not a reversal.
  Bounce = price recovers but MAs still point down.
  Reversal = price AND MAs both turn upward.
  Strategy waits for MA confirmation, not price move.
  Prevents re-entering too early into a bear trap.

======================================================================
## Day 7 — March 17, 2026 (Tuesday)
======================================================================
- Position:              FLAT
- Close price (Mar 17):  $668.96
- Realized P&L (locked): +$15.58
- Portfolio value:       $100,015.58
- Benchmark (if B&H):   $98,897.13  |  Alpha: +1.119%
- Reference (if held):  (668.96 − 666.436) × 10 = +$25.24
  ⚠️  Honest note: If still holding today, unrealized would be
      +$25.24 — $9.66 MORE than our realized +$15.58.
      On this day, the exit cost us $9.66 vs holding.
      This is a valid data point. Two-day bounces after death
      crosses are common before the next leg down.
      The system is designed to avoid the next leg down,
      not to optimise the bounce exit. Process is correct.

- Regime call:           CAUTIOUS — dead-cat bounce, not reversal
- Market context:
  SPY +$1.76 (+0.26%). Oil pulled back from $100 briefly.
  Nvidia announced $1 trillion Blackwell + Vera Rubin orders.
  Jensen Huang keynote drove tech gains.
  Oil back above $95 by afternoon — gains faded.
  Fed meeting March 18-19. No cut expected.
  10-year yield: 4.20%. Gold at $5,019. Bitcoin -$980.
  Risk-off under the surface despite tech strength.

- Strategy note:
  MA20 still below MA50. No re-entry signal. FLAT is correct.
  Tech can rally on company-specific catalysts during a
  macro shock. Macro bears + sector bulls can coexist.
  Pure SPY = full beta to macro shock, no tech offset.
  Lesson for Alpha-Core: sector weighting matters, not just
  regime state.

- Key learning today:
  One green day in a downtrend is still not a reversal.
  The system correctly holds cash while market tries to
  call the bottom. Doing nothing IS the strategy.

======================================================================
## Day 8 — March 18, 2026 (Wednesday)
======================================================================
- Position:              FLAT
- Close price (Mar 18):  $659.63
- Realized P&L (locked): +$15.58
- Portfolio value:       $100,015.58
- Benchmark (if B&H):   $97,517.81  |  Alpha: +2.498%
- Reference (if held):  (659.63 − 666.436) × 10 = −$68.06
  Signal saved vs holding: +$15.58 − (−$68.06) = +$83.64

- Regime call:           RISK-OFF / Hawkish Fed + Oil compounding
- Market context:
  FOMC decision: Fed held at 3.5–3.75%. No cut.
  Powell: "limited progress on inflation, Iran conflict driving
  oil higher, no signal of imminent rate ease."
  S&P 500 -1.36% to 6,624.70. Dow -768 pts (-1.63%). Nasdaq -1.46%.
  Middle East attacks targeted energy infrastructure directly.
  PPI came in hotter than expected.
  Three simultaneous headwinds: oil up, rates sticky, PPI hot.
  Stagflation trifecta. Market had no defence.

- Strategy note:
  Signal has saved $83.64 vs passive hold at today's close.
  The cost of being flat = missing any future recovery.
  The benefit = not losing more in drawdown.
  For a 90-day process-building record, flat is exactly right.

- Anomaly journal entry #004:
  Fed hawkishness + oil shock = compounding negative event.
  Neither alone would cause -1.36%. Interaction is non-linear.
  HMM in Alpha-Core Week 7 needs 3 state inputs:
  1. Oil price direction (energy shock proxy)
  2. Fed stance delta (hawkish/neutral/dovish shift)
  3. Credit spreads / VIX (fear gauge)
  When all three align bearish → risk of -1%+ day is high.
  Status: Open — formalise as feature set in Week 7.

- Key learning today:
  The Fed is trapped. Cut → inflation + oil = worse inflation.
  Hold → growth slows, market re-rates lower.
  When the Fed is trapped, downside risk is asymmetric.
  This is a regime the SMA crossover was never designed for.

======================================================================
## Day 9 — March 19, 2026 (Thursday)
======================================================================
- Position:              FLAT
- Close price (Mar 19):  $658.00
- Realized P&L (locked): +$15.58
- Portfolio value:       $100,015.58
- Benchmark (if B&H):   $97,276.84  |  Alpha: +2.739%
- Reference (if held):  (658.00 − 666.436) × 10 = −$84.36
  Signal saved vs holding: +$15.58 − (−$84.36) = +$99.94

- Regime call:           BEARISH — four-month lows, no floor found
- Market context:
  SPY at four-month lows. Middle East attacks continued targeting
  energy infrastructure. Oil supply disruption = structural.
  Market beginning to price extended conflict.
  10-year yield rose to 4.30% (+4bps).
  USD Index flat at 100.01. Gold elevated. Risk-off confirmed.

- Strategy note:
  +$15.58 realized vs −$84.36 if held. That's +$99.94 saved.
  That's 1.50% of deployed capital protected by following
  one simple rule-based exit. No emotion. No "it'll come back."
  At interview: "My model exited before the Fed shock and
  protected $99.94 per $6,664 deployed. Here's the log."

- Key learning today:
  The signal exited before: the Fed meeting, the energy attack,
  the four-month low. The MA system isn't smart. It doesn't
  know about Powell or oil. It knows price structure.
  Price structure warned first.
  Technical signals encode fear before the news arrives
  on your screen. This is why they exist.

- What I did today:
  AlpacaDaily.py run — FLAT, no signal.
  Journal Days 7–9 written and committed.

======================================================================
## Day 10 — March 20, 2026 (Friday)
======================================================================
- Script run:            11:07 PM IST (12:37 PM EST — regular session)
- Session:               REGULAR ✅
- Signal:                BEARISH (MA20 $675.82 < MA50 $683.95)
- Position:              FLAT
- Action:                None — waiting for Golden Cross
- Close price (Mar 20):  $648.57  (EOD, Alpaca source)
  Note: $651.28 was intraday price at script run time (12:37 PM EST)
- Realized P&L (locked): +$15.58
- Portfolio value:       $100,015.58  (Alpaca equity confirmed)
- Benchmark (if B&H):   $95,882.74  |  Alpha: +4.133%
- Reference (if held):  (648.57 − 666.436) × 10 = −$178.66
  Signal saved vs holding: +$15.58 − (−$178.66) = +$194.24

======================================================================
TRADE #001 — CLOSED
  Entry:         Mar 09 @ $666.436/share (after-hours fill)
  Exit:          Mar 13 @ $667.994/share (Death Cross, premarket fill)
  Qty:           10 shares SPY
  Realized P&L:  +$15.58  (+0.023%)
  Exit reason:   MA20 crossed below MA50 — strategy rule followed

POST-EXIT OUTCOME (Day 10 validation):
  SPY at exit (Mar 13 EOD): $660.49
  SPY at Day 10 (Mar 20):   $648.57
  Drop since exit:           -$11.92/share × 10 = -$119.20
  If held entire time:       (648.57 - 666.436) × 10 = -$178.66
  Actual realized:           +$15.58
  Total protection:          +$194.24

Verdict: Strategy worked. Doing nothing was the right trade.
======================================================================

- Infrastructure completed today:
  ✅ API keys rotated, moved to .env
  ✅ load_dotenv(override=True) — stale key bug fixed
  ✅ Startup auth validation (fail fast pattern)
  ✅ TAF → FEE fix (try/except wrapper)
  ✅ yfinance removed from all P&L calculations
  ✅ Alpaca FILL activities = source of truth
  ✅ Session detector (PRE / REGULAR / AFTER-HOURS / CLOSED)
  ✅ Market orders during regular session only
  ✅ Limit + extended_hours=True during pre/after-hours
  ✅ Cron job configured (9:31 PM IST = 9:31 AM EST, Mon–Fri)
  ✅ Duplicate cron entry found and fixed
  ✅ README updated (Week 1 honest status)
  ✅ GitHub repo pushed (live-trading-alpha)
  ✅ .gitignore protecting .env, .venv, *.csv, cron.log

- Feature engineering completed:
  Stocks:   RELIANCE.NS, TCS.NS, INFY.NS
  Data:     2y daily OHLCV via yfinance
  Rows:     ~850  |  Features: 15
  Saved:    nse_model_ready.csv
  Features: MA_50, MA_200, MA_cross, Volume_ratio, RSI_14,
            Return_1d/5d/20d, Price_vs_MA50/200_pct,
            RSI_x_Volume, MA_spread, Log_Volume,
            Return_accel, RSI_zone, Ticker_encoded,
            Market_regime (KMeans 4 states), PC1/PC2, Target

- Key learning today:
  "The MA system isn't smart. It doesn't know about Powell.
  It doesn't know about oil. It knows price structure.
  Price structure warned first."

- Portfolio snapshot EOD:
  Starting capital:    $100,000.00
  Realized P&L:        +$15.58  (+0.016%)
  SPY EOD return:      (648.57/676.42 - 1) = -4.12%
  Alpha Day 1→10:      +4.133%
  Alpaca equity:       $100,015.57 ← confirmed source of truth

================================================================
Day 10 of 90. System operational. Signal: waiting for Golden Cross.
================================================================

======================================================================
## Day 11 — March 23, 2026 (Monday)
======================================================================
- Position:              FLAT
- Close price (Mar 23):  $655.41
- Realized P&L (locked): +$15.58
- Portfolio value:       $100,015.58  (Alpaca equity: $100,015.57)
- Benchmark (if B&H):   $96,893.94  |  Alpha: +3.122%
- Reference (if held):  (655.41 − 666.436) × 10 = −$110.26
  Signal saved vs holding: +$15.58 − (−$110.26) = +$125.84

- Regime call:           BEARISH — slight recovery from Day 10 lows
- Strategy note:
  MA20 still below MA50. No Golden Cross. FLAT is correct.
  SPY recovered +$6.84 from Day 10 close ($648.57 → $655.41).
  Not a reversal — a one-day bounce in an established downtrend.
  Same pattern as Days 6-7. Resistance at MA50 (~$684) still far.

## Day 12 and 13 — March 25, 2026 (Wednesday)

--- LATEST SNAPSHOT ---
Actual Entry:     $666.436/share  (Alpaca fills)
Actual Exit:      $667.994/share  (Alpaca fills)
Realized P&L:     $+15.58
Current Close:    $658.22  (yfinance)
Position:         FLAT
Journal Value:    $100,015.58
Alpaca Equity:    $100,015.57  ← source of truth
Alpaca Cash:      $100,015.57


## Day 14 — March 26, 2026 (Thursday)
Position: FLAT

Close price: $645.09

Portfolio value: $100,015.58 | Benchmark: $95,368.23 | Alpha: +4.648%

Reference if held: ($645.09 − $666.436) × 10 = −$213.46 | Signal saved: +$229.04

Regime call: RISK-OFF — macro shock resumes, bounce fully negated

Market context: The Day 13 ceasefire optimism was priced out in a single session. SPY fell -$11.73 (-1.79%), the largest single-day drop since Day 4. US energy infrastructure reports showed disruption was more persistent than initially priced. Bond yields rose. Credit spreads widened. The benchmark collapsed from $97,102 to $95,368 — a single-session loss of $1,734 for a passive holder. Strategy sat in cash.

Strategy note: Day 14 erased three days of benchmark recovery in one session. The MA-based exit from Day 4 continues to compound its advantage. This is the asymmetry of downside protection — the cost of missing one good day is small; the cost of sitting through one bad day is disproportionate.

Key learning: Regime transitions aren't linear. The market does not announce "the bounce is over" — it punishes re-entrants on the first shock after recovery. Waiting for the Golden Cross protects against this trap.

## Day 15 — March 27, 2026 (Friday)
Position: FLAT

Close price: $634.09

Portfolio value: $100,015.58 | Benchmark: $93,742.03 | Alpha: +6.274%

Reference if held: ($634.09 − $666.436) × 10 = −$323.46 | Signal saved: +$339.04

Regime call: BEARISH — five-month lows, structural breakdown

Market context: SPY at $634.09, down -6.26% from Day 1 close ($676.42). The benchmark is now below $94k on a $100k starting portfolio — a drawdown of over $6,200 for a passive holder. Two consecutive closes below key support at $640 confirmed a structural breakdown, not a correction. Oil remained elevated. Fed paralysed between inflation and growth. Gold and USD both elevated — classic risk-off trifecta.

Strategy note: Signal saved reached +$339.04 — the highest to date. The Death Cross on Day 4 effectively protected the full cost of two round-trip trades. At this price level ($634.09), MA20 is approximately $668 and MA50 approximately $682 — the Golden Cross requires SPY to sustain a rally of 5–7% from current levels and hold it long enough to shift the 50-day average. Re-entry is weeks away, not days.

Key learning: $339.04 protected on $6,664 deployed = 5.09% capital protection. This is the most important line in the journal so far. The system does not need to be smart about oil. It just needs to honour the rule.

## Day 16 — March 30, 2026 (Monday)
Position: FLAT

Close price: $631.97

Portfolio value: $100,015.58 | Benchmark: $93,428.61 | Alpha: +6.587% ← PEAK ALPHA

Reference if held: ($631.97 − $666.436) × 10 = −$344.66 | Signal saved: +$360.24 ← PEAK SAVE

Regime call: BEARISH — new cycle lows

Market context: SPY slid another -$2.12 to $631.97 — the lowest close since the October 2025 correction. Benchmark value fell to $93,428.61, representing a -6.57% drawdown from Day 1. The strategy's alpha hit its peak of +6.587%, meaning the MA crossover exit has outperformed passive holding by $6,587 per $100k. Monday gap-down reflects weekend risk aversion: energy supply fears, no ceasefire confirmation, and increasing recession pricing in bond markets (2-year yield inverted relative to 10-year briefly).

Strategy note: Peak alpha day. This is the validation event for the 90-day journal. A single SMA crossover rule, executed mechanically on Day 4, produced +6.587% outperformance over passive by Day 16. No ML, no news sentiment, no macro model. Pure price structure. The Alpha-Core HMM model (Week 7) will attempt to improve on this — but this establishes the baseline it must beat.

Key learning: The baseline is now set: +6.587% alpha, +$360.24 signal-saved, achieved by one rule, followed once. Any enhancement must prove it improves this number with consistency, not just in hindsight.

## Day 17 — March 31, 2026 (Tuesday)
Position: FLAT

Close price: $641.47

Portfolio value: $100,015.58 | Benchmark: $94,833.06 | Alpha: +5.183%

Reference if held: ($641.47 − $666.436) × 10 = −$249.66 | Signal saved: +$265.24

Regime call: BEARISH with bounce — month-end rebalancing, not reversal

Market context: SPY recovered +$9.50 (+1.50%) from Day 16 lows. Quarter-end / month-end rebalancing by institutional portfolios mechanically buys equities — this is a calendar effect, not a macro shift. Despite today's bounce, SPY remains -5.17% from Day 1 close ($676.42) and -1.47% below the exit price ($667.994). Alpha compressed from peak +6.587% (Day 16) to +5.183% today — entirely expected as SPY bounces while the strategy stays flat in cash.

Strategy note: The benchmark closes March at $94,833.06 vs the strategy's $100,015.58 — a $5,182.52 real-dollar gap on a $100k portfolio. MA20 now approximately $665 vs MA50 approximately $680. The gap is narrowing as SPY bounces, but the Golden Cross requires MA20 > MA50 sustained — still approximately 2–4 weeks away at current recovery rates.

Key learning: Month-end bounces are noise. The question is whether the quarter-end catalyst becomes a sustained trend or fades into April. Oil, Fed, and geopolitics remain unchanged. Regime = BEARISH until MA confirmation. Doing nothing remains the trade.