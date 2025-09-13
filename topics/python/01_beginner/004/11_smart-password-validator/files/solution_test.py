import unittest
import subprocess
import sys
import os


class TestAdventureDoor(unittest.TestCase):
    """Test suite for the Adventure Door Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

    def run_script(self, inputs):
        """Run the solution with a list of inputs and return the output."""
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
                self.fail(f"Program crashed with error:\n{result.stderr}")
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            self.fail("Program took too long to run (possible infinite loop).")

    def test_red_door_success(self):
        """Test: Red door with enough gold."""
        output = self.run_script(["أحمر", "100"])
        self.assertIn(
            "لقد قمت برشوة الحارس ومررت بأمان!",
            output,
            "Failed on Red Door with enough gold. Check your logic and output message.",
        )

    def test_red_door_fail(self):
        """Test: Red door with insufficient gold."""
        output = self.run_script(["أحمر", "10"])
        self.assertIn(
            "الحارس يضحك منك ويلقيك في الزنزانة.",
            output,
            "Failed on Red Door with insufficient gold. Check your logic and output message.",
        )

    def test_red_door_exact_gold(self):
        """Test: Red door with exactly 50 gold."""
        output = self.run_script(["أحمر", "50"])
        self.assertIn(
            "لقد قمت برشوة الحارس ومررت بأمان!",
            output,
            "Failed on Red Door with exactly 50 gold. Remember the condition is >= 50.",
        )

    def test_blue_door_success(self):
        """Test: Blue door on the correct day."""
        output = self.run_script(["أزرق", "الثلاثاء"])
        self.assertIn(
            "الباب السحري يفتح لك!",
            output,
            "Failed on Blue Door on Tuesday. Check your logic and output message.",
        )

    def test_blue_door_fail(self):
        """Test: Blue door on the wrong day."""
        output = self.run_script(["أزرق", "الأحد"])
        self.assertIn(
            "الباب يبقى مغلقاً بإحكام.",
            output,
            "Failed on Blue Door on a day other than Tuesday. Check your logic and output message.",
        )

    def test_invalid_door_choice(self):
        """Test: Invalid door choice."""
        output = self.run_script(["أخضر"])
        self.assertIn(
            "لقد ترددت طويلاً وتحولت إلى حجر.",
            output,
            "Failed on invalid door choice. Check your final if condition for the first choice.",
        )

    def test_prompts_are_correct(self):
        """Test if the prompts match the requirements exactly."""
        # Test red door prompts
        output_red = self.run_script(["أحمر", "10"])
        self.assertIn(
            "أمامك بابان، باب أحمر وباب أزرق. أي واحد تختار؟ (أحمر/أزرق)", output_red
        )
        self.assertIn("كم لديك من الذهب؟", output_red)

        # Test blue door prompts
        output_blue = self.run_script(["أزرق", "الاثنين"])
        self.assertIn(
            "أمامك بابان، باب أحمر وباب أزرق. أي واحد تختار؟ (أحمر/أزرق)", output_blue
        )
        self.assertIn("ما هو اليوم من أيام الأسبوع؟", output_blue)


if __name__ == "__main__":
    unittest.main(verbosity=2)
