import unittest
from solution import toArabicDigits


class TestToArabicDigits(unittest.TestCase):
    def test_mixed_text_with_numbers(self):
        self.assertEqual(toArabicDigits("rhc123"), "rhc١٢٣")

    def test_text_at_end(self):
        self.assertEqual(toArabicDigits("hello789"), "hello٧٨٩")

    def test_zero(self):
        self.assertEqual(toArabicDigits("test0"), "test٠")

    def test_no_numbers(self):
        self.assertEqual(toArabicDigits("no numbers"), "no numbers")

    def test_only_numbers(self):
        self.assertEqual(toArabicDigits("0123456789"), "٠١٢٣٤٥٦٧٨٩")

    def test_numbers_at_start(self):
        self.assertEqual(toArabicDigits("42test"), "٤٢test")

    def test_empty_string(self):
        self.assertEqual(toArabicDigits(""), "")

    def test_special_characters(self):
        self.assertEqual(toArabicDigits("code@123!"), "code@١٢٣!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
