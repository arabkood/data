import unittest
from solution import parseCSV


class TestParseCSV(unittest.TestCase):
    def test_simple_csv(self):
        self.assertEqual(parseCSV("name,age", "Ali,25"), {"name": "Ali", "age": "25"})

    def test_three_columns(self):
        self.assertEqual(parseCSV("x,y,z", "1,2,3"), {"x": "1", "y": "2", "z": "3"})

    def test_single_column(self):
        self.assertEqual(parseCSV("name", "Ali"), {"name": "Ali"})

    def test_longer_values(self):
        result = parseCSV("first,last,city", "Ahmed,Ali,Cairo")
        self.assertEqual(result, {"first": "Ahmed", "last": "Ali", "city": "Cairo"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
