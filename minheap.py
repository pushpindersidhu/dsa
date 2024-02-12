from typing import List


class MinHeap:

    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) == 0:
            return -1

        if len(self.heap) == 1:
            return self.heap.pop()

        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return val

    @staticmethod
    def heapify(array: List[int]) -> None:
        for i in range(len(array) // 2 - 1, -1, -1):
            MinHeap._heapify(array, i)

    @staticmethod
    def _heapify(array: List[int], index: int) -> None:
        min_index = index
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        if left_index < len(array) and array[min_index] > array[left_index]:
            min_index = left_index

        if right_index < len(array) and array[min_index] > array[right_index]:
            min_index = right_index

        if min_index != index:
            array[index], array[min_index] = array[min_index], array[index]
            MinHeap._heapify(array, min_index)

    def _heapify_up(self, index: int) -> None:
        while index > 0 and self._parent(index) > self.heap[index]:
            pindex = self._parent_index(index)
            self._swap(index, pindex)
            index = pindex

    def _heapify_down(self, index: int) -> None:
        lindex = self._left_child_index(index)
        rindex = self._right_child_index(index)

        min_index = index
        if lindex < len(self.heap) and self.heap[lindex] < self.heap[min_index]:
            min_index = lindex
        if rindex < len(self.heap) and self.heap[rindex] < self.heap[min_index]:
            min_index = rindex

        if min_index != index:
            self._swap(index, min_index)
            self._heapify_down(min_index)

    def _parent_index(self, index: int) -> int:
        return index // 2

    def _parent(self, index: int) -> int:
        return self.heap[self._parent_index(index)]

    def _left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def _left_child(self, index: int) -> int:
        return self.heap[self._left_child_index(index)]

    def _right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def _right_child(self, index: int) -> int:
        return self.heap[self._right_child_index(index)]

    def _swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


if __name__ == "__main__":
    import unittest

    class TestMinHeap(unittest.TestCase):

        def test_min_heap(self):
            min_heap = MinHeap()
            min_heap.push(5)
            min_heap.push(3)
            min_heap.push(7)
            min_heap.push(2)
            min_heap.push(1)
            self.assertEqual(min_heap.pop(), 1)
            self.assertEqual(min_heap.pop(), 2)
            self.assertEqual(min_heap.pop(), 3)
            self.assertEqual(min_heap.pop(), 5)
            self.assertEqual(min_heap.pop(), 7)
            self.assertEqual(min_heap.pop(), -1)

        def test_heapify(self):
            test_cases = [
                (
                    [73, 20, 29, 12, 38, 44, 32, 46, 34, 52, 65],
                    [12, 20, 29, 34, 38, 44, 32, 46, 73, 52, 65],
                ),
                ([5, 3, 7, 2, 1], [1, 2, 7, 5, 3]),
                ([3, 7, 2, 1], [1, 3, 2, 7]),
                ([7, 2, 1], [1, 2, 7]),
                ([2, 1], [1, 2]),
                ([1], [1]),
            ]

            for array, expected in test_cases:
                MinHeap.heapify(array)
                self.assertEqual(array, expected)

    unittest.main()
