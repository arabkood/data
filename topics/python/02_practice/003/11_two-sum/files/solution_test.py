import unittest
from solution import twoSum


class TestTwoSum(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_middle_indices(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_same_numbers(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def test_no_solution(self):
        self.assertIsNone(twoSum([1, 2, 3], 10))

    def test_multiple_same_value(self):
        self.assertEqual(twoSum([5, 5, 5], 10), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_large_numbers(self):
        self.assertEqual(twoSum([1, 2, 3, 4, 5], 9), [3, 4])

    def test_zero_target(self):
        self.assertEqual(twoSum([-1, 0, 1], 0), [0, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
