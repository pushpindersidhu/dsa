from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Merge Sort

    Split array in half until each subarray has only one element.
    Merge subarrays to a single sorted array.

    Stable, Not in-place, Comparison sort

    Time complexity:
        Worst: O(n log n)
        Average: O(n log n)
        Best: O(n log n)

    Space complexity: O(n)

    Args:
        arr: List[int]: List of integers to be sorted

    Returns:
        List[int]: Sorted list of integers
    """

    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


if __name__ == "__main__":
    from test_sort import test

    test(merge_sort)
