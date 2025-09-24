import unittest
import subprocess
import sys
import os


class TestGradeAnalyzer(unittest.TestCase):
    """Test suite for the Grade Analyzer Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_solution(self, grades_input):
        """Run the solution with given inputs and return the output."""
        # Convert grades list to string input (add -1 at the end)
        input_lines = []
        for grade in grades_input:
            input_lines.append(str(grade))
        input_lines.append("-1")  # Add terminator
        input_data = "\n".join(input_lines)

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

    def test_basic_grades(self):
        """Test with basic valid grades."""
        grades = [85, 92, 67, 45, 73]
        output = self.run_solution(grades)

        # Check for required outputs
        self.assertIn("عدد الطلاب: 5", output, "Should show correct student count")
        self.assertIn("أعلى درجة: 92", output, "Should show highest grade")
        self.assertIn("أقل درجة: 45", output, "Should show lowest grade")
        self.assertIn("المتوسط: 72.4", output, "Should show correct average")
        self.assertIn("الناجحون: 4", output, "Should count 4 passing students")
        self.assertIn("الراسبون: 1", output, "Should count 1 failing student")

    def test_all_passing(self):
        """Test when all students pass."""
        grades = [95, 88, 76, 82, 90]
        output = self.run_solution(grades)

        self.assertIn("عدد الطلاب: 5", output)
        self.assertIn("أعلى درجة: 95", output)
        self.assertIn("أقل درجة: 76", output)
        self.assertIn("المتوسط: 86.2", output)
        self.assertIn("الناجحون: 5", output)
        self.assertIn("الراسبون: 0", output)

    def test_all_failing(self):
        """Test when all students fail."""
        grades = [45, 32, 58, 29, 50]
        output = self.run_solution(grades)

        self.assertIn("عدد الطلاب: 5", output)
        self.assertIn("أعلى درجة: 58", output)
        self.assertIn("أقل درجة: 29", output)
        self.assertIn("المتوسط: 42.8", output)
        self.assertIn("الناجحون: 0", output)
        self.assertIn("الراسبون: 5", output)

    def test_invalid_grades_handling(self):
        """Test handling of invalid grades."""
        # Include invalid grades that should be rejected
        grades = [85, 150, 92, -10, 67, 200, 73]
        output = self.run_solution(grades)

        # Should show error messages for invalid grades
        self.assertIn("درجة غير صحيحة", output, "Should show error for invalid grades")

        # Should only process valid grades (85, 92, 67, 73)
        self.assertIn("عدد الطلاب: 4", output, "Should only count valid grades")
        self.assertIn("أعلى درجة: 92", output)
        self.assertIn("أقل درجة: 67", output)

    def test_single_student(self):
        """Test with only one student."""
        grades = [75]
        output = self.run_solution(grades)

        self.assertIn("عدد الطلاب: 1", output)
        self.assertIn("أعلى درجة: 75", output)
        self.assertIn("أقل درجة: 75", output)
        self.assertIn("المتوسط: 75", output)
        self.assertIn("الناجحون: 1", output)
        self.assertIn("الراسبون: 0", output)

    def test_no_grades(self):
        """Test when no grades are entered (immediate -1)."""
        grades = []  # Will immediately send -1
        output = self.run_solution(grades)

        self.assertIn(
            "لم يتم إدخال أي درجات",
            output,
            "Should show message when no grades entered",
        )

    def test_boundary_grades(self):
        """Test with boundary values (0, 60, 100)."""
        grades = [0, 60, 100]
        output = self.run_solution(grades)

        self.assertIn("عدد الطلاب: 3", output)
        self.assertIn("أعلى درجة: 100", output)
        self.assertIn("أقل درجة: 0", output)
        self.assertIn("المتوسط: 53.33", output)
        self.assertIn("الناجحون: 2", output, "60 should be passing")
        self.assertIn("الراسبون: 1", output)

    def test_decimal_grades(self):
        """Test with decimal grades."""
        grades = [85.5, 92.75, 67.25, 45.5, 73.0]
        output = self.run_solution(grades)

        self.assertIn("عدد الطلاب: 5", output)
        self.assertIn("أعلى درجة: 92.75", output)
        self.assertIn("أقل درجة: 45.5", output)
        # Average should be 72.8
        self.assertIn("72.8", output)

    def test_prompts_present(self):
        """Test that input prompts are present."""
        grades = [80, 90]
        output = self.run_solution(grades)

        # Count number of prompts (should be one for each grade + the -1)
        prompt_count = output.count("أدخل درجة الطالب (-1 للإنهاء):")
        self.assertGreaterEqual(prompt_count, 2, "Should show prompt for each input")

    def test_large_class(self):
        """Test with many students."""
        grades = [
            78,
            82,
            91,
            67,
            55,
            88,
            73,
            95,
            60,
            45,
            83,
            79,
            92,
            68,
            71,
            86,
            58,
            90,
            77,
            84,
        ]
        output = self.run_solution(grades)

        self.assertIn("عدد الطلاب: 20", output)
        self.assertIn("أعلى درجة: 95", output)
        self.assertIn("أقل درجة: 45", output)

        # Calculate expected average
        avg = sum(grades) / len(grades)
        avg_str = f"{avg:.2f}"
        self.assertIn(avg_str, output, f"Should show average as {avg_str}")

        # Count passing/failing
        passing = sum(1 for g in grades if g >= 60)
        failing = sum(1 for g in grades if g < 60)
        self.assertIn(f"الناجحون: {passing}", output)
        self.assertIn(f"الراسبون: {failing}", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
