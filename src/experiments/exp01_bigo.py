"""EXP-01: Big-O verification — do measured scalings match CIU claims?
Claim: push O(1) amortized, binary search O(log n), mergesort/quicksort O(n log n), BFS O(V+E).
Method: fit log-log slope; PASS if slope within tolerance of theory.
"""
from __future__ import annotations
import time, random, math, json, pathlib
from src.dsa.core import mergesort, binary_search, Graph

random.seed(42)
ROOT = pathlib.Path(__file__).resolve().parents[2]

def slope(ns, ts):
    import math
    lx = [math.log(n) for n in ns]
    ly = [math.log(max(t, 1e-9)) for t in ts]
    mx, my = sum(lx)/len(lx), sum(ly)/len(ly)
    num = sum((x-mx)*(y-my) for x, y in zip(lx, ly))
    den = sum((x-mx)**2 for x in lx) or 1e-12
    return num/den

def timeit(fn, *a, repeat=3):
    best = float("inf")
    for _ in range(repeat):
        t = time.perf_counter(); fn(*a)
        best = min(best, time.perf_counter()-t)
    return best

def main():
    ns = [2000, 4000, 8000, 16000]
    t_sort = [timeit(mergesort, [random.randint(0,10**9) for _ in range(n)]) for n in ns]
    s_sort = slope(ns, t_sort)  # theory ~1.0-1.15 in log-log with log factor
    arr = sorted(range(200000))
    ns2 = [10000, 40000, 160000]
    t_bs = [timeit(binary_search, arr[:n], n-1) for n in ns2]
    # binary search should be ~flat: slope ~0
    s_bs = slope(ns2, t_bs)
    g_sizes = [500, 1000, 2000, 4000]
    t_bfs = []
    for n in g_sizes:
        g = Graph(directed=False)
        for i in range(n):
            g.add_edge(i, (i+1) % n)
        t_bfs.append(timeit(g.bfs, 0))
    s_bfs = slope(g_sizes, t_bfs)  # theory ~1.0
    verdict = {
        "mergesort_loglog_slope": round(s_sort, 3),
        "mergesort_expect": "~1.0-1.3 (n log n)",
        "mergesort_pass": 0.8 <= s_sort <= 1.5,
        "binary_search_loglog_slope": round(s_bs, 3),
        "binary_search_expect": "~0 (log n)",
        "binary_search_pass": s_bs < 0.5,
        "bfs_loglog_slope": round(s_bfs, 3),
        "bfs_expect": "~1.0 (V+E)",
        "bfs_pass": 0.7 <= s_bfs <= 1.4,
    }
    out = {"ns_sort": ns, "t_sort": t_sort, "t_bs": t_bs, "t_bfs": t_bfs, "verdict": verdict}
    (ROOT/"results"/"exp01_bigo.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(verdict, indent=2))

if __name__ == "__main__":
    main()
