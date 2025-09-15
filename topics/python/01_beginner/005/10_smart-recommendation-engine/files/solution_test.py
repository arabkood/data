import unittest
import subprocess
import sys
import os


class TestRecommendationEngine(unittest.TestCase):
    """اختبارات محرك التوصيات الذكي"""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists("solution.py"):
            raise FileNotFoundError("لم يتم العثور على ملف solution.py")

    def run_solution(self, inputs):
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
                self.fail(f"البرنامج توقف مع خطأ:\n{result.stderr}")
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            self.fail("البرنامج استغرق وقتاً طويلاً")

    def check_output(self, inputs, expected_activity, test_name):
        output = self.run_solution(inputs)

        # التحقق من وجود رسائل الإدخال
        prompts = [
            "ما هي حالة الطقس اليوم؟ (sunny, rainy, cloudy):",
            "ما هي حالتك المزاجية؟ (energetic, relaxed):",
            "كم عدد الأشخاص؟:",
        ]

        for prompt in prompts:
            self.assertIn(prompt, output, f"رسالة الإدخال مفقودة: {prompt}")

        expected_result = f"النشاط المقترح هو: {expected_activity}"
        self.assertIn(
            expected_result,
            output,
            f"فشل اختبار {test_name}\nالمدخلات: {inputs}\nالمتوقع: {expected_result}\nالفعلي: {output}",
        )

    def test_rainy_weather(self):
        """اختبار الطقس الممطر"""
        self.check_output(
            ["rainy", "energetic", 3], "مشاهدة فيلم في المنزل", "الطقس الممطر"
        )

    def test_sunny_energetic_group(self):
        """اختبار طقس مشمس ونشيط مع مجموعة"""
        self.check_output(
            ["sunny", "energetic", 4], "لعب كرة القدم في الحديقة", "مشمس نشيط مجموعة"
        )

    def test_sunny_energetic_alone(self):
        """اختبار طقس مشمس ونشيط بمفرده"""
        self.check_output(["sunny", "energetic", 1], "الذهاب للجري", "مشمس نشيط وحيد")

    def test_sunny_relaxed(self):
        """اختبار طقس مشمس ومسترخي"""
        self.check_output(
            ["sunny", "relaxed", 2], "قراءة كتاب على الشاطئ", "مشمس مسترخي"
        )

    def test_cloudy_energetic(self):
        """اختبار طقس غائم ونشيط"""
        self.check_output(["cloudy", "energetic", 2], "زيارة متحف", "غائم نشيط")

    def test_cloudy_relaxed(self):
        """اختبار طقس غائم ومسترخي"""
        self.check_output(["cloudy", "relaxed", 1], "الذهاب إلى مقهى", "غائم مسترخي")

    def test_unknown_weather(self):
        """اختبار طقس غير معروف"""
        self.check_output(
            ["snowy", "relaxed", 2], "ابقى في المنزل واتعلم بايثون!", "طقس غير معروف"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
