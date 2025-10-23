import unittest
from solution import matrixRowSum


class TestMatrixRowSum(unittest.TestCase):
    def test_two_rows(self):
        self.assertEqual(matrixRowSum([[1, 2, 3], [4, 5, 6]]), [6, 15])

    def test_three_rows(self):
        self.assertEqual(matrixRowSum([[1, 2], [3, 4], [5, 6]]), [3, 7, 11])

    def test_single_element(self):
        self.assertEqual(matrixRowSum([[10]]), [10])

    def test_empty_matrix(self):
        self.assertEqual(matrixRowSum([]), [])

    def test_single_row(self):
        self.assertEqual(matrixRowSum([[1, 2, 3]]), [6])

    def test_different_row_sizes(self):
        self.assertEqual(matrixRowSum([[1, 2], [3, 4, 5], [6]]), [3, 12, 6])

    def test_negative_numbers(self):
        self.assertEqual(matrixRowSum([[1, -2, 3], [-4, 5]]), [2, 1])

    def test_zeros(self):
        self.assertEqual(matrixRowSum([[0, 0], [0, 0, 0]]), [0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
