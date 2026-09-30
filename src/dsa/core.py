"""BST, MaxHeap, binary search, sorting, graphs, trie, DP samples — CIU core."""
from __future__ import annotations
from collections import deque
import heapq


def binary_search(a: list[int], target: int) -> int:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(a: list[int], target: int, lo=0, hi=None) -> int:
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == target:
        return mid
    if a[mid] < target:
        return binary_search_recursive(a, target, mid + 1, hi)
    return binary_search_recursive(a, target, lo, mid - 1)


class BSTNode:
    __slots__ = ("v", "left", "right")

    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self._n = 0

    def insert(self, v) -> None:
        if self.root is None:
            self.root = BSTNode(v)
            self._n += 1
            return
        cur = self.root
        while True:
            if v == cur.v:
                return
            if v < cur.v:
                if cur.left is None:
                    cur.left = BSTNode(v)
                    self._n += 1
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = BSTNode(v)
                    self._n += 1
                    return
                cur = cur.right

    def get_node_count(self) -> int:
        return self._n

    def print_values(self) -> list:
        out = []

        def inorder(n):
            if n is None:
                return
            inorder(n.left)
            out.append(n.v)
            inorder(n.right)

        inorder(self.root)
        return out

    def is_in_tree(self, v) -> bool:
        cur = self.root
        while cur is not None:
            if v == cur.v:
                return True
            cur = cur.left if v < cur.v else cur.right
        return False

    def get_height(self) -> int:
        def h(n):
            if n is None:
                return 0
            return 1 + max(h(n.left), h(n.right))

        return h(self.root)

    def get_min(self):
        if self.root is None:
            raise ValueError("empty")
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.v

    def get_max(self):
        if self.root is None:
            raise ValueError("empty")
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.v

    def is_binary_search_tree(self) -> bool:
        def valid(n, lo, hi):
            if n is None:
                return True
            if not (lo < n.v < hi):
                return False
            return valid(n.left, lo, n.v) and valid(n.right, n.v, hi)

        return valid(self.root, float("-inf"), float("inf"))

    def delete_value(self, v) -> None:
        def delete(n, v):
            if n is None:
                return None, False
            if v < n.v:
                n.left, d = delete(n.left, v)
                return n, d
            if v > n.v:
                n.right, d = delete(n.right, v)
                return n, d
            # found
            if n.left is None:
                return n.right, True
            if n.right is None:
                return n.left, True
            # successor
            s = n.right
            while s.left is not None:
                s = s.left
            n.v = s.v
            n.right, _ = delete(n.right, s.v)
            return n, True

        self.root, deleted = delete(self.root, v)
        if deleted:
            self._n -= 1

    def get_successor(self, v):
        succ = None
        cur = self.root
        while cur is not None:
            if v < cur.v:
                succ = cur.v
                cur = cur.left
            else:
                cur = cur.right
        return succ if succ is not None else -1

    def delete_tree(self) -> None:
        self.root = None
        self._n = 0


