import unittest
import subprocess
import sys
import os

# The user's code file
file_to_test = "broken_welcome.py"


class TestChallenge(unittest.TestCase):
    def test_banner_challenge(self):
        """
        Runs the user's script and checks its output and source code for requirements.
        """
        # Check if the user's file exists
        if not os.path.exists(file_to_test):
            self.fail(f"لم يتم العثور على الملف '{file_to_test}'.")

        # Define the exact expected output, removing leading/trailing whitespace
        expected_output = (
            "******************************\n"
            "مرحباً بك يا محارب طه!\n"
            "أنت تبدأ من المستوى 5\n"
            "******************************"
        ).strip()

        try:
            # Run the user's script as a separate process to catch all errors
            process = subprocess.run(
                [sys.executable, file_to_test],
                capture_output=True,
                text=True,
                check=True,
                timeout=5,
            )
            actual_output = process.stdout.strip()

        except subprocess.CalledProcessError as e:
            # If the script exits with an error, fail the test and provide the error message
            self.fail(f"فشل تشغيل السكريبت الخاص بك.\n--- الخطأ ---\n{e.stderr}")
        except subprocess.TimeoutExpired:
            self.fail(
                "استغرق السكريبت وقتاً طويلاً للتشغيل. قد يكون عالقاً في حلقة تكرارية."
            )

        # 1. Check if the output matches the expected banner
        self.assertEqual(
            expected_output,
            actual_output,
            # f"لافتة المخرجات غير صحيحة.\n--- المخرجات المتوقعة ---\n{expected_output}\n\n--- المخرجات الخاصة بك ---\n{actual_output}",
        )

        # 2. Check for the required introductory comment
        with open(file_to_test, "r") as f:
            content = f.read()
            self.assertTrue(
                any(line.strip().startswith("#") for line in content.splitlines()),
                "السكريبت الخاص بك يفتقد التعليق المطلوب في الأعلى الذي يشرح وظيفته (مثال: '# هذا السكريبت يُنشئ لافتة ترحيب للاعب.').",
            )
