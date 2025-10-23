import unittest
from solution import pipeline


class TestPipeline(unittest.TestCase):
    def test_single_transform(self):
        result = pipeline([1, 2, 3], [lambda x: [i * 2 for i in x]])
        self.assertEqual(result, [2, 4, 6])

    def test_multiple_transforms(self):
        result = pipeline([1, 2, 3, 4], [
            lambda x: [i * 2 for i in x],
            lambda x: [i for i in x if i > 4]
        ])
        self.assertEqual(result, [6, 8])

    def test_no_transforms(self):
        result = pipeline([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])

    def test_add_then_filter(self):
        result = pipeline([1, 2, 3], [
            lambda x: [i + 10 for i in x],
            lambda x: [i for i in x if i % 2 == 0]
        ])
        self.assertEqual(result, [12])

    def test_sum_transform(self):
        result = pipeline([1, 2, 3], [lambda x: sum(x)])
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
