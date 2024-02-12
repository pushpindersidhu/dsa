from typing import List, Tuple


def interval_scheduling(jobs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    jobs.sort(key=lambda job: job[1])

    selected_jobs = []
    last_job_finish_time = 0
    for job in jobs:
        if last_job_finish_time <= job[0]:
            selected_jobs.append(job)
            last_job_finish_time = job[1]

    return selected_jobs


if __name__ == "__main__":
    import unittest

    class TestIntervalScheduling(unittest.TestCase):

        def test_interval_scheduling(self):
            test_cases = [
                ([(1, 3), (2, 5), (3, 9), (6, 8)], [(1, 3), (6, 8)]),
                (
                    [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)],
                    [(1, 4), (4, 7), (8, 11)],
                ),
            ]

            for jobs, expected in test_cases:
                self.assertEqual(interval_scheduling(jobs), expected)

    unittest.main()
