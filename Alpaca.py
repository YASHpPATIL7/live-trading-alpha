import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Load API keys from .env file (never hardcode keys!)
load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

if not API_KEY or not SECRET_KEY:
    raise ValueError("Missing ALPACA_API_KEY or ALPACA_SECRET_KEY in .env file")

client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Check account
account = client.get_account()
print(f"Status: {account.status}")
print(f"Cash: ${account.cash}")
print(f"Portfolio Value: ${account.portfolio_value}")

# Place first paper trade — SPY (S&P 500 ETF proxy)
# order = client.submit_order(MarketOrderRequest(
#     symbol="SPY",
#     qty=10,
#     side=OrderSide.BUY,
#     time_in_force=TimeInForce.DAY
# ))
# print(f"Order placed: {order.symbol} {order.qty} shares")
