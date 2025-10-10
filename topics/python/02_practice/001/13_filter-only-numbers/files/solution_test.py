import unittest
from solution import filterNumbers


class TestFilterNumbers(unittest.TestCase):
    def test_mixed_types(self):
        self.assertEqual(filterNumbers([1, "hello", 3.5, True, 7]), [1, 3.5, 7])

    def test_only_strings(self):
        self.assertEqual(filterNumbers(["a", "b", "c"]), [])

    def test_only_numbers(self):
        self.assertEqual(filterNumbers([10, 20, 30]), [10, 20, 30])

    def test_empty_list(self):
        self.assertEqual(filterNumbers([]), [])

    def test_with_floats(self):
        self.assertEqual(filterNumbers([1.1, 2.2, "test", 3.3]), [1.1, 2.2, 3.3])

    def test_with_booleans(self):
        self.assertEqual(filterNumbers([True, False, 5, 10]), [5, 10])

    def test_with_lists_and_dicts(self):
        self.assertEqual(filterNumbers([1, [2, 3], {"key": 4}, 5]), [1, 5])

    def test_negative_numbers(self):
        self.assertEqual(filterNumbers([-5, "text", -10.5, None, 0]), [-5, -10.5, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
