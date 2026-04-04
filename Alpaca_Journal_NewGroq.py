import alpaca_trade_api as tradeapi
import yfinance as yf
import pandas as pd
from datetime import date
from dotenv import load_dotenv
import os
import json
import requests
from groq import Groq


load_dotenv(override=True)


# ============================================================
# CONFIG
# ============================================================
API_KEY       = os.getenv("ALPACA_API_KEY")
SECRET_KEY    = os.getenv("ALPACA_SECRET_KEY")
GROQ_API_KEY  = os.getenv("GROQ_API_KEY")
BASE_URL      = "https://paper-api.alpaca.markets"
SYMBOL        = "SPY"
STARTING_CASH = 100_000
NARRATIVES_FILE = "alpaca_journal_narratives.json"


if not API_KEY or not SECRET_KEY:
    raise EnvironmentError("Alpaca keys not found. Check your .env file.")


api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")


# ============================================================
# PULL FILLS VIA DIRECT REST (returns list of dicts)
# ============================================================
_headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
_resp = requests.get(
    f"{BASE_URL}/v2/account/activities/FILL",
    headers=_headers
)
_resp.raise_for_status()
activities = _resp.json()   # list of dicts — use ["key"] not .key


# Filter buys / sells using dict access
buys  = [a for a in activities if a["symbol"] == SYMBOL and a["side"] == "buy"]
sells = [a for a in activities if a["symbol"] == SYMBOL and a["side"] == "sell"]


if not buys:
    raise ValueError(f"No buy fills found for {SYMBOL}")


total_buy_cost = sum(float(b["price"]) * float(b["qty"]) for b in buys)
total_buy_qty  = sum(float(b["qty"]) for b in buys)
actual_entry   = total_buy_cost / total_buy_qty
entry_date     = min(pd.Timestamp(b["transaction_time"]) for b in buys).strftime("%Y-%m-%d")


if sells:
    total_sell_proceeds = sum(float(s["price"]) * float(s["qty"]) for s in sells)
    total_sell_qty      = sum(float(s["qty"]) for s in sells)
    actual_exit         = total_sell_proceeds / total_sell_qty
    exit_date           = max(pd.Timestamp(s["transaction_time"]) for s in sells).strftime("%Y-%m-%d")
    has_exited          = True
    realized_pnl        = round((actual_exit - actual_entry) * total_buy_qty, 2)
else:
    actual_exit  = None
    exit_date    = None
    has_exited   = False
    realized_pnl = 0.0


account       = api.get_account()
portfolio_val = float(account.equity)
cash          = float(account.cash)


try:
    api.get_position(SYMBOL)
    has_position = True
except Exception:
    has_position = False


