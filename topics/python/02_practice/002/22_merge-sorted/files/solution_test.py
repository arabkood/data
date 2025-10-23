import unittest
from solution import mergeSorted


class TestMergeSorted(unittest.TestCase):
    def test_interleaved(self):
        self.assertEqual(mergeSorted([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_sequential(self):
        self.assertEqual(mergeSorted([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_empty_first(self):
        self.assertEqual(mergeSorted([], [1, 2]), [1, 2])

    def test_empty_second(self):
        self.assertEqual(mergeSorted([1], []), [1])

    def test_both_empty(self):
        self.assertEqual(mergeSorted([], []), [])

    def test_different_lengths(self):
        self.assertEqual(mergeSorted([1, 5], [2, 3, 4, 6]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
