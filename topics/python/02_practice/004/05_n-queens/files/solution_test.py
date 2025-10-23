import unittest
from solution import solveNQueens


class TestSolveNQueens(unittest.TestCase):
    def test_n_equals_1(self):
        result = solveNQueens(1)
        self.assertEqual(result, [[0]])

    def test_n_equals_4(self):
        result = solveNQueens(4)
        self.assertEqual(len(result), 2)
        self.assertIn([1, 3, 0, 2], result)
        self.assertIn([2, 0, 3, 1], result)

    def test_n_equals_2(self):
        result = solveNQueens(2)
        self.assertEqual(result, [])

    def test_n_equals_3(self):
        result = solveNQueens(3)
        self.assertEqual(result, [])

    def test_n_equals_5(self):
        result = solveNQueens(5)
        self.assertEqual(len(result), 10)

    def test_solutions_valid(self):
        solutions = solveNQueens(4)
        for solution in solutions:
            # Check each solution is valid
            self.assertEqual(len(solution), 4)
            # Check no two queens in same column
            self.assertEqual(len(set(solution)), 4)
            # Check no two queens on same diagonal
            for i in range(4):
                for j in range(i + 1, 4):
                    self.assertNotEqual(abs(solution[i] - solution[j]), abs(i - j))


if __name__ == "__main__":
    unittest.main(verbosity=2)
