import heapq
from typing import List, Tuple


def interval_partitioning(intervals: List[Tuple[int, int]]) -> int:
    """Interval Partitioning: Minimum number of rooms required to hold all classes

    Find minimum number of rooms required to schedule all the classes such that
    no two classes are held at the same time. Each class is represented by
    an interval (start, end) where start is the start time of the class and
    end is the end time of the class.

    Args:
        intervals:
            List of intervals where each interval is represented
            by a tuple (start, end)

    Returns:
        Minimum number of rooms required to hold all the classes
    """

    intervals.sort(key=lambda x: x[0])

    end_times = []
    for start, end in intervals:
        if end_times and start >= end_times[0]:
            heapq.heappop(end_times)

        heapq.heappush(end_times, end)

    return len(end_times)


if __name__ == "__main__":
    import unittest

    class TestIntervalPartitioning(unittest.TestCase):

        def test_interval_partitioning(self):
            test_cases = [
                (
                    [
                        (0, 3),
                        (0, 7),
                        (12, 15),
                        (4, 10),
                        (8, 11),
                        (8, 11),
                        (4, 7),
                        (0, 3),
                        (10, 15),
                        (12, 15),
                    ],
                    3,
                ),
            ]

            for intervals, expected in test_cases:
                self.assertEqual(interval_partitioning(intervals), expected)

    unittest.main()