class MaxHeap:
    def __init__(self):
        self.a: list = []

    def get_size(self) -> int:
        return len(self.a)

    def is_empty(self) -> bool:
        return len(self.a) == 0

    def insert(self, v) -> None:
        self.a.append(v)
        self._sift_up(len(self.a) - 1)

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = (i - 1) // 2
            if self.a[i] <= self.a[p]:
                break
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p

    def get_max(self):
        if not self.a:
            raise IndexError("empty")
        return self.a[0]

    def extract_max(self):
        if not self.a:
            raise IndexError("empty")
        top = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            self._sift_down(0)
        return top

    def _sift_down(self, i: int) -> None:
        n = len(self.a)
        while True:
            l, r, big = 2 * i + 1, 2 * i + 2, i
            if l < n and self.a[l] > self.a[big]:
                big = l
            if r < n and self.a[r] > self.a[big]:
                big = r
            if big == i:
                return
            self.a[i], self.a[big] = self.a[big], self.a[i]
            i = big

    def remove(self, i: int) -> None:
        if i < 0 or i >= len(self.a):
            raise IndexError("index out of bounds")
        last = self.a.pop()
        if i < len(self.a):
            self.a[i] = last
            self._sift_up(i)
            self._sift_down(i)

    @classmethod
    def heapify(cls, arr: list):
        h = cls()
        h.a = list(arr)
        for i in range(len(h.a) // 2 - 1, -1, -1):
            h._sift_down(i)
        return h

    def heap_sort(self, arr: list) -> list:
        h = MaxHeap.heapify(arr)
        out = [h.extract_max() for _ in range(len(h.a))]
        return out[::-1]


def mergesort(a: list) -> list:
    if len(a) <= 1:
        return list(a)
    m = len(a) // 2
    L, R = mergesort(a[:m]), mergesort(a[m:])
    i = j = 0
    out = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1
    out.extend(L[i:])
    out.extend(R[j:])
    return out


def quicksort(a: list) -> list:
    if len(a) <= 1:
        return list(a)
    import random

    p = a[random.randrange(len(a))]
    lt = [x for x in a if x < p]
    eq = [x for x in a if x == p]
    gt = [x for x in a if x > p]
    return quicksort(lt) + eq + quicksort(gt)


class Graph:
    """Adjacency-list directed/undirected graph with BFS/DFS/Dijkstra/toposort."""

    def __init__(self, directed: bool = True):
        self.adj: dict = {}
        self.directed = directed

    def add_edge(self, u, v, w: float = 1.0) -> None:
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, [])
        if not self.directed:
            self.adj[v].append((u, w))

    def bfs(self, s):
        seen = {s}
        q = deque([s])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return order

    def dfs_recursive(self, s):
        seen, order = set(), []

        def dfs(u):
            seen.add(u)
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in seen:
                    dfs(v)

        dfs(s)
        return order

    def dfs_iterative(self, s):
        seen, st, order = set(), [s], []
        while st:
            u = st.pop()
            if u in seen:
                continue
            seen.add(u)
            order.append(u)
            for v, _ in reversed(self.adj.get(u, [])):
                if v not in seen:
                    st.append(v)
        return order

    def dijkstra(self, s):
        dist = {s: 0.0}
        pq = [(0.0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, float("inf")):
                continue
            for v, w in self.adj.get(u, []):
                nd = d + w
                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist

    def has_cycle(self) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {u: WHITE for u in self.adj}

        def dfs(u):
            color[u] = GRAY
            for v, _ in self.adj.get(u, []):
                if color.get(v, WHITE) == GRAY:
                    return True
                if color.get(v, WHITE) == WHITE and dfs(v):
                    return True
            color[u] = BLACK
            return False

        return any(dfs(u) for u in self.adj if color[u] == WHITE)

    def topological_sort(self):
        if self.has_cycle():
            raise ValueError("graph has cycle")
        seen, out = set(), []

        def dfs(u):
            seen.add(u)
            for v, _ in self.adj.get(u, []):
                if v not in seen:
                    dfs(v)
            out.append(u)

        for u in self.adj:
            if u not in seen:
                dfs(u)
        return out[::-1]

    def connected_components_undirected(self):
        seen, comps = set(), []
        for s in self.adj:
            if s in seen:
                continue
            comp, stack = [], [s]
            seen.add(s)
            while stack:
                u = stack.pop()
                comp.append(u)
                for v, _ in self.adj.get(u, []):
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            comps.append(comp)
        return comps


class Trie:
    def __init__(self):
        self.root: dict = {}
        self.END = "$"

    def insert(self, word: str) -> None:
        n = self.root
        for ch in word:
            n = n.setdefault(ch, {})
        n[self.END] = True

    def search(self, word: str) -> bool:
        n = self.root
        for ch in word:
            if ch not in n:
                return False
            n = n[ch]
        return self.END in n

    def starts_with(self, prefix: str) -> bool:
        n = self.root
        for ch in prefix:
            if ch not in n:
                return False
            n = n[ch]
        return True


def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def coin_change(coins: list[int], amount: int) -> int:
    INF = amount + 1
    dp = [0] + [INF] * amount
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] != INF else -1
