import alpaca_trade_api as tradeapi
import yfinance as yf
import pandas as pd
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

# ============================================================
# CONFIG
# ============================================================
API_KEY    = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL   = "https://paper-api.alpaca.markets"
SYMBOL     = "SPY"
STARTING_CASH = 100_000

if not API_KEY or not SECRET_KEY:
    raise EnvironmentError("Keys not found. Check your .env file.")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# ============================================================
# PULL FILLS
# ============================================================
activities = api.get_activities(activity_types="FILL")

buys  = [a for a in activities if a.symbol == SYMBOL and a.side == "buy"]
sells = [a for a in activities if a.symbol == SYMBOL and a.side == "sell"]

if not buys:
    raise ValueError(f"No buy fills found for {SYMBOL}")

total_buy_cost = sum(float(b.price) * float(b.qty) for b in buys)
total_buy_qty  = sum(float(b.qty) for b in buys)
actual_entry   = total_buy_cost / total_buy_qty
entry_date     = min(pd.Timestamp(b.transaction_time) for b in buys).strftime("%Y-%m-%d")

if sells:
    total_sell_proceeds = sum(float(s.price) * float(s.qty) for s in sells)
    actual_exit  = total_sell_proceeds / total_sell_qty if (total_sell_qty := sum(float(s.qty) for s in sells)) else 0
    exit_date    = max(pd.Timestamp(s.transaction_time) for s in sells).strftime("%Y-%m-%d")
    has_exited   = True
    realized_pnl = round((actual_exit - actual_entry) * total_buy_qty, 2)
    # TAF fee is $0.01 on paper — negligible, not fetched
else:
    actual_exit  = None
    exit_date    = None
    has_exited   = False
    realized_pnl = 0.0

# ============================================================
# ACCOUNT
# ============================================================
account       = api.get_account()
portfolio_val = float(account.equity)
cash          = float(account.cash)

try:
    position     = api.get_position(SYMBOL)
    has_position = True
except Exception:
    has_position = False

# ============================================================
# SPY PRICES
# ============================================================
spy = yf.download(
    SYMBOL,
    start=entry_date,
    end=(date.today() + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    auto_adjust=True,
    progress=False
)

exit_dt = pd.Timestamp(exit_date) if exit_date else None

# ============================================================
# BUILD JOURNAL
# ============================================================
rows = []
for idx, row in spy.iterrows():
    spy_close = round(float(row["Close"].item()), 2)

    if exit_dt is None or idx <= exit_dt:
        unrealized = round((spy_close - actual_entry) * total_buy_qty, 2)
        pnl_pct    = round(((spy_close - actual_entry) / actual_entry) * 100, 3)
        port_val   = round(STARTING_CASH + unrealized, 2)
        status     = f"Long {int(total_buy_qty)} {SYMBOL}"
        capital    = round(actual_entry * total_buy_qty, 2)
    else:
        unrealized = 0.00
        pnl_pct    = 0.000
        port_val   = round(STARTING_CASH + realized_pnl, 2)
        status     = "FLAT"
        capital    = 0.00

    rows.append({
        "Date":             idx.strftime("%Y-%m-%d"),
        "SPY_Close":        spy_close,
        "Status":           status,
        "Capital_Deployed": capital,
        "Unrealized_PnL":   unrealized,
        "PnL_Pct":          pnl_pct,
        "Portfolio_Value":  port_val
    })

journal = pd.DataFrame(rows)
journal.index = [f"Day {i+1}" for i in range(len(journal))]
journal.index.name = "Day"

# ============================================================
# PRINT
# ============================================================
print("=" * 70)
print(f"ALPACA PAPER JOURNAL — {SYMBOL}")
print("=" * 70)
print(journal[[
    "Date", "SPY_Close", "Status",
    "Unrealized_PnL", "PnL_Pct", "Portfolio_Value"
]].to_string())

latest  = journal.iloc[-1]
is_flat = latest["Status"] == "FLAT"

print("\n--- LATEST SNAPSHOT ---")
print(f"Actual Entry:     ${actual_entry:.3f}/share  (Alpaca fills)")
if has_exited:
    print(f"Actual Exit:      ${actual_exit:.3f}/share  (Alpaca fills)")
    print(f"Realized P&L:     ${realized_pnl:+.2f}")
print(f"Current Close:    ${latest['SPY_Close']:.2f}  (yfinance)")
print(f"Position:         {latest['Status']}")
if not is_flat:
    print(f"Unrealized P&L:   ${latest['Unrealized_PnL']:+.2f}")
    print(f"P&L %:            {latest['PnL_Pct']:+.3f}%")
print(f"Journal Value:    ${latest['Portfolio_Value']:,.2f}")
print(f"Alpaca Equity:    ${portfolio_val:,.2f}  ← source of truth")
print(f"Alpaca Cash:      ${cash:,.2f}")

journal.to_csv("alpaca_journal.csv")
print("\nSaved: alpaca_journal.csv")
