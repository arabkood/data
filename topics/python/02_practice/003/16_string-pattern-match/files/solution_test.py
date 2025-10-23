import unittest
from solution import wordPattern


class TestWordPattern(unittest.TestCase):
    def test_valid_pattern(self):
        self.assertTrue(wordPattern("abba", "dog cat cat dog"))

    def test_invalid_pattern_different_word(self):
        self.assertFalse(wordPattern("abba", "dog cat cat fish"))

    def test_invalid_pattern_same_char_different_words(self):
        self.assertFalse(wordPattern("aaaa", "dog cat cat dog"))

    def test_invalid_pattern_same_word_different_chars(self):
        self.assertFalse(wordPattern("abba", "dog dog dog dog"))

    def test_simple_valid(self):
        self.assertTrue(wordPattern("abc", "dog cat fish"))

    def test_length_mismatch(self):
        self.assertFalse(wordPattern("abc", "dog cat"))

    def test_single_char(self):
        self.assertTrue(wordPattern("a", "dog"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
