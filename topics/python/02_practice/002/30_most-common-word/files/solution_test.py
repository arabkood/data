import unittest
from solution import mostCommonWord


class TestMostCommonWord(unittest.TestCase):
    def test_simple_text(self):
        self.assertEqual(mostCommonWord("hello world hello"), "hello")

    def test_with_article(self):
        self.assertEqual(mostCommonWord("the cat and the dog"), "the")

    def test_all_unique(self):
        self.assertEqual(mostCommonWord("one two three"), "one")

    def test_case_insensitive(self):
        self.assertEqual(mostCommonWord("Hello HELLO hello"), "hello")

    def test_single_word(self):
        self.assertEqual(mostCommonWord("test"), "test")


if __name__ == "__main__":
    unittest.main(verbosity=2)
