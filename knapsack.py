from typing import List


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[-1]


if __name__ == "__main__":
    import unittest

    class TestKnapsack(unittest.TestCase):
        test_cases = [
            ([1, 2, 3], [6, 10, 12], 5, 22),
            ([2, 1, 3, 2], [12, 10, 20, 15], 5, 37),
            ([2, 4, 3, 5, 6], [4, 10, 3, 7, 11], 12, 25),
            ([8, 8, 10, 4, 9], [24, 64, 70, 16, 90], 30, 224),
        ]

        def test_knapsack(self):
            for weights, values, capacity, expected in self.test_cases:
                with self.subTest(
                    weights=weights,
                    values=values,
                    capacity=capacity,
                    expected=expected,
                ):
                    self.assertEqual(knapsack(weights, values, capacity), expected)

    unittest.main()
