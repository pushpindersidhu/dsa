from typing import List


def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    items = sorted(
        [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))],
        reverse=True,
    )

    max_val = 0
    for item in items:
        if capacity >= item[1]:
            capacity -= item[1]
            max_val += item[2]
        else:
            max_val += item[0] * capacity
            break

    return max_val


if __name__ == "__main__":
    import unittest

    class TestFractionalKnapsack(unittest.TestCase):
        test_cases = [
                ([10, 20, 30], [60, 100, 120], 50, 240.0),
        ]

        def test_fractional_knapsack(self):
            for weights, values, capacity, expected in self.test_cases:
                with self.subTest(
                    weights=weights,
                    values=values,
                    capacity=capacity,
                    expected=expected,
                ):
                    self.assertEqual(fractional_knapsack(weights, values, capacity), expected)

    unittest.main()
