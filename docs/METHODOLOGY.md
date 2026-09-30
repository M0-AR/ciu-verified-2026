# METHODOLOGY — voting, 429-safety, no-hand-write-without-verify

1. One search at a time (never parallel websearch). Backoff 5s→10s×3 on 429; fallback DuckDuckGo lite fetch.
2. Distinct keywords per tool (see README §2 table). Snippets never cited — only fetched reads.
3. Inclusion: 2026+ practitioner guides + public datasets + canonical docs. Exclusion: paywalled/undated anecdote alone.
4. Voting: code/README claim needs ≥2 independent 2026 sources + 1 runnable check. Else labeled hypothesis (H1–H5).
5. Negative results kept (searxng outage, arxiv off-topic, SO/GDELT nulls) to avoid publication bias.
6. Live data: single yfinance quote persisted with provenance; synthetic walk deterministically anchored (seed 42, last bar = live quote).
7. Slopes: log-log OLS on wall-clock best-of-3; tolerances pre-registered in exp01.
8. Retention: desirable-difficulty model (massed penalty 0.5×, spaced bonus 1+gap/5) — documents assumption explicitly; not a human trial.
