import unittest
from solution import findInNested


class TestFindInNested(unittest.TestCase):
    def test_simple_list_found(self):
        self.assertTrue(findInNested([1, 2, 3], 2))

    def test_one_level_nested_found(self):
        self.assertTrue(findInNested([1, [2, 3], 4], 3))

    def test_deep_nested_found(self):
        self.assertTrue(findInNested([[1, 2], [3, [4, 5]]], 5))

    def test_not_found(self):
        self.assertFalse(findInNested([1, 2, 3], 5))

    def test_deep_not_found(self):
        self.assertFalse(findInNested([1, [2, [3]]], 4))

    def test_empty_list(self):
        self.assertFalse(findInNested([], 1))

    def test_string_value(self):
        self.assertTrue(findInNested(["a", ["b", "c"]], "c"))

    def test_first_element(self):
        self.assertTrue(findInNested([5, [2, 3]], 5))


if __name__ == "__main__":
    unittest.main(verbosity=2)
