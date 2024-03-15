from typing import List


def max_coins(matrix: List[List[int]]) -> int:
    res = [[0] * len(matrix[i]) for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                res[i][j] = matrix[i][j]
            elif i == 0:
                res[i][j] = res[i][j - 1] + matrix[i][j]
            elif j == 0:
                res[i][j] = res[i - 1][j] + matrix[i][j]
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1]) + matrix[i][j]

    return res[-1][-1]


if __name__ == "__main__":

    import unittest

    class Test(unittest.TestCase):
        test_cases = [
            (
                [
                    [0, 0, 0, 0, 1, 0],
                    [0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 1],
                    [0, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 1, 0],
                ],
                5,
            ),
            (
                [
                    [1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1],
                ],
                5,
            ),
            (
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0],
                ],
                1,
            ),
        ]

        def test_max_coins(self):
            for matrix, expected in self.test_cases:
                with self.subTest(matrix=matrix, expected=expected):
                    self.assertEqual(max_coins(matrix), expected)

    unittest.main()
