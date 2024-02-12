from disjoint_set import DisjointSet


class Kruskal:
    @staticmethod
    def mst_cost(edges: list) -> int:
        size = len(set([e[0] for e in edges] + [e[1] for e in edges]))
        edges.sort(key=lambda e: e[2])

        cost = 0
        ds = DisjointSet(size)
        for u, v, w in edges:
            if ds.find(u) != ds.find(v):
                cost += w
                ds.union(u, v)

        return cost


if __name__ == "__main__":
    import unittest

    class TestKruskal(unittest.TestCase):

        def test_kruskal(self):
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
                self.assertEqual(Kruskal.mst_cost(edges), expected)

    unittest.main()
