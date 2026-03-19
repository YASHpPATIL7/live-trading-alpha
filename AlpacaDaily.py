# sma_crossover.py
# Run this once — it checks signal and places/exits order automatically

import alpaca_trade_api as tradeapi
import yfinance as yf

API_KEY    = "PK2KLCSVJWIG5IQAKOT6ORFZBR"
SECRET_KEY = "E17Ufqj3GZG3VKJZW6F8CTBxQ2GHsqVFj4paKCL9Wcez"
BASE_URL   = "https://paper-api.alpaca.markets"  # paper trading URL

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# Pull SPY data via yfinance (simpler than Alpaca bars)
spy = yf.download("SPY", period="60d", auto_adjust=True, progress=False)
ma_20 = spy["Close"].rolling(20).mean().iloc[-1].item()
ma_50 = spy["Close"].rolling(50).mean().iloc[-1].item()
# Check current position
try:
    position = api.get_position("SPY")
    has_position = True
except:
    has_position = False

# Signal logic
if ma_20 > ma_50:
    if not has_position:
        api.submit_order(
            symbol="SPY",
            qty=10,
            side="buy",
            type="market",
            time_in_force="day"
        )
        print(f"BUY signal: MA20={ma_20:.2f} > MA50={ma_50:.2f}")
    else:
        print(f"HOLD: Already long. MA20={ma_20:.2f} > MA50={ma_50:.2f}")
else:
    if has_position:
        api.close_position("SPY")
        print(f"SELL signal: MA20={ma_20:.2f} < MA50={ma_50:.2f}")
    else:
        print(f"FLAT: No position. MA20={ma_20:.2f} < MA50={ma_50:.2f}")
