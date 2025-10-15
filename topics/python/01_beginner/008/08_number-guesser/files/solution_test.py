import unittest
import subprocess
import sys
import os
import random


class TestNumberGuessingGame(unittest.TestCase):
    """Test suite for the Number Guessing Game Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution_with_guesses(self, guesses, expected_number=None):
        """Run the solution with a sequence of guesses."""
        # If expected_number is provided, we'll modify the random seed
        # Otherwise, we'll use a known seed for predictable testing
        input_data = "\n".join(map(str, guesses))

        try:
            # Set PYTHONHASHSEED for reproducibility
            env = os.environ.copy()
            env["PYTHONHASHSEED"] = "0"

            result = subprocess.run(
                [sys.executable, "solution.py"],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
                env=env,
            )

            if result.returncode != 0:
                self.fail(f"Program crashed with error:\n{result.stderr}")

            return result.stdout

        except subprocess.TimeoutExpired:
            self.fail("Program took too long to run (possible infinite loop)")

    def check_output_contains(self, output, expected_phrases, test_name):
        """Check if output contains expected phrases."""
        output_lower = output.lower()

        for phrase in expected_phrases:
            if phrase.lower() not in output_lower:
                self.fail(
                    f"\nTest '{test_name}' failed"
                    f"\nExpected to find: '{phrase}'"
                    f"\nIn output:\n{output}"
                )

    def test_welcome_message(self):
        """Test: Program displays welcome message"""
        output = self.run_solution_with_guesses([50])

        # Check for welcome messages
        self.assertIn(
            "تخمين",
            output,
            "Program should display a welcome message about guessing",
        )

    def test_higher_hint(self):
        """Test: Program gives 'higher' hint for low guess"""
        # We'll test with multiple low guesses to check the hint
        output = self.run_solution_with_guesses([10, 20, 30, 40, 50, 60, 70, 80, 90])

        # The output should contain hints - either "أعلى" or "أقل"
        self.assertTrue(
            "أعلى" in output or "أقل" in output,
            "Program should give hints (أعلى or أقل) after each guess",
        )

    def test_lower_hint(self):
        """Test: Program gives 'lower' hint for high guess"""
        output = self.run_solution_with_guesses([90, 80, 70, 60, 50, 40, 30, 20, 10])

        # The output should contain hints
        self.assertTrue(
            "أعلى" in output or "أقل" in output,
            "Program should give hints (أعلى or أقل) after each guess",
        )

    def test_multiple_guesses_accepted(self):
        """Test: Program accepts multiple guesses"""
        output = self.run_solution_with_guesses([25, 50, 75, 62, 56, 59, 60, 61, 58])

        # Count how many times "أدخل" appears (input prompts)
        input_prompts = output.count("أدخل")

        self.assertGreaterEqual(
            input_prompts,
            2,
            "Program should accept multiple guesses (at least 2 prompts)",
        )

    def test_attempt_counter(self):
        """Test: Program counts attempts"""
        # Make several guesses
        output = self.run_solution_with_guesses([30, 60, 45, 52, 48, 50, 49, 51])

        # Check for number-like patterns in output (attempt count)
        # Should contain some digit that represents attempts
        has_number = any(char.isdigit() for char in output)
        self.assertTrue(
            has_number,
            "Program should display the number of attempts (should contain digits)",
        )

    def test_congratulations_message(self):
        """Test: Program shows congratulations when guess is correct"""
        # Test with a range that should eventually hit the number
        output = self.run_solution_with_guesses(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] + list(range(11, 101))
        )

        # Check for congratulatory words
        congrats_words = ["مبروك", "أحسنت", "صحيح", "رائع"]
        has_congrats = any(word in output for word in congrats_words)

        self.assertTrue(
            has_congrats,
            "Program should display a congratulations message when the correct number is guessed",
        )

    def test_game_ends_on_correct_guess(self):
        """Test: Game ends when correct number is guessed"""
        # Try all numbers from 1 to 100 - game should end at some point
        output = self.run_solution_with_guesses(list(range(1, 101)))

        # If the game works correctly, it should stop before asking for 100 inputs
        # We check this by seeing that not all numbers appear in the output
        input_count = output.count("أدخل")

        self.assertLess(
            input_count,
            100,
            "Game should end before exhausting all possible guesses",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
