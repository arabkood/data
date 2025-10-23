import unittest
from solution import countVowels


class TestCountVowels(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(countVowels("hello"), 2)

    def test_one_vowel(self):
        self.assertEqual(countVowels("world"), 1)

    def test_capital_vowel(self):
        self.assertEqual(countVowels("Python"), 1)

    def test_all_vowels(self):
        self.assertEqual(countVowels("aeiou"), 5)

    def test_no_vowels(self):
        self.assertEqual(countVowels("xyz"), 0)

    def test_mixed_case(self):
        self.assertEqual(countVowels("Programming"), 3)

    def test_empty_string(self):
        self.assertEqual(countVowels(""), 0)

    def test_uppercase_vowels(self):
        self.assertEqual(countVowels("AEIOU"), 5)

    def test_with_spaces(self):
        self.assertEqual(countVowels("hello world"), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
