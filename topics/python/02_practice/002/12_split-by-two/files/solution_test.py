import unittest
from solution import splitByTwo


class TestSplitByTwo(unittest.TestCase):
    def test_even_length(self):
        self.assertEqual(splitByTwo("abcdef"), ["ab", "cd", "ef"])

    def test_odd_length(self):
        self.assertEqual(splitByTwo("abcde"), ["ab", "cd", "e_"])

    def test_five_chars(self):
        self.assertEqual(splitByTwo("hello"), ["he", "ll", "o_"])

    def test_empty_string(self):
        self.assertEqual(splitByTwo(""), [])

    def test_two_chars(self):
        self.assertEqual(splitByTwo("ab"), ["ab"])

    def test_one_char(self):
        self.assertEqual(splitByTwo("a"), ["a_"])

    def test_long_even(self):
        self.assertEqual(splitByTwo("abcdefgh"), ["ab", "cd", "ef", "gh"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
