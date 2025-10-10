import unittest
from solution import findLongestWord


class TestFindLongestWord(unittest.TestCase):
    def test_two_words(self):
        self.assertEqual(findLongestWord("hello world"), "hello")

    def test_multiple_words(self):
        self.assertEqual(findLongestWord("Python is amazing"), "amazing")

    def test_increasing_length(self):
        self.assertEqual(findLongestWord("a bb ccc"), "ccc")

    def test_empty_string(self):
        self.assertEqual(findLongestWord(""), "")

    def test_single_word(self):
        self.assertEqual(findLongestWord("word"), "word")

    def test_same_length_words(self):
        self.assertEqual(findLongestWord("cat dog bat"), "cat")

    def test_longest_at_end(self):
        self.assertEqual(findLongestWord("hi there beautiful"), "beautiful")

    def test_longest_in_middle(self):
        self.assertEqual(findLongestWord("a programming is fun"), "programming")


if __name__ == "__main__":
    unittest.main(verbosity=2)
