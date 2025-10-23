import unittest
from solution import formatLikes


class TestFormatLikes(unittest.TestCase):
    def test_no_one(self):
        self.assertEqual(formatLikes([]), "no one likes this")

    def test_one_person(self):
        self.assertEqual(formatLikes(["Peter"]), "Peter likes this")

    def test_two_people(self):
        self.assertEqual(formatLikes(["Jacob", "Alex"]), "Jacob and Alex like this")

    def test_three_people(self):
        self.assertEqual(formatLikes(["Max", "John", "Mark"]), "Max, John and Mark like this")

    def test_four_people(self):
        self.assertEqual(formatLikes(["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")

    def test_five_people(self):
        self.assertEqual(formatLikes(["A", "B", "C", "D", "E"]), "A, B and 3 others like this")

    def test_many_people(self):
        self.assertEqual(formatLikes(["A", "B", "C", "D", "E", "F", "G"]), "A, B and 5 others like this")


if __name__ == "__main__":
    unittest.main(verbosity=2)
