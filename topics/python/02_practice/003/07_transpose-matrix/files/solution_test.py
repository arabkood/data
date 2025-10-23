import unittest
from solution import transposeMatrix


class TestTransposeMatrix(unittest.TestCase):
    def test_2x2_matrix(self):
        self.assertEqual(transposeMatrix([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_2x3_matrix(self):
        self.assertEqual(
            transposeMatrix([[1, 2, 3], [4, 5, 6]]),
            [[1, 4], [2, 5], [3, 6]]
        )

    def test_single_element(self):
        self.assertEqual(transposeMatrix([[1]]), [[1]])

    def test_empty_matrix(self):
        self.assertEqual(transposeMatrix([]), [])

    def test_single_row(self):
        self.assertEqual(transposeMatrix([[1, 2, 3]]), [[1], [2], [3]])

    def test_single_column(self):
        self.assertEqual(transposeMatrix([[1], [2], [3]]), [[1, 2, 3]])

    def test_3x3_matrix(self):
        self.assertEqual(
            transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
