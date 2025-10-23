import unittest
from solution import parseSimpleJSON


class TestParseSimpleJSON(unittest.TestCase):
    def test_string_and_number(self):
        result = parseSimpleJSON('{"name": "Ali", "age": 25}')
        self.assertEqual(result, {"name": "Ali", "age": 25})

    def test_single_number(self):
        result = parseSimpleJSON('{"x": 10}')
        self.assertEqual(result, {"x": 10})

    def test_empty_object(self):
        result = parseSimpleJSON('{}')
        self.assertEqual(result, {})

    def test_multiple_strings(self):
        result = parseSimpleJSON('{"first": "Ali", "last": "Ahmed"}')
        self.assertEqual(result, {"first": "Ali", "last": "Ahmed"})

    def test_multiple_numbers(self):
        result = parseSimpleJSON('{"x": 1, "y": 2, "z": 3}')
        self.assertEqual(result, {"x": 1, "y": 2, "z": 3})


if __name__ == "__main__":
    unittest.main(verbosity=2)
