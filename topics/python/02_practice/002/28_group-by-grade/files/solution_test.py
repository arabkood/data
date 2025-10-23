import unittest
from solution import groupByGrade


class TestGroupByGrade(unittest.TestCase):
    def test_multiple_grades(self):
        students = [
            {"name": "Ali", "grade": "A"},
            {"name": "Sara", "grade": "B"},
            {"name": "Omar", "grade": "A"}
        ]
        result = groupByGrade(students)
        self.assertEqual(result, {"A": ["Ali", "Omar"], "B": ["Sara"]})

    def test_single_grade(self):
        students = [{"name": "Ali", "grade": "A"}, {"name": "Sara", "grade": "A"}]
        result = groupByGrade(students)
        self.assertEqual(result, {"A": ["Ali", "Sara"]})

    def test_empty_list(self):
        self.assertEqual(groupByGrade([]), {})

    def test_all_different_grades(self):
        students = [
            {"name": "Ali", "grade": "A"},
            {"name": "Sara", "grade": "B"},
            {"name": "Omar", "grade": "C"}
        ]
        result = groupByGrade(students)
        self.assertEqual(result, {"A": ["Ali"], "B": ["Sara"], "C": ["Omar"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
