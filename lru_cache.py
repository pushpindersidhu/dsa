from typing import Dict, Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.size = 0
        self.capacity = capacity
        self.map: Dict[int, Node] = {}
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._prepend(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)

        if key in self.map:
            self._remove(self.map[key])
            self.map.pop(key)
            self._prepend(node)
            self.map[key] = node
            return

        if self.size == self.capacity:
            if self.tail:
                self.map.pop(self.tail.key)
                self._remove_tail()
                self.size -= 1

        self._prepend(node)
        self.map[key] = node
        self.size += 1

    def _prepend(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def _remove(self, node: Node) -> None:
        if node == self.head:
            node.prev = None
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev
            node.next = None

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def _remove_tail(self) -> None:
        if self.head == self.tail:
            self.head = None
            self.tail = None

        if self.tail:
            if self.tail.prev:
                self.tail.prev.next = None
            self.tail = self.tail.prev


if __name__ == "__main__":
    import unittest

    class TestLRUCache(unittest.TestCase):

        def test_lru_cache(self):
            lru = LRUCache(3)

            self.assertEqual(lru.get(1), -1)
            lru.put(1, 1)
            self.assertEqual(lru.get(1), 1)

            lru.put(2, 2)
            self.assertEqual(lru.get(2), 2)

            lru.put(3, 3)
            self.assertEqual(lru.get(3), 3)

            lru.put(4, 4)
            self.assertEqual(lru.get(4), 4)
            self.assertEqual(lru.get(1), -1)
            self.assertEqual(lru.get(2), 2)

            lru.put(5, 5)
            self.assertEqual(lru.get(3), -1)

            lru.put(5, 0)
            self.assertEqual(lru.get(5), 0)

    unittest.main()
