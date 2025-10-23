import unittest
from solution import findPath


class TestFindPath(unittest.TestCase):
    def test_simple_key(self):
        self.assertEqual(findPath({"a": 1}, "a"), ["a"])

    def test_nested_one_level(self):
        self.assertEqual(findPath({"a": {"b": 2}}, "b"), ["a", "b"])

    def test_deep_nested(self):
        self.assertEqual(findPath({"a": {"b": {"c": 3}}}, "c"), ["a", "b", "c"])

    def test_key_not_found(self):
        self.assertIsNone(findPath({"a": 1}, "z"))

    def test_multiple_branches(self):
        self.assertEqual(findPath({"a": {"b": 1}, "c": {"d": 2}}, "d"), ["c", "d"])

    def test_root_level_key(self):
        self.assertEqual(findPath({"x": {"y": 1}, "z": 2}, "z"), ["z"])

    def test_empty_dict(self):
        self.assertIsNone(findPath({}, "a"))

    def test_very_deep(self):
        self.assertEqual(
            findPath({"a": {"b": {"c": {"d": {"e": 5}}}}}, "e"),
            ["a", "b", "c", "d", "e"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
