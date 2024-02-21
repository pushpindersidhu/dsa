from typing import List


def quick_select(arr: List[int], k: int) -> int:
    k = len(arr) - k
    _quick_select(arr, k, 0, len(arr) - 1)

    return arr[k]


def _quick_select(arr: List[int], k: int, left: int, right: int) -> None:
    pivot, p = arr[right], left
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
    arr[p], arr[right] = arr[right], arr[p]

    if p > k:
        _quick_select(arr, k, left, p - 1)
    elif p < k:
        _quick_select(arr, k, p + 1, right)


if __name__ == "__main__":
    import unittest

    class TestQuickSelect(unittest.TestCase):
        def test_quick_select(self):
            test_cases = [
                ([3, 2, 1, 5, 6, 4], 2, 5),
                ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
            ]

            for nums, k, expected in test_cases:
                with self.subTest(nums=nums, k=k, expected=expected):
                    self.assertEqual(quick_select(nums, k), expected)

    unittest.main()
