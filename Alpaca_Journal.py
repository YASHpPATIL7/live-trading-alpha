import alpaca_trade_api as tradeapi
import yfinance as yf
import pandas as pd
from datetime import date

# ============================================================
# CONFIG
# ============================================================
API_KEY    = "your_key"
SECRET_KEY = "your_secret"
BASE_URL   = "https://paper-api.alpaca.markets"

ENTRY_DATE     = "2026-03-09"
EXIT_DATE      = "2026-03-12"    # None if still holding
SHARES         = 10
STARTING_CASH  = 100_000

# Pull ACTUAL fill prices from Alpaca activity (not yfinance)
# From your activity log:
ACTUAL_ENTRY   = (5330.56 + 1333.80) / 10   # = $666.436
ACTUAL_EXIT    = (4007.94 + 2672.00) / 10   # = $667.994
TAF_FEE        = 0.01
REALIZED_PNL   = round((ACTUAL_EXIT - ACTUAL_ENTRY) * SHARES - TAF_FEE, 2)
# = (667.994 - 666.436) × 10 - 0.01 = +$15.57

# ============================================================
# FETCH SPY PRICES (display only — NOT used for P&L calc)
# ============================================================
spy = yf.download(
    "SPY",
    start=ENTRY_DATE,
    end=(date.today() + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    auto_adjust=True,
    progress=False
)

exit_dt = pd.Timestamp(EXIT_DATE) if EXIT_DATE else None

# ============================================================
# BUILD JOURNAL
# ============================================================
rows = []
for i, (idx, row) in enumerate(spy.iterrows()):
    trade_date = idx
    spy_close  = round(float(row["Close"].item()), 2)

    if exit_dt is None or trade_date <= exit_dt:
        # Position OPEN — P&L vs actual fill price
        unrealized = round((spy_close - ACTUAL_ENTRY) * SHARES, 2)
        pnl_pct    = round(((spy_close - ACTUAL_ENTRY) / ACTUAL_ENTRY) * 100, 3)
        port_val   = round(STARTING_CASH + unrealized, 2)
        status     = f"Long {SHARES} SPY"
        capital    = round(ACTUAL_ENTRY * SHARES, 2)
    else:
        # Position FLAT — everything frozen at realized P&L
        unrealized = 0.00
        pnl_pct    = 0.000
        port_val   = round(STARTING_CASH + REALIZED_PNL, 2)
        status     = "FLAT"
        capital    = 0.00

    rows.append({
        "Date":             trade_date.strftime("%Y-%m-%d"),
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
print("ALPACA PAPER JOURNAL — SPY (Actual Fill Prices)")
print("=" * 70)
print(journal[[
    "Date", "SPY_Close", "Status",
    "Unrealized_PnL", "PnL_Pct", "Portfolio_Value"
]].to_string())

latest  = journal.iloc[-1]
is_flat = latest["Status"] == "FLAT"

print("\n--- LATEST SNAPSHOT ---")
print(f"Actual Entry Price:      ${ACTUAL_ENTRY:.3f}/share (Alpaca fill)")
print(f"Actual Exit Price:       ${ACTUAL_EXIT:.3f}/share (Alpaca fill)")
print(f"Current SPY Close:       ${latest['SPY_Close']:.2f} (yfinance ref)")
print(f"Position:                {latest['Status']}")
if is_flat:
    print(f"Realized P&L:            ${REALIZED_PNL:+.2f} (incl. TAF fee)")
    print(f"Unrealized P&L:          $0.00")
else:
    print(f"Unrealized P&L:          ${latest['Unrealized_PnL']:+.2f}")
    print(f"P&L %:                   {latest['PnL_Pct']:+.3f}%")
print(f"Portfolio Value:         ${latest['Portfolio_Value']:,.2f}")
print(f"(Alpaca cash balance:    $100,015.57 — source of truth)")

journal.to_csv("alpaca_journal.csv")
print("\nSaved: alpaca_journal.csv")
