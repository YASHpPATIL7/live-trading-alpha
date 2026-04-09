import alpaca_trade_api as tradeapi
import yfinance as yf
import pandas as pd
from datetime import date
from dotenv import load_dotenv
import os, json, requests
from groq import Groq

load_dotenv(override=True)

# ============================================================
# CONFIG
# ============================================================
API_KEY         = os.getenv("ALPACA_API_KEY")
SECRET_KEY      = os.getenv("ALPACA_SECRET_KEY")
GROQ_API_KEY    = os.getenv("GROQ_API_KEY")
BASE_URL        = "https://paper-api.alpaca.markets"
SYMBOL          = "SPY"
STARTING_CASH   = 100_000
NARRATIVES_FILE = "alpaca_journal_narratives.json"

if not API_KEY or not SECRET_KEY:
    raise EnvironmentError("Alpaca keys not found.")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# ============================================================
# READ SIGNAL STATE — written by AlpacaDaily.py (single source of truth)
# Never recompute MAs here — use what the trade engine decided
# ============================================================
def load_signal_state():
    if os.path.exists("signal_state.json"):
        with open("signal_state.json", "r") as f:
            state = json.load(f)
        print(f"Signal state loaded: {state}")
        return state
    # Fallback if AlpacaDaily hasn't run yet today
    print("WARNING: signal_state.json not found — computing MAs as fallback")
    spy    = yf.download(SYMBOL, period="6mo", auto_adjust=True, progress=False)
    close  = spy["Close"].squeeze()
    ma_20  = close.rolling(20).mean()
    ma_50  = close.rolling(50).mean()
    recent_bull = all(ma_20.iloc[-i] > ma_50.iloc[-i] for i in range(1, 4))
    recent_bear = all(ma_20.iloc[-i] < ma_50.iloc[-i] for i in range(1, 4))
    signal = "BULLISH" if recent_bull else ("BEARISH" if recent_bear else "NEUTRAL")
    return {
        "date":    date.today().strftime("%Y-%m-%d"),
        "session": "UNKNOWN",
        "signal":  signal,
        "ma20":    round(float(ma_20.iloc[-1]), 2),
        "ma50":    round(float(ma_50.iloc[-1]), 2),
        "confirmed_days": 3
    }

signal_state = load_signal_state()
signal       = signal_state["signal"]
ma20_val     = signal_state["ma20"]
ma50_val     = signal_state["ma50"]

# ============================================================
# PULL FILLS VIA DIRECT REST
# ============================================================
_headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
_resp    = requests.get(f"{BASE_URL}/v2/account/activities/FILL", headers=_headers)
_resp.raise_for_status()
activities = _resp.json()

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

# ============================================================
# DOWNLOAD SPY BARS VIA ALPACA
# ============================================================
def get_spy_bars_alpaca(symbol, start_date, end_date, api_key, secret_key):
    url     = f"https://data.alpaca.markets/v2/stocks/{symbol}/bars"
    headers = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": secret_key}
    params  = {
        "start": start_date, "end": end_date,
        "timeframe": "1Day", "adjustment": "all",
        "limit": 1000, "feed": "iex"
    }
    bars = []
    while True:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        bars.extend(data.get("bars", []))
        next_token = data.get("next_page_token")
        if not next_token:
            break
        params["page_token"] = next_token

    if not bars:
        raise RuntimeError(f"Alpaca returned no bars for {symbol}")

    df = pd.DataFrame(bars)
    df["t"] = pd.to_datetime(df["t"]).dt.tz_localize(None)
    df = df.set_index("t").rename(
        columns={"c": "Close", "o": "Open", "h": "High", "l": "Low", "v": "Volume"}
    )
    df.index.name = "Date"
    return df

