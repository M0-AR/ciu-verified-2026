"""Stack, Queue (linked + circular array), HashTable (linear probing) — CIU modules."""
from __future__ import annotations
from collections import deque
from typing import Optional


class Stack:
    def __init__(self):
        self._d = []

    def push(self, v) -> None:
        self._d.append(v)

    def pop(self):
        if not self._d:
            raise IndexError("pop from empty stack")
        return self._d.pop()

    def peek(self):
        if not self._d:
            raise IndexError("empty")
        return self._d[-1]

    def empty(self) -> bool:
        return len(self._d) == 0

    def __len__(self):
        return len(self._d)


class QueueLinked:
    def __init__(self):
        self._d = deque()

    def enqueue(self, v) -> None:
        self._d.append(v)

    def dequeue(self):
        if not self._d:
            raise IndexError("dequeue from empty")
        return self._d.popleft()

    def empty(self) -> bool:
        return len(self._d) == 0


class QueueFixedArray:
    """Circular buffer FIFO with O(1) enqueue/dequeue."""

    def __init__(self, capacity: int):
        assert capacity > 0
        self._a = [None] * capacity
        self._cap = capacity
        self._head = 0
        self._count = 0

    def empty(self) -> bool:
        return self._count == 0

    def full(self) -> bool:
        return self._count == self._cap

    def enqueue(self, v) -> None:
        if self.full():
            raise OverflowError("queue full")
        tail = (self._head + self._count) % self._cap
        self._a[tail] = v
        self._count += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty")
        v = self._a[self._head]
        self._a[self._head] = None
        self._head = (self._head + 1) % self._cap
        self._count -= 1
        return v


_MISSING = object()


class HashTable:
    """Open addressing, linear probing, lazy deletion. hash(k,m) exposed."""

    def __init__(self, m: int = 64):
        assert m > 0
        self.m = m
        self.keys = [None] * m
        self.vals = [None] * m
        self._deleted = [False] * m
        self.n = 0

    @staticmethod
    def hash(k, m: int) -> int:
        return hash(k) % m

    def _probe(self, key):
        h = self.hash(key, self.m)
        first_del = -1
        for i in range(self.m):
            j = (h + i) % self.m
            if self.keys[j] is None and not self._deleted[j]:
                return (first_del if first_del != -1 else j), False
            if self._deleted[j] and first_del == -1:
                first_del = j
            elif self.keys[j] == key and not self._deleted[j]:
                return j, True
        if first_del != -1:
            return first_del, False
        raise OverflowError("hash table full")

    def add(self, key, value) -> None:
        j, found = self._probe(key)
        if found:
            self.vals[j] = value
            return
        self.keys[j] = key
        self.vals[j] = value
        self._deleted[j] = False
        self.n += 1

    def exists(self, key) -> bool:
        _, found = self._probe(key)
        return found

    def get(self, key):
        j, found = self._probe(key)
        if not found:
            raise KeyError(key)
        return self.vals[j]

    def remove(self, key) -> None:
        j, found = self._probe(key)
        if not found:
            raise KeyError(key)
        self.keys[j] = None
        self.vals[j] = None
        self._deleted[j] = True
        self.n -= 1
