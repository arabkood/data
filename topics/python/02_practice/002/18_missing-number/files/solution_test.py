import unittest
from solution import findMissing


class TestFindMissing(unittest.TestCase):
    def test_missing_middle(self):
        self.assertEqual(findMissing([1, 2, 4, 5]), 3)

    def test_unordered_list(self):
        self.assertEqual(findMissing([3, 1, 2, 5, 6]), 4)

    def test_missing_first(self):
        self.assertEqual(findMissing([2, 3, 4, 5]), 1)

    def test_missing_near_end(self):
        self.assertEqual(findMissing([1, 2, 3, 4, 5, 7]), 6)

    def test_small_list(self):
        self.assertEqual(findMissing([1, 3]), 2)

    def test_larger_sequence(self):
        self.assertEqual(findMissing([1, 2, 3, 4, 5, 6, 8, 9, 10]), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
