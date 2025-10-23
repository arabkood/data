import unittest
from solution import charPositions


class TestCharPositions(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(charPositions("hello"), {"h": [0], "e": [1], "l": [2, 3], "o": [4]})

    def test_repeated_chars(self):
        self.assertEqual(charPositions("abba"), {"a": [0, 3], "b": [1, 2]})

    def test_single_char(self):
        self.assertEqual(charPositions("a"), {"a": [0]})

    def test_empty_string(self):
        self.assertEqual(charPositions(""), {})

    def test_all_same(self):
        self.assertEqual(charPositions("aaa"), {"a": [0, 1, 2]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
