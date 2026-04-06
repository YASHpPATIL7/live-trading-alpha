import alpaca_trade_api as tradeapi
import yfinance as yf
from datetime import datetime, timedelta
from dotenv import load_dotenv
import pytz, os

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
SYMBOL         = "SPY"
RISK_PCT       = 0.02      # risk 2% of equity per trade
STOP_LOSS_PCT  = 0.02      # stop-loss 2% below entry
TAKE_PROFIT_PCT= 0.06      # take-profit 6% above entry (3:1 R:R)
SIGNAL_CONFIRM = 3         # MA20 must be > MA50 for 3 consecutive days


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

if session == "CLOSED":
    print("Market closed. Exiting.")
    exit()


# ============================================================
# BEST PRICE — use Alpaca latest quote, not yfinance
# ============================================================
def get_best_price(side):
    """
    BUY  → use ask price (what market makers sell at)
    SELL → use bid price (what market makers buy at)
    Falls back to last trade price if quote unavailable.
    """
    try:
        quote = api.get_latest_quote(SYMBOL)
        ask   = float(quote.ap)   # ask price
        bid   = float(quote.bp)   # bid price
        spread = round(ask - bid, 4)
        print(f"Quote:  Bid ${bid:.2f} | Ask ${ask:.2f} | Spread ${spread:.4f}")
        return ask if side == "buy" else bid
    except Exception:
        # fallback: last trade
        trade = api.get_latest_trade(SYMBOL)
        price = float(trade.p)
        print(f"Fallback last trade: ${price:.2f}")
        return price


# ============================================================
# SIGNAL — confirmed MA crossover (3 days, no whipsaw)
# ============================================================
spy    = yf.download(SYMBOL, period="6mo", auto_adjust=True, progress=False)
close  = spy["Close"].squeeze()
ma_20  = close.rolling(20).mean()
ma_50  = close.rolling(50).mean()

# Check last SIGNAL_CONFIRM days all agree
recent_bull = all(ma_20.iloc[-i] > ma_50.iloc[-i] for i in range(1, SIGNAL_CONFIRM + 1))
recent_bear = all(ma_20.iloc[-i] < ma_50.iloc[-i] for i in range(1, SIGNAL_CONFIRM + 1))

signal = "BULLISH" if recent_bull else ("BEARISH" if recent_bear else "NEUTRAL")
print(f"MA20: ${float(ma_20.iloc[-1]):.2f} | MA50: ${float(ma_50.iloc[-1]):.2f}")
print(f"Signal: {signal} (confirmed {SIGNAL_CONFIRM} days)")


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
    print("Position:  FLAT")


# ============================================================
# ACCOUNT + POSITION SIZING
# ============================================================
account    = api.get_account()
equity     = float(account.equity)
cash       = float(account.cash)
print(f"Equity: ${equity:,.2f} | Cash: ${cash:,.2f}")

def calc_shares(price):
    """
    Risk 2% of equity. Stop is 2% below entry.
    shares = (equity × risk%) / (entry × stop%)
    e.g. $100k equity → risk $2k → stop $10 below $500 entry → 200 shares
    """
    risk_dollars = equity * RISK_PCT
    stop_dollars = price  * STOP_LOSS_PCT
    qty          = int(risk_dollars / stop_dollars)
    max_qty      = int((cash * 0.95) / price)   # never use more than 95% cash
    qty          = min(qty, max_qty)
    print(f"Position size: {qty} shares (risking ${risk_dollars:.0f})")
    return max(qty, 1)


# ============================================================
# ORDER FUNCTIONS
# ============================================================
def submit_buy():
    price  = get_best_price("buy")
    qty    = calc_shares(price)
    sl     = round(price * (1 - STOP_LOSS_PCT),  2)
    tp     = round(price * (1 + TAKE_PROFIT_PCT), 2)

    if session == "REGULAR":
        # Bracket order: entry + stop-loss + take-profit in one call
        api.submit_order(
            symbol     = SYMBOL,
            qty        = qty,
            side       = "buy",
            type       = "market",
            time_in_force = "day",
            order_class   = "bracket",
            stop_loss     = {"stop_price": sl},
            take_profit   = {"limit_price": tp}
        )
        print(f"BUY BRACKET ORDER: {qty} shares")
        print(f"  Stop-loss:   ${sl:.2f} (-{STOP_LOSS_PCT*100:.0f}%)")
        print(f"  Take-profit: ${tp:.2f} (+{TAKE_PROFIT_PCT*100:.0f}%)")

    elif session == "AFTER_HOURS":
        # Limit at ask — best realistic fill in after-hours
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
        print("  Manual stop/TP will need to be set at open tomorrow.")


def submit_sell():
    if session == "REGULAR":
        api.close_position(SYMBOL)
        print(f"SELL: Closing full position (market order)")

    elif session == "AFTER_HOURS":
        price = get_best_price("sell")   # use bid for sell
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
# STOP-LOSS CHECK — exit if position dropped 2%
# ============================================================
if has_position and avg_entry > 0:
    current_price = get_best_price("sell")
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
        print("HOLD — already long, signal confirmed")

elif signal == "BEARISH":
    if has_position:
        submit_sell()
    else:
        print("FLAT — waiting for Golden Cross")

else:
    print("NEUTRAL — MA crossover not confirmed yet, no action")
