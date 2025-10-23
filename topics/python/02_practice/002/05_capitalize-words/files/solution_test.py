import unittest
from solution import capitalizeWords


class TestCapitalizeWords(unittest.TestCase):
    def test_two_words(self):
        self.assertEqual(capitalizeWords("hello world"), "Hello World")

    def test_multiple_words(self):
        self.assertEqual(capitalizeWords("python programming"), "Python Programming")

    def test_uppercase_word(self):
        self.assertEqual(capitalizeWords("HELLO"), "Hello")

    def test_single_letters(self):
        self.assertEqual(capitalizeWords("a b c"), "A B C")

    def test_single_word(self):
        self.assertEqual(capitalizeWords("hello"), "Hello")

    def test_mixed_case(self):
        self.assertEqual(capitalizeWords("hELLo WOrLD"), "Hello World")

    def test_empty_string(self):
        self.assertEqual(capitalizeWords(""), "")

    def test_many_words(self):
        self.assertEqual(capitalizeWords("the quick brown fox"), "The Quick Brown Fox")


if __name__ == "__main__":
    unittest.main(verbosity=2)
