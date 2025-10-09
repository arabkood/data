import unittest
from solution import makeNegative


class TestMakeNegative(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(makeNegative(5), -5)

    def test_negative_number(self):
        self.assertEqual(makeNegative(-3), -3)

    def test_zero(self):
        self.assertEqual(makeNegative(0), 0)

    def test_large_positive(self):
        self.assertEqual(makeNegative(42), -42)

    def test_large_negative(self):
        self.assertEqual(makeNegative(-100), -100)

    def test_one(self):
        self.assertEqual(makeNegative(1), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
