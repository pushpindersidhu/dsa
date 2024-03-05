def coin_row(row):
    a = b = 0
    max_amount = 0
    for coin in row:
        max_amount = max(b, a + coin)
        a, b = b, max_amount

    return max_amount


if __name__ == "__main__":
    import unittest

    class TestCoinRow(unittest.TestCase):
        test_cases = [
            ([5, 1, 2, 10, 6, 2], 17),
            (
                [
                    42,
                    90,
                    48,
                    96,
                    81,
                    18,
                    77,
                    64,
                    54,
                    48,
                    43,
                    92,
                    61,
                    65,
                    9,
                    36,
                    95,
                    69,
                    62,
                ],
                631,
            ),
        ]

        def test_coin_row(self):
            for row, expected in self.test_cases:
                with self.subTest(row=row, expected=expected):
                    self.assertEqual(coin_row(row), expected)

    unittest.main()
