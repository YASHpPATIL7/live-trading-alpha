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
# Supports both old format (ma20/ma50 only) and new dual-timeframe format
# ============================================================
def load_signal_state():
    if os.path.exists("signal_state.json"):
        with open("signal_state.json", "r") as f:
            state = json.load(f)
        print(f"Signal state loaded: {state}")
        # Ensure backward compatibility with old format
        if "ma10" not in state:
            state["ma10"] = state.get("ma20", 0)
            state["ma30"] = state.get("ma50", 0)
        if "regime" not in state:
            state["regime"] = "UNKNOWN"
        if "momentum" not in state:
            state["momentum"] = "UNKNOWN"
        return state
    # Fallback if AlpacaDaily hasn't run yet today
    print("WARNING: signal_state.json not found — computing MAs as fallback")
    spy    = yf.download(SYMBOL, period="6mo", auto_adjust=True, progress=False)
    close  = spy["Close"].squeeze()
    ma_10  = close.rolling(10).mean()
    ma_30  = close.rolling(30).mean()
    ma_20  = close.rolling(20).mean()
    ma_50  = close.rolling(50).mean()
    fast_bull = float(ma_10.iloc[-1]) > float(ma_30.iloc[-1])
    regime_gap = (float(ma_20.iloc[-1]) - float(ma_50.iloc[-1])) / float(ma_50.iloc[-1]) * 100
    if fast_bull and regime_gap > -1.5:
        signal = "BULLISH"
    elif not fast_bull:
        signal = "BEARISH"
    else:
        signal = "NEUTRAL"
    return {
        "date":    date.today().strftime("%Y-%m-%d"),
        "session": "UNKNOWN",
        "signal":  signal,
        "ma10":    round(float(ma_10.iloc[-1]), 2),
        "ma30":    round(float(ma_30.iloc[-1]), 2),
        "ma20":    round(float(ma_20.iloc[-1]), 2),
        "ma50":    round(float(ma_50.iloc[-1]), 2),
        "regime":  "BULL" if regime_gap > 0 else ("STRONG_BEAR" if regime_gap < -1.5 else "BEAR"),
        "momentum": "UNKNOWN"
    }

signal_state = load_signal_state()
signal       = signal_state["signal"]
ma10_val     = signal_state.get("ma10", signal_state.get("ma20", 0))
ma30_val     = signal_state.get("ma30", signal_state.get("ma50", 0))
ma20_val     = signal_state.get("ma20", 0)
ma50_val     = signal_state.get("ma50", 0)
regime_val   = signal_state.get("regime", "UNKNOWN")
momentum_val = signal_state.get("momentum", "UNKNOWN")

# ============================================================
# PULL FILLS VIA DIRECT REST
# ============================================================
_headers = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}
_resp    = requests.get(f"{BASE_URL}/v2/account/activities/FILL", headers=_headers)
_resp.raise_for_status()
activities = _resp.json()

all_fills = [a for a in activities if a["symbol"] == SYMBOL]
all_fills.sort(key=lambda a: pd.Timestamp(a["transaction_time"]))

# ============================================================
# PARSE FILLS INTO ROUND-TRIP TRADES
# ============================================================
# Each trade = buy fills → sell fills (chronological pairs)
trades = []
pending_buys = []

for fill in all_fills:
    side  = fill["side"]
    qty   = float(fill["qty"])
    price = float(fill["price"])
    ts    = pd.Timestamp(fill["transaction_time"])

    if side == "buy":
        pending_buys.append({"qty": qty, "price": price, "time": ts})
    elif side == "sell" and pending_buys:
        # Close out the pending buys
        buy_cost = sum(b["price"] * b["qty"] for b in pending_buys)
        buy_qty  = sum(b["qty"] for b in pending_buys)
        entry_price = buy_cost / buy_qty
        entry_time  = min(b["time"] for b in pending_buys)

        trade = {
            "id":          len(trades) + 1,
            "entry_price": entry_price,
            "entry_date":  entry_time.strftime("%Y-%m-%d"),
            "entry_ts":    entry_time,
            "shares":      int(buy_qty),
            "exit_price":  price,
            "exit_date":   ts.strftime("%Y-%m-%d"),
            "exit_ts":     ts,
            "pnl":         round((price - entry_price) * buy_qty, 2),
            "status":      "CLOSED"
        }
        trades.append(trade)
        pending_buys = []

