import unittest
from solution import areAnagrams


class TestAreAnagrams(unittest.TestCase):
    def test_simple_anagrams(self):
        self.assertEqual(areAnagrams("listen", "silent"), True)

    def test_not_anagrams(self):
        self.assertEqual(areAnagrams("hello", "world"), False)

    def test_case_insensitive(self):
        self.assertEqual(areAnagrams("Triangle", "Integral"), True)

    def test_different_lengths(self):
        self.assertEqual(areAnagrams("apple", "pale"), False)

    def test_same_word(self):
        self.assertEqual(areAnagrams("test", "test"), True)

    def test_with_spaces(self):
        self.assertEqual(areAnagrams("a gentleman", "elegant man"), True)

    def test_empty_strings(self):
        self.assertEqual(areAnagrams("", ""), True)

    def test_one_empty(self):
        self.assertEqual(areAnagrams("hello", ""), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
