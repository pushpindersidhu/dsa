from typing import List, Dict

def min_coins(amount: int, coins: List[int]) -> Dict[int, int]:
    coins.sort(reverse=True)

    coins_paid = {}
    for coin in coins:
        coins_paid[coin] = amount // coin
        amount %= coin

    return coins_paid


if __name__ == "__main__":
    import unittest

    class TestMinCoins(unittest.TestCase):
        test_cases = [
            (11, [1, 2, 5], {5: 2, 2: 0, 1: 1}),
            (15, [1, 2, 5], {5: 3, 2: 0, 1: 0}),
            (15, [1, 2, 5, 10], {10: 1, 5: 1, 2: 0, 1: 0}),
            (153, [1, 2, 5, 25, 100], {100: 1, 25: 2, 5: 0, 2: 1, 1: 1}),
        ]

        def test_min_coins(self):
            for amount, coins, expected in self.test_cases:
                self.assertEqual(min_coins(amount, coins), expected)

    unittest.main()
