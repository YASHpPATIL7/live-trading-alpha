import yfinance as yf
import pandas as pd
from datetime import datetime, date

# ============================================================
# FETCH SPY PRICES FOR ALPACA JOURNAL
# ============================================================

spy = yf.download("SPY",
                  start="2026-03-09",
                  end=(date.today() + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
                  auto_adjust=True,
                  progress=False)
# end = tomorrow's date → always includes today's close once market shuts
# Run this after 9:30 PM IST to get today's final price


# Your trade details
entry_price = spy["Close"].iloc[0]  # Day 1 close = your fill price
shares = 10
starting_cash = 100_000

# Build journal table
journal = pd.DataFrame()
journal["Date"] = spy.index
journal["SPY_Close"] = spy["Close"].values.round(2)
journal["Capital_Deployed"] = (entry_price * shares).round(2)
journal["Unrealized_PnL"] = ((spy["Close"].values - float(entry_price)) * shares).round(2)
journal["PnL_Pct"] = (((spy["Close"].values - float(entry_price)) / float(entry_price)) * 100).round(3)
journal["Portfolio_Value"] = (starting_cash + journal["Unrealized_PnL"]).round(2)
journal["Day"] = [f"Day {i+1}" for i in range(len(journal))]

journal = journal.set_index("Day")

print("=" * 65)
print("ALPACA PAPER JOURNAL — SPY LONG 10 SHARES")
print("=" * 65)
print(journal[["Date", "SPY_Close", "Unrealized_PnL", "PnL_Pct", "Portfolio_Value"]].to_string())

print("\n--- LATEST SNAPSHOT ---")
latest = journal.iloc[-1]
print(f"Entry Price (Day 1):     ${float(entry_price):.2f}")
print(f"Current Price:           ${latest['SPY_Close']:.2f}")
print(f"Shares:                  {shares}")
print(f"Capital Deployed:        ${float(entry_price) * shares:,.2f}")
print(f"Unrealized P&L:          ${latest['Unrealized_PnL']:,.2f}")
print(f"P&L %:                   {latest['PnL_Pct']:.3f}%")
print(f"Portfolio Value:         ${latest['Portfolio_Value']:,.2f}")

# Save to CSV — append this to your journal folder
journal.to_csv("alpaca_journal.csv")
print("\nSaved: alpaca_journal.csv")
