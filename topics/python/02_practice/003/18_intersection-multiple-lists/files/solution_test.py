import unittest
from solution import intersection


class TestIntersection(unittest.TestCase):
    def test_three_lists(self):
        result = sorted(intersection([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
        self.assertEqual(result, [2, 3])

    def test_single_common(self):
        self.assertEqual(intersection([[1, 2], [2, 3], [2, 4]]), [2])

    def test_no_common(self):
        self.assertEqual(intersection([[1, 2], [3, 4]]), [])

    def test_with_duplicates(self):
        result = sorted(intersection([[1, 1, 2], [1, 2, 2]]))
        self.assertEqual(result, [1, 2])

    def test_single_list(self):
        self.assertEqual(intersection([[5]]), [5])

    def test_all_same(self):
        result = sorted(intersection([[1, 2], [1, 2], [1, 2]]))
        self.assertEqual(result, [1, 2])

    def test_empty_result(self):
        self.assertEqual(intersection([[1], [2], [3]]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
