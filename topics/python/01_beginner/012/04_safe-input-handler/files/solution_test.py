import unittest
import subprocess
import sys
import os


class TestSafeInputHandler(unittest.TestCase):
    """Test suite for Safe Input Handler Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, inputs):
        """Run the solution with given inputs and return the output."""
        input_data = "\n".join(inputs)

        try:
            result = subprocess.run(
                [sys.executable, "solution.py"],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
            )

            if result.returncode != 0:
                self.fail(f"Program crashed with error:\n{result.stderr}")

            return result.stdout

        except subprocess.TimeoutExpired:
            self.fail("Program took too long to run (possible infinite loop)")

    def test_valid_inputs(self):
        """Test: Two valid numbers"""
        output = self.run_solution(["10", "20"])

        self.assertIn("أدخل رقماً:", output, "Should prompt for number input")
        self.assertIn("30", output, "Should print sum of 10 + 20 = 30")

    def test_error_handling(self):
        """Test: Invalid then valid input"""
        output = self.run_solution(["abc", "10", "20"])

        self.assertIn("خطأ", output, "Should print error message for invalid input")
        self.assertIn("30", output, "Should eventually print correct sum")

    def test_multiple_errors(self):
        """Test: Multiple invalid inputs"""
        output = self.run_solution(["abc", "xyz", "15", "def", "25"])

        error_count = output.count("خطأ")
        self.assertGreaterEqual(
            error_count,
            3,
            f"Should handle multiple errors, found {error_count} error messages",
        )
        self.assertIn("40", output, "Should print sum of 15 + 25 = 40")

    def test_has_function(self):
        """Test: get_safe_number function exists"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn(
            "def get_safe_number", code, "Should define get_safe_number() function"
        )

    def test_uses_try_except(self):
        """Test: Uses try-except"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn("try", code, "Should use try block")
        self.assertIn("except", code, "Should use except block")

    def test_uses_valueerror(self):
        """Test: Catches ValueError specifically"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn("ValueError", code, "Should catch ValueError specifically")


if __name__ == "__main__":
    unittest.main(verbosity=2)
