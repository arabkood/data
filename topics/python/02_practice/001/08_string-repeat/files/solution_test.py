import unittest
from solution import repeatString


class TestRepeatString(unittest.TestCase):
    def test_repeat_three_times(self):
        self.assertEqual(repeatString("abc", 3), "abcabcabc")

    def test_repeat_twice(self):
        self.assertEqual(repeatString("Hello", 2), "HelloHello")

    def test_repeat_single_char(self):
        self.assertEqual(repeatString("x", 5), "xxxxx")

    def test_repeat_zero_times(self):
        self.assertEqual(repeatString("test", 0), "")

    def test_repeat_negative(self):
        self.assertEqual(repeatString("abc", -2), "")

    def test_repeat_once(self):
        self.assertEqual(repeatString("Python", 1), "Python")

    def test_empty_string(self):
        self.assertEqual(repeatString("", 5), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
