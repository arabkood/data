import unittest
from solution import textSimilarity


class TestTextSimilarity(unittest.TestCase):
    def test_partial_match(self):
        self.assertAlmostEqual(textSimilarity("hello world", "hello there"), 50.0, places=1)

    def test_exact_match(self):
        self.assertAlmostEqual(textSimilarity("hello world", "hello world"), 100.0, places=1)

    def test_no_match(self):
        self.assertAlmostEqual(textSimilarity("abc def", "xyz"), 0.0, places=1)

    def test_case_insensitive(self):
        self.assertAlmostEqual(textSimilarity("Hello World", "hello world"), 100.0, places=1)

    def test_single_word_match(self):
        self.assertAlmostEqual(textSimilarity("hello", "hello"), 100.0, places=1)

    def test_one_common_word(self):
        self.assertAlmostEqual(textSimilarity("a b c", "c d e"), 33.33, places=1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
