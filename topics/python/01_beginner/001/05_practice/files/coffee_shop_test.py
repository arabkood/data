import unittest
import sys
from io import StringIO
import importlib.util
import os


class TestCoffeeShop(unittest.TestCase):
    def setUp(self):

        if not os.path.exists("coffee_shop.py"):
            raise FileNotFoundError(
                "coffee_shop.py file not found in current directory",
                os.listdir()
            )

        spec = importlib.util.spec_from_file_location("coffee_shop", "coffee_shop.py")
        if spec is None:
            raise ImportError("Could not create spec for coffee_shop.py")

        self.main_module = importlib.util.module_from_spec(spec)
        if spec.loader is None:
            raise ImportError("Could not create loader for coffee_shop.py")

        # Capture print output
        self.held, sys.stdout = sys.stdout, StringIO()

        # Execute the module
        spec.loader.exec_module(self.main_module)

    def tearDown(self):
        sys.stdout = self.held

    def test_drink_variable_exists(self):
        print("Current working directory:", os.getcwd())
        print("Files in current directory:", os.listdir())

    def test_price_variable_exists(self):
        """Test that price variable exists and is a number"""
        self.assertTrue(
            hasattr(self.main_module, "price"), "المتغير `price` يجب أن يكون موجودًا"
        )
        self.assertIsInstance(
            self.main_module.price,
            (int, float),
            "المتغير `price` يجب أن يكون من نوع `رقم`",
        )
        self.assertGreaterEqual(
            self.main_module.price, 0.0, "السعر يجب أن يكون 0.00 على الأقل"
        )

    def test_total_calculation(self):
        """Test that total is calculated correctly"""
        self.assertTrue(
            hasattr(self.main_module, "total"), "المتغير `total` يجب أن يكون موجودًا"
        )
        self.assertIsInstance(
            self.main_module.total,
            (int, float),
            "المتغير `total` يجب أن يكون من نوع `رقم`",
        )
        expected_total = self.main_module.price + 2
        self.assertEqual(
            self.main_module.total,
            expected_total,
            f"الإجمالي (`total`) يجب أن يساوي {expected_total} (أي `price` + 2)",
        )

    def test_output_format(self):
        """Test that the output contains all required information"""
        output = sys.stdout.getvalue()
        self.assertIn(
            "- المشروب:", output, "الناتج يجب أن يحتوي على العنوان '- المشروب:'"
        )
        self.assertIn("- السعر:", output, "الناتج يجب أن يحتوي على العنوان '- السعر:'")
        self.assertIn(
            "- الإكرامية:", output, "الناتج يجب أن يحتوي على العنوان '- الإكرامية:'"
        )
        self.assertIn(
            "- الإجمالي:", output, "الناتج يجب أن يحتوي على العنوان '- الإجمالي:'"
        )
        self.assertIn(
            self.main_module.drink, output, "الناتج يجب أن يحتوي على اسم المشروب"
        )
        self.assertIn(
            str(self.main_module.price), output, "الناتج يجب أن يحتوي على السعر"
        )
        self.assertIn("2", output, "الناتج يجب أن يحتوي على قيمة الإكرامية")
        self.assertIn(
            str(self.main_module.total),
            output,
            "الناتج يجب أن يحتوي على القيمة الإجمالية",
        )

    def test_correct_data_types(self):
        """Test that correct data types are used"""
        self.assertIsInstance(
            self.main_module.drink,
            str,
            "المتغير `drink` يجب أن يكون من نوع `نص` (مكتوب بين علامتي اقتباس)",
        )
        self.assertIsInstance(
            self.main_module.price,
            (int, float),
            "المتغير `price` يجب أن يكون من نوع `رقم` (بدون علامات اقتباس)",
        )
        self.assertIsInstance(
            self.main_module.total,
            (int, float),
            "المتغير `total` يجب أن يكون من نوع `رقم` (بدون علامات اقتباس)",
        )
