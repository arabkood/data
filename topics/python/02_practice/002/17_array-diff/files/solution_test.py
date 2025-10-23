import unittest
from solution import arrayDiff


class TestArrayDiff(unittest.TestCase):
    def test_simple_diff(self):
        self.assertEqual(arrayDiff([1, 2, 3], [2]), [1, 3])

    def test_with_duplicates(self):
        self.assertEqual(arrayDiff([1, 2, 2, 3], [2]), [1, 3])

    def test_remove_all(self):
        self.assertEqual(arrayDiff([1, 2, 3], [1, 2, 3]), [])

    def test_empty_second_list(self):
        self.assertEqual(arrayDiff([1, 2, 3], []), [1, 2, 3])

    def test_empty_first_list(self):
        self.assertEqual(arrayDiff([], [1, 2]), [])

    def test_no_common_elements(self):
        self.assertEqual(arrayDiff([1, 2, 3], [4, 5, 6]), [1, 2, 3])

    def test_multiple_removals(self):
        self.assertEqual(arrayDiff([1, 2, 3, 4, 5], [2, 4]), [1, 3, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
