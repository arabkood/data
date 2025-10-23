import unittest
from solution import mostCommonChar


class TestMostCommonChar(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(mostCommonChar("hello"), "l")

    def test_equal_frequency(self):
        self.assertEqual(mostCommonChar("aabbcc"), "a")

    def test_multiple_same(self):
        self.assertEqual(mostCommonChar("programming"), "g")

    def test_with_spaces(self):
        self.assertEqual(mostCommonChar("hello world"), "l")

    def test_single_char(self):
        self.assertEqual(mostCommonChar("aaaa"), "a")

    def test_long_text(self):
        self.assertEqual(mostCommonChar("mississippi"), "i")

    def test_mixed_case(self):
        self.assertEqual(mostCommonChar("AaBbCc"), "A")


if __name__ == "__main__":
    unittest.main(verbosity=2)
