import unittest
from solution import formatPhone


class TestFormatPhone(unittest.TestCase):
    def test_simple_number(self):
        self.assertEqual(formatPhone("1234567890"), "(123) 456-7890")

    def test_another_number(self):
        self.assertEqual(formatPhone("5551234567"), "(555) 123-4567")

    def test_all_zeros(self):
        self.assertEqual(formatPhone("0000000000"), "(000) 000-0000")

    def test_all_nines(self):
        self.assertEqual(formatPhone("9999999999"), "(999) 999-9999")

    def test_mixed_digits(self):
        self.assertEqual(formatPhone("1112223333"), "(111) 222-3333")

    def test_sequential(self):
        self.assertEqual(formatPhone("0123456789"), "(012) 345-6789")


if __name__ == "__main__":
    unittest.main(verbosity=2)
