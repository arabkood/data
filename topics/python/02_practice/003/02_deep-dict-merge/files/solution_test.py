import unittest
from solution import deepMerge


class TestDeepMerge(unittest.TestCase):
    def test_no_overlap(self):
        self.assertEqual(deepMerge({"a": 1}, {"b": 2}), {"a": 1, "b": 2})

    def test_simple_overlap(self):
        self.assertEqual(deepMerge({"a": 1}, {"a": 2}), {"a": 2})

    def test_nested_no_overlap(self):
        self.assertEqual(
            deepMerge({"a": {"b": 1}}, {"a": {"c": 2}}),
            {"a": {"b": 1, "c": 2}}
        )

    def test_nested_overlap(self):
        self.assertEqual(
            deepMerge({"a": {"b": 1}}, {"a": {"b": 2}}),
            {"a": {"b": 2}}
        )

    def test_deep_nested(self):
        self.assertEqual(
            deepMerge({"a": {"b": {"c": 1}}}, {"a": {"b": {"d": 2}}}),
            {"a": {"b": {"c": 1, "d": 2}}}
        )

    def test_empty_dicts(self):
        self.assertEqual(deepMerge({}, {}), {})

    def test_first_empty(self):
        self.assertEqual(deepMerge({}, {"a": 1}), {"a": 1})

    def test_second_empty(self):
        self.assertEqual(deepMerge({"a": 1}, {}), {"a": 1})

    def test_mixed_types(self):
        self.assertEqual(
            deepMerge({"a": 1, "b": {"c": 2}}, {"b": {"d": 3}, "e": 4}),
            {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
        )

    def test_override_non_dict_with_dict(self):
        self.assertEqual(
            deepMerge({"a": 1}, {"a": {"b": 2}}),
            {"a": {"b": 2}}
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