spy = yf.download(
    SYMBOL,
    start=entry_date,
    end=(date.today() + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    auto_adjust=True,
    progress=False
)


exit_dt = pd.Timestamp(exit_date) if exit_date else None


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


benchmark_entry_price = journal["SPY_Close"].iloc[0]
benchmark_shares      = round(STARTING_CASH / benchmark_entry_price, 4)

journal["Benchmark_Value"]      = round(benchmark_shares * journal["SPY_Close"], 2)
journal["Benchmark_Return_Pct"] = round((journal["Benchmark_Value"] - STARTING_CASH) / STARTING_CASH * 100, 3)
journal["Strategy_Return_Pct"]  = round((journal["Portfolio_Value"] - STARTING_CASH) / STARTING_CASH * 100, 4)
journal["Alpha_Pct"]            = round(journal["Strategy_Return_Pct"] - journal["Benchmark_Return_Pct"], 3)
journal["Reference_IfHeld"]     = round((journal["SPY_Close"] - actual_entry) * total_buy_qty, 2)
journal["Signal_Saved"]         = round(realized_pnl - journal["Reference_IfHeld"], 2)


# ============================================================
# CONSOLE PRINT + CSV
# ============================================================
print("=" * 70)
print(f"ALPACA PAPER JOURNAL — {SYMBOL}")
print("=" * 70)
print(journal[["Date", "SPY_Close", "Status", "Unrealized_PnL", "PnL_Pct", "Portfolio_Value"]].to_string())

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
# FETCH MARKET CONTEXT
# ============================================================
def fetch_market_context(spy_df: pd.DataFrame) -> dict:
    ctx = {}
    spy_hist = yf.Ticker(SYMBOL).history(period="60d")["Close"]
    ctx["ma20"] = round(float(spy_hist.rolling(20).mean().iloc[-1]), 2)
    ctx["ma50"] = round(float(spy_hist.rolling(50).mean().iloc[-1]), 2)
    ctx["signal"] = "BEARISH — Death Cross" if ctx["ma20"] < ctx["ma50"] else "BULLISH — Golden Cross"

    try:
        vix = yf.Ticker("^VIX").history(period="5d")["Close"]
        ctx["vix"] = round(float(vix.iloc[-1]), 2)
    except Exception:
        ctx["vix"] = "N/A"

    try:
        oil = yf.Ticker("CL=F").history(period="5d")["Close"]
        ctx["oil"] = round(float(oil.iloc[-1]), 2)
    except Exception:
        ctx["oil"] = "N/A"

    try:
        tnx = yf.Ticker("^TNX").history(period="5d")["Close"]
        ctx["yield_10y"] = round(float(tnx.iloc[-1]), 3)
    except Exception:
        ctx["yield_10y"] = "N/A"

    try:
        news_items = yf.Ticker(SYMBOL).news or []
        headlines = []
        for item in news_items[:5]:
            content = item.get("content", {})
            title   = content.get("title", "")
            pub     = content.get("pubDate", "")[:10]
            if title:
                headlines.append(f"[{pub}] {title}")
        ctx["headlines"] = headlines if headlines else ["No headlines available"]
    except Exception:
        ctx["headlines"] = ["Could not fetch news"]

    return ctx


# ============================================================
# GROQ NARRATIVE GENERATOR
# ============================================================
def generate_narrative(day_label, row, ctx, actual_entry, realized_pnl, has_exited):
    if not GROQ_API_KEY:
        print("⚠️  GROQ_API_KEY not set — skipping narrative generation.")
        return _placeholder_narrative()

    client = Groq(api_key=GROQ_API_KEY)

    pnl_line = (
        f"Realized P&L locked: ${realized_pnl:+.2f} (exited)"
        if has_exited and row["Status"] == "FLAT"
        else f"Unrealized P&L: ${row['Unrealized_PnL']:+.2f} ({row['PnL_Pct']:+.3f}%)"
    )

    signal_saved_line = (
        f"Signal saved vs passive hold: ${row['Signal_Saved']:+.2f}"
        if has_exited else ""
    )

    headlines_block = "\n".join(f"  • {h}" for h in ctx["headlines"])

    prompt = f"""You are writing daily narrative entries for a quantitative trading journal.
The trader runs a paper portfolio ($100k) on SPY using a simple MA20/MA50 crossover strategy.
Write ONLY based on the data provided. Do not invent facts. Be concise and analytical.

=== TODAY'S DATA ===
Day label: {day_label}
Date: {row['Date']}
SPY close: ${row['SPY_Close']:.2f}
Entry price (Alpaca fill): ${actual_entry:.3f}
Position status: {row['Status']}
{pnl_line}
{signal_saved_line}
Portfolio value: ${row['Portfolio_Value']:,.2f}
Benchmark (SPY B&H): ${row['Benchmark_Value']:,.2f}
Cumulative alpha: {row['Alpha_Pct']:+.3f}%

=== MACRO DATA ===
MA20: ${ctx['ma20']} | MA50: ${ctx['ma50']} | Signal: {ctx['signal']}
VIX: {ctx['vix']}
WTI Oil: ${ctx['oil']}/barrel
10Y Treasury yield: {ctx['yield_10y']}%

=== TODAY'S SPY HEADLINES ===
{headlines_block}

=== INSTRUCTIONS ===
Return ONLY a JSON object with exactly these 4 keys:
{{
  "regime_call": "one short label, e.g. RISK-OFF / Fed Shock or CAUTIOUS — dead-cat bounce",
  "market_context": "2–3 sentences summarising what actually happened in markets today based on headlines and macro data",
  "strategy_note": "1–2 sentences: MA status, what the system did (or didn't do), and why that was correct",
  "key_learning": "one punchy sentence — the most important lesson from today's data"
}}
No explanation, no markdown, no extra keys. Pure JSON only."""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.4,
            max_tokens=512
        )
        result = json.loads(response.choices[0].message.content)
        for key in ("regime_call", "market_context", "strategy_note", "key_learning"):
            if key not in result:
                result[key] = "_fill in_"
        result["source"] = "groq"
        return result
    except Exception as e:
        print(f"⚠️  Groq call failed: {e}")
        return _placeholder_narrative()


