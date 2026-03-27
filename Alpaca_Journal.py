import alpaca_trade_api as tradeapi
import yfinance as yf
import pandas as pd
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# ============================================================
# CONFIG
# ============================================================
API_KEY       = os.getenv("ALPACA_API_KEY")
SECRET_KEY    = os.getenv("ALPACA_SECRET_KEY")
BASE_URL      = "https://paper-api.alpaca.markets"
SYMBOL        = "SPY"
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
    total_sell_qty      = sum(float(s.qty) for s in sells)
    actual_exit         = total_sell_proceeds / total_sell_qty
    exit_date           = max(pd.Timestamp(s.transaction_time) for s in sells).strftime("%Y-%m-%d")
    has_exited          = True
    realized_pnl        = round((actual_exit - actual_entry) * total_buy_qty, 2)
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
    api.get_position(SYMBOL)
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
# BUILD JOURNAL DATAFRAME
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
# BENCHMARK + SIGNAL SAVED
# ============================================================
benchmark_entry_price = journal["SPY_Close"].iloc[0]
benchmark_shares      = round(STARTING_CASH / benchmark_entry_price, 4)

journal["Benchmark_Value"]      = round(benchmark_shares * journal["SPY_Close"], 2)
journal["Benchmark_Return_Pct"] = round((journal["Benchmark_Value"] - STARTING_CASH) / STARTING_CASH * 100, 3)
journal["Strategy_Return_Pct"]  = round((journal["Portfolio_Value"] - STARTING_CASH) / STARTING_CASH * 100, 4)
journal["Alpha_Pct"]            = round(journal["Strategy_Return_Pct"] - journal["Benchmark_Return_Pct"], 3)
journal["Reference_IfHeld"]     = round((journal["SPY_Close"] - actual_entry) * total_buy_qty, 2)
journal["Signal_Saved"]         = round(realized_pnl - journal["Reference_IfHeld"], 2)

# ============================================================
# PRINT TO CONSOLE  (unchanged from original)
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

# ============================================================
# MARKDOWN HELPERS
# ============================================================
def _fmt(val):
    return f"+${val:.2f}" if val >= 0 else f"-${abs(val):.2f}"

def _signal_note(val):
    if val > 0:
        return f"Flat saved **{_fmt(val)}** vs holding"
    return f"Holding would have been **${abs(val):.2f}** better — honest entry"

