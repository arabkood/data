import unittest
from solution import groupAndSum


class TestGroupAndSum(unittest.TestCase):
    def test_different_categories(self):
        result = groupAndSum([{"category": "A", "value": 10}, {"category": "B", "value": 20}])
        self.assertEqual(result, {"A": 10, "B": 20})

    def test_same_category(self):
        result = groupAndSum([{"category": "A", "value": 10}, {"category": "A", "value": 5}])
        self.assertEqual(result, {"A": 15})

    def test_mixed_categories(self):
        result = groupAndSum([
            {"category": "X", "value": 1},
            {"category": "Y", "value": 2},
            {"category": "X", "value": 3}
        ])
        self.assertEqual(result, {"X": 4, "Y": 2})

    def test_empty_list(self):
        self.assertEqual(groupAndSum([]), {})

    def test_single_item(self):
        result = groupAndSum([{"category": "A", "value": 100}])
        self.assertEqual(result, {"A": 100})

    def test_multiple_same(self):
        result = groupAndSum([
            {"category": "A", "value": 1},
            {"category": "A", "value": 2},
            {"category": "A", "value": 3}
        ])
        self.assertEqual(result, {"A": 6})

    def test_three_categories(self):
        result = groupAndSum([
            {"category": "A", "value": 10},
            {"category": "B", "value": 20},
            {"category": "C", "value": 30},
            {"category": "A", "value": 5}
        ])
        self.assertEqual(result, {"A": 15, "B": 20, "C": 30})


if __name__ == "__main__":
    unittest.main(verbosity=2)
