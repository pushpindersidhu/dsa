from typing import List, Tuple


def minimizing_lateness(jobs: List[Tuple[int, int]]) -> int:
    """Minimizing Lateness: Minimize the total lateness of jobs

    Minimize the total lateness of jobs. Each job has a deadline and a duration.
    The lateness of a job is the difference between the completion time of the
    job and the deadline. The total lateness is the sum of the lateness of all
    the jobs.

    Args:
        jobs:
            List of jobs where each job is represented by a
            tuple (duration, deadline)

    Returns:
        Minimum total lateness of all the jobs
    """

    jobs.sort(key=lambda x: x[1])

    time = 0
    lateness = 0
    for job in jobs:
        time += job[0]
        lateness += max(time - job[1], 0)

    return lateness


if __name__ == "__main__":
    import unittest

    class TestMinimizingLateness(unittest.TestCase):

        def test_minimizing_lateness(self):
            test_cases = [
                (
                    [
                        (3, 6),
                        (2, 8),
                        (1, 9),
                        (4, 9),
                        (3, 14),
                        (2, 15),
                    ],
                    1,
                ),
            ]

            for jobs, expected in test_cases:
                self.assertEqual(minimizing_lateness(jobs), expected)

    unittest.main()
