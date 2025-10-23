import unittest
from solution import findPairs


class TestFindPairs(unittest.TestCase):
    def test_simple_pairs(self):
        self.assertEqual(findPairs([1, 2, 3, 4, 5], 5), [[1, 4], [2, 3]])

    def test_with_duplicates(self):
        self.assertEqual(findPairs([1, 1, 2, 3], 4), [[1, 3]])

    def test_no_pairs(self):
        self.assertEqual(findPairs([1, 2, 3], 10), [])

    def test_single_pair(self):
        self.assertEqual(findPairs([1, 5, 3], 6), [[1, 5]])

    def test_empty_list(self):
        self.assertEqual(findPairs([], 5), [])

    def test_negative_numbers(self):
        self.assertEqual(findPairs([-1, 2, 3, 4], 3), [[-1, 4], [2]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
