import unittest
from solution import removeNthFromEnd


class TestRemoveNthFromEnd(unittest.TestCase):
    def test_second_from_end(self):
        self.assertEqual(removeNthFromEnd([1, 2, 3, 4, 5], 2), [1, 2, 3, 5])

    def test_last_element(self):
        self.assertEqual(removeNthFromEnd([1, 2, 3], 1), [1, 2])

    def test_first_element(self):
        self.assertEqual(removeNthFromEnd([1, 2], 2), [2])

    def test_middle_element(self):
        self.assertEqual(removeNthFromEnd([1, 2, 3, 4, 5], 3), [1, 2, 4, 5])

    def test_single_element(self):
        self.assertEqual(removeNthFromEnd([1], 1), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
