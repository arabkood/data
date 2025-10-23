import unittest
from solution import isValid


class TestIsValid(unittest.TestCase):
    def test_simple_parentheses(self):
        self.assertTrue(isValid("()"))

    def test_multiple_types(self):
        self.assertTrue(isValid("()[]{}"))

    def test_mismatch(self):
        self.assertFalse(isValid("(]"))

    def test_wrong_order(self):
        self.assertFalse(isValid("([)]"))

    def test_nested_valid(self):
        self.assertTrue(isValid("{[]}"))

    def test_empty_string(self):
        self.assertTrue(isValid(""))

    def test_only_opening(self):
        self.assertFalse(isValid("((("))

    def test_only_closing(self):
        self.assertFalse(isValid(")))"))

    def test_complex_valid(self):
        self.assertTrue(isValid("([{}])"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
