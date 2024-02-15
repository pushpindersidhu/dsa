from typing import List


def bubble_sort(arr: List[int]) -> None:
    """Bubble sort algorithm

    Stable, In-Place, Comparison sorting algorithm
    Compare each pair of adjacent items and swap them if they are in the wrong order.

    Time complexity:
        Worst Case: O(n^2)
        Average Case: O(n^2)
        Best Case: O(n)

    Args:
        arr: List[int]: list of integers to be sorted

    Returns:
        None
    """

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    from test_sort import test

    test(bubble_sort)
