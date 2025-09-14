import unittest
import subprocess
import sys
import os


class TestRecommendationEngine(unittest.TestCase):
    """
    Test suite for the Smart Recommendation Engine challenge.
    """

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "لم يتم العثور على ملف solution.py. يرجى إنشاء ملف الحل الخاص بك."
            )

    def run_solution(self, inputs):
        """Run the solution with a given set of inputs and return the captured output."""
        input_data = "\n".join(map(str, inputs))
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
                self.fail(f"البرنامج توقف مع وجود خطأ:\n{result.stderr}")
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            self.fail(
                "استغرق البرنامج وقتاً طويلاً للتشغيل (قد تكون هناك حلقة لا نهائية)."
            )
        except Exception as e:
            self.fail(f"حدث خطأ غير متوقع أثناء تشغيل الكود: {e}")

    def check_output(self, inputs, expected_activity, test_name):
        """Helper method to run a test case and verify the output."""
        output = self.run_solution(inputs)

        prompts = [
            "ما هي حالة الطقس اليوم؟ (sunny, rainy, cloudy):",
            "ما هي حالتك المزاجية؟ (energetic, relaxed):",
            "كم عدد الأشخاص؟:",
        ]
        for prompt in prompts:
            self.assertIn(
                prompt,
                output,
                f"لم يتم العثور على رسالة الإدخال المطلوبة '{prompt}' في اختبار '{test_name}'.",
            )

        expected_result = f"النشاط المقترح هو: {expected_activity}"
        self.assertIn(
            expected_result,
            output,
            f"\n--- فشل اختبار '{test_name}' ---\n"
            f"المدخلات: {inputs}\n"
            f"النتيجة المتوقعة يجب أن تحتوي على: '{expected_result}'\n"
            f"النتيجة الفعلية: '{output}'",
        )

    def test_rainy_day(self):
        """Test: Rainy weather should always suggest watching a movie."""
        inputs = ["rainy", "energetic", 5]
        self.check_output(inputs, "مشاهدة فيلم في المنزل", "Rainy Day")

    def test_sunny_energetic_group(self):
        """Test: Sunny, energetic, with a group."""
        inputs = ["sunny", "energetic", 4]
        self.check_output(inputs, "لعب كرة القدم في الحديقة", "Sunny Energetic Group")

    def test_sunny_energetic_solo(self):
        """Test: Sunny, energetic, but alone."""
        inputs = ["sunny", "energetic", 1]
        self.check_output(inputs, "الذهاب للجري", "Sunny Energetic Solo")

    def test_sunny_relaxed(self):
        """Test: Sunny and relaxed."""
        inputs = ["sunny", "relaxed", 2]
        self.check_output(inputs, "قراءة كتاب على الشاطئ", "Sunny Relaxed")

    def test_cloudy_energetic(self):
        """Test: Cloudy and energetic."""
        inputs = ["cloudy", "energetic", 3]
        self.check_output(inputs, "زيارة متحف", "Cloudy Energetic")

    def test_cloudy_relaxed(self):
        """Test: Cloudy and relaxed."""
        inputs = ["cloudy", "relaxed", 1]
        self.check_output(inputs, "الذهاب إلى مقهى", "Cloudy Relaxed")

    def test_default_case_unknown_weather(self):
        """Test: A weather type not in the logic should trigger the default case."""
        inputs = ["snowy", "relaxed", 2]
        self.check_output(
            inputs, "ابقى في المنزل و تعلم بايثون!", "Default Case (Unknown Weather)"
        )

    def test_edge_case_people_boundary(self):
        """Test: Check the boundary condition for number of people (more than 1)."""
        inputs = ["sunny", "energetic", 2]
        self.check_output(inputs, "لعب كرة القدم في الحديقة", "Edge Case (2 People)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
