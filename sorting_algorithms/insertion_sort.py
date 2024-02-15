from typing import List


def insertion_sort(arr: List[int]) -> None:
    """Insertion sort

    Stable, In-Place, Comparison sorting algorithm
    Builds the final sorted array one item at a time.

    Time Complexity:
        Worst Case: O(n^2)
        Average Case: O(n^2)
        Best Case: O(n)

    Space Complexity: O(1)

    Args:
        arr: List[int]: list of integers to be sorted

    Returns:
        None
    """

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


if __name__ == "__main__":
    from test_sort import test

    test(insertion_sort)