spy = get_spy_bars_alpaca(
    SYMBOL,
    entry_date,
    (date.today() + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    API_KEY, SECRET_KEY
)

# ============================================================
# BUILD JOURNAL
# ============================================================
exit_dt = pd.Timestamp(exit_date) if exit_date else None
rows = []

for idx, row in spy.iterrows():
    spy_close = round(float(row["Close"]), 2)
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
        "Date": idx.strftime("%Y-%m-%d"), "SPY_Close": spy_close,
        "Status": status, "Capital_Deployed": capital,
        "Unrealized_PnL": unrealized, "PnL_Pct": pnl_pct,
        "Portfolio_Value": port_val
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

print(journal[["Date","SPY_Close","Status","Unrealized_PnL","Portfolio_Value"]].to_string())
journal.to_csv("alpaca_journal.csv")
print("Saved: alpaca_journal.csv")

# ============================================================
# AUTO "WHAT I DID TODAY" — no more fill in placeholder
# ============================================================
def generate_what_i_did(signal, has_position, has_exited, realized_pnl, pct_chg=None):
    if has_exited and not has_position:
        return (
            f"System exited the position. Realized P&L locked at ${realized_pnl:+.2f}. "
            f"Now FLAT, waiting for next Golden Cross to re-enter."
        )
    elif has_position:
        return (
            f"System held long SPY. Signal remained {signal}. "
            f"Unrealized P&L: {pct_chg:+.2f}% from entry. No exit triggered."
        )
    elif signal == "BULLISH":
        return (
            f"Signal was BULLISH but system is still FLAT — "
            f"possible after-hours limit order did not fill, or entry was missed. "
            f"Monitoring for confirmed open-market entry tomorrow."
        )
    elif signal == "BEARISH":
        return (
            f"System stayed FLAT. Death Cross confirmed (MA20 ${ma20_val} < MA50 ${ma50_val}). "
            f"Capital preserved at ${STARTING_CASH + realized_pnl:,.2f}. Waiting for Golden Cross."
        )
    else:
        return (
            f"System stayed FLAT. Signal NEUTRAL — MA20/MA50 crossover not confirmed "
            f"for {signal_state['confirmed_days']} consecutive days. No trade taken."
        )

# ============================================================
# FETCH MARKET CONTEXT
# ============================================================
def fetch_market_context() -> dict:
    ctx = {
        "ma20":   ma20_val,
        "ma50":   ma50_val,
        "signal": f"{'BULLISH — Golden Cross' if signal == 'BULLISH' else 'BEARISH — Death Cross' if signal == 'BEARISH' else 'NEUTRAL'}",
        "signal_source": f"signal_state.json ({signal_state['date']})"
    }
    for ticker, key in [("^VIX", "vix"), ("CL=F", "oil"), ("^TNX", "yield_10y")]:
        try:
            val = yf.Ticker(ticker).history(period="5d")["Close"]
            ctx[key] = round(float(val.iloc[-1]), 2)
        except Exception:
            ctx[key] = "N/A"
    try:
        news_items = yf.Ticker(SYMBOL).news or []
        headlines  = []
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
# GROQ NARRATIVE
# ============================================================
def generate_narrative(day_label, row, ctx, actual_entry, realized_pnl,
                       has_exited, has_position):
    if not GROQ_API_KEY:
        return _placeholder_narrative()

    client   = Groq(api_key=GROQ_API_KEY)
    is_flat  = row["Status"] == "FLAT"

    pnl_line = (
        f"Realized P&L locked: ${realized_pnl:+.2f} (position exited)"
        if has_exited and is_flat
        else f"Unrealized P&L: ${row['Unrealized_PnL']:+.2f} ({row['PnL_Pct']:+.3f}%)"
    )
    signal_saved_line = (
        f"Signal saved vs passive hold: ${row['Signal_Saved']:+.2f}"
        if has_exited else ""
    )
    what_i_did_auto = generate_what_i_did(
        signal, has_position, has_exited, realized_pnl,
        pct_chg=row["PnL_Pct"] if not is_flat else None
    )
    headlines_block = "\n".join(f"  - {h}" for h in ctx["headlines"])

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
Signal source: {ctx['signal_source']}
VIX: {ctx['vix']}
WTI Oil: ${ctx['oil']}/barrel
10Y Treasury yield: {ctx['yield_10y']}%

=== TODAY'S SPY HEADLINES ===
{headlines_block}

=== WHAT THE SYSTEM DID TODAY (pre-computed, do not override) ===
{what_i_did_auto}

=== INSTRUCTIONS ===
Return ONLY a JSON object with exactly these 4 keys:
{{
  "regime_call": "one short label e.g. RISK-OFF / Fed Shock",
  "market_context": "2-3 sentences on what happened in markets today",
  "strategy_note": "1-2 sentences on MA status and what the system did",
  "key_learning": "one punchy sentence — the most important lesson from today"
}}
No explanation, no markdown, no extra keys. Pure JSON only."""

    try:
        response = Groq(api_key=GROQ_API_KEY).chat.completions.create(
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
        result["what_i_did_today"] = what_i_did_auto   # always use computed, never Groq
        result["source"] = "groq"
        return result
    except Exception as e:
        print(f"  Groq call failed: {e}")
        return _placeholder_narrative()

def _placeholder_narrative():
    return {
        "regime_call":    "_fill in_",
        "market_context": "_fill in_",
        "strategy_note":  "_fill in_",
        "key_learning":   "_fill in_",
        "what_i_did_today": generate_what_i_did(signal, has_position, has_exited, realized_pnl),
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

def get_or_generate_narrative(day_label, row, narratives, ctx,
                               actual_entry, realized_pnl, has_exited,
                               has_position, force_regenerate=False):
    date_key = row["Date"]
    if date_key in narratives:
        existing = narratives[date_key]
        # Always refresh what_i_did_today — never use stale version
        existing["what_i_did_today"] = generate_what_i_did(
            signal, has_position, has_exited, realized_pnl,
            pct_chg=row["PnL_Pct"] if row["Status"] != "FLAT" else None
        )
        if existing.get("source") == "manual":
            print(f"  {day_label} ({date_key}): manual narrative — preserved")
            return existing
        if existing.get("source") == "groq" and not force_regenerate:
            print(f"  {day_label} ({date_key}): cached groq narrative")
            return existing

    print(f"  {day_label} ({date_key}): generating via Groq...")
    return generate_narrative(day_label, row, ctx, actual_entry,
                              realized_pnl, has_exited, has_position)

# ============================================================
# POPULATE NARRATIVES
# ============================================================
print("\n--- GENERATING NARRATIVES ---")
narratives = load_narratives()
ctx        = fetch_market_context()

for day_label, row in journal.iterrows():
    narrative = get_or_generate_narrative(
        day_label, row, narratives, ctx,
        actual_entry, realized_pnl, has_exited, has_position
    )
    narratives[row["Date"]] = narrative

save_narratives(narratives)
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
             narratives, signal_state):

    today_str  = date.today().strftime("%B %d, %Y")
    total_days = len(journal)
    latest     = journal.iloc[-1]
    L = []

    L += [
        f"# ALPACA PAPER JOURNAL — {SYMBOL}",
        f"_Last updated: {today_str} | Day {total_days} of 90_",
        f"_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_",
        f"_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_",
        "",
        "> ⚠️ **RECONCILIATION NOTE**  ",
        f"> All P&L uses Alpaca fill prices. Entry: **${actual_entry:.3f}/share**",
        f"> ({entry_date}, after-hours fill).",
        "",
        f"> 📡 **CURRENT SIGNAL** ({signal_state['date']}): **{signal_state['signal']}**  ",
        f"> MA20: ${signal_state['ma20']} | MA50: ${signal_state['ma50']} | Session: {signal_state['session']}",
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
        f"| Capital deployed | ${actual_entry * total_buy_qty:,.2f} |",
        f"| Starting capital | ${STARTING_CASH:,} |",
        f"| Alpaca equity | ${portfolio_val:,.2f} |",
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
        "## Benchmark vs Strategy", "",
        "| Day | Date | Strategy | Benchmark | Strat Return | BH Return | Alpha |",
        "|---|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        L.append(f"| {lbl} | {row['Date']} | ${row['Portfolio_Value']:,.2f} | "
                 f"${row['Benchmark_Value']:,.2f} | {row['Strategy_Return_Pct']:+.4f}% | "
                 f"{row['Benchmark_Return_Pct']:+.3f}% | **{row['Alpha_Pct']:+.3f}%** |")
    L.append("")

    L += [
        "## Signal Saved vs Holding", "",
        "| Day | Date | SPY Close | If Held | Signal Saved | Note |",
        "|---|---|---|---|---|---|",
    ]
    for lbl, row in journal.iterrows():
        note = _signal_note(row["Signal_Saved"]) if row["Status"] == "FLAT" else "Position open"
        L.append(f"| {lbl} | {row['Date']} | ${row['SPY_Close']:.2f} | "
                 f"{_fmt(row['Reference_IfHeld'])} | {_fmt(row['Signal_Saved'])} | {note} |")
    L.append("")

    L += ["---", "", "## Daily Entries", ""]

    for lbl, row in journal.iterrows():
        is_long  = row["Status"] != "FLAT"
        date_key = row["Date"]
        narr     = narratives.get(date_key, _placeholder_narrative())

        regime_call    = narr.get("regime_call",      "_fill in_")
        market_context = narr.get("market_context",   "_fill in_")
        strategy_note  = narr.get("strategy_note",    "_fill in_")
        key_learning   = narr.get("key_learning",     "_fill in_")
        what_i_did     = narr.get("what_i_did_today", "_fill in_")
        narr_source    = narr.get("source",           "placeholder")

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
        elif has_exited:
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
    narratives=narratives,
    signal_state=signal_state
)

md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alpaca_journal.md")
with open(md_path, "w") as f:
    f.write(md_content)
print(f"Saved: {md_path}")
