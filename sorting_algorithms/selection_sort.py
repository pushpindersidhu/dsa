from typing import List


def selection_sort(arr: List[int]) -> None:
    """Selection Sort

    Find the minimum element in unsorted part of array and swap it with
    the first element of unsorted part of array.

    Unstable, In-Place, Comparison sorting algorithm

    Time Complexity:
        Worst Case: O(n^2)
        Average Case: O(n^2)
        Best Case: O(n^2)

    Space Complexity: O(1)

    Args:
        arr: List[int]: list of integers to be sorted

    Returns:
        None
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    from test_sort import test

    test(selection_sort)
