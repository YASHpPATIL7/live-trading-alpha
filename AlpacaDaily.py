import alpaca_trade_api as tradeapi
import yfinance as yf
from datetime import datetime
from dotenv import load_dotenv
import pytz, os, json

load_dotenv(override=True)

API_KEY    = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL   = "https://paper-api.alpaca.markets"

if not API_KEY or not SECRET_KEY:
    raise EnvironmentError("Keys not found")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# ============================================================
# CONSTANTS
# ============================================================
SYMBOL          = "SPY"
RISK_PCT        = 0.02          # 2% risk per trade
STOP_LOSS_PCT   = 0.015         # 1.5% stop — tighter for faster MAs
TAKE_PROFIT_PCT = 0.04          # 4% take-profit
MAX_ALLOC_PCT   = 0.40          # Deploy up to 40% of equity per trade

# ============================================================
# SESSION DETECTOR
# ============================================================
def get_session():
    est = pytz.timezone("US/Eastern")
    now = datetime.now(est)
    if now.weekday() >= 5:
        return "CLOSED"
    t = now.time()
    from datetime import time
    if   time(9, 31) <= t < time(16, 0): return "REGULAR"
    elif time(16, 0) <= t < time(20, 0): return "AFTER_HOURS"
    else:                                 return "CLOSED"

session = get_session()
print(f"Session: {session}")

# ============================================================
# DUAL-TIMEFRAME SIGNAL ENGINE
# ============================================================
# Fast MAs (SMA 10/30) → trade signals (more responsive)
# Slow MAs (SMA 20/50) → regime filter (trend context)
#
# BUY  when: fast_bull (MA10 > MA30)  AND  regime != STRONG_BEAR
# SELL when: fast_bear (MA10 < MA30)  OR   regime == STRONG_BEAR
# ============================================================
spy   = yf.download(SYMBOL, period="6mo", auto_adjust=True, progress=False)
close = spy["Close"].squeeze()

# Fast MAs — entry/exit signals
ma_10 = close.rolling(10).mean()
ma_30 = close.rolling(30).mean()

# Slow MAs — regime context
ma_20 = close.rolling(20).mean()
ma_50 = close.rolling(50).mean()

# Current values (latest closed bar)
ma10_now = float(ma_10.iloc[-1])
ma30_now = float(ma_30.iloc[-1])
ma20_now = float(ma_20.iloc[-1])
ma50_now = float(ma_50.iloc[-1])
close_now = float(close.iloc[-1])

# Fast signal — 1-day confirmation (no multi-day lag)
fast_bull = ma10_now > ma30_now
fast_bear = ma10_now < ma30_now

# Regime — slow MAs
regime_gap_pct = (ma20_now - ma50_now) / ma50_now * 100
if ma20_now > ma50_now:
    regime = "BULL"
elif regime_gap_pct < -1.5:
    regime = "STRONG_BEAR"    # MA20 more than 1.5% below MA50 — avoid longs
else:
    regime = "BEAR"           # mild bear — can still take fast signals

# ── PRICE-ACTION OVERRIDES ──────────────────────────────────
# The slow regime filter (MA20/MA50) can lag badly in V-shaped recoveries.
# If price has clearly recovered above the slow MAs, override the regime.
price_above_both_slow = close_now > ma20_now and close_now > ma50_now
price_pct_above_ma50  = (close_now - ma50_now) / ma50_now * 100
price_override        = price_above_both_slow and price_pct_above_ma50 > 2.0

# Price also above both fast MAs = breakout confirmation
price_above_fast      = close_now > ma10_now and close_now > ma30_now

# Combined signal — with price-action override
if fast_bull and regime != "STRONG_BEAR":
    signal = "BULLISH"
elif price_override and price_above_fast:
    signal = "BULLISH"   # Price-action override — market clearly recovered
    print(f"⚡ PRICE OVERRIDE: Close ${close_now:.2f} is {price_pct_above_ma50:+.1f}% above MA50 "
          f"— overriding {regime} regime (MA20 still < MA50)")
elif fast_bear and not price_override:
    signal = "BEARISH"
else:
    signal = "NEUTRAL"

# Price relative to MAs — momentum check
above_ma10 = close_now > ma10_now
price_momentum = "STRONG" if close_now > ma10_now > ma30_now else (
    "RECOVERING" if close_now > ma30_now else "WEAK"
)

print(f"Fast  MA10: ${ma10_now:.2f} | MA30: ${ma30_now:.2f} | {'BULL' if fast_bull else 'BEAR'}")
print(f"Slow  MA20: ${ma20_now:.2f} | MA50: ${ma50_now:.2f} | Regime: {regime} ({regime_gap_pct:+.2f}%)")
print(f"Close: ${close_now:.2f} | Momentum: {price_momentum}")
print(f"Signal: {signal}")

signal_state = {
    "date":           datetime.now().strftime("%Y-%m-%d"),
    "session":        session,
    "signal":         signal,
    "ma10":           round(ma10_now, 2),
    "ma30":           round(ma30_now, 2),
    "ma20":           round(ma20_now, 2),
    "ma50":           round(ma50_now, 2),
    "regime":         regime,
    "regime_gap_pct": round(regime_gap_pct, 2),
    "momentum":       price_momentum,
    "close":          round(close_now, 2),
    "price_override": price_override,
    "price_pct_above_ma50": round(price_pct_above_ma50, 2)
}
with open("signal_state.json", "w") as f:
    json.dump(signal_state, f, indent=2)
print(f"Signal state saved → signal_state.json")

