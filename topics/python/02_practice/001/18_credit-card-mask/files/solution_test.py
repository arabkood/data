import unittest
from solution import maskCard


class TestMaskCard(unittest.TestCase):
    def test_standard_card(self):
        self.assertEqual(maskCard("1234567812345678"), "############5678")

    def test_another_card(self):
        self.assertEqual(maskCard("4123456789012345"), "############2345")

    def test_short_number(self):
        self.assertEqual(maskCard("12"), "12")

    def test_exactly_four(self):
        self.assertEqual(maskCard("1234"), "1234")

    def test_five_digits(self):
        self.assertEqual(maskCard("12345"), "#2345")

    def test_eight_digits(self):
        self.assertEqual(maskCard("12345678"), "####5678")

    def test_long_card(self):
        self.assertEqual(maskCard("12345678901234567890"), "################7890")

    def test_single_digit(self):
        self.assertEqual(maskCard("5"), "5")

    def test_three_digits(self):
        self.assertEqual(maskCard("123"), "123")


if __name__ == "__main__":
    unittest.main(verbosity=2)
