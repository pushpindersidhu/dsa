import heapq
from collections import defaultdict
from typing import Dict, List

# Problem: Dijkstra's Shortest Path Algorithm
# https://neetcode.io/problems/dijkstra

# Implement Dijkstra's shortest path algorithm.

# Given a weighted, directed graph, and a starting vertex, return the
# shortest distance from the starting vertex to every vertex in the graph.

# Input:

# number_of_vertices - the number of vertices in the graph.
# Each vertex is labeled from 0 to n - 1.

# edges - a list of tuples, each representing a directed edge in the form (u, v, w),
# where u is the source vertex, v is the destination vertex,
# and w is the weight of the edge, where (1 <= w <= 10).

# start - starting vertex from which to start the algorithm, where (0 <= src < n).

# Note: If a vertex is unreachable from the source vertex,
# the shortest path distance for the unreachable vertex should be -1.


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
            w1, v1 = heapq.heappop(heap)
            if v1 in shortest:
                continue

            shortest[v1] = w1
            for v2, w2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(heap, (w1 + w2, v2))

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
