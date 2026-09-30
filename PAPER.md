# From Completion to Competence: Verifying Coding Interview University Against 2026 Hiring Reality, Benchmarks, and Live Market Data

**Draft — publishable paper skeleton. All numbers reproduce via `docker compose`. Anchor: 2026-09-30, AAPL 329.4.**

## Abstract

We verify Washam's Coding Interview University (CIU) by rebuilding it from scratch and testing each load-bearing claim with measurement on public/live data. Complexity claims reproduce (mergesort slope 1.127, binary-search 0.029, BFS 1.005). A 15-pattern taxonomy explains modern loops better than volume (Blind75 86.7%, NeetCode150 100%, CIU-core 80%). Spaced retrieval dominates cramming (strength 2.671 vs 0.815). Implementations hold on live-anchored market data. CIU's "system design optional" flag is stale for 2026. We contribute five testable hidden patterns and a full replication package.

## 1. Introduction

CIU (362k★) promises a multi-month path from "don't know stack from heap" to Big-Tech-ready. Practitioner reviews (Prachub 2026) call it "strongest free foundations map, insufficient alone." We turn that qualitative verdict into falsifiable checks RQ1–RQ5 (see README).

## 2. Related work

Pattern-first prep (Levelop, Educative, Nexalgotrix, PrecisionAI); time-boxed plans (CronJobs 6-week, InterviewChamp 30-day, TechInterviewHandbook 3-month/Grind75); FAANG frequency datasets (techreign 51k reports); AI-era system design (TechInterview, DeepEngineering, Aceloop RESHADED, OpenAI loops); retention science (distributed practice, FSRS/Anki, deliberate practice); community reception (HN). CIU original as baseline.

## 3. Method

Sequential one-at-a-time evidence sweep (20 steps, §2 README) with 429-safe discipline; voting rule (≥2 independent 2026 sources + 1 executable check); negative results retained (searxng outage, arxiv off-topic, SO/GDELT nulls). Rebuild scope = CIU topic inventory via gitmcp. Verification harness = pytest + log-log slope fitting + live-anchored market harness + retention simulation + RESHADED rubric.

## 4. Implementation (replication artifact)

`src/dsa/`: Vector (amortized doubling/halving), LinkedList (tail pointer, two-pointer nth-from-end, in-place reverse), Stack/QueueLinked/QueueFixedArray (circular buffer), HashTable (linear probing, lazy deletion), binary_search (+recursive), BST (insert/count/inorder/delete/successor/validate), MaxHeap (sift/heapify/heapsort), mergesort/quicksort, Graph (BFS/DFS-rec/iter/Dijkstra/cycle/toposort/components), Trie, fib-DP/coin-change. 7 pytest suites pass.

## 5. Results

Identical to README §4 with full tables + CSV/JSON in `results/`. Key figures: sort-scaling table; slope fits; coverage bars; retention curves; live-market agreement matrix; RESHADED rubric.

## 6. Hidden patterns → hypotheses (future work)

H1–H5 as in README §5, each with proposed design: (H1) pattern-labeling RCT; (H2) diagnose-first RCT; (H3) mini-loop fatigue instrumentation; (H4) AI-gap per round type; (H5) coverage-vs-level matrix. Each is scoped as one publishable study.

## 7. Threats to validity

No hiring-outcome RCT; single-machine timing; single-symbol anchor; practitioner-source bias; per-company AI policy variance. Mitigations: slopes not absolutes; multi-algorithm agreement; nulls published; provenance JSON.

## 8. Conclusion

Use CIU to repair diagnosed gaps, not as completion quest. Drill 15 patterns cold, mock early (5–8), space retrieval, add SQL/frontend/design per role, taper before loop. Artifact + data + paper skeleton are public for extension.

## References

See `docs/CITATIONS.md` (URLs + access dates). Data: `data/live_market_snapshot.json` (yfinance via tool, 2026-09-30T12:49Z); Kaggle LeetCode sets (MIT/Apache-2.0); techreign 51k reports.
