import unittest
from solution import toHackerSpeak


class TestToHackerSpeak(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(toHackerSpeak("hello"), "h3ll0")

    def test_multiple_replacements(self):
        self.assertEqual(toHackerSpeak("awesome"), "4w350m3")

    def test_uppercase(self):
        self.assertEqual(toHackerSpeak("HACKER"), "H4CK3R")

    def test_with_spaces(self):
        self.assertEqual(toHackerSpeak("Python is fun"), "Pyth0n 15 fun")

    def test_no_replacements(self):
        self.assertEqual(toHackerSpeak("xyz"), "xyz")

    def test_mixed_case(self):
        self.assertEqual(toHackerSpeak("EaSy"), "34Sy")

    def test_all_replaceable(self):
        self.assertEqual(toHackerSpeak("aeiou"), "431 0u")

    def test_with_numbers(self):
        self.assertEqual(toHackerSpeak("test123"), "t35t123")


if __name__ == "__main__":
    unittest.main(verbosity=2)
