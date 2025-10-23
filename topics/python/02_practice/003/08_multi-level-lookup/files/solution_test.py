import unittest
from solution import getValue


class TestGetValue(unittest.TestCase):
    def test_simple_path(self):
        self.assertEqual(getValue({"a": 1}, ["a"]), 1)

    def test_nested_path(self):
        self.assertEqual(getValue({"a": {"b": 2}}, ["a", "b"]), 2)

    def test_deep_nested(self):
        self.assertEqual(getValue({"a": {"b": {"c": 3}}}, ["a", "b", "c"]), 3)

    def test_path_not_found(self):
        self.assertIsNone(getValue({"a": 1}, ["z"]))

    def test_partial_path_found(self):
        self.assertIsNone(getValue({"a": {"b": 2}}, ["a", "c"]))

    def test_string_value(self):
        self.assertEqual(getValue({"x": {"y": {"z": "hello"}}}, ["x", "y", "z"]), "hello")

    def test_empty_path(self):
        self.assertEqual(getValue({"a": 1}, []), {"a": 1})

    def test_list_value(self):
        self.assertEqual(getValue({"a": {"b": [1, 2, 3]}}, ["a", "b"]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
