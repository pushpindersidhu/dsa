from typing import List


def quick_sort(arr: List[int]) -> None:
    """
    Quick Sort

    Choose a pivot and partition the array into two subarrays:
    - Elements less than the pivot
    - Elements greater than the pivot
    Recursively apply quick sort to the subarrays.

    Not stable, In-place, Comparison sort

    Time complexity:
        Worst: O(n^2)
        Average: O(n log n)
        Best: O(n log n)

    Space complexity: Due to height of recursion tree.
        Worst: O(n)
        Average: O(log n)
        Best: O(log n)

    Args:
        arr: List[int]: List of integers to be sorted

    Returns:
        None
    """

    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr: List[int], left: int, right: int) -> None:
    if left >= right:
        return

    pivot = arr[(left + right) // 2]
    i, j = left, right

    while i <= j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    _quick_sort(arr, left, i - 1)
    _quick_sort(arr, i, right)


if __name__ == "__main__":
    from test_sort import test

    test(quick_sort)
