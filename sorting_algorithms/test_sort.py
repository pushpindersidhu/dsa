import unittest
from typing import List, Callable


def test(sort: Callable[[List[int]], List[int] | None]) -> None:
    class TestSort(unittest.TestCase):
        def test_sort(self):
            test_cases = [
                ([], []),
                ([1], [1]),
                ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
                ([2, -4, -2, 4, 0], [-4, -2, 0, 2, 4]),
                (
                    [30, 24, -45, 32, 113, -24, 43, 23, 12, 0],
                    [-45, -24, 0, 12, 23, 24, 30, 32, 43, 113],
                ),
            ]

            for input, expected in test_cases:
                with self.subTest(input=input, expected=expected):
                    output = sort(input)
                    if output is not None:
                        self.assertEqual(output, expected)
                    else:
                        self.assertEqual(input, expected)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSort)
    unittest.TextTestRunner().run(suite)
