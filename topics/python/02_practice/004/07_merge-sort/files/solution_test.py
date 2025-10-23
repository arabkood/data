import unittest
from solution import mergeSort


class TestMergeSort(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(mergeSort([38, 27, 43, 3, 9, 82, 10]), [3, 9, 10, 27, 38, 43, 82])

    def test_simple_case(self):
        self.assertEqual(mergeSort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])

    def test_already_sorted(self):
        self.assertEqual(mergeSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(mergeSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_single_element(self):
        self.assertEqual(mergeSort([42]), [42])

    def test_empty_list(self):
        self.assertEqual(mergeSort([]), [])

    def test_duplicates(self):
        self.assertEqual(mergeSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(mergeSort([-5, 3, -1, 7, -10]), [-10, -5, -1, 3, 7])


if __name__ == "__main__":
    unittest.main(verbosity=2)
