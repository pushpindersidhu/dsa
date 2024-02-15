from typing import List


def heap_sort(arr: List[int]) -> None:
    """Heap Sort

    Heap sort uses binary heap to sort the list.

    Unstable, In-place, Comparison sort

    Args:
        arr: List[int]: List of integers to be sorted

    Returns:
        None: The list is sorted in place
    """

    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, i, len(arr))

    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


def heapify(arr: List[int], start: int, end: int) -> None:
    left = start * 2 + 1
    right = start * 2 + 2

    max_index = start
    if left < end and arr[left] > arr[max_index]:
        max_index = left
    if right < end and arr[right] > arr[max_index]:
        max_index = right

    if max_index != start:
        arr[start], arr[max_index] = arr[max_index], arr[start]
        heapify(arr, max_index, end)


if __name__ == "__main__":
    from test_sort import test

    test(heap_sort)
