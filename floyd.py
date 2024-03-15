from typing import List, Tuple


def floyd(n: int, edges: List[Tuple[int, int, int]]) -> List[List[float]]:
    adj = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        adj[i][i] = 0

    for u, v, w in edges:
        adj[u][v] = w

    for i in range(len(adj)):
        for j in range(len(adj)):
            for k in range(len(adj)):
                adj[j][k] = min(adj[j][k], adj[j][i] + adj[i][k])

    return adj


if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        test_cases = [
            (
                5,
                [
                    (0, 1, 4),
                    (0, 3, 5),
                    (1, 2, 1),
                    (1, 4, 6),
                    (2, 0, 2),
                    (2, 3, 3),
                    (3, 2, 1),
                    (3, 4, 2),
                    (4, 0, 1),
                    (4, 3, 4),
                ],
                [
                    [0, 4, 5, 5, 7],
                    [3, 0, 1, 4, 6],
                    [2, 6, 0, 3, 5],
                    [3, 7, 1, 0, 2],
                    [1, 5, 5, 4, 0],
                ],
            )
        ]

        def test_floyd(self):
            for n, edges, expected in self.test_cases:
                with self.subTest(n=n, edges=edges, expected=expected):
                    result = floyd(n, edges)
                    self.assertEqual(result, expected)

    unittest.main()
