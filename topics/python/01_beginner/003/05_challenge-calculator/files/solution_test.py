import unittest
import subprocess
import sys
import os
from typing import List

# The name of the user's code file.
# This file must be in the same directory as this test script.
# We assume the user's code is in a file named `solution.py`.
file_to_test = "solution.py"


class TestBillSplitter(unittest.TestCase):
    """
    Test suite for the Bill Splitter Challenge.
    Each test case is defined in its own method.
    """

    @classmethod
    def setUpClass(cls):
        """
        A class-level setup method. It runs once before any tests.
        Here, we check if the user's solution file exists.
        """
        if not os.path.exists(file_to_test):
            raise FileNotFoundError(
                f"Test aborted: The file '{file_to_test}' was not found. "
                "Please make sure your solution is saved in a file with this exact name."
            )

    def _run_student_code(self, input_data: str) -> subprocess.CompletedProcess:
        """
        Helper method to run the user's script in a separate process.
        This isolates the test runner from the user's code and allows us
        to capture its output and errors.

        Args:
            input_data: A string to be fed into the script's standard input.

        Returns:
            A CompletedProcess object containing the script's output and status.
        """
        try:
            return subprocess.run(
                [sys.executable, file_to_test],
                input=input_data,
                capture_output=True,
                text=True,
                check=True,  # Raises CalledProcessError if the script returns a non-zero exit code
                timeout=5,
                encoding="utf-8",
            )
        except subprocess.CalledProcessError as e:
            # The user's script crashed (e.g., SyntaxError, ValueError).
            self.fail(
                f"\n\n--- فشل تشغيل السكريبت الخاص بك ---\n"
                f"المدخلات التي تم توفيرها للسكريبت:\n{input_data.replace(r'\n', ' (ثم Enter) ')}\n\n"
                f"--- رسالة الخطأ ---\n{e.stderr}"
            )
        except subprocess.TimeoutExpired:
            # The user's script took too long, likely an infinite loop.
            self.fail(
                "استغرق السكريبت وقتاً طويلاً للتشغيل. قد يكون عالقاً في حلقة لا نهائية."
            )

    def _verify_output(
        self,
        process: subprocess.CompletedProcess,
        test_name: str,
        input_data: str,
        expected_line: str,
    ):
        """Helper method to perform common assertions on the script's output."""

        actual_output = process.stdout

        # 1. Check for the required input prompts.
        prompt1 = "ما هو المبلغ الإجمالي للفاتورة؟"
        prompt2 = "كم عدد الأشخاص؟"
        self.assertIn(
            prompt1,
            actual_output,
            f"\n\n--- خطأ في رسالة الإدخال الأولى في اختبار '{test_name}' ---\n"
            f"لم يتم العثور على الرسالة المطلوبة: '{prompt1}'",
        )
        self.assertIn(
            prompt2,
            actual_output,
            f"\n\n--- خطأ في رسالة الإدخال الثانية في اختبار '{test_name}' ---\n"
            f"لم يتم العثور على الرسالة المطلوبة: '{prompt2}'",
        )

        # 2. Check that the final output line is correct.
        # We strip whitespace to make the comparison robust.
        actual_last_line = actual_output.strip().splitlines()[-1]
        expected_line_stripped = expected_line.strip()

        self.assertEqual(
            expected_line_stripped,
            actual_last_line,
            f"\n\n--- فشل في حالة الاختبار: '{test_name}' ---\n"
            f"المدخلات التي تم توفيرها للسكريبت:\n{input_data.replace(r'\n', ' (ثم Enter) ')}\n\n"
            f"--- السطر الأخير المتوقع من المخرجات ---\n{expected_line_stripped}\n\n"
            f"--- السطر الأخير الفعلي من المخرجات ---\n{actual_last_line}\n\n"
            "تلميح: تأكد من أن السطر الأخير من المخرجات يطابق الصيغة المطلوبة تمامًا.",
        )

    def test_basic_case(self):
        """Tests a standard case with whole numbers (100 / 4)."""
        test_name = "حالة أساسية"
        input_data = "100\n4"
        expected = "كل شخص يجب أن يدفع: 25.0"

        process = self._run_student_code(input_data)
        self._verify_output(process, test_name, input_data, expected)

    def test_decimal_bill(self):
        """Tests a case with a decimal bill amount (150.75 / 3)."""
        test_name = "فاتورة عشرية"
        input_data = "150.75\n3"
        expected = "كل شخص يجب أن يدفع: 50.25"

        process = self._run_student_code(input_data)
        self._verify_output(process, test_name, input_data, expected)

    def test_large_number_of_people(self):
        """Tests a case with a larger bill and more people (2500 / 10)."""
        test_name = "عدد كبير من الأشخاص"
        input_data = "2500\n10"
        expected = "كل شخص يجب أن يدفع: 250.0"

        process = self._run_student_code(input_data)
        self._verify_output(process, test_name, input_data, expected)

    def test_two_people(self):
        """Tests a simple case with two people (99.50 / 2)."""
        test_name = "شخصان"
        input_data = "99.50\n2"
        expected = "كل شخص يجب أن يدفع: 49.75"

        process = self._run_student_code(input_data)
        self._verify_output(process, test_name, input_data, expected)

    def test_single_person(self):
        """Tests the edge case of a bill for just one person (85.20 / 1)."""
        test_name = "فاتورة فردية"
        input_data = "85.20\n1"
        expected = "كل شخص يجب أن يدفع: 85.2"

        process = self._run_student_code(input_data)
        self._verify_output(process, test_name, input_data, expected)


# This allows the test script to be run from the command line.
if __name__ == "__main__":
    unittest.main(verbosity=2)
