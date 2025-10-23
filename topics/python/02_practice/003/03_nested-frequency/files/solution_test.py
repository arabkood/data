import unittest
from solution import nestedFrequency


class TestNestedFrequency(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(nestedFrequency([1, 2, 1]), {1: 2, 2: 1})

    def test_one_level_nested(self):
        self.assertEqual(nestedFrequency([1, [2, 1], 3]), {1: 2, 2: 1, 3: 1})

    def test_deep_nested(self):
        self.assertEqual(nestedFrequency([[1, 2], [1, [2, 3]]]), {1: 2, 2: 2, 3: 1})

    def test_empty_list(self):
        self.assertEqual(nestedFrequency([]), {})

    def test_string_values(self):
        self.assertEqual(nestedFrequency(["a", ["b", "a"]]), {"a": 2, "b": 1})

    def test_all_same(self):
        self.assertEqual(nestedFrequency([1, [1, [1]]]), {1: 3})

    def test_mixed_types(self):
        self.assertEqual(
            nestedFrequency([1, "a", [1, "a", 2]]),
            {1: 2, "a": 2, 2: 1}
        )

    def test_nested_empty_lists(self):
        self.assertEqual(nestedFrequency([1, [], [2, []], 3]), {1: 1, 2: 1, 3: 1})


if __name__ == "__main__":
    unittest.main(verbosity=2)
