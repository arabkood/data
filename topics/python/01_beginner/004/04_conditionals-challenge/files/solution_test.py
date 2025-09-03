import unittest
import subprocess
import sys
import os


class TestNumberClassifier(unittest.TestCase):
    """Test suite for the Number Classifier challenge using user input."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        cls.solution_path = "solution.py"
        if not os.path.exists(cls.solution_path):
            raise FileNotFoundError(
                f"{cls.solution_path} not found. Please create your solution file."
            )

    def run_solution(self, input_data):
        """Run the solution with given input and return the stripped output."""
        try:
            result = subprocess.run(
                [sys.executable, self.solution_path],
                input=str(input_data),
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
            )
            if result.returncode != 0:
                self.fail(
                    f"Program crashed with input '{input_data}'.\nError:\n{result.stderr}"
                )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            self.fail(
                f"Program took too long to run with input '{input_data}' (possible infinite loop)."
            )

    def test_case_is_zero(self):
        """Test: Input is '0'"""
        input_val = 0
        output = self.run_solution(input_val)
        expected_text = "The number is zero."
        # We check if the expected text is at the end of the output, after the prompt.
        self.assertTrue(
            output.endswith(expected_text),
            f"\nTest failed for input: {input_val}"
            f"\nExpected the output to end with: '{expected_text}'"
            f"\nActual output: '{output}'",
        )

    def test_case_is_positive_integer(self):
        """Test: Input is '42'"""
        input_val = 42
        output = self.run_solution(input_val)
        expected_text = "The number is not zero."
        self.assertTrue(
            output.endswith(expected_text),
            f"\nTest failed for input: {input_val}"
            f"\nExpected the output to end with: '{expected_text}'"
            f"\nActual output: '{output}'",
        )

    def test_case_is_negative_integer(self):
        """Test: Input is '-15'"""
        input_val = -15
        output = self.run_solution(input_val)
        expected_text = "The number is not zero."
        self.assertTrue(
            output.endswith(expected_text),
            f"\nTest failed for input: {input_val}"
            f"\nExpected the output to end with: '{expected_text}'"
            f"\nActual output: '{output}'",
        )

    def test_case_is_large_positive_integer(self):
        """Test: Input is '1000000'"""
        input_val = 1000000
        output = self.run_solution(input_val)
        expected_text = "The number is not zero."
        self.assertTrue(
            output.endswith(expected_text),
            f"\nTest failed for input: {input_val}"
            f"\nExpected the output to end with: '{expected_text}'"
            f"\nActual output: '{output}'",
        )

    def test_prompt_message(self):
        """Test: The prompt message 'Enter a number: ' is correct"""
        input_val = 1
        output = self.run_solution(input_val)
        expected_prompt = "Enter a number: "
        self.assertTrue(
            output.startswith(expected_prompt),
            f"\nTest for correct prompt message failed."
            f"\nExpected output to start with: '{expected_prompt}'"
            f"\nActual output: '{output}'",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
