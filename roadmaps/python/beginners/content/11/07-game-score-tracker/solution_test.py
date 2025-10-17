import unittest
import subprocess
import sys
import os


class TestGameScoreTracker(unittest.TestCase):
    """Test suite for Game Score Tracker Challenge."""

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
        lines = [line.strip() for line in output.strip().split('\n') if line.strip()]

        self.assertEqual(
            len(lines), 3,
            f"Expected 3 lines of output, got {len(lines)}"
        )

    def test_first_score(self):
        """Test: After +100 -30 = 70"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split('\n') if line.strip()]

        self.assertEqual(
            lines[0], "70",
            f"First score should be 70 (100-30), got '{lines[0]}'"
        )

    def test_second_score(self):
        """Test: After +100 -30 +50 = 120"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split('\n') if line.strip()]

        self.assertEqual(
            lines[1], "120",
            f"Second score should be 120 (70+50), got '{lines[1]}'"
        )

    def test_reset_score(self):
        """Test: After reset = 0"""
        output = self.run_solution()
        lines = [line.strip() for line in output.strip().split('\n') if line.strip()]

        self.assertEqual(
            lines[2], "0",
            f"Final score should be 0 (after reset), got '{lines[2]}'"
        )

    def test_has_global_keyword(self):
        """Test: Code uses global keyword"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        global_count = code.count("global")
        self.assertGreaterEqual(
            global_count, 3,
            f"Should use 'global' keyword at least 3 times, found {global_count}"
        )

    def test_has_required_functions(self):
        """Test: All required functions exist"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        required_functions = ["add_points", "subtract_points", "get_score", "reset_score"]

        for func_name in required_functions:
            self.assertIn(
                f"def {func_name}",
                code,
                f"Function '{func_name}' not found"
            )

    def test_score_variable_exists(self):
        """Test: score variable is defined"""
        with open("solution.py", "r", encoding="utf-8") as f:
            code = f.read()

        self.assertIn(
            "score",
            code,
            "Variable 'score' not found"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
