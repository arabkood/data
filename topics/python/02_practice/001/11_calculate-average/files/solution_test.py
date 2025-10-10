import unittest
from solution import calculateAverage


class TestCalculateAverage(unittest.TestCase):
    def test_simple_average(self):
        self.assertEqual(calculateAverage([1, 2, 3, 4, 5]), 3.0)

    def test_three_numbers(self):
        self.assertEqual(calculateAverage([10, 20, 30]), 20.0)

    def test_single_number(self):
        self.assertEqual(calculateAverage([5]), 5.0)

    def test_empty_list(self):
        self.assertEqual(calculateAverage([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(calculateAverage([-5, -10, -15]), -10.0)

    def test_mixed_numbers(self):
        self.assertEqual(calculateAverage([-10, 0, 10]), 0.0)

    def test_large_list(self):
        self.assertEqual(calculateAverage([100, 200, 300, 400]), 250.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
