import unittest
from solution import findMax


class TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(findMax([1, 5, 3, 9, 2]), 9)

    def test_single_number(self):
        self.assertEqual(findMax([10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(findMax([-5, -2, -10, -1]), -1)

    def test_large_numbers(self):
        self.assertEqual(findMax([100, 50, 75, 200]), 200)

    def test_max_at_start(self):
        self.assertEqual(findMax([50, 10, 20, 30]), 50)

    def test_all_same(self):
        self.assertEqual(findMax([7, 7, 7, 7]), 7)

    def test_mixed_numbers(self):
        self.assertEqual(findMax([-10, 0, 15, -3, 8]), 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