def _placeholder_narrative():
    return {
        "regime_call":    "_fill in_",
        "market_context": "_fill in_",
        "strategy_note":  "_fill in_",
        "key_learning":   "_fill in_",
        "source":         "placeholder"
    }


# ============================================================
# NARRATIVE STORE
# ============================================================
def load_narratives():
    if os.path.exists(NARRATIVES_FILE):
        with open(NARRATIVES_FILE, "r") as f:
            return json.load(f)
    return {}


def save_narratives(narratives):
    with open(NARRATIVES_FILE, "w") as f:
        json.dump(narratives, f, indent=2)
    print(f"Saved: {NARRATIVES_FILE}")


def get_or_generate_narrative(day_label, row, narratives, ctx,
                               actual_entry, realized_pnl, has_exited,
                               force_regenerate=False):
    date_key = row["Date"]

    if date_key in narratives:
        existing = narratives[date_key]
        if existing.get("source") == "manual":
            print(f"  {day_label} ({date_key}): using manual narrative — preserved")
            return existing
        if existing.get("source") == "groq" and not force_regenerate:
            print(f"  {day_label} ({date_key}): using cached groq narrative")
            return existing

    print(f"  {day_label} ({date_key}): generating via Groq...")
    narrative = generate_narrative(day_label, row, ctx, actual_entry, realized_pnl, has_exited)
    narratives[date_key] = narrative
    return narrative


# ============================================================
# POPULATE NARRATIVES
# ============================================================
print("\n--- GENERATING NARRATIVES ---")
narratives = load_narratives()
ctx = fetch_market_context(spy)

for day_label, row in journal.iterrows():
    narratives = load_narratives()
    narrative = get_or_generate_narrative(
        day_label=day_label,
        row=row,
        narratives=narratives,
        ctx=ctx,
        actual_entry=actual_entry,
        realized_pnl=realized_pnl,
        has_exited=has_exited
    )
    date_key = row["Date"]
    stored = load_narratives()
    if date_key not in stored or stored[date_key].get("source") not in ("manual", "groq"):
        stored[date_key] = narrative
        save_narratives(stored)

narratives = load_narratives()
print(f"Narratives ready for {len(narratives)} days.\n")


# ============================================================
# MARKDOWN HELPERS
# ============================================================
def _fmt(val):
    return f"+${val:.2f}" if val >= 0 else f"-${abs(val):.2f}"


def _signal_note(val):
    if val > 0:
        return f"Flat saved **{_fmt(val)}** vs holding"
    return f"Holding would have been **${abs(val):.2f}** better — honest entry"


