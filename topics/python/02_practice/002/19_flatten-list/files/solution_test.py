import unittest
from solution import flattenList


class TestFlattenList(unittest.TestCase):
    def test_two_sublists(self):
        self.assertEqual(flattenList([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_multiple_sublists(self):
        self.assertEqual(flattenList([[1], [2], [3]]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(flattenList([]), [])

    def test_single_sublist(self):
        self.assertEqual(flattenList([[1, 2, 3]]), [1, 2, 3])

    def test_different_sizes(self):
        self.assertEqual(flattenList([[1], [2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_with_empty_sublists(self):
        self.assertEqual(flattenList([[1, 2], [], [3, 4]]), [1, 2, 3, 4])

    def test_strings(self):
        self.assertEqual(flattenList([["a", "b"], ["c"]]), ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
