import unittest
import subprocess
import sys
import os


class TestSumCalculator(unittest.TestCase):
    """Test suite for the Sum Calculator Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, input_number):
        """Run the solution with given input and return the output."""
        input_data = str(input_number)

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

    def check_output(self, output, input_number, test_name):
        """Verify the output contains required prompt and correct result."""

        # Check required prompt exists
        prompt = "أدخل رقم موجب:"

        self.assertIn(
            prompt, output, f"Missing input prompt in test '{test_name}': '{prompt}'"
        )

        # Calculate expected sum
        expected_sum = sum(range(1, input_number + 1))
        expected_result = f"مجموع الأرقام من 1 إلى {input_number} هو: {expected_sum}"

        # Check if the expected result appears in output
        self.assertIn(
            expected_result,
            output,
            f"\nTest '{test_name}' failed"
            f"\nInput: {input_number}"
            f"\nExpected to find: '{expected_result}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_small_number(self):
        """Test: Sum of 1 to 5 = 15"""
        output = self.run_solution(5)
        self.check_output(output, 5, "Small number (5)")

    def test_ten(self):
        """Test: Sum of 1 to 10 = 55"""
        output = self.run_solution(10)
        self.check_output(output, 10, "Number 10")

    def test_medium_number(self):
        """Test: Sum of 1 to 50 = 1275"""
        output = self.run_solution(50)
        self.check_output(output, 50, "Medium number (50)")

    def test_hundred(self):
        """Test: Sum of 1 to 100 = 5050"""
        output = self.run_solution(100)
        self.check_output(output, 100, "Number 100")

    def test_one(self):
        """Test: Sum of 1 to 1 = 1"""
        output = self.run_solution(1)
        self.check_output(output, 1, "Edge case (1)")

    def test_larger_number(self):
        """Test: Sum of 1 to 200 = 20100"""
        output = self.run_solution(200)
        self.check_output(output, 200, "Larger number (200)")

    def test_performance(self):
        """Test: Program should handle large numbers efficiently"""
        import time

        start_time = time.time()
        output = self.run_solution(1000)
        end_time = time.time()

        # Check correctness
        self.check_output(output, 1000, "Performance test (1000)")

        # Check performance (should complete in under 2 seconds)
        execution_time = end_time - start_time
        self.assertLess(
            execution_time,
            2,
            f"Program took too long ({execution_time:.2f}s) for input 1000",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
