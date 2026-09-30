#!/usr/bin/env bash
# 40-second proof demo: tests + Big-O + live-market. Pipe to asciinema or vhs.
set -e
echo "=== ciu-verified-2026 — 40-second proof ==="
python -m pytest -v
echo "--- Big-O verification ---"
python -m src.experiments.exp01_bigo
echo "--- Live-market verification (AAPL anchored) ---"
python -m src.experiments.exp04_live_market
echo "=== DONE: all numbers above reproduce via docker compose ==="
