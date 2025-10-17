import unittest
import subprocess
import sys
import os


class TestScopeDetective(unittest.TestCase):
    """Test suite for Scope Detective Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self):
        """Run the solution and return the output."""
        try:
            result = subprocess.run(
                [sys.executable, "solution.py"],
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
            )

            if result.returncode != 0:
                self.fail(f"Program crashed with error:\n{result.stderr}")

            return result.stdout

        except subprocess.TimeoutExpired:
            self.fail("Program took too long to run")

    def test_output_format(self):
        """Test: Output has 3 lines"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split("\n") if line.strip()]

        self.assertEqual(len(lines), 3, f"Expected 3 lines of output, got {len(lines)}")

    def test_counter_value(self):
        """Test: counter is 2 after two increments"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split("\n") if line.strip()]

        self.assertEqual(
            lines[0], "2", f"First line should be '2' (counter value), got '{lines[0]}'"
        )

    def test_get_double_value(self):
        """Test: get_double returns counter * 2 = 4"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split("\n") if line.strip()]

        self.assertEqual(
            lines[1], "4", f"Second line should be '4' (counter * 2), got '{lines[1]}'"
        )

    def test_process_value(self):
        """Test: process(5) returns 5 + 10 = 15"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split("\n") if line.strip()]

        self.assertEqual(
            lines[2], "15", f"Third line should be '15' (5 + 10), got '{lines[2]}'"
        )

    def test_has_global_keyword(self):
        """Test: Code uses global keyword"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn(
            "global", code, "Code should use 'global' keyword for increment function"
        )

    def test_has_increment_function(self):
        """Test: increment function exists"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn("def increment", code, "Should define increment() function")

    def test_has_get_double_function(self):
        """Test: get_double function exists"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn("def get_double", code, "Should define get_double() function")

    def test_has_process_function(self):
        """Test: process function exists"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertTrue("def process" in code, "Should define process(x) function")


if __name__ == "__main__":
    unittest.main(verbosity=2)