# ============================================================
# BUILD MARKDOWN
# ============================================================
def build_md(journal, actual_entry, actual_exit, has_exited, realized_pnl,
             entry_date, exit_date, portfolio_val, cash, total_buy_qty,
             benchmark_shares, benchmark_entry_price, SYMBOL, STARTING_CASH):

    today_str  = date.today().strftime("%B %d, %Y")
    total_days = len(journal)
    latest     = journal.iloc[-1]
    L = []

    # ── HEADER ──────────────────────────────────────────────
    L += [
        f"# ALPACA PAPER JOURNAL — {SYMBOL}",
        f"_Last updated: {today_str} | Day {total_days} of 90_",
        f"_Source of truth: Alpaca fills | Close prices: yfinance EOD_",
        "",
        "> ⚠️ **RECONCILIATION NOTE**  ",
        f"> All P&L uses Alpaca fill prices. Entry: **${actual_entry:.3f}/share**",
        f"> ({entry_date}, after-hours fill). yfinance is used for close prices only.",
        "",
    ]

    # ── TRADE SUMMARY ───────────────────────────────────────
    L += [
        "## Trade Summary",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Symbol | {SYMBOL} |",
        f"| Entry (Alpaca fill) | ${actual_entry:.3f}/share — {entry_date} |",
    ]
    if has_exited:
        L += [
            f"| Exit (Alpaca fill) | ${actual_exit:.3f}/share — {exit_date} |",
            f"| Realized P&L | {_fmt(realized_pnl)} |",
        ]
    L += [
        f"| Shares | {int(total_buy_qty)} |",
        f"| Capital deployed | ${actual_entry * total_buy_qty:,.2f}"
        f" ({actual_entry * total_buy_qty / STARTING_CASH * 100:.2f}% of portfolio) |",
        f"| Starting capital | ${STARTING_CASH:,} |",
        f"| Alpaca equity | ${portfolio_val:,.2f} ← source of truth |",
        f"| Alpaca cash | ${cash:,.2f} |",
        "",
    ]

    # ── MASTER TABLE ────────────────────────────────────────
    L += [
        "## Master Table",
        "",
        "| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |",
        "|---|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        unr = _fmt(row["Unrealized_PnL"]) if row["Unrealized_PnL"] != 0 else "—"
        pct = f"{row['PnL_Pct']:+.3f}%"  if row["Unrealized_PnL"] != 0 else "—"
        L.append(f"| {lbl} | {row['Date']} | ${row['SPY_Close']:.2f} | "
                 f"{row['Status']} | {unr} | {pct} | ${row['Portfolio_Value']:,.2f} |")
    L.append("")

    # ── BENCHMARK TABLE ─────────────────────────────────────
    L += [
        "## Benchmark vs Strategy",
        f"_Buy-and-hold from Day 1 close ${benchmark_entry_price:.2f}"
        f" — {benchmark_shares:.4f} shares_",
        "",
        "| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |",
        "|---|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        L.append(f"| {lbl} | {row['Date']} | ${row['Portfolio_Value']:,.2f} | "
                 f"${row['Benchmark_Value']:,.2f} | {row['Strategy_Return_Pct']:+.4f}% | "
                 f"{row['Benchmark_Return_Pct']:+.3f}% | **{row['Alpha_Pct']:+.3f}%** |")
    L.append("")

    # ── SIGNAL SAVED TABLE ──────────────────────────────────
    L += [
        "## Signal Saved vs Holding",
        "_Unrealized P&L if position was never closed — honest comparison._",
        "",
        "| Day | Date | SPY Close | If Held | Signal Saved | Note |",
        "|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        note = _signal_note(row["Signal_Saved"]) if row["Status"] == "FLAT" else "Position open"
        L.append(f"| {lbl} | {row['Date']} | ${row['SPY_Close']:.2f} | "
                 f"{_fmt(row['Reference_IfHeld'])} | {_fmt(row['Signal_Saved'])} | {note} |")
    L.append("")

    # ── DAILY ENTRIES (scaffold — numbers auto, narrative manual) ───────
    L += ["---", "", "## Daily Entries", "",
          "> 📝 Numbers are auto-generated. Regime call, market context,",
          "> strategy note, learnings — fill in manually each day.", ""]

    for i, (lbl, row) in enumerate(journal.iterrows()):
        is_long = row["Status"] != "FLAT"
        L += [f"### {lbl} — {row['Date']}", "",
              "| Field | Value |", "|---|---|",
              f"| Position | {row['Status']} |",
              f"| Entry (Alpaca fill) | ${actual_entry:.3f}/share |",
              f"| Close price | ${row['SPY_Close']:.2f} |"]

        if is_long:
            L += [f"| Unrealized P&L | {_fmt(row['Unrealized_PnL'])} |",
                  f"| P&L % | {row['PnL_Pct']:+.3f}% |"]
        else:
            if has_exited:
                L += [f"| Realized P&L (locked) | {_fmt(realized_pnl)} |",
                      f"| Reference if held | {_fmt(row['Reference_IfHeld'])} |",
                      f"| Signal saved | {_fmt(row['Signal_Saved'])} |"]

        L += [f"| Portfolio value | ${row['Portfolio_Value']:,.2f} |",
              f"| Benchmark value | ${row['Benchmark_Value']:,.2f} |",
              f"| Alpha (cumulative) | {row['Alpha_Pct']:+.3f}% |",
              "",
              "**Regime call:** _fill in_", "",
              "**Market context:** _fill in_", "",
              "**Strategy note:** _fill in_", "",
              "**What I did today:** _fill in_", "",
              "**Key learning:** _fill in_", "",
              "---", ""]

    # ── ANOMALY LOG ─────────────────────────────────────────
    L += [
        "## Anomaly Log",
        "",
        "| # | Date | Observation | Hypothesis | Status |",
        "|---|---|---|---|---|",
        "| _add entries here_ | | | | |",
        "",
    ]

    # ── FOOTER ──────────────────────────────────────────────
    L += [
        "---",
        f"_Day {total_days} of 90 · Alpaca equity: ${portfolio_val:,.2f}"
        f" · Cumulative alpha vs SPY: {latest['Alpha_Pct']:+.3f}%_",
    ]

    return "\n".join(L)


md_content = build_md(
    journal, actual_entry, actual_exit, has_exited, realized_pnl,
    entry_date, exit_date, portfolio_val, cash, total_buy_qty,
    benchmark_shares, benchmark_entry_price, SYMBOL, STARTING_CASH
)

md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alpaca_journal.md")
with open(md_path, "w") as f:
    f.write(md_content)

print(f"Saved: {md_path}")
