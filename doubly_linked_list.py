from typing import Optional, List


class Node:

    def __init__(self, value: int) -> None:
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        node = Node(value)
        if not self.tail:
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def prepend(self, value: int) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def remove_head(self) -> Optional[int]:
        if not self.head:
            return None

        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return value

    def remove_tail(self) -> Optional[int]:
        if not self.tail:
            return None

        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return value

    def remove(self, value: int) -> None:
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                break

            current = current.next

    def search(self, value: int) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def traverse(self, reversed: bool = False) -> List[int]:
        result = []
        current = self.tail if reversed else self.head
        while current:
            result.append(current.value)
            current = current.prev if reversed else current.next

        return result


if __name__ == "__main__":
    import unittest

    class TestDoublyLinkedList(unittest.TestCase):

        def test_double_linked_list(self):
            dll = DoublyLinkedList()

            self.assertEqual(dll.traverse(), [])

            dll.append(1)
            dll.append(2)
            self.assertEqual(dll.traverse(), [1, 2])
            self.assertEqual(dll.traverse(reversed=True), [2, 1])

            dll.prepend(0)
            self.assertEqual(dll.traverse(), [0, 1, 2])
            self.assertEqual(dll.traverse(reversed=True), [2, 1, 0])

            self.assertTrue(dll.search(2))
            self.assertFalse(dll.search(3))

            self.assertEqual(dll.remove_head(), 0)
            self.assertEqual(dll.traverse(), [1, 2])

            self.assertEqual(dll.remove_tail(), 2)
            self.assertEqual(dll.traverse(), [1])

            dll.remove(1)
            self.assertEqual(dll.traverse(), [])

            self.assertEqual(dll.remove_head(), None)
            self.assertEqual(dll.remove_tail(), None)

    unittest.main()
