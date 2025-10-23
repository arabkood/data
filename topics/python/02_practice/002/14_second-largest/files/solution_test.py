import unittest
from solution import secondLargest


class TestSecondLargest(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(secondLargest([1, 2, 3, 4, 5]), 4)

    def test_unordered_list(self):
        self.assertEqual(secondLargest([10, 5, 8, 12, 3]), 10)

    def test_all_same(self):
        self.assertEqual(secondLargest([7, 7, 7]), None)

    def test_two_elements(self):
        self.assertEqual(secondLargest([5, 1]), 1)

    def test_with_duplicates(self):
        self.assertEqual(secondLargest([5, 5, 3, 3, 1]), 3)

    def test_negative_numbers(self):
        self.assertEqual(secondLargest([-1, -5, -3, -10]), -3)

    def test_single_element(self):
        self.assertEqual(secondLargest([5]), None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
