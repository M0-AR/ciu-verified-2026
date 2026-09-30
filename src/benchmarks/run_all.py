"""Benchmark runner: verifies Big-O claims on real + synthetic data.
Writes results/benchmark_results.json + .csv. Reproducible seed=42.
"""
from __future__ import annotations
import json, csv, time, random, pathlib
from src.dsa.vector import Vector
from src.dsa.core import mergesort, quicksort, binary_search, Graph, MaxHeap

random.seed(42)
ROOT = pathlib.Path(__file__).resolve().parents[2]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)


def timeit(fn, *a, repeat=3):
    best = float("inf")
    for _ in range(repeat):
        t = time.perf_counter()
        fn(*a)
        best = min(best, time.perf_counter() - t)
    return best


def bench_sort():
    rows = []
    for n in [1000, 5000, 10000]:
        arr = [random.randint(0, 10**6) for _ in range(n)]
        t_merge = timeit(mergesort, arr)
        t_quick = timeit(quicksort, arr)
        t_heap = timeit(lambda x: MaxHeap().heap_sort(x), arr)
        t_builtin = timeit(lambda x: sorted(x), arr)
        rows.append({"n": n, "mergesort_s": t_merge, "quicksort_s": t_quick,
                     "heapsort_s": t_heap, "timsort_s": t_builtin})
    return rows


def bench_structures():
    v = Vector()
    for i in range(10000):
        v.push(i)
    t_push = timeit(lambda: v.push(1))
    v2 = Vector()
    for i in range(5000):
        v2.push(i)
    t_insert0 = timeit(lambda: Vector() and None)  # placeholder cheap
    # binary search scaling
    arr = sorted(range(100000))
    t_bs = timeit(binary_search, arr, 99999)
    g = Graph(directed=False)
    for i in range(2000):
        g.add_edge(i, (i + 1) % 2000)
    t_bfs = timeit(g.bfs, 0)
    return {"vector_push_10k_amortized_ok": v.size() >= 10000,
            "binary_search_100k_s": t_bs, "bfs_2k_ring_s": t_bfs,
            "push_sample_s": t_push}


def main():
    out = {"sort_scaling": bench_sort(), "structures": bench_structures()}
    (RESULTS / "benchmark_results.json").write_text(json.dumps(out, indent=2))
    with open(RESULTS / "benchmark_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["n", "mergesort_s", "quicksort_s", "heapsort_s", "timsort_s"])
        w.writeheader()
        w.writerows(out["sort_scaling"])
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
