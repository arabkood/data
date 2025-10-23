import unittest
from solution import moveZeros


class TestMoveZeros(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(moveZeros([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test_zeros_at_start(self):
        self.assertEqual(moveZeros([0, 0, 1]), [1, 0, 0])

    def test_no_zeros(self):
        self.assertEqual(moveZeros([1, 2, 3]), [1, 2, 3])

    def test_all_zeros(self):
        self.assertEqual(moveZeros([0, 0, 0]), [0, 0, 0])

    def test_single_zero(self):
        self.assertEqual(moveZeros([1, 2, 0, 3]), [1, 2, 3, 0])

    def test_empty_list(self):
        self.assertEqual(moveZeros([]), [])

    def test_preserve_order(self):
        self.assertEqual(moveZeros([5, 0, 3, 0, 1, 0, 2]), [5, 3, 1, 2, 0, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
