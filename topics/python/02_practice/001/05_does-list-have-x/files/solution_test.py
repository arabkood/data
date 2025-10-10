import unittest
from solution import hasElement


class TestHasElement(unittest.TestCase):
    def test_element_exists(self):
        self.assertEqual(hasElement([1, 2, 3, 4, 5], 3), True)

    def test_element_not_exists(self):
        self.assertEqual(hasElement([1, 2, 3, 4, 5], 6), False)

    def test_empty_list(self):
        self.assertEqual(hasElement([], 1), False)

    def test_string_element_exists(self):
        self.assertEqual(hasElement(["a", "b", "c"], "b"), True)

    def test_first_element(self):
        self.assertEqual(hasElement([10, 20, 30], 10), True)

    def test_last_element(self):
        self.assertEqual(hasElement([10, 20, 30], 30), True)

    def test_zero_in_list(self):
        self.assertEqual(hasElement([0, 1, 2], 0), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
