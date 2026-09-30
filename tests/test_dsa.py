import random
from src.dsa.vector import Vector
from src.dsa.linked_list import LinkedList
from src.dsa.stack_queue_hash import Stack, QueueLinked, QueueFixedArray, HashTable
from src.dsa.core import (binary_search, binary_search_recursive, BST, MaxHeap,
    mergesort, quicksort, Graph, Trie, fib_dp, coin_change)


def test_vector():
    v = Vector()
    for i in range(100):
        v.push(i)
    assert v.size() == 100 and v.capacity() >= 100
    assert v.at(0) == 0 and v.find(50) == 50 and v.find(999) == -1
    v.insert(0, -1); assert v.at(0) == -1
    v.prepend(-2); assert v.at(0) == -2
    assert v.pop() == 99
    v.delete(0); assert v.at(0) == -1
    v.remove(-1); assert v.find(-1) == -1
    assert not v.is_empty()


def test_linked_list():
    ll = LinkedList()
    ll.push_back(1); ll.push_back(2); ll.push_front(0)
    assert ll.to_list() == [0, 1, 2] and ll.size() == 3
    assert ll.front() == 0 and ll.back() == 2
    assert ll.value_at(1) == 1 and ll.value_n_from_end(1) == 2
    ll.insert(1, 9); assert ll.to_list() == [0, 9, 1, 2]
    ll.erase(1); assert ll.to_list() == [0, 1, 2]
    ll.reverse(); assert ll.to_list() == [2, 1, 0]
    assert ll.pop_front() == 2 and ll.pop_back() == 0
    assert ll.remove_value(1) and ll.empty()


def test_stack_queue():
    s = Stack(); s.push(1); s.push(2)
    assert s.pop() == 2 and s.peek() == 1 and not s.empty()
    q = QueueLinked(); q.enqueue(1); q.enqueue(2)
    assert q.dequeue() == 1 and not q.empty()
    f = QueueFixedArray(2); f.enqueue("a"); f.enqueue("b")
    assert f.full() and f.dequeue() == "a" and not f.full()


def test_hash():
    h = HashTable(m=16)
    h.add("a", 1); h.add("b", 2); h.add("a", 3)
    assert h.get("a") == 3 and h.exists("b") and not h.exists("z")
    h.remove("b"); assert not h.exists("b")


def test_search_sort():
    a = sorted(random.sample(range(10000), 1000))
    assert binary_search(a, a[500]) == 500 and binary_search(a, -1) == -1
    assert binary_search_recursive(a, a[10]) == 10
    arr = [random.randint(0, 1000) for _ in range(500)]
    assert mergesort(arr) == sorted(arr) and quicksort(arr) == sorted(arr)
    assert MaxHeap().heap_sort(arr) == sorted(arr)


def test_bst_heap():
    b = BST()
    for x in [5, 3, 7, 2, 4, 6, 8]:
        b.insert(x)
    assert b.get_node_count() == 7 and b.print_values() == [2, 3, 4, 5, 6, 7, 8]
    assert b.is_in_tree(4) and not b.is_in_tree(9)
    assert b.get_height() == 3 and b.get_min() == 2 and b.get_max() == 8
    assert b.is_binary_search_tree() and b.get_successor(5) == 6 and b.get_successor(8) == -1
    b.delete_value(5); assert b.is_binary_search_tree() and b.get_node_count() == 6
    h = MaxHeap()
    for x in [3, 1, 4, 1, 5]:
        h.insert(x)
    assert h.get_max() == 5 and h.extract_max() == 5 and h.get_size() == 4


def test_graph_trie_dp():
    g = Graph(directed=True)
    g.add_edge("A", "B"); g.add_edge("B", "C"); g.add_edge("A", "C", 5)
    assert g.bfs("A") == ["A", "B", "C"]
    assert set(g.dfs_recursive("A")) == {"A", "B", "C"}
    assert g.dijkstra("A")["C"] == 2.0  # A->B->C (1+1) beats direct A->C weight 5
    assert not g.has_cycle()
    g2 = Graph(); g2.add_edge("X", "Y"); g2.add_edge("Y", "X")
    assert g2.has_cycle()
    dag = Graph(); dag.add_edge(1, 2); dag.add_edge(1, 3); dag.add_edge(2, 3)
    assert dag.topological_sort()[0] == 1
    t = Trie(); t.insert("hello")
    assert t.search("hello") and not t.search("hell") and t.starts_with("hell")
    assert fib_dp(10) == 55 and coin_change([1, 3, 4], 6) == 2
