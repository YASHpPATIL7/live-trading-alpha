#!/bin/bash
PROJECT_DIR="/Users/yashpatil/Local_Mark1/live-trading-alpha"
VENV="/Users/yashpatil/Local_Mark1/live-trading-alpha/.venv/bin/python"
LOG_DIR="$PROJECT_DIR/logs"
SESSION_LABEL="${1:-UNNAMED}"
mkdir -p "$LOG_DIR"
LOGFILE="$LOG_DIR/alpaca_$(date +%Y-%m-%d)_${SESSION_LABEL}.log"
echo "======================================" >> "$LOGFILE"
echo "[$(date '+%Y-%m-%d %H:%M:%S IST')] SESSION: $SESSION_LABEL" >> "$LOGFILE"
echo "======================================" >> "$LOGFILE"
echo "[$(date '+%H:%M:%S')] START AlpacaDaily.py" >> "$LOGFILE"
"$VENV" "$PROJECT_DIR/AlpacaDaily.py" >> "$LOGFILE" 2>&1
EXIT1=$?
if [ $EXIT1 -ne 0 ]; then
  echo "[$(date '+%H:%M:%S')] AlpacaDaily.py FAILED (exit $EXIT1) — aborting" >> "$LOGFILE"
  exit 1
fi
echo "[$(date '+%H:%M:%S')] AlpacaDaily.py OK" >> "$LOGFILE"
echo "[$(date '+%H:%M:%S')] START Alpaca_Journal_NewGroq.py" >> "$LOGFILE"
"$VENV" "$PROJECT_DIR/Alpaca_Journal_NewGroq.py" >> "$LOGFILE" 2>&1
echo "[$(date '+%H:%M:%S')] Alpaca_Journal_NewGroq.py done" >> "$LOGFILE"
echo "[$(date '+%H:%M:%S')] Pipeline complete" >> "$LOGFILE"
