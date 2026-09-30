"""Singly linked list with tail pointer + doubly-linked note — CIU Linked Lists."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: object
    nxt: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def empty(self) -> bool:
        return self._size == 0

    def _node_at(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError("index out of bounds")
        cur = self.head
        for _ in range(index):
            cur = cur.nxt  # type: ignore
        return cur  # type: ignore

    def value_at(self, index: int):
        return self._node_at(index).value

    def push_front(self, value) -> None:
        n = Node(value, self.head)
        self.head = n
        if self.tail is None:
            self.tail = n
        self._size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty")
        v = self.head.value
        self.head = self.head.nxt
        if self.head is None:
            self.tail = None
        self._size -= 1
        return v

    def push_back(self, value) -> None:
        n = Node(value)
        if self.tail is None:
            self.head = self.tail = n
        else:
            self.tail.nxt = n
            self.tail = n
        self._size += 1

    def pop_back(self):
        if self.head is None:
            raise IndexError("pop from empty")
        if self._size == 1:
            v = self.head.value
            self.head = self.tail = None
            self._size = 0
            return v
        prev = self._node_at(self._size - 2)
        assert prev.nxt is not None and self.tail is not None
        v = self.tail.value
        prev.nxt = None
        self.tail = prev
        self._size -= 1
        return v

    def front(self):
        if self.head is None:
            raise IndexError("empty")
        return self.head.value

    def back(self):
        if self.tail is None:
            raise IndexError("empty")
        return self.tail.value

    def insert(self, index: int, value) -> None:
        if index < 0 or index > self._size:
            raise IndexError("index out of bounds")
        if index == 0:
            return self.push_front(value)
        if index == self._size:
            return self.push_back(value)
        prev = self._node_at(index - 1)
        prev.nxt = Node(value, prev.nxt)
        self._size += 1

    def erase(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("index out of bounds")
        if index == 0:
            self.pop_front()
            return
        prev = self._node_at(index - 1)
        assert prev.nxt is not None
        if prev.nxt is self.tail:
            self.tail = prev
        prev.nxt = prev.nxt.nxt
        self._size -= 1

    def value_n_from_end(self, n: int):
        # 1-indexed from end: n=1 -> last
        if n <= 0 or n > self._size:
            raise IndexError("n out of bounds")
        fast = self.head
        for _ in range(n):
            fast = fast.nxt  # type: ignore
        slow = self.head
        while fast is not None:
            fast = fast.nxt
            slow = slow.nxt  # type: ignore
        assert slow is not None
        return slow.value

    def reverse(self) -> None:
        prev = None
        cur = self.head
        self.tail = self.head
        while cur is not None:
            nxt = cur.nxt
            cur.nxt = prev
            prev = cur
            cur = nxt
        self.head = prev

    def remove_value(self, value) -> bool:
        cur = self.head
        prev = None
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    self.pop_front()
                else:
                    assert cur is not None
                    prev.nxt = cur.nxt
                    if cur is self.tail:
                        self.tail = prev
                    self._size -= 1
                return True
            prev = cur
            cur = cur.nxt
        return False

    def to_list(self):
        out, cur = [], self.head
        while cur is not None:
            out.append(cur.value)
            cur = cur.nxt
        return out
