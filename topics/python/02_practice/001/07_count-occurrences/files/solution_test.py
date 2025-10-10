import unittest
from solution import countOccurrences


class TestCountOccurrences(unittest.TestCase):
    def test_multiple_occurrences(self):
        self.assertEqual(countOccurrences([1, 2, 3, 2, 4, 2], 2), 3)

    def test_all_same(self):
        self.assertEqual(countOccurrences([1, 1, 1, 1], 1), 4)

    def test_not_found(self):
        self.assertEqual(countOccurrences([1, 2, 3], 5), 0)

    def test_empty_list(self):
        self.assertEqual(countOccurrences([], 1), 0)

    def test_single_occurrence(self):
        self.assertEqual(countOccurrences([5, 10, 15, 20], 10), 1)

    def test_with_strings(self):
        self.assertEqual(countOccurrences(["a", "b", "a", "c", "a"], "a"), 3)

    def test_zero_in_list(self):
        self.assertEqual(countOccurrences([0, 1, 0, 2, 0], 0), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
