import unittest
from solution import rotateList


class TestRotateList(unittest.TestCase):
    def test_rotate_once(self):
        self.assertEqual(rotateList([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4])

    def test_rotate_twice(self):
        self.assertEqual(rotateList([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_rotate_zero(self):
        self.assertEqual(rotateList([1, 2, 3], 0), [1, 2, 3])

    def test_rotate_full_cycle(self):
        self.assertEqual(rotateList([1, 2, 3], 3), [1, 2, 3])

    def test_rotate_more_than_length(self):
        self.assertEqual(rotateList([1, 2, 3], 4), [3, 1, 2])

    def test_empty_list(self):
        self.assertEqual(rotateList([], 5), [])

    def test_single_element(self):
        self.assertEqual(rotateList([1], 10), [1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
