import unittest
from solution import coinChange


class TestCoinChange(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)

    def test_impossible_case(self):
        self.assertEqual(coinChange([2], 3), -1)

    def test_zero_amount(self):
        self.assertEqual(coinChange([1], 0), 0)

    def test_optimal_choice(self):
        self.assertEqual(coinChange([1, 3, 4], 6), 2)

    def test_single_coin(self):
        self.assertEqual(coinChange([5], 10), 2)

    def test_large_amount(self):
        self.assertEqual(coinChange([1, 2, 5], 100), 20)

    def test_multiple_solutions(self):
        self.assertEqual(coinChange([1, 5, 10, 25], 30), 2)

    def test_no_solution(self):
        self.assertEqual(coinChange([3, 7], 1), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
