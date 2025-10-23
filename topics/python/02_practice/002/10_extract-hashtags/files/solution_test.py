import unittest
from solution import extractHashtags


class TestExtractHashtags(unittest.TestCase):
    def test_single_hashtag(self):
        self.assertEqual(extractHashtags("I love #python programming"), ["python"])

    def test_multiple_hashtags(self):
        self.assertEqual(extractHashtags("#hello #world"), ["hello", "world"])

    def test_no_hashtags(self):
        self.assertEqual(extractHashtags("No hashtags here"), [])

    def test_with_numbers(self):
        self.assertEqual(extractHashtags("#code #test123 #python3"), ["code", "test123", "python3"])

    def test_hashtag_at_end(self):
        self.assertEqual(extractHashtags("Learn to code #python"), ["python"])

    def test_multiple_in_sentence(self):
        self.assertEqual(extractHashtags("I #love #coding in #python"), ["love", "coding", "python"])

    def test_empty_string(self):
        self.assertEqual(extractHashtags(""), [])

    def test_only_hash_symbol(self):
        self.assertEqual(extractHashtags("#"), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
