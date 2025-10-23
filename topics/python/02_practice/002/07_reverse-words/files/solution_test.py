import unittest
from solution import reverseWords


class TestReverseWords(unittest.TestCase):
    def test_two_words(self):
        self.assertEqual(reverseWords("hello world"), "world hello")

    def test_three_words(self):
        self.assertEqual(reverseWords("Python is fun"), "fun is Python")

    def test_four_words(self):
        self.assertEqual(reverseWords("a b c d"), "d c b a")

    def test_single_word(self):
        self.assertEqual(reverseWords("one"), "one")

    def test_many_words(self):
        self.assertEqual(reverseWords("the quick brown fox"), "fox brown quick the")

    def test_empty_string(self):
        self.assertEqual(reverseWords(""), "")

    def test_two_long_words(self):
        self.assertEqual(reverseWords("programming language"), "language programming")


if __name__ == "__main__":
    unittest.main(verbosity=2)
