import unittest
from solution import sum_numbers


class TestSumNumbers(unittest.TestCase):
    """Test suite for Sum of Numbers challenge."""

    def test_simple_list(self):
        """Test: [1, 2, 3] → 6"""
        result = sum_numbers([1, 2, 3])
        self.assertEqual(result, 6, "Failed on simple list [1, 2, 3]")

    def test_single_number(self):
        """Test: [42] → 42"""
        result = sum_numbers([42])
        self.assertEqual(result, 42, "Failed on single number [42]")

    def test_larger_numbers(self):
        """Test: [10, 20, 30, 40] → 100"""
        result = sum_numbers([10, 20, 30, 40])
        self.assertEqual(result, 100, "Failed on [10, 20, 30, 40]")

    def test_with_zero(self):
        """Test: [5, 0, 10] → 15"""
        result = sum_numbers([5, 0, 10])
        self.assertEqual(result, 15, "Failed when list contains zero")

    def test_negative_numbers(self):
        """Test: [1, -2, 3, -4] → -2"""
        result = sum_numbers([1, -2, 3, -4])
        self.assertEqual(result, -2, "Failed with negative numbers")

    def test_all_negatives(self):
        """Test: [-5, -10, -15] → -30"""
        result = sum_numbers([-5, -10, -15])
        self.assertEqual(result, -30, "Failed with all negative numbers")

    def test_floats(self):
        """Test: [1.5, 2.5, 3.0] → 7.0"""
        result = sum_numbers([1.5, 2.5, 3.0])
        self.assertAlmostEqual(
            result, 7.0, places=2, msg="Failed with floating point numbers"
        )

    def test_longer_list(self):
        """Test: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → 55"""
        result = sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, 55, "Failed on longer list")


if __name__ == "__main__":
    unittest.main(verbosity=2)
