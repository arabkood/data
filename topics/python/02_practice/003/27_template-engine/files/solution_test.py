import unittest
from solution import renderTemplate


class TestRenderTemplate(unittest.TestCase):
    def test_single_variable(self):
        self.assertEqual(
            renderTemplate("Hello {{name}}!", {"name": "Ali"}),
            "Hello Ali!"
        )

    def test_multiple_variables(self):
        self.assertEqual(
            renderTemplate("{{x}} + {{y}} = {{z}}", {"x": 1, "y": 2, "z": 3}),
            "1 + 2 = 3"
        )

    def test_missing_variable(self):
        self.assertEqual(renderTemplate("Hello {{name}}!", {}), "Hello !")

    def test_no_variables(self):
        self.assertEqual(renderTemplate("No variables", {"x": 1}), "No variables")

    def test_repeated_variable(self):
        self.assertEqual(
            renderTemplate("{{x}} {{x}} {{x}}", {"x": "test"}),
            "test test test"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
