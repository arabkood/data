import unittest
from solution import RangeQuery


class TestRangeQuery(unittest.TestCase):
    def test_basic_range(self):
        rq = RangeQuery([1, 3, 5, 7, 9])
        self.assertEqual(rq.sumRange(0, 2), 9)

    def test_middle_range(self):
        rq = RangeQuery([1, 3, 5, 7, 9])
        self.assertEqual(rq.sumRange(1, 3), 15)

    def test_end_range(self):
        rq = RangeQuery([1, 3, 5, 7, 9])
        self.assertEqual(rq.sumRange(2, 4), 21)

    def test_single_element(self):
        rq = RangeQuery([1, 3, 5, 7, 9])
        self.assertEqual(rq.sumRange(2, 2), 5)

    def test_full_range(self):
        rq = RangeQuery([1, 3, 5, 7, 9])
        self.assertEqual(rq.sumRange(0, 4), 25)

    def test_negative_numbers(self):
        rq = RangeQuery([-2, 0, 3, -5, 2, -1])
        self.assertEqual(rq.sumRange(0, 2), 1)
        self.assertEqual(rq.sumRange(2, 5), -1)

    def test_multiple_queries(self):
        rq = RangeQuery([1, 2, 3, 4, 5])
        self.assertEqual(rq.sumRange(0, 1), 3)
        self.assertEqual(rq.sumRange(1, 3), 9)
        self.assertEqual(rq.sumRange(0, 4), 15)


if __name__ == "__main__":
    unittest.main(verbosity=2)
