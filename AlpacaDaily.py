import alpaca_trade_api as tradeapi
import yfinance as yf
from datetime import datetime
from dotenv import load_dotenv
import pytz
import os

load_dotenv(override=True)

API_KEY    = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL   = "https://paper-api.alpaca.markets"

if not API_KEY or not SECRET_KEY:
    raise EnvironmentError("Keys not found — check .env file")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# ============================================================
# SESSION DETECTOR — returns what session we're in right now
# ============================================================
def get_session():
    est = pytz.timezone("US/Eastern")
    now = datetime.now(est)

    if now.weekday() >= 5:
        return "CLOSED"  # weekend

    t = now.time()
    from datetime import time

    if   time(4,  0) <= t < time(9, 30):  return "PRE_MARKET"
    elif time(9, 30) <= t < time(16,  0): return "REGULAR"
    elif time(16, 0) <= t < time(20,  0): return "AFTER_HOURS"
    else:                                  return "CLOSED"

session = get_session()
print(f"Session: {session}")

if session == "CLOSED":
    print("Market fully closed. No orders possible. Exiting.")
    exit()

# ============================================================
# SIGNAL — yfinance for MA only
# ============================================================
spy          = yf.download("SPY", period="60d", auto_adjust=True, progress=False)
ma_20        = float(spy["Close"].rolling(20).mean().iloc[-1].item())
ma_50        = float(spy["Close"].rolling(50).mean().iloc[-1].item())
latest_close = float(spy["Close"].iloc[-1].item())

print(f"MA20: ${ma_20:.2f}  |  MA50: ${ma_50:.2f}")
print(f"Signal: {'BULLISH (MA20 > MA50)' if ma_20 > ma_50 else 'BEARISH (MA20 < MA50)'}")

# ============================================================
# POSITION CHECK
# ============================================================
try:
    position     = api.get_position("SPY")
    shares       = int(position.qty)
    avg_entry    = float(position.avg_entry_price)
    has_position = True
    print(f"Position:  Long {shares} shares @ ${avg_entry:.3f}")
    print(f"Ref P&L:   ${(latest_close - avg_entry) * shares:+.2f}")
except Exception as e:
    has_position = False
    print(f"Position:  FLAT")

# ============================================================
# ACCOUNT
# ============================================================
account = api.get_account()
print(f"Equity:    ${float(account.equity):,.2f}")
print(f"Cash:      ${float(account.cash):,.2f}")

# ============================================================
# ORDER BUILDER — behaves like real market
# ============================================================
def submit_buy(limit_price=None):
    """
    Regular session  → market order (instant fill, tight spreads)
    Pre/After-hours  → limit order at latest close (extended_hours=True)
    """
    if session == "REGULAR":
        api.submit_order(
            symbol="SPY", qty=10,
            side="buy", type="market",
            time_in_force="day"
        )
        print("ACTION: BUY MARKET ORDER SUBMITTED (regular session)")

    else:
        # Use latest close as limit price if none provided
        price = round(limit_price or latest_close, 2)
        api.submit_order(
            symbol="SPY", qty=10,
            side="buy", type="limit",
            time_in_force="day",        # cancels if not filled by end of session
            limit_price=price,
            extended_hours=True
        )
        print(f"ACTION: BUY LIMIT ORDER @ ${price} SUBMITTED ({session})")
        print("        Will fill if SPY drops to this price before session ends.")
        print("        Cancelled at end of session if unfilled (time_in_force=day).")


def submit_sell(limit_price=None):
    """
    Regular session  → close_position (market order, instant)
    Pre/After-hours  → limit order at latest close (extended_hours=True)
    """
    if session == "REGULAR":
        api.close_position("SPY")
        print("ACTION: SELL MARKET ORDER SUBMITTED (regular session)")

    else:
        price = round(limit_price or latest_close, 2)
        api.submit_order(
            symbol="SPY", qty=shares,
            side="sell", type="limit",
            time_in_force="day",
            limit_price=price,
            extended_hours=True
        )
        print(f"ACTION: SELL LIMIT ORDER @ ${price} SUBMITTED ({session})")
        print("        Will fill if SPY rises to this price before session ends.")
        print("        Cancelled at end of session if unfilled (time_in_force=day).")


# ============================================================
# ACTION — signal drives decision, session drives order type
# ============================================================
if ma_20 > ma_50:
    if not has_position:
        submit_buy()
    else:
        print("ACTION: HOLD — already long, signal unchanged")
else:
    if has_position:
        submit_sell()
    else:
        print("ACTION: FLAT — waiting for Golden Cross")
