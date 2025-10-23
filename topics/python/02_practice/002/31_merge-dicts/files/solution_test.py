import unittest
from solution import mergeDicts


class TestMergeDicts(unittest.TestCase):
    def test_no_overlap(self):
        self.assertEqual(mergeDicts({"a": 1}, {"b": 2}), {"a": 1, "b": 2})

    def test_complete_overlap(self):
        self.assertEqual(mergeDicts({"a": 1}, {"a": 2}), {"a": 2})

    def test_partial_overlap(self):
        self.assertEqual(mergeDicts({"a": 1, "b": 2}, {"b": 3, "c": 4}), {"a": 1, "b": 3, "c": 4})

    def test_empty_dicts(self):
        self.assertEqual(mergeDicts({}, {}), {})

    def test_first_empty(self):
        self.assertEqual(mergeDicts({}, {"a": 1}), {"a": 1})

    def test_second_empty(self):
        self.assertEqual(mergeDicts({"a": 1}, {}), {"a": 1})


if __name__ == "__main__":
    unittest.main(verbosity=2)
