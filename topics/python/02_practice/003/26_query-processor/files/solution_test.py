import unittest
from solution import queryData


class TestQueryData(unittest.TestCase):
    def test_single_condition(self):
        result = queryData(
            [{"name": "Ali", "age": 25}, {"name": "Sara", "age": 30}],
            {"age": 25}
        )
        self.assertEqual(result, [{"name": "Ali", "age": 25}])

    def test_multiple_conditions(self):
        result = queryData(
            [{"name": "Ali", "age": 25, "city": "Cairo"}],
            {"name": "Ali", "age": 25}
        )
        self.assertEqual(result, [{"name": "Ali", "age": 25, "city": "Cairo"}])

    def test_no_match(self):
        result = queryData([{"x": 1}, {"x": 2}], {"x": 3})
        self.assertEqual(result, [])

    def test_empty_query(self):
        result = queryData([{"x": 1}, {"x": 2}], {})
        self.assertEqual(result, [{"x": 1}, {"x": 2}])

    def test_multiple_matches(self):
        result = queryData(
            [{"type": "A", "value": 1}, {"type": "A", "value": 2}],
            {"type": "A"}
        )
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
