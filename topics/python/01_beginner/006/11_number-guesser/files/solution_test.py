import unittest
import subprocess
import sys
import os


class TestNumberGuessingGame(unittest.TestCase):
    """Test suite for the Number Guessing Game."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, guesses):
        """Run the solution with given guesses."""
        input_data = "\n".join(str(g) for g in guesses)

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

    def test_welcome_message(self):
        """Test welcome messages."""
        output = self.run_solution([15])  # Win immediately

        self.assertIn("أهلاً", output, "Missing welcome message")

        self.assertIn("لقد اخترت رقمًا بين 1 و 20", output, "Missing game explanation")

        self.assertIn("5 محاولات", output, "Missing attempts information")

    def test_win_first_try(self):
        """Test winning on first attempt."""
        output = self.run_solution([15])

        self.assertIn("محاولات متبقية: 5", output, "Should show 5 attempts remaining")

        self.assertIn("مبروك! الرقم الصحيح هو 15", output, "Missing win message")

    def test_higher_hint(self):
        """Test hint when guess is too low."""
        output = self.run_solution([10, 15])

        self.assertIn(
            "لا، الرقم أكبر", output, "Should tell player the number is higher"
        )

    def test_lower_hint(self):
        """Test hint when guess is too high."""
        output = self.run_solution([20, 15])

        self.assertIn(
            "لا، الرقم أصغر", output, "Should tell player the number is lower"
        )

    def test_win_third_attempt(self):
        """Test winning after multiple attempts."""
        output = self.run_solution([10, 20, 15])

        self.assertIn("محاولات متبقية: 5", output, "Should start with 5 attempts")

        self.assertIn(
            "محاولات متبقية: 4", output, "Should show 4 attempts after first guess"
        )

        self.assertIn(
            "محاولات متبقية: 3", output, "Should show 3 attempts after second guess"
        )

        self.assertIn(
            "مبروك! الرقم الصحيح هو 15", output, "Should win on third attempt"
        )

    def test_lose_all_attempts(self):
        """Test losing after 5 wrong attempts."""
        output = self.run_solution([1, 2, 3, 4, 5])

        self.assertIn("محاولات متبقية: 1", output, "Should reach last attempt")

        self.assertIn(
            "انتهت المحاولات! الرقم كان 15",
            output,
            "Should show game over message with correct number",
        )

    def test_attempts_counter(self):
        """Test that attempts decrease correctly."""
        output = self.run_solution([10, 12, 14, 16, 18])

        for i in range(5, 0, -1):
            self.assertIn(
                f"محاولات متبقية: {i}",
                output,
                f"Missing attempt counter for {i} attempts",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
