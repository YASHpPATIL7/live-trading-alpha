# sma_crossover.py
# Run this once — it checks signal and places/exits order automatically

import alpaca_trade_api as tradeapi
import yfinance as yf
import pandas as pd
from datetime import datetime, date


API_KEY    = "PK2KLCSVJWIG5IQAKOT6ORFZBR"
SECRET_KEY = "E17Ufqj3GZG3VKJZW6F8CTBxQ2GHsqVFj4paKCL9Wcez"
BASE_URL   = "https://paper-api.alpaca.markets"  # paper trading URL


api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# ============================================================
# WEEKEND GUARD
# ============================================================
if datetime.today().weekday() >= 5:
    print("Market closed — weekend. No action.")
    exit()

# ============================================================
# SPY SIGNAL — yfinance for MA calc only (closes are fine for MA)
# ============================================================
spy    = yf.download("SPY", period="60d", auto_adjust=True, progress=False)
ma_20  = float(spy["Close"].rolling(20).mean().iloc[-1].item())
ma_50  = float(spy["Close"].rolling(50).mean().iloc[-1].item())
latest_close = float(spy["Close"].iloc[-1].item())

print(f"MA20: ${ma_20:.2f}  |  MA50: ${ma_50:.2f}")
print(f"Signal: {'BULLISH (MA20 > MA50)' if ma_20 > ma_50 else 'BEARISH (MA20 < MA50)'}")

# ============================================================
# POSITION CHECK — Alpaca is source of truth
# ============================================================
try:
    position      = api.get_position("SPY")
    shares        = int(position.qty)
    avg_entry     = float(position.avg_entry_price)  # ACTUAL fill price
    has_position  = True
    unrealized    = (latest_close - avg_entry) * shares
    print(f"Position:  Long {shares} shares")
    print(f"Avg Entry: ${avg_entry:.3f}  (Alpaca actual fill)")
    print(f"Ref P&L:   ${unrealized:+.2f} vs yfinance close")
except:
    has_position = False
    print("Position:  FLAT")

# ============================================================
# ACCOUNT — Alpaca is source of truth
# ============================================================
account = api.get_account()
print(f"Portfolio: ${float(account.equity):,.2f}  (Alpaca equity)")
print(f"Cash:      ${float(account.cash):,.2f}")

# ============================================================
# SIGNAL + ACTION
# ============================================================
if ma_20 > ma_50:
    if not has_position:
        api.submit_order(
            symbol="SPY", qty=10,
            side="buy", type="market", time_in_force="day"
        )
        print("ACTION: BUY ORDER SUBMITTED")
    else:
        print("ACTION: HOLD — long, signal unchanged")
else:
    if has_position:
        api.close_position("SPY")
        print("ACTION: SELL — position closed")
    else:
        print("ACTION: FLAT — no signal to buy")