import unittest
from solution import listIntersection


class TestListIntersection(unittest.TestCase):
    def test_common_elements(self):
        result = listIntersection([1, 2, 3], [2, 3, 4])
        self.assertEqual(sorted(result), [2, 3])

    def test_with_duplicates(self):
        result = listIntersection([1, 2, 2, 3], [2, 3, 3])
        self.assertEqual(sorted(result), [2, 3])

    def test_no_common(self):
        self.assertEqual(listIntersection([1, 2], [3, 4]), [])

    def test_all_common(self):
        result = listIntersection([1, 2, 3], [1, 2, 3])
        self.assertEqual(sorted(result), [1, 2, 3])

    def test_empty_first(self):
        self.assertEqual(listIntersection([], [1, 2]), [])

    def test_empty_second(self):
        self.assertEqual(listIntersection([1, 2], []), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
