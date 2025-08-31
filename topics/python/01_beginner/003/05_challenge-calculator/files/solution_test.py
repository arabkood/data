import unittest
import subprocess
import sys
import os


class TestBillSplitter(unittest.TestCase):
    """Simple test suite for the Bill Splitter Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, bill_amount, num_people):
        """Run the solution with given inputs and return the output."""
        input_data = f"{bill_amount}\n{num_people}"

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

    def check_output(self, output, bill_amount, num_people, test_name):
        """Verify the output contains required prompts and correct result."""

        # Check required prompts exist
        prompt1 = "ما هو المبلغ الإجمالي للفاتورة؟"
        prompt2 = "كم عدد الأشخاص؟"

        self.assertIn(
            prompt1, output, f"Missing first prompt in test '{test_name}': '{prompt1}'"
        )
        self.assertIn(
            prompt2, output, f"Missing second prompt in test '{test_name}': '{prompt2}'"
        )

        # Calculate expected result
        expected_amount = bill_amount / num_people
        expected_result = f"كل شخص يجب أن يدفع: {expected_amount}"

        # Check if the expected result appears in output
        self.assertIn(
            expected_result,
            output,
            f"\nTest '{test_name}' failed"
            f"\nInput: {bill_amount}, {num_people}"
            f"\nExpected to find: '{expected_result}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_basic_case(self):
        """Test: 100 / 4 = 25.0"""
        output = self.run_solution(100, 4)
        self.check_output(output, 100, 4, "Basic case")

    def test_decimal_bill(self):
        """Test: 150.75 / 3 = 50.25"""
        output = self.run_solution(150.75, 3)
        self.check_output(output, 150.75, 3, "Decimal bill")

    def test_large_group(self):
        """Test: 2500 / 10 = 250.0"""
        output = self.run_solution(2500, 10)
        self.check_output(output, 2500, 10, "Large group")

    def test_two_people(self):
        """Test: 99.50 / 2 = 49.75"""
        output = self.run_solution(99.50, 2)
        self.check_output(output, 99.50, 2, "Two people")

    def test_single_person(self):
        """Test: 85.20 / 1 = 85.2"""
        output = self.run_solution(85.20, 1)
        self.check_output(output, 85.20, 1, "Single person")


if __name__ == "__main__":
    unittest.main(verbosity=2)
