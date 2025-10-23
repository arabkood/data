import unittest
from solution import flattenList


class TestFlattenList(unittest.TestCase):
    def test_simple_nested(self):
        self.assertEqual(flattenList([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_deep_nested(self):
        self.assertEqual(flattenList([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_very_deep_nested(self):
        self.assertEqual(flattenList([[1, 2], [3, [4, [5]]]]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(flattenList([]), [])

    def test_no_nesting(self):
        self.assertEqual(flattenList([1, 2, 3]), [1, 2, 3])

    def test_all_nested(self):
        self.assertEqual(flattenList([[[[1]]]]), [1])

    def test_mixed_types(self):
        self.assertEqual(flattenList([1, ["a", [2, "b"]], 3]), [1, "a", 2, "b", 3])

    def test_nested_empty_lists(self):
        self.assertEqual(flattenList([1, [], [2, []], 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
