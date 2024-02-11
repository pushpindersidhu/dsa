import heapq
from collections import defaultdict
from typing import Dict, List


class Dijkstra:
    @staticmethod
    def shortest_path(
        edges: List[List[int]], number_of_vertices: int, start: int
    ) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        shortest = {}
        heap = [(0, start)]
        while heap:
            w1, u1 = heapq.heappop(heap)
            if u1 in shortest:
                continue

            shortest[u1] = w1
            for u2, w2 in adj[u1]:
                if u2 not in shortest:
                    heapq.heappush(heap, (w1 + w2, u2))

        for i in range(number_of_vertices):
            if i not in shortest:
                shortest[i] = -1

        return shortest


if __name__ == "__main__":
    import unittest

    class TestDijkstra(unittest.TestCase):
        def test_shortest_path(self):
            self.assertEqual(
                Dijkstra.shortest_path(
                    [
                        [0, 1, 10],
                        [0, 2, 3],
                        [1, 3, 2],
                        [2, 1, 4],
                        [2, 3, 8],
                        [2, 4, 2],
                        [3, 4, 5],
                    ],
                    5,
                    0,
                ),
                {0: 0, 1: 7, 2: 3, 3: 9, 4: 5},
            )
            self.assertEqual(Dijkstra.shortest_path([[0, 1, 5]], 2, 0), {0: 0, 1: 5})
            self.assertEqual(
                Dijkstra.shortest_path([[0, 1, 3], [1, 2, 1], [2, 0, 4]], 3, 0),
                {0: 0, 1: 3, 2: 4},
            )
            self.assertEqual(
                Dijkstra.shortest_path(
                    [[0, 1, 5], [0, 2, 7], [1, 2, 2], [1, 3, 6], [2, 3, 4]],
                    4,
                    1,
                ),
                {0: -1, 1: 0, 2: 2, 3: 6},
            )

    unittest.main()
