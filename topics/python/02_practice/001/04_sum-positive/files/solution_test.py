import unittest
from solution import sumPositive


class TestSumPositive(unittest.TestCase):
    def test_all_positive(self):
        self.assertEqual(sumPositive([1, 2, 3, 4, 5]), 15)

    def test_mixed_numbers(self):
        self.assertEqual(sumPositive([1, -2, 3, -4, 5]), 9)

    def test_all_negative(self):
        self.assertEqual(sumPositive([-1, -2, -3, -4, -5]), 0)

    def test_empty_list(self):
        self.assertEqual(sumPositive([]), 0)

    def test_with_zeros(self):
        self.assertEqual(sumPositive([0, 2, 0, 5, 0]), 7)

    def test_single_positive(self):
        self.assertEqual(sumPositive([10]), 10)

    def test_single_negative(self):
        self.assertEqual(sumPositive([-10]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
