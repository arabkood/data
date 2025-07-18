import unittest
import sys
from io import StringIO
import importlib.util
import os


class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("coffee_shop.py"):
            raise FileNotFoundError(
                "coffee_shop.py file not found in current directory"
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

    def assertHasAttr(self, name: str):
        if not hasattr(self.main_module, name):
            raise AssertionError(f"`{name}` لم يتم العثور على المتغير")

    def assertAttrIsInstance(self, obj, cls, name):
        if not isinstance(obj, cls):
            # type_map = {
            #     str: "`نص` (string)",
            #     (int, float): "`رقم` (number)",
            # }
            # key = (
            #     cls
            #     if isinstance(cls, type)
            #     else tuple(sorted(cls, key=lambda x: x.__name__))
            # )
            # expected_type_str = type_map.get(key, str(cls))

            raise AssertionError(f"غير صحيح `{name}` نوع المتغير")

    def test_step_one(self):
        self.assertHasAttr("drink")
        self.assertHasAttr("price")
        self.assertHasAttr("tip")
        self.assertAttrIsInstance(self.main_module.drink, str, "drink")
        self.assertAttrIsInstance(self.main_module.price, (int, float), "price")
        self.assertAttrIsInstance(self.main_module.tip, (int, float), "tip")

    def test_step_two(self):
        self.assertHasAttr("total")
        self.assertAttrIsInstance(self.main_module.total, (int, float), "total")
        expected_total = self.main_module.price + self.main_module.tip
        self.assertEqual(
            self.main_module.total,
            expected_total,
            "Total should be equal to 'price' + 'tip'",
        )

    def test_output_format(self):
        output = sys.stdout.getvalue()

        expected_output = f"{self.main_module.drink}\n{self.main_module.total}"

        error_message = (
            f"شكل المخرجات المطبوعة غير مطابق للمطلوب.\n\n"
            f"توقعنا أن نرى:\n---\n{expected_output}\n---\n\n"
            f"ولكن كانت نتيجة الكود الخاص بك:\n---\n{output}\n---\n\n"
        )
        try:
            self.assertEqual(output.strip(), expected_output)
        except:  # noqa: E722
            raise AssertionError(error_message)
