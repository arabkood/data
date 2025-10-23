import unittest
from solution import hasConflict


class TestHasConflict(unittest.TestCase):
    def test_no_conflict_adjacent(self):
        self.assertFalse(hasConflict([
            {"start": 9, "end": 10},
            {"start": 10, "end": 11}
        ]))

    def test_has_conflict(self):
        self.assertTrue(hasConflict([
            {"start": 9, "end": 11},
            {"start": 10, "end": 12}
        ]))

    def test_single_meeting(self):
        self.assertFalse(hasConflict([{"start": 9, "end": 10}]))

    def test_empty_list(self):
        self.assertFalse(hasConflict([]))

    def test_no_conflict_separate(self):
        self.assertFalse(hasConflict([
            {"start": 9, "end": 10},
            {"start": 11, "end": 12}
        ]))

    def test_complete_overlap(self):
        self.assertTrue(hasConflict([
            {"start": 9, "end": 12},
            {"start": 10, "end": 11}
        ]))

    def test_three_meetings_conflict(self):
        self.assertTrue(hasConflict([
            {"start": 9, "end": 10},
            {"start": 11, "end": 12},
            {"start": 9, "end": 11}
        ]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
