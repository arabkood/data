import unittest
import subprocess
import sys
import os


class TestLoginSystem(unittest.TestCase):
    """Comprehensive test suite for the Simple Login System Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, username, access_code):
        """Run the solution with given inputs and return the output."""
        input_data = f"{username}\n{access_code}"
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

    def check_prompts_exist(self, output, test_name):
        """Verify the output contains required prompts."""
        prompt1 = "أدخل اسم المستخدم: "
        prompt2 = "أدخل رمز الدخول: "

        self.assertIn(
            prompt1,
            output,
            f"Missing username prompt in test '{test_name}': '{prompt1}'",
        )
        self.assertIn(
            prompt2,
            output,
            f"Missing access code prompt in test '{test_name}': '{prompt2}'",
        )

    def test_correct_code_simple_username(self):
        """Test: Correct code (6419) with simple username 'ahmed'"""
        output = self.run_solution("ahmed", "6419")
        self.check_prompts_exist(output, "Correct code - simple username")

        expected_welcome = "أهلاً بك يا ahmed"
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Correct code - simple username' failed"
            f"\nInput: username='ahmed', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_correct_code_with_spaces_and_uppercase(self):
        """Test: Correct code with username containing spaces and uppercase '  ALI  '"""
        output = self.run_solution("  ALI  ", "6419")
        self.check_prompts_exist(output, "Correct code - spaces and uppercase")

        expected_welcome = "أهلاً بك يا ali"
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Correct code - spaces and uppercase' failed"
            f"\nInput: username='  ALI  ', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_correct_code_mixed_case_username(self):
        """Test: Correct code with mixed case username 'SaRaH'"""
        output = self.run_solution("SaRaH", "6419")
        self.check_prompts_exist(output, "Correct code - mixed case")

        expected_welcome = "أهلاً بك يا sarah"
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Correct code - mixed case' failed"
            f"\nInput: username='SaRaH', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_correct_code_with_leading_spaces(self):
        """Test: Correct code with username having only leading spaces '   omar'"""
        output = self.run_solution("   omar", "6419")
        self.check_prompts_exist(output, "Correct code - leading spaces")

        expected_welcome = "أهلاً بك يا omar"
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Correct code - leading spaces' failed"
            f"\nInput: username='   omar', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_correct_code_with_trailing_spaces(self):
        """Test: Correct code with username having only trailing spaces 'fatima   '"""
        output = self.run_solution("fatima   ", "6419")
        self.check_prompts_exist(output, "Correct code - trailing spaces")

        expected_welcome = "أهلاً بك يا fatima"
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Correct code - trailing spaces' failed"
            f"\nInput: username='fatima   ', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_incorrect_code_too_high(self):
        """Test: Incorrect code (6420) - should produce no welcome message"""
        output = self.run_solution("user", "6420")
        self.check_prompts_exist(output, "Incorrect code - too high")

        # Should NOT contain any welcome message
        self.assertNotIn(
            "أهلاً بك يا",
            output,
            f"\nTest 'Incorrect code - too high' failed"
            f"\nInput: username='user', code='6420'"
            f"\nShould not contain welcome message but found it in: '{output.strip()}'",
        )

    def test_incorrect_code_too_low(self):
        """Test: Incorrect code (6418) - should produce no welcome message"""
        output = self.run_solution("user", "6418")
        self.check_prompts_exist(output, "Incorrect code - too low")

        # Should NOT contain any welcome message
        self.assertNotIn(
            "أهلاً بك يا",
            output,
            f"\nTest 'Incorrect code - too low' failed"
            f"\nInput: username='user', code='6418'"
            f"\nShould not contain welcome message but found it in: '{output.strip()}'",
        )

    def test_incorrect_code_completely_wrong(self):
        """Test: Completely wrong code (1234) - should produce no welcome message"""
        output = self.run_solution("user", "1234")
        self.check_prompts_exist(output, "Incorrect code - completely wrong")

        # Should NOT contain any welcome message
        self.assertNotIn(
            "أهلاً بك يا",
            output,
            f"\nTest 'Incorrect code - completely wrong' failed"
            f"\nInput: username='user', code='1234'"
            f"\nShould not contain welcome message but found it in: '{output.strip()}'",
        )

    def test_incorrect_code_zero(self):
        """Test: Zero code (0) - should produce no welcome message"""
        output = self.run_solution("user", "0")
        self.check_prompts_exist(output, "Incorrect code - zero")

        # Should NOT contain any welcome message
        self.assertNotIn(
            "أهلاً بك يا",
            output,
            f"\nTest 'Incorrect code - zero' failed"
            f"\nInput: username='user', code='0'"
            f"\nShould not contain welcome message but found it in: '{output.strip()}'",
        )

    def test_incorrect_code_negative(self):
        """Test: Negative code (-6419) - should produce no welcome message"""
        output = self.run_solution("user", "-6419")
        self.check_prompts_exist(output, "Incorrect code - negative")

        # Should NOT contain any welcome message
        self.assertNotIn(
            "أهلاً بك يا",
            output,
            f"\nTest 'Incorrect code - negative' failed"
            f"\nInput: username='user', code='-6419'"
            f"\nShould not contain welcome message but found it in: '{output.strip()}'",
        )

    def test_edge_case_empty_username_correct_code(self):
        """Test: Empty username (after strip) with correct code"""
        output = self.run_solution("   ", "6419")
        self.check_prompts_exist(output, "Empty username - correct code")

        expected_welcome = "أهلاً بك يا "  # Empty username after cleaning
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Empty username - correct code' failed"
            f"\nInput: username='   ', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )

    def test_arabic_username_correct_code(self):
        """Test: Arabic username with correct code"""
        output = self.run_solution("محمد", "6419")
        self.check_prompts_exist(output, "Arabic username - correct code")

        expected_welcome = "أهلاً بك يا محمد"
        self.assertIn(
            expected_welcome,
            output,
            f"\nTest 'Arabic username - correct code' failed"
            f"\nInput: username='محمد', code='6419'"
            f"\nExpected to find: '{expected_welcome}'"
            f"\nActual output: '{output.strip()}'",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
