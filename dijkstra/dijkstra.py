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
