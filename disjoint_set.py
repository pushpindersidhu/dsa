class DisjointSet:

    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        iset = self.find(i)
        jset = self.find(j)

        if iset == jset:
            return

        irank = self.rank[iset]
        jrank = self.rank[jset]

        if irank < jrank:
            self.parent[iset] = jset
        elif jrank < irank:
            self.parent[jset] = iset
        else:
            self.parent[iset] = jset
            self.rank[jset] += 1


if __name__ == "__main__":
    import unittest

    class TestDisjointSet(unittest.TestCase):

        def test_disjoint_set(self):
            size = 5
            ds = DisjointSet(size)

            ds.union(0, 1)
            ds.union(2, 3)
            ds.union(1, 3)

            self.assertEqual(ds.find(0), 3)
            self.assertEqual(ds.find(1), 3)
            self.assertEqual(ds.find(2), 3)
            self.assertEqual(ds.find(3), 3)
            self.assertEqual(ds.find(4), 4)

    unittest.main()
