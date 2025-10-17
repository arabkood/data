import unittest
import sys
import os


class TestCalculatorFunctions(unittest.TestCase):
    """Test suite for Calculator Functions Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists and import it."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

        # Import the solution module
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        try:
            import solution

            cls.solution = solution
        except Exception as e:
            raise ImportError(f"Could not import solution.py: {e}")

    def test_add_function_exists(self):
        """Test: add function exists"""
        self.assertTrue(
            hasattr(self.solution, "add"),
            "Function 'add' not found. Please define the add function.",
        )

    def test_add_basic(self):
        """Test: add(10, 5) returns 15"""
        result = self.solution.add(10, 5)
        self.assertEqual(result, 15, "add(10, 5) should return 15")

    def test_add_negative(self):
        """Test: add with negative numbers"""
        result = self.solution.add(-5, 3)
        self.assertEqual(result, -2, "add(-5, 3) should return -2")

    def test_subtract_function_exists(self):
        """Test: subtract function exists"""
        self.assertTrue(
            hasattr(self.solution, "subtract"),
            "Function 'subtract' not found. Please define the subtract function.",
        )

    def test_subtract_basic(self):
        """Test: subtract(10, 5) returns 5"""
        result = self.solution.subtract(10, 5)
        self.assertEqual(result, 5, "subtract(10, 5) should return 5")

    def test_subtract_negative_result(self):
        """Test: subtract resulting in negative"""
        result = self.solution.subtract(3, 8)
        self.assertEqual(result, -5, "subtract(3, 8) should return -5")

    def test_multiply_function_exists(self):
        """Test: multiply function exists"""
        self.assertTrue(
            hasattr(self.solution, "multiply"),
            "Function 'multiply' not found. Please define the multiply function.",
        )

    def test_multiply_basic(self):
        """Test: multiply(10, 5) returns 50"""
        result = self.solution.multiply(10, 5)
        self.assertEqual(result, 50, "multiply(10, 5) should return 50")

    def test_multiply_by_zero(self):
        """Test: multiply by zero"""
        result = self.solution.multiply(10, 0)
        self.assertEqual(result, 0, "multiply(10, 0) should return 0")

    def test_divide_function_exists(self):
        """Test: divide function exists"""
        self.assertTrue(
            hasattr(self.solution, "divide"),
            "Function 'divide' not found. Please define the divide function.",
        )

    def test_divide_basic(self):
        """Test: divide(10, 5) returns 2.0"""
        result = self.solution.divide(10, 5)
        self.assertAlmostEqual(result, 2.0, "divide(10, 5) should return 2.0")

    def test_divide_decimal(self):
        """Test: divide with decimal result"""
        result = self.solution.divide(10, 4)
        self.assertAlmostEqual(result, 2.5, "divide(10, 4) should return 2.5")

    def test_all_functions_return_not_print(self):
        """Test: Functions return values, not print"""
        # Verify that functions return values
        self.assertIsNotNone(
            self.solution.add(1, 1), "add should return a value, not None"
        )
        self.assertIsNotNone(
            self.solution.subtract(1, 1), "subtract should return a value, not None"
        )
        self.assertIsNotNone(
            self.solution.multiply(1, 1), "multiply should return a value, not None"
        )
        self.assertIsNotNone(
            self.solution.divide(1, 1), "divide should return a value, not None"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
