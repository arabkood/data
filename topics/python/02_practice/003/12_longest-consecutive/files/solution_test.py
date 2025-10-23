import unittest
from solution import longestConsecutive


class TestLongestConsecutive(unittest.TestCase):
    def test_simple_sequence(self):
        self.assertEqual(longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_long_sequence(self):
        self.assertEqual(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_empty_list(self):
        self.assertEqual(longestConsecutive([]), 0)

    def test_single_element(self):
        self.assertEqual(longestConsecutive([1]), 1)

    def test_no_consecutive(self):
        self.assertEqual(longestConsecutive([1, 3, 5, 7]), 1)

    def test_all_consecutive(self):
        self.assertEqual(longestConsecutive([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(longestConsecutive([-1, 0, 1, 2]), 4)

    def test_duplicates(self):
        self.assertEqual(longestConsecutive([1, 2, 0, 1]), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
