import unittest
from solution import longestStreak


class TestLongestStreak(unittest.TestCase):
    def test_simple_streak(self):
        self.assertEqual(longestStreak([1, 2, 3, 1, 2]), 3)

    def test_streak_in_middle(self):
        self.assertEqual(longestStreak([1, 2, 5, 6, 7, 8]), 4)

    def test_no_streak(self):
        self.assertEqual(longestStreak([1, 3, 5, 7]), 1)

    def test_descending(self):
        self.assertEqual(longestStreak([5, 4, 3, 2, 1]), 1)

    def test_all_consecutive(self):
        self.assertEqual(longestStreak([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(longestStreak([]), 0)

    def test_single_element(self):
        self.assertEqual(longestStreak([5]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
