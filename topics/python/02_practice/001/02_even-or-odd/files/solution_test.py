import unittest
from solution import evenOrOdd


class TestEvenOrOdd(unittest.TestCase):
    def test_positive_even(self):
        self.assertEqual(evenOrOdd(4), "Even")

    def test_positive_odd(self):
        self.assertEqual(evenOrOdd(7), "Odd")

    def test_zero(self):
        self.assertEqual(evenOrOdd(0), "Even")

    def test_negative_odd(self):
        self.assertEqual(evenOrOdd(-3), "Odd")

    def test_negative_even(self):
        self.assertEqual(evenOrOdd(-8), "Even")

    def test_large_number(self):
        self.assertEqual(evenOrOdd(1000), "Even")


if __name__ == "__main__":
    unittest.main(verbosity=2)
