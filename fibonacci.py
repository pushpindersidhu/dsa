class Fibonacci:
    cache = {}

    @classmethod
    def memoize(cls, n: int) -> int:
        if n < 2:
            return n

        if n not in cls.cache:
            cls.cache[n] = Fibonacci.memoize(n - 1) + Fibonacci.memoize(n - 2)

        return cls.cache[n]

    @classmethod
    def bottom_up(cls, n: int) -> int:
        if n < 2:
            return n

        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b

        return b


if __name__ == "__main__":
    import unittest

    class Test(unittest.TestCase):
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (5, 5),
            (8, 21),
            (13, 233),
            (14, 377),
            (40, 102334155),
            (100, 354224848179261915075),
        ]

        def test_memoize(self):
            for n, expected in self.test_cases:
                with self.subTest(n=n, expected=expected):
                    self.assertEqual(Fibonacci.memoize(n), expected)

        def test_bottom_up(self):
            for n, expected in self.test_cases:
                with self.subTest(n=n, expected=expected):
                    self.assertEqual(Fibonacci.bottom_up(n), expected)

    unittest.main()
