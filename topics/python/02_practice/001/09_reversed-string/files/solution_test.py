import unittest
from solution import reverseString


class TestReverseString(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(reverseString("hello"), "olleh")

    def test_capitalized_word(self):
        self.assertEqual(reverseString("Python"), "nohtyP")

    def test_single_character(self):
        self.assertEqual(reverseString("a"), "a")

    def test_empty_string(self):
        self.assertEqual(reverseString(""), "")

    def test_with_spaces(self):
        self.assertEqual(reverseString("hello world"), "dlrow olleh")

    def test_numbers_as_string(self):
        self.assertEqual(reverseString("12345"), "54321")

    def test_palindrome(self):
        self.assertEqual(reverseString("madam"), "madam")


if __name__ == "__main__":
    unittest.main(verbosity=2)
