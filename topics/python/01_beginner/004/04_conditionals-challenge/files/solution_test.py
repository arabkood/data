import unittest
import subprocess
import sys
import os
import tempfile


class TestNumberClassifier(unittest.TestCase):
    """
    Test suite for the Number Classifier challenge.
    It works by creating a temporary script for each test case,
    injecting the test number, running it, and checking the output.
    """

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        cls.solution_path = "solution.py"
        if not os.path.exists(cls.solution_path):
            raise FileNotFoundError(
                f"{cls.solution_path} not found. Please create your solution file."
            )
        with open(cls.solution_path, "r", encoding="utf-8") as f:
            cls.user_code = f.read()

    def run_solution_with_number(self, number_value):
        """
        Runs the user's code with a specific number injected
        and returns the standard output.
        """
        # Create a temporary file to run the test
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".py", encoding="utf-8"
        ) as temp_f:
            temp_script_path = temp_f.name
            # Write the number assignment first
            temp_f.write(f"number = {number_value}\n\n")
            # Write the user's code
            temp_f.write(self.user_code)

        try:
            # Execute the temporary script
            result = subprocess.run(
                [sys.executable, temp_script_path],
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
            )

            if result.returncode != 0:
                # If the script fails, include stderr in the failure message
                self.fail(
                    f"Program crashed for number = {number_value}.\n"
                    f"Error:\n{result.stderr}"
                )

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            self.fail(f"Program took too long to run for number = {number_value}.")
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_script_path):
                os.remove(temp_script_path)

    def test_case_is_zero(self):
        """Test: number = 0"""
        number = 0
        output = self.run_solution_with_number(number)
        expected_output = "The number is zero."
        self.assertEqual(
            output,
            expected_output,
            f"\nTest failed for input: number = {number}"
            f"\nExpected output: '{expected_output}'"
            f"\nActual output:   '{output}'",
        )

    def test_case_is_positive_integer(self):
        """Test: number = 42"""
        number = 42
        output = self.run_solution_with_number(number)
        expected_output = "The number is not zero."
        self.assertEqual(
            output,
            expected_output,
            f"\nTest failed for input: number = {number}"
            f"\nExpected output: '{expected_output}'"
            f"\nActual output:   '{output}'",
        )

    def test_case_is_negative_integer(self):
        """Test: number = -15"""
        number = -15
        output = self.run_solution_with_number(number)
        expected_output = "The number is not zero."
        self.assertEqual(
            output,
            expected_output,
            f"\nTest failed for input: number = {number}"
            f"\nExpected output: '{expected_output}'"
            f"\nActual output:   '{output}'",
        )

    def test_case_is_large_positive_integer(self):
        """Test: number = 1000000"""
        number = 1000000
        output = self.run_solution_with_number(number)
        expected_output = "The number is not zero."
        self.assertEqual(
            output,
            expected_output,
            f"\nTest failed for input: number = {number}"
            f"\nExpected output: '{expected_output}'"
            f"\nActual output:   '{output}'",
        )

    def test_case_is_large_negative_integer(self):
        """Test: number = -987654"""
        number = -987654
        output = self.run_solution_with_number(number)
        expected_output = "The number is not zero."
        self.assertEqual(
            output,
            expected_output,
            f"\nTest failed for input: number = {number}"
            f"\nExpected output: '{expected_output}'"
            f"\nActual output:   '{output}'",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
