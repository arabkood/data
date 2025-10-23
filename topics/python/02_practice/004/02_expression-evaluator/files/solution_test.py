import unittest
from solution import evaluate


class TestEvaluate(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(evaluate("3 + 5"), 8)

    def test_simple_subtraction(self):
        self.assertEqual(evaluate("10 - 3"), 7)

    def test_simple_multiplication(self):
        self.assertEqual(evaluate("4 * 5"), 20)

    def test_simple_division(self):
        self.assertEqual(evaluate("20 / 4"), 5)

    def test_operator_precedence_1(self):
        self.assertEqual(evaluate("2 * 3 + 4"), 10)

    def test_operator_precedence_2(self):
        self.assertEqual(evaluate("2 + 3 * 4"), 14)

    def test_parentheses_1(self):
        self.assertEqual(evaluate("(2 + 3) * 4"), 20)

    def test_parentheses_2(self):
        self.assertEqual(evaluate("(5 + 3) * (2 - 1)"), 8)

    def test_complex_expression(self):
        self.assertEqual(evaluate("10 / 2 - 3"), 2)

    def test_nested_parentheses(self):
        self.assertEqual(evaluate("((2 + 3) * 4) - 5"), 15)

    def test_no_spaces(self):
        self.assertEqual(evaluate("2+3*4"), 14)


if __name__ == "__main__":
    unittest.main(verbosity=2)
