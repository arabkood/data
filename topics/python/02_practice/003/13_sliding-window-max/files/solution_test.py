import unittest
from solution import maxSlidingWindow


class TestMaxSlidingWindow(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(
            maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7]
        )

    def test_single_element_k1(self):
        self.assertEqual(maxSlidingWindow([1], 1), [1])

    def test_k_equals_1(self):
        self.assertEqual(maxSlidingWindow([1, -1], 1), [1, -1])

    def test_k_equals_length(self):
        self.assertEqual(maxSlidingWindow([9, 11], 2), [11])

    def test_negative_and_positive(self):
        self.assertEqual(maxSlidingWindow([4, -2], 2), [4])

    def test_all_same(self):
        self.assertEqual(maxSlidingWindow([5, 5, 5, 5], 2), [5, 5, 5])

    def test_decreasing_order(self):
        self.assertEqual(maxSlidingWindow([5, 4, 3, 2, 1], 3), [5, 4, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
