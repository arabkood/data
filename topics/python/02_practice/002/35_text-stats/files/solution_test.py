import unittest
from solution import textStats


class TestTextStats(unittest.TestCase):
    def test_simple_text(self):
        result = textStats("hello world")
        self.assertEqual(result, {"chars": 10, "words": 2, "lines": 1, "spaces": 1})

    def test_multiline(self):
        result = textStats("hello\nworld")
        self.assertEqual(result, {"chars": 10, "words": 2, "lines": 2, "spaces": 0})

    def test_empty_string(self):
        result = textStats("")
        self.assertEqual(result, {"chars": 0, "words": 0, "lines": 1, "spaces": 0})

    def test_single_word(self):
        result = textStats("hello")
        self.assertEqual(result, {"chars": 5, "words": 1, "lines": 1, "spaces": 0})

    def test_multiple_lines(self):
        result = textStats("hello\nworld\ntest")
        self.assertEqual(result, {"chars": 14, "words": 3, "lines": 3, "spaces": 0})

    def test_with_multiple_spaces(self):
        result = textStats("hello  world")
        self.assertEqual(result, {"chars": 10, "words": 2, "lines": 1, "spaces": 2})


if __name__ == "__main__":
    unittest.main(verbosity=2)
