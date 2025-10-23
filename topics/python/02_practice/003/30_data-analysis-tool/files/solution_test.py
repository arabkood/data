import unittest
from solution import analyzeData


class TestAnalyzeData(unittest.TestCase):
    def test_simple_sequence(self):
        result = analyzeData([1, 2, 3, 4, 5])
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["median"], 3)
        self.assertEqual(result["mode"], 1)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 5)
        self.assertEqual(result["range"], 4)

    def test_with_duplicates(self):
        result = analyzeData([1, 1, 2, 3])
        self.assertAlmostEqual(result["mean"], 1.75, places=2)
        self.assertEqual(result["median"], 1.5)
        self.assertEqual(result["mode"], 1)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 3)
        self.assertEqual(result["range"], 2)

    def test_empty_list(self):
        result = analyzeData([])
        self.assertIsNone(result["mean"])
        self.assertIsNone(result["median"])
        self.assertIsNone(result["mode"])
        self.assertIsNone(result["min"])
        self.assertIsNone(result["max"])
        self.assertIsNone(result["range"])

    def test_single_element(self):
        result = analyzeData([5])
        self.assertEqual(result["mean"], 5.0)
        self.assertEqual(result["median"], 5)
        self.assertEqual(result["mode"], 5)
        self.assertEqual(result["min"], 5)
        self.assertEqual(result["max"], 5)
        self.assertEqual(result["range"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
