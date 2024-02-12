from typing import Optional


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node | None = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.root = None

    def insert_at_start(self, val: int) -> None:
        node = Node(val)
        if self.root:
            node.next = self.root

        self.root = node

    def insert_at_end(self, val: int) -> None:
        if not self.root:
            self.root = Node(val)
            return

        curr = self.root
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def remove(self, index: Optional[int] = None) -> int:
        if not self.root:
            return -1

        if index is None or index == 0:
            val = self.root.val
            self.root = self.root.next
            return val

        curr = self.root
        for _ in range(index - 1):
            if not curr.next:
                return -1
            curr = curr.next

        if not curr.next:
            return -1

        val = curr.next.val
        curr.next = curr.next.next

        return val

    def is_empty(self) -> bool:
        return not self.root

    def traverse(self) -> list[int]:
        values = []
        curr = self.root
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values


if __name__ == "__main__":
    import unittest

    class TestSinglyLinkedList(unittest.TestCase):
        def test_singly_linked_list(self):
            singly_linked_list = SinglyLinkedList()
            self.assertTrue(singly_linked_list.is_empty())

            singly_linked_list.insert_at_start(1)
            singly_linked_list.insert_at_start(2)
            singly_linked_list.insert_at_start(3)
            self.assertEqual(singly_linked_list.traverse(), [3, 2, 1])

            singly_linked_list.insert_at_end(4)
            singly_linked_list.insert_at_end(5)
            singly_linked_list.insert_at_end(6)
            self.assertEqual(singly_linked_list.traverse(), [3, 2, 1, 4, 5, 6])

            self.assertEqual(singly_linked_list.remove(), 3)
            self.assertEqual(singly_linked_list.remove(0), 2)
            self.assertEqual(singly_linked_list.remove(3), 6)
            self.assertEqual(singly_linked_list.traverse(), [1, 4, 5])

            self.assertFalse(singly_linked_list.is_empty())

    unittest.main()