# If there are pending buys with no matching sell → currently in a position
if pending_buys:
    buy_cost = sum(b["price"] * b["qty"] for b in pending_buys)
    buy_qty  = sum(b["qty"] for b in pending_buys)
    entry_price = buy_cost / buy_qty
    entry_time  = min(b["time"] for b in pending_buys)
    trades.append({
        "id":          len(trades) + 1,
        "entry_price": entry_price,
        "entry_date":  entry_time.strftime("%Y-%m-%d"),
        "entry_ts":    entry_time,
        "shares":      int(buy_qty),
        "exit_price":  None,
        "exit_date":   None,
        "exit_ts":     None,
        "pnl":         0.0,
        "status":      "OPEN"
    })

if not trades:
    raise ValueError(f"No trades found for {SYMBOL}")

# Summary variables for backward compatibility
total_trades    = len(trades)
closed_trades   = [t for t in trades if t["status"] == "CLOSED"]
open_trade      = next((t for t in trades if t["status"] == "OPEN"), None)
total_realized  = round(sum(t["pnl"] for t in closed_trades), 2)
has_position    = open_trade is not None

# Legacy compatibility — use first trade for entry date (journal start)
first_entry_date = trades[0]["entry_date"]
actual_entry     = trades[0]["entry_price"]  # first trade entry for reference

# For last closed trade
if closed_trades:
    last_closed   = closed_trades[-1]
    actual_exit   = last_closed["exit_price"]
    exit_date     = last_closed["exit_date"]
    has_exited    = True
    realized_pnl  = total_realized
else:
    actual_exit   = None
    exit_date     = None
    has_exited    = False
    realized_pnl  = 0.0

# Current position info
if open_trade:
    total_buy_qty = open_trade["shares"]
else:
    total_buy_qty = trades[0]["shares"]  # for reference

print(f"\n--- TRADE HISTORY ({total_trades} trades) ---")
for t in trades:
    if t["status"] == "CLOSED":
        print(f"  Trade {t['id']}: CLOSED | Entry ${t['entry_price']:.3f} ({t['entry_date']}) "
              f"→ Exit ${t['exit_price']:.3f} ({t['exit_date']}) | P&L: ${t['pnl']:+.2f}")
    else:
        print(f"  Trade {t['id']}: OPEN   | Entry ${t['entry_price']:.3f} ({t['entry_date']}) "
              f"| {t['shares']} shares")
print(f"  Total realized P&L: ${total_realized:+.2f}")

account       = api.get_account()
portfolio_val = float(account.equity)
cash          = float(account.cash)

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
    first_entry_date,
    (date.today() + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    API_KEY, SECRET_KEY
)

# ============================================================
# BUILD JOURNAL — MULTI-TRADE AWARE
# ============================================================
rows = []
cumulative_realized = 0.0

