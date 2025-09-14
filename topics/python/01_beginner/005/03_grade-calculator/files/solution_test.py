import unittest
import subprocess
import sys
import os


class TestGradeCalculator(unittest.TestCase):
    """
    Test suite for the Grade Calculator challenge.
    """

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "لم يتم العثور على ملف solution.py. يرجى إنشاء ملف الحل الخاص بك."
            )

    def run_solution(self, score_input):
        """Run the solution with a given score and return the captured output."""
        try:
            result = subprocess.run(
                [sys.executable, "solution.py"],
                input=str(score_input),
                capture_output=True,
                text=True,
                timeout=5,
                encoding="utf-8",
            )
            if result.returncode != 0:
                self.fail(f"البرنامج توقف مع وجود خطأ:\n{result.stderr}")
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            self.fail(
                "استغرق البرنامج وقتاً طويلاً للتشغيل (قد تكون هناك حلقة لا نهائية)."
            )
        except Exception as e:
            self.fail(f"حدث خطأ غير متوقع أثناء تشغيل الكود: {e}")

    def check_output(self, score_input, expected_grade, test_name):
        """Helper method to run a test case and verify the output."""
        output = self.run_solution(score_input)

        prompt = "ادخل الدرجة الرقمية:"
        # We check if the prompt is present, but allow for extra text or spacing.
        self.assertIn(
            prompt,
            output,
            f"لم يتم العثور على رسالة الإدخال المطلوبة '{prompt}' في اختبار '{test_name}'.",
        )

        expected_result = f"التقدير هو: {expected_grade}"
        self.assertIn(
            expected_result,
            output,
            f"\n--- فشل اختبار '{test_name}' ---\n"
            f"المدخل: {score_input}\n"
            f"النتيجة المتوقعة يجب أن تحتوي على: '{expected_result}'\n"
            f"النتيجة الفعلية: '{output}'",
        )

    def test_grade_A_high(self):
        """Test: 95 -> A"""
        self.check_output(95, "A", "Grade A - High Score")

    def test_grade_A_boundary(self):
        """Test: 90 -> A"""
        self.check_output(90, "A", "Grade A - Boundary Score")

    def test_grade_A_float(self):
        """Test: 99.9 -> A"""
        self.check_output(99.9, "A", "Grade A - Float Score")

    def test_grade_B_mid(self):
        """Test: 85 -> B"""
        self.check_output(85, "B", "Grade B - Mid Score")

    def test_grade_B_boundary_high(self):
        """Test: 89.9 -> B"""
        self.check_output(89.9, "B", "Grade B - High Boundary")

    def test_grade_B_boundary_low(self):
        """Test: 80 -> B"""
        self.check_output(80, "B", "Grade B - Low Boundary")

    def test_grade_C_mid(self):
        """Test: 75.5 -> C"""
        self.check_output(75.5, "C", "Grade C - Mid Score")

    def test_grade_C_boundary(self):
        """Test: 70 -> C"""
        self.check_output(70, "C", "Grade C - Boundary Score")

    def test_grade_D_mid(self):
        """Test: 62 -> D"""
        self.check_output(62, "D", "Grade D - Mid Score")

    def test_grade_D_boundary(self):
        """Test: 60 -> D"""
        self.check_output(60, "D", "Grade D - Boundary Score")

    def test_grade_F_high(self):
        """Test: 59.9 -> F"""
        self.check_output(59.9, "F", "Grade F - High Score")

    def test_grade_F_mid(self):
        """Test: 45 -> F"""
        self.check_output(45, "F", "Grade F - Mid Score")

    def test_grade_F_zero(self):
        """Test: 0 -> F"""
        self.check_output(0, "F", "Grade F - Zero Score")

    def test_grade_F_negative(self):
        """Test: -10 -> F"""
        self.check_output(-10, "F", "Grade F - Negative Score")


if __name__ == "__main__":
    unittest.main(verbosity=2)
