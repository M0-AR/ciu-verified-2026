# REPRODUCIBILITY

Requires: Python 3.12, Docker 29+ (optional but recommended), 2GB RAM.

```bash
cd /home/md/src/ciu-verified-2026
pip install -r requirements.txt
pytest -v                          # expect 7 passed
python -m src.benchmarks.run_all   # results/benchmark_results.{json,csv}
for e in exp01_bigo exp02_patterns exp03_retention exp04_live_market exp05_system_design; do python -m src.experiments.$e; done
docker compose build && docker compose run benchmarks
docker compose run lab
```

Seeds: 42 everywhere. Outputs deterministic except wall-clock timings (slopes stable).
Live snapshot frozen in `data/live_market_snapshot.json`; re-query yfinance to refresh.
CI: `.github/workflows/ci.yml` runs full chain on push/PR.
Share publicly: push this folder to GitHub; artifact includes code+data+paper+docker.