for idx, row in spy.iterrows():
    spy_close = round(float(row["Close"]), 2)
    day_date  = idx.strftime("%Y-%m-%d")

    # Find which trade is active on this day
    active_trade = None
    for t in trades:
        entry_dt = pd.Timestamp(t["entry_date"])
        if t["status"] == "OPEN":
            if idx >= entry_dt:
                active_trade = t
                break
        else:  # CLOSED
            exit_dt = pd.Timestamp(t["exit_date"])
            if entry_dt <= idx <= exit_dt:
                active_trade = t
                break

    # Calculate cumulative realized P&L from trades closed BEFORE this day
    cum_realized = 0.0
    for t in closed_trades:
        exit_dt = pd.Timestamp(t["exit_date"])
        if idx > exit_dt:
            cum_realized += t["pnl"]

    if active_trade:
        entry_p   = active_trade["entry_price"]
        shares    = active_trade["shares"]
        unrealized = round((spy_close - entry_p) * shares, 2)
        pnl_pct    = round(((spy_close - entry_p) / entry_p) * 100, 3)
        port_val   = round(STARTING_CASH + cum_realized + unrealized, 2)
        status     = f"Long {shares} {SYMBOL} (T{active_trade['id']})"
        capital    = round(entry_p * shares, 2)
    else:
        unrealized = 0.00
        pnl_pct    = 0.000
        port_val   = round(STARTING_CASH + cum_realized, 2)
        status     = "FLAT"
        capital    = 0.00

    rows.append({
        "Date": day_date, "SPY_Close": spy_close,
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
journal["Reference_IfHeld"]     = round((journal["SPY_Close"] - trades[0]["entry_price"]) * trades[0]["shares"], 2)
journal["Signal_Saved"]         = round(total_realized - journal["Reference_IfHeld"], 2)

print(journal[["Date","SPY_Close","Status","Unrealized_PnL","Portfolio_Value"]].to_string())
journal.to_csv("alpaca_journal.csv")
print("Saved: alpaca_journal.csv")

# ============================================================
# AUTO "WHAT I DID TODAY" — dual-timeframe aware
# ============================================================
def generate_what_i_did(signal, has_position, has_exited, realized_pnl, pct_chg=None):
    regime_note = f"Regime: {regime_val} (MA20 ${ma20_val} vs MA50 ${ma50_val})."

    if has_exited and not has_position:
        return (
            f"System exited the position. Realized P&L locked at ${realized_pnl:+.2f}. "
            f"{regime_note} "
            f"Fast signal (MA10/MA30): {'bullish' if signal == 'BULLISH' else 'bearish'}. "
            f"Monitoring for re-entry on next fast golden cross."
        )
    elif has_position:
        return (
            f"System held long SPY. Fast signal remained {signal}. "
            f"{regime_note} Momentum: {momentum_val}. "
            f"Unrealized P&L: {pct_chg:+.2f}% from entry. No exit triggered."
        )
    elif signal == "BULLISH":
        return (
            f"Fast signal turned BULLISH (MA10 ${ma10_val} > MA30 ${ma30_val}). "
            f"{regime_note} "
            f"System entering long position at next market open."
        )
    elif signal == "BEARISH":
        return (
            f"System stayed FLAT. Fast signal bearish (MA10 ${ma10_val} < MA30 ${ma30_val}). "
            f"{regime_note} "
            f"Capital preserved at ${STARTING_CASH + realized_pnl:,.2f}. "
            f"Waiting for MA10 > MA30 crossover."
        )
    else:  # NEUTRAL
        return (
            f"System stayed FLAT. Signal NEUTRAL — fast MAs narrowing. "
            f"MA10: ${ma10_val} | MA30: ${ma30_val} | Gap closing. "
            f"{regime_note} "
            f"Regime is blocking entry. Watching for regime improvement."
        )

# ============================================================
# FETCH MARKET CONTEXT
# ============================================================
def fetch_market_context() -> dict:
    signal_label = (
        "BULLISH — Fast Golden Cross (MA10 > MA30)"
        if signal == "BULLISH"
        else "BEARISH — Fast Death Cross (MA10 < MA30)"
        if signal == "BEARISH"
        else "NEUTRAL — Regime blocking"
    )
    ctx = {
        "ma10":   ma10_val,
        "ma30":   ma30_val,
        "ma20":   ma20_val,
        "ma50":   ma50_val,
        "regime": regime_val,
        "momentum": momentum_val,
        "signal": signal_label,
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

    is_flat  = row["Status"] == "FLAT"
    day_has_pos = not is_flat
    
    what_i_did_auto = generate_what_i_did(
        signal, day_has_pos, has_exited, realized_pnl,
        pct_chg=row["PnL_Pct"] if day_has_pos else None
    )

    if not GROQ_API_KEY:
        return _placeholder_narrative(what_i_did_auto)

    client   = Groq(api_key=GROQ_API_KEY)
    is_flat  = row["Status"] == "FLAT"
    day_has_pos = not is_flat

    pnl_line = (
        f"Realized P&L locked: ${realized_pnl:+.2f} (position exited)"
        if has_exited and is_flat
        else f"Unrealized P&L: ${row['Unrealized_PnL']:+.2f} ({row['PnL_Pct']:+.3f}%)"
    )
    signal_saved_line = (
        f"Signal saved vs passive hold: ${row['Signal_Saved']:+.2f}"
        if has_exited else ""
    )
    headlines_block = "\n".join(f"  - {h}" for h in ctx["headlines"])

    prompt = f"""You are writing daily narrative entries for a quantitative trading journal.
The trader runs a paper portfolio ($100k) on SPY using a dual-timeframe SMA crossover strategy:
- Fast signal: SMA 10/30 crossover for entries and exits
- Slow filter: SMA 20/50 as regime context (avoid longs in strong bear regimes)
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

=== SIGNAL ENGINE ===
Fast MAs: MA10 ${ctx['ma10']} | MA30 ${ctx['ma30']} | Signal: {ctx['signal']}
Slow MAs: MA20 ${ctx['ma20']} | MA50 ${ctx['ma50']} | Regime: {ctx['regime']}
Momentum: {ctx['momentum']}
Signal source: {ctx['signal_source']}

=== MACRO DATA ===
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
  "regime_call": "one short label e.g. RISK-OFF / Recovery Rally / Consolidation",
  "market_context": "2-3 sentences on what happened in markets today",
  "strategy_note": "1-2 sentences on the dual-timeframe signal and what the system did",
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
        return _placeholder_narrative(what_i_did_auto)

def _placeholder_narrative(what_i_did_auto):
    return {
        "regime_call":    "_fill in_",
        "market_context": "_fill in_",
        "strategy_note":  "_fill in_",
        "key_learning":   "_fill in_",
        "what_i_did_today": what_i_did_auto,
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
    is_flat  = row["Status"] == "FLAT"
    day_has_pos = not is_flat

    if date_key in narratives:
        existing = narratives[date_key]
        # Always refresh what_i_did_today — never use stale version
        existing["what_i_did_today"] = generate_what_i_did(
            signal, day_has_pos, has_exited, realized_pnl,
            pct_chg=row["PnL_Pct"] if day_has_pos else None
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
             narratives, signal_state, trades=None):

    today_str  = date.today().strftime("%B %d, %Y")
    total_days = len(journal)
    latest     = journal.iloc[-1]
    L = []

    # Header — now shows dual-timeframe info
    regime_label = signal_state.get("regime", "UNKNOWN")
    momentum_label = signal_state.get("momentum", "UNKNOWN")
    override_note = ""
    if signal_state.get("price_override"):
        override_note = f" | ⚡ Price Override Active (+{signal_state.get('price_pct_above_ma50', 0):.1f}% above MA50)"

    L += [
        f"# ALPACA PAPER JOURNAL — {SYMBOL}",
        f"_Last updated: {today_str} | Day {total_days} of 90_",
        f"_Strategy: Dual-Timeframe SMA Crossover (Fast: 10/30, Regime: 20/50) + Price Override_",
        f"_Source of truth: Alpaca fills | Close prices: Alpaca Market Data API_",
        f"_Signal source: signal_state.json | Narrative: Groq llama-3.1-8b-instant_",
        "",
        "> ⚠️ **RECONCILIATION NOTE**  ",
        f"> All P&L uses Alpaca fill prices. First entry: **${actual_entry:.3f}/share**",
        f"> ({entry_date}, after-hours fill).",
        "",
        f"> 📡 **CURRENT SIGNAL** ({signal_state['date']}): **{signal_state['signal']}**{override_note}  ",
        f"> Fast: MA10 ${signal_state.get('ma10', 'N/A')} | MA30 ${signal_state.get('ma30', 'N/A')}  ",
        f"> Slow: MA20 ${signal_state.get('ma20', 'N/A')} | MA50 ${signal_state.get('ma50', 'N/A')}  ",
        f"> Regime: **{regime_label}** | Momentum: **{momentum_label}** | Session: {signal_state['session']}",
        "",
    ]

    # Strategy description
    L += [
        "## Strategy Description", "",
        "This journal tracks a **dual-timeframe SMA crossover** strategy on SPY:", "",
        "| Component | MAs | Purpose |",
        "|---|---|---|",
        "| **Fast Signal** | SMA 10 / SMA 30 | Entry and exit triggers |",
        "| **Regime Filter** | SMA 20 / SMA 50 | Trend context — blocks longs in strong bear regimes |",
        "| **Price Override** | Close > MA50 × 1.02 | Overrides bearish regime if price has clearly recovered |",
        "| **Position Sizing** | 40% max allocation | Risk-based sizing with 1.5% stop-loss |", "",
        "**Rules:**",
        "- BUY when MA10 > MA30 AND regime ≠ STRONG_BEAR",
        "- BUY when price > 2% above MA50 AND above both fast MAs (price override)",
        "- SELL when MA10 < MA30 (unless price override active)",
        "- Long-only (no shorting)", "",
    ]

    # Trade History — show ALL trades
    if trades:
        closed = [t for t in trades if t["status"] == "CLOSED"]
        open_t = next((t for t in trades if t["status"] == "OPEN"), None)
        total_real = sum(t["pnl"] for t in closed)

        L += [
            "## Trade History", "",
            f"**Total trades:** {len(trades)} | **Closed:** {len(closed)} | "
            f"**Open:** {'Yes' if open_t else 'No'} | "
            f"**Cumulative Realized P&L:** {_fmt(total_real)}", "",
            "| Trade | Entry | Exit | Shares | P&L | Status |",
            "|---|---|---|---|---|---|",
        ]
        for t in trades:
            if t["status"] == "CLOSED":
                L.append(f"| T{t['id']} | ${t['entry_price']:.3f} ({t['entry_date']}) | "
                          f"${t['exit_price']:.3f} ({t['exit_date']}) | "
                          f"{t['shares']} | {_fmt(t['pnl'])} | ✅ Closed |")
            else:
                L.append(f"| T{t['id']} | ${t['entry_price']:.3f} ({t['entry_date']}) | "
                          f"— | {t['shares']} | — | 🟢 Open |")
        L.append("")

    # Legacy trade summary
    L += [
        "## Account Summary", "",
        "| Field | Value |", "|---|---|",
        f"| Symbol | {SYMBOL} |",
        f"| Starting capital | ${STARTING_CASH:,} |",
        f"| Alpaca equity | ${portfolio_val:,.2f} |",
        f"| Alpaca cash | ${cash:,.2f} |",
        f"| Cumulative realized P&L | {_fmt(realized_pnl)} |",
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
        narr     = narratives.get(date_key, _placeholder_narrative("_fill in_"))

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

    # Strategy evolution log — shows the fix
    L += [
        "## Strategy Evolution Log", "",
        "| Date | Change | Rationale |",
        "|---|---|---|",
        "| 2026-03-09 | Initial deployment: SMA 20/50 crossover | Simple trend-following baseline |",
        "| 2026-04-16 | Upgraded to dual-timeframe SMA 10/30 + 20/50 regime filter | "
        "SMA 20/50 too slow — sat flat 24/27 days during volatile market. "
        "Faster MAs capture recovery rallies. 20/50 retained as regime filter. |",
        "| 2026-04-16 | Added price-action override | If price closes >2% above MA50 AND above "
        "both fast MAs, override bearish regime filter. Prevents sitting flat during V-shaped recoveries. "
        "Multi-trade journal tracking added. |",
        "",
    ]

    L += [
        "## Anomaly Log", "",
        "| # | Date | Observation | Hypothesis | Status |",
        "|---|---|---|---|---|",
        "| 1 | 2026-03-12 to 2026-04-15 | System sat FLAT for 24 consecutive days despite "
        "10%+ SPY recovery | SMA 20/50 too slow to catch regime change; death cross persisted "
        "even as price recovered above both MAs | Fixed — switched to SMA 10/30 |",
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
    first_entry_date, exit_date, portfolio_val, cash, total_buy_qty,
    benchmark_shares, benchmark_entry_price, SYMBOL, STARTING_CASH,
    narratives=narratives,
    signal_state=signal_state,
    trades=trades
)

md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alpaca_journal.md")
with open(md_path, "w") as f:
    f.write(md_content)
print(f"Saved: {md_path}")
