import unittest
from solution import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 4, "-"), 6)

    def test_multiplication(self):
        self.assertEqual(calculate(7, 6, "*"), 42)

    def test_division(self):
        self.assertEqual(calculate(20, 5, "/"), 4.0)

    def test_division_by_zero(self):
        self.assertEqual(calculate(10, 0, "/"), "ERROR")

    def test_invalid_operation(self):
        self.assertEqual(calculate(5, 3, "%"), "ERROR")

    def test_negative_numbers(self):
        self.assertEqual(calculate(-5, 3, "+"), -2)

    def test_decimal_division(self):
        self.assertEqual(calculate(10, 3, "/"), 10 / 3)

    def test_multiplication_with_zero(self):
        self.assertEqual(calculate(5, 0, "*"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
