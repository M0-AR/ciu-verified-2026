"""Vector (dynamic array) — CIU Arrays module, verified implementation."""
from __future__ import annotations


class Vector:
    def __init__(self, capacity: int = 16):
        cap = 16
        while cap < capacity:
            cap *= 2
        self._cap = cap
        self._data = [None] * self._cap
        self._size = 0

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._cap

    def is_empty(self) -> bool:
        return self._size == 0

    def at(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("index out of bounds")
        return self._data[index]

    def push(self, item) -> None:
        if self._size == self._cap:
            self._resize(self._cap * 2)
        self._data[self._size] = item
        self._size += 1

    def insert(self, index: int, item) -> None:
        if index < 0 or index > self._size:
            raise IndexError("index out of bounds")
        if self._size == self._cap:
            self._resize(self._cap * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def prepend(self, item) -> None:
        self.insert(0, item)

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size > 0 and self._size == self._cap // 4:
            self._resize(self._cap // 2)
        return val

    def delete(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("index out of bounds")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size > 0 and self._size == self._cap // 4:
            self._resize(max(16, self._cap // 2))

    def remove(self, item) -> None:
        i = self.find(item)
        while i != -1:
            self.delete(i)
            i = self.find(item)

    def find(self, item) -> int:
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def _resize(self, new_cap: int) -> None:
        new_cap = max(16, new_cap)
        nd = [None] * new_cap
        for i in range(self._size):
            nd[i] = self._data[i]
        self._data = nd
        self._cap = new_cap

    def to_list(self):
        return [self._data[i] for i in range(self._size)]
