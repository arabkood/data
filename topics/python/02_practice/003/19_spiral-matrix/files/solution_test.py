import unittest
from solution import spiralOrder


class TestSpiralOrder(unittest.TestCase):
    def test_3x3_matrix(self):
        self.assertEqual(
            spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        )

    def test_2x2_matrix(self):
        self.assertEqual(
            spiralOrder([[1, 2], [3, 4]]),
            [1, 2, 4, 3]
        )

    def test_single_row(self):
        self.assertEqual(spiralOrder([[1, 2, 3]]), [1, 2, 3])

    def test_single_column(self):
        self.assertEqual(spiralOrder([[1], [2], [3]]), [1, 2, 3])

    def test_single_element(self):
        self.assertEqual(spiralOrder([[1]]), [1])

    def test_2x3_matrix(self):
        self.assertEqual(
            spiralOrder([[1, 2, 3], [4, 5, 6]]),
            [1, 2, 3, 6, 5, 4]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
