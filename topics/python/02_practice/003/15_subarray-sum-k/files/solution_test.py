import unittest
from solution import subarraySum


class TestSubarraySum(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(subarraySum([1, 1, 1], 2), 2)

    def test_multiple_subarrays(self):
        self.assertEqual(subarraySum([1, 2, 3], 3), 2)

    def test_no_match(self):
        self.assertEqual(subarraySum([1], 0), 0)

    def test_with_negatives(self):
        self.assertEqual(subarraySum([1, -1, 0], 0), 3)

    def test_complex_case(self):
        self.assertEqual(subarraySum([1, 2, 1, 2, 1], 3), 4)

    def test_single_element_match(self):
        self.assertEqual(subarraySum([5], 5), 1)

    def test_all_elements(self):
        self.assertEqual(subarraySum([1, 2, 3], 6), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
