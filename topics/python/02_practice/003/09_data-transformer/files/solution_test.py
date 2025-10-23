import unittest
from solution import transformData


class TestTransformData(unittest.TestCase):
    def test_single_item(self):
        result = transformData([{"id": 1, "name": "Ali"}])
        self.assertEqual(result, {1: {"name": "Ali"}})

    def test_multiple_items(self):
        result = transformData([
            {"id": 1, "name": "Ali"},
            {"id": 2, "name": "Sara"}
        ])
        self.assertEqual(result, {1: {"name": "Ali"}, 2: {"name": "Sara"}})

    def test_string_ids(self):
        result = transformData([
            {"id": "a", "value": 10},
            {"id": "b", "value": 20}
        ])
        self.assertEqual(result, {"a": {"value": 10}, "b": {"value": 20}})

    def test_empty_list(self):
        self.assertEqual(transformData([]), {})

    def test_multiple_fields(self):
        result = transformData([
            {"id": 1, "name": "Ali", "age": 25, "city": "Cairo"}
        ])
        self.assertEqual(result, {1: {"name": "Ali", "age": 25, "city": "Cairo"}})

    def test_three_items(self):
        result = transformData([
            {"id": 1, "x": 10},
            {"id": 2, "x": 20},
            {"id": 3, "x": 30}
        ])
        self.assertEqual(result, {1: {"x": 10}, 2: {"x": 20}, 3: {"x": 30}})


if __name__ == "__main__":
    unittest.main(verbosity=2)