# Exit AFTER saving signal state
if session == "CLOSED":
    print("Market closed. Signal state saved. Exiting.")
    exit()

# ============================================================
# BEST PRICE
# ============================================================
def get_best_price(side):
    try:
        quote  = api.get_latest_quote(SYMBOL)
        ask    = float(quote.ap)
        bid    = float(quote.bp)
        spread = round(ask - bid, 4)
        print(f"Quote:  Bid ${bid:.2f} | Ask ${ask:.2f} | Spread ${spread:.4f}")
        return ask if side == "buy" else bid
    except Exception:
        trade = api.get_latest_trade(SYMBOL)
        price = float(trade.p)
        print(f"Fallback last trade: ${price:.2f}")
        return price

# ============================================================
# POSITION CHECK
# ============================================================
try:
    pos          = api.get_position(SYMBOL)
    shares       = int(pos.qty)
    avg_entry    = float(pos.avg_entry_price)
    has_position = True
    unrealized   = float(pos.unrealized_pl)
    pct_chg      = float(pos.unrealized_plpc) * 100
    print(f"Position:  Long {shares} shares @ ${avg_entry:.2f}")
    print(f"Unrealized P&L: ${unrealized:+.2f} ({pct_chg:+.2f}%)")
except Exception:
    has_position = False
    shares       = 0
    avg_entry    = 0.0
    pct_chg      = 0.0
    print("Position:  FLAT")

# ============================================================
# ACCOUNT + POSITION SIZING (FIXED — uses MAX_ALLOC_PCT)
# ============================================================
account = api.get_account()
equity  = float(account.equity)
cash    = float(account.cash)
print(f"Equity: ${equity:,.2f} | Cash: ${cash:,.2f}")

def calc_shares(price):
    # Method 1: Risk-based sizing
    risk_dollars = equity * RISK_PCT
    stop_dollars = price  * STOP_LOSS_PCT
    qty_risk     = int(risk_dollars / stop_dollars)

    # Method 2: Max allocation cap
    qty_alloc    = int((equity * MAX_ALLOC_PCT) / price)

    # Method 3: Available cash
    qty_cash     = int((cash * 0.95) / price)

    # Take the minimum of risk-based and allocation, capped by cash
    qty = min(qty_risk, qty_alloc, qty_cash)
    qty = max(qty, 1)   # at least 1 share

    print(f"Position size: {qty} shares | risk-based: {qty_risk} | alloc-cap: {qty_alloc} | cash-cap: {qty_cash}")
    print(f"Capital deployed: ${qty * price:,.2f} ({qty * price / equity * 100:.1f}% of equity)")
    return qty

# ============================================================
# ORDER FUNCTIONS
# ============================================================
def submit_buy():
    price = get_best_price("buy")
    qty   = calc_shares(price)
    sl    = round(price * (1 - STOP_LOSS_PCT),  2)
    tp    = round(price * (1 + TAKE_PROFIT_PCT), 2)

    if session == "REGULAR":
        api.submit_order(
            symbol        = SYMBOL,
            qty           = qty,
            side          = "buy",
            type          = "market",
            time_in_force = "day",
            order_class   = "bracket",
            stop_loss     = {"stop_price": sl},
            take_profit   = {"limit_price": tp}
        )
        print(f"BUY BRACKET ORDER: {qty} shares")
        print(f"  Stop-loss:   ${sl:.2f} (-{STOP_LOSS_PCT*100:.1f}%)")
        print(f"  Take-profit: ${tp:.2f} (+{TAKE_PROFIT_PCT*100:.0f}%)")

    elif session == "AFTER_HOURS":
        api.submit_order(
            symbol        = SYMBOL,
            qty           = qty,
            side          = "buy",
            type          = "limit",
            time_in_force = "day",
            limit_price   = price,
            extended_hours= True
        )
        print(f"BUY LIMIT @ ${price:.2f} ({qty} shares) — after-hours")
        print("  Note: bracket orders not supported in extended hours.")

def submit_sell():
    if session == "REGULAR":
        api.close_position(SYMBOL)
        print(f"SELL: Closing full position (market order)")

    elif session == "AFTER_HOURS":
        price = get_best_price("sell")
        api.submit_order(
            symbol        = SYMBOL,
            qty           = shares,
            side          = "sell",
            type          = "limit",
            time_in_force = "day",
            limit_price   = price,
            extended_hours= True
        )
        print(f"SELL LIMIT @ ${price:.2f} ({shares} shares) — after-hours")

# ============================================================
# STOP-LOSS CHECK
# ============================================================
if has_position and avg_entry > 0:
    current_price  = get_best_price("sell")
    pct_from_entry = (current_price - avg_entry) / avg_entry * 100
    if pct_from_entry <= -STOP_LOSS_PCT * 100:
        print(f"STOP-LOSS TRIGGERED: {pct_from_entry:.2f}% from entry — closing position")
        submit_sell()
        exit()

# ============================================================
# MAIN LOGIC
# ============================================================
if signal == "BULLISH":
    if not has_position:
        submit_buy()
    else:
        print("HOLD — already long, fast signal confirmed")

elif signal == "BEARISH":
    if has_position:
        submit_sell()
    else:
        print(f"FLAT — fast signal bearish | Regime: {regime} | Waiting for MA10>MA30 crossover")

else:  # NEUTRAL
    if has_position:
        print(f"HOLD — signal neutral, regime {regime}, keeping position")
    else:
        print(f"NEUTRAL — regime {regime} blocking entry | MA10 trying to cross MA30 | Patience")