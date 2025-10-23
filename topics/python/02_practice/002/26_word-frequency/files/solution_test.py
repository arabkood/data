import unittest
from solution import wordFrequency


class TestWordFrequency(unittest.TestCase):
    def test_with_duplicates(self):
        self.assertEqual(wordFrequency("hello world hello"), {"hello": 2, "world": 1})

    def test_no_duplicates(self):
        self.assertEqual(wordFrequency("Python is fun"), {"python": 1, "is": 1, "fun": 1})

    def test_case_insensitive(self):
        self.assertEqual(wordFrequency("test TEST Test"), {"test": 3})

    def test_single_word(self):
        self.assertEqual(wordFrequency("hello"), {"hello": 1})

    def test_empty_string(self):
        self.assertEqual(wordFrequency(""), {})

    def test_multiple_duplicates(self):
        result = wordFrequency("the quick brown fox jumps over the lazy dog the")
        self.assertEqual(result["the"], 3)
        self.assertEqual(result["quick"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
