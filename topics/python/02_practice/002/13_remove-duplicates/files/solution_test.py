import unittest
from solution import removeDuplicates


class TestRemoveDuplicates(unittest.TestCase):
    def test_with_duplicates(self):
        self.assertEqual(removeDuplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_same(self):
        self.assertEqual(removeDuplicates([1, 1, 1, 1]), [1])

    def test_no_duplicates(self):
        self.assertEqual(removeDuplicates([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])

    def test_empty_list(self):
        self.assertEqual(removeDuplicates([]), [])

    def test_multiple_duplicates(self):
        self.assertEqual(removeDuplicates([1, 2, 3, 1, 2, 3]), [1, 2, 3])

    def test_strings(self):
        self.assertEqual(removeDuplicates(["a", "b", "a", "c"]), ["a", "b", "c"])

    def test_preserve_order(self):
        self.assertEqual(removeDuplicates([3, 1, 2, 1, 3, 4]), [3, 1, 2, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
