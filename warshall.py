from typing import List


def warshall(adj: List[List[int]]) -> List[List[int]]:
    for i in range(len(adj)):
        for j in range(len(adj)):
            for k in range(len(adj)):
                if adj[i][k] == 1 and adj[j][i] == 1:
                    adj[j][k] = 1

    return adj


if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        test_cases = [
            (
                [
                    [0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0, 1],
                    [1, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 1],
                ],
                [
                    [1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 0, 1],
                ],
            )
        ]

        def test_warshall(self):
            for edges, expected in self.test_cases:
                with self.subTest(edges=edges, expected=expected):
                    result = warshall(edges)
                    self.assertEqual(result, expected)

    unittest.main()