def build_md(journal, actual_entry, actual_exit, has_exited, realized_pnl,
             entry_date, exit_date, portfolio_val, cash, total_buy_qty,
             benchmark_shares, benchmark_entry_price, SYMBOL, STARTING_CASH,
             narratives):

    today_str  = date.today().strftime("%B %d, %Y")
    total_days = len(journal)
    latest     = journal.iloc[-1]
    L = []

    L += [
        f"# ALPACA PAPER JOURNAL — {SYMBOL}",
        f"_Last updated: {today_str} | Day {total_days} of 90_",
        f"_Source of truth: Alpaca fills | Close prices: yfinance EOD_",
        f"_Narrative context: auto-generated via Groq (llama-3.1-8b-instant) + yfinance news_",
        "",
        "> ⚠️ **RECONCILIATION NOTE**  ",
        f"> All P&L uses Alpaca fill prices. Entry: **${actual_entry:.3f}/share**",
        f"> ({entry_date}, after-hours fill). yfinance is used for close prices only.",
        "",
    ]

    L += [
        "## Trade Summary", "",
        "| Field | Value |", "|---|---|",
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

    L += [
        "## Master Table", "",
        "| Day | Date | SPY Close | Status | Unrealized P&L | P&L % | Portfolio Value |",
        "|---|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        unr = _fmt(row["Unrealized_PnL"]) if row["Unrealized_PnL"] != 0 else "—"
        pct = f"{row['PnL_Pct']:+.3f}%" if row["Unrealized_PnL"] != 0 else "—"
        L.append(f"| {lbl} | {row['Date']} | ${row['SPY_Close']:.2f} | "
                 f"{row['Status']} | {unr} | {pct} | ${row['Portfolio_Value']:,.2f} |")
    L.append("")

    L += [
        "## Benchmark vs Strategy",
        f"_Buy-and-hold from Day 1 close ${benchmark_entry_price:.2f}"
        f" — {benchmark_shares:.4f} shares_", "",
        "| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |",
        "|---|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        L.append(f"| {lbl} | {row['Date']} | ${row['Portfolio_Value']:,.2f} | "
                 f"${row['Benchmark_Value']:,.2f} | {row['Strategy_Return_Pct']:+.4f}% | "
                 f"{row['Benchmark_Return_Pct']:+.3f}% | **{row['Alpha_Pct']:+.3f}%** |")
    L.append("")

    L += [
        "## Signal Saved vs Holding",
        "_Unrealized P&L if position was never closed — honest comparison._", "",
        "| Day | Date | SPY Close | If Held | Signal Saved | Note |",
        "|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        note = _signal_note(row["Signal_Saved"]) if row["Status"] == "FLAT" else "Position open"
        L.append(f"| {lbl} | {row['Date']} | ${row['SPY_Close']:.2f} | "
                 f"{_fmt(row['Reference_IfHeld'])} | {_fmt(row['Signal_Saved'])} | {note} |")
    L.append("")

    L += ["---", "", "## Daily Entries", ""]

    for i, (lbl, row) in enumerate(journal.iterrows()):
        is_long  = row["Status"] != "FLAT"
        date_key = row["Date"]

        narr = narratives.get(date_key, _placeholder_narrative())
        regime_call    = narr.get("regime_call",    "_fill in_")
        market_context = narr.get("market_context", "_fill in_")
        strategy_note  = narr.get("strategy_note",  "_fill in_")
        key_learning   = narr.get("key_learning",   "_fill in_")
        what_i_did     = narr.get("what_i_did_today", "_fill in_")
        narr_source    = narr.get("source", "placeholder")

        L += [
            f"### {lbl} — {row['Date']}"
            + (f" _(narrative: {narr_source})_" if narr_source != "placeholder" else ""),
            "",
            "| Field | Value |", "|---|---|",
            f"| Position | {row['Status']} |",
            f"| Entry (Alpaca fill) | ${actual_entry:.3f}/share |",
            f"| Close price | ${row['SPY_Close']:.2f} |",
        ]

        if is_long:
            L += [
                f"| Unrealized P&L | {_fmt(row['Unrealized_PnL'])} |",
                f"| P&L % | {row['PnL_Pct']:+.3f}% |",
            ]
        else:
            if has_exited:
                L += [
                    f"| Realized P&L (locked) | {_fmt(realized_pnl)} |",
                    f"| Reference if held | {_fmt(row['Reference_IfHeld'])} |",
                    f"| Signal saved | {_fmt(row['Signal_Saved'])} |",
                ]

        L += [
            f"| Portfolio value | ${row['Portfolio_Value']:,.2f} |",
            f"| Benchmark value | ${row['Benchmark_Value']:,.2f} |",
            f"| Alpha (cumulative) | {row['Alpha_Pct']:+.3f}% |",
            "",
            f"**Regime call:** {regime_call}", "",
            f"**Market context:** {market_context}", "",
            f"**Strategy note:** {strategy_note}", "",
            f"**What I did today:** {what_i_did}", "",
            f"**Key learning:** {key_learning}", "",
            "---", "",
        ]

    L += [
        "## Anomaly Log", "",
        "| # | Date | Observation | Hypothesis | Status |",
        "|---|---|---|---|---|",
        "| _add entries here_ | | | | |", "",
    ]

    L += [
        "---",
        f"_Day {total_days} of 90 · Alpaca equity: ${portfolio_val:,.2f}"
        f" · Cumulative alpha vs SPY: {latest['Alpha_Pct']:+.3f}%_",
    ]

    return "\n".join(L)


# ============================================================
# WRITE MARKDOWN
# ============================================================
md_content = build_md(
    journal, actual_entry, actual_exit, has_exited, realized_pnl,
    entry_date, exit_date, portfolio_val, cash, total_buy_qty,
    benchmark_shares, benchmark_entry_price, SYMBOL, STARTING_CASH,
    narratives=narratives
)

md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alpaca_journal.md")
with open(md_path, "w") as f:
    f.write(md_content)

print(f"Saved: {md_path}")
