import unittest
from solution import removeVowels


class TestRemoveVowels(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(removeVowels("hello"), "hll")

    def test_another_word(self):
        self.assertEqual(removeVowels("world"), "wrld")

    def test_capital_vowel(self):
        self.assertEqual(removeVowels("Python"), "Pythn")

    def test_all_vowels(self):
        self.assertEqual(removeVowels("AEIOU"), "")

    def test_no_vowels(self):
        self.assertEqual(removeVowels("xyz123"), "xyz123")

    def test_mixed_case(self):
        self.assertEqual(removeVowels("Programming"), "Prgrmmng")

    def test_empty_string(self):
        self.assertEqual(removeVowels(""), "")

    def test_with_spaces(self):
        self.assertEqual(removeVowels("hello world"), "hll wrld")

    def test_only_lowercase_vowels(self):
        self.assertEqual(removeVowels("aeiou"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
