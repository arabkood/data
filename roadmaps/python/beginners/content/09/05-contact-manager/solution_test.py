import unittest
import subprocess
import sys
import os


class TestContactManager(unittest.TestCase):
    """Test suite for Contact Manager Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, contact1_name, contact1_phone, contact2_name, contact2_phone):
        """Run the solution with given inputs and return the output."""
        input_data = f"{contact1_name}\n{contact1_phone}\n{contact2_name}\n{contact2_phone}"

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

    def check_output(self, output, name1, phone1, name2, phone2, test_name):
        """Verify the output contains all required elements."""

        # Check for prompts
        prompt_name = "أدخل اسم جهة الاتصال:"
        prompt_phone = "أدخل رقم الهاتف:"

        self.assertIn(
            prompt_name,
            output,
            f"Missing name prompt in test '{test_name}'"
        )
        self.assertIn(
            prompt_phone,
            output,
            f"Missing phone prompt in test '{test_name}'"
        )

        # Check for count
        count_message = "عدد جهات الاتصال: 2"
        self.assertIn(
            count_message,
            output,
            f"Missing or incorrect count message in test '{test_name}'\nExpected: '{count_message}'"
        )

        # Check for both contacts in output
        contact1 = f"{name1}: {phone1}"
        contact2 = f"{name2}: {phone2}"

        self.assertIn(
            contact1,
            output,
            f"Missing contact 1 in test '{test_name}'\nExpected to find: '{contact1}'"
        )
        self.assertIn(
            contact2,
            output,
            f"Missing contact 2 in test '{test_name}'\nExpected to find: '{contact2}'"
        )

    def test_basic_contacts(self):
        """Test: Basic two contacts"""
        output = self.run_solution("أحمد", "0551234567", "سارة", "0559876543")
        self.check_output(output, "أحمد", "0551234567", "سارة", "0559876543", "Basic contacts")

    def test_different_contacts(self):
        """Test: Different names and numbers"""
        output = self.run_solution("علي", "0501111111", "فاطمة", "0502222222")
        self.check_output(output, "علي", "0501111111", "فاطمة", "0502222222", "Different contacts")

    def test_english_names(self):
        """Test: English names"""
        output = self.run_solution("John", "0551234567", "Alice", "0559876543")
        self.check_output(output, "John", "0551234567", "Alice", "0559876543", "English names")

    def test_short_numbers(self):
        """Test: Shorter phone numbers"""
        output = self.run_solution("محمد", "123456", "خالد", "789012")
        self.check_output(output, "محمد", "123456", "خالد", "789012", "Short numbers")


if __name__ == "__main__":
    unittest.main(verbosity=2)
