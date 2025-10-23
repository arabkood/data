import unittest
from solution import invertDict


class TestInvertDict(unittest.TestCase):
    def test_simple_dict(self):
        self.assertEqual(invertDict({"a": 1, "b": 2}), {1: "a", 2: "b"})

    def test_another_dict(self):
        self.assertEqual(invertDict({"x": 10, "y": 20}), {10: "x", 20: "y"})

    def test_empty_dict(self):
        self.assertEqual(invertDict({}), {})

    def test_string_values(self):
        self.assertEqual(invertDict({"name": "Ali", "city": "Cairo"}), {"Ali": "name", "Cairo": "city"})

    def test_single_item(self):
        self.assertEqual(invertDict({"key": "value"}), {"value": "key"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
