import unittest
import subprocess
import sys
import os


class TestMatrixPatternBuilder(unittest.TestCase):
    """Test suite for the Matrix Pattern Builder Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, size):
        """Run the solution with given input and return the output."""
        input_data = str(size)

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

    def check_pattern_in_output(self, output, expected_lines, pattern_name, size):
        """Check if the expected pattern exists in the output."""
        output_lines = output.strip().split("\n")

        # Check if all expected pattern lines are in output
        for expected_line in expected_lines:
            if expected_line not in output_lines:
                self.fail(
                    f"\n{pattern_name} (size {size}) is incorrect."
                    f"\nExpected line: '{expected_line}'"
                    f"\nNot found in output:\n{output}"
                )

    def test_size_3(self):
        """Test: Pattern with size 3"""
        size = 3
        output = self.run_solution(size)

        # Pattern 1: Square 3x3
        square_pattern = ["***", "***", "***"]

        # Pattern 2: Increasing triangle
        increasing_pattern = ["*", "**", "***"]

        # Pattern 3: Decreasing triangle
        decreasing_pattern = ["***", "**", "*"]

        self.check_pattern_in_output(output, square_pattern, "Square pattern", size)
        self.check_pattern_in_output(
            output, increasing_pattern, "Increasing triangle", size
        )
        self.check_pattern_in_output(
            output, decreasing_pattern, "Decreasing triangle", size
        )

    def test_size_4(self):
        """Test: Pattern with size 4"""
        size = 4
        output = self.run_solution(size)

        square_pattern = ["****", "****", "****", "****"]
        increasing_pattern = ["*", "**", "***", "****"]
        decreasing_pattern = ["****", "***", "**", "*"]

        self.check_pattern_in_output(output, square_pattern, "Square pattern", size)
        self.check_pattern_in_output(
            output, increasing_pattern, "Increasing triangle", size
        )
        self.check_pattern_in_output(
            output, decreasing_pattern, "Decreasing triangle", size
        )

    def test_size_5(self):
        """Test: Pattern with size 5"""
        size = 5
        output = self.run_solution(size)

        square_pattern = ["*****", "*****", "*****", "*****", "*****"]
        increasing_pattern = ["*", "**", "***", "****", "*****"]
        decreasing_pattern = ["*****", "****", "***", "**", "*"]

        self.check_pattern_in_output(output, square_pattern, "Square pattern", size)
        self.check_pattern_in_output(
            output, increasing_pattern, "Increasing triangle", size
        )
        self.check_pattern_in_output(
            output, decreasing_pattern, "Decreasing triangle", size
        )

    def test_size_2(self):
        """Test: Pattern with size 2"""
        size = 2
        output = self.run_solution(size)

        square_pattern = ["**", "**"]
        increasing_pattern = ["*", "**"]
        decreasing_pattern = ["**", "*"]

        self.check_pattern_in_output(output, square_pattern, "Square pattern", size)
        self.check_pattern_in_output(
            output, increasing_pattern, "Increasing triangle", size
        )
        self.check_pattern_in_output(
            output, decreasing_pattern, "Decreasing triangle", size
        )

    def test_size_6(self):
        """Test: Pattern with size 6"""
        size = 6
        output = self.run_solution(size)

        square_pattern = ["******", "******", "******", "******", "******", "******"]
        increasing_pattern = ["*", "**", "***", "****", "*****", "******"]
        decreasing_pattern = ["******", "*****", "****", "***", "**", "*"]

        self.check_pattern_in_output(output, square_pattern, "Square pattern", size)
        self.check_pattern_in_output(
            output, increasing_pattern, "Increasing triangle", size
        )
        self.check_pattern_in_output(
            output, decreasing_pattern, "Decreasing triangle", size
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
