import heapq
from collections import defaultdict


class Prim:
    @staticmethod
    def mst_cost(edges):
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        cost = 0
        visited = set()
        heap = [(0, 0)]
        while heap and len(visited) != len(adj):
            w, u = heapq.heappop(heap)
            if u in visited:
                continue

            cost += w
            visited.add(u)

            for v, w in adj[u]:
                if v not in visited:
                    heapq.heappush(heap, (w, v))

        return cost


if __name__ == "__main__":
    import unittest

    class TestPrim(unittest.TestCase):

        def test_prim(self):
            test_cases = [
                (
                    [
                        (0, 1, 1),
                        (0, 2, 7),
                        (1, 2, 5),
                        (1, 3, 4),
                        (2, 4, 6),
                        (3, 4, 2),
                        (1, 4, 3),
                    ],
                    11,
                ),
                (
                    [
                        (0, 1, 4),
                        (0, 2, 4),
                        (1, 2, 2),
                        (1, 0, 4),
                        (2, 0, 4),
                        (2, 1, 2),
                        (2, 3, 3),
                        (2, 5, 2),
                        (2, 4, 4),
                        (3, 2, 3),
                        (3, 4, 3),
                        (4, 2, 4),
                        (4, 3, 3),
                        (5, 2, 2),
                        (5, 4, 3),
                    ],
                    14,
                ),
            ]

            for edges, expected in test_cases:
                self.assertEqual(Prim.mst_cost(edges), expected)

    unittest.main()
