import unittest
from solution import abbreviateName


class TestAbbreviateName(unittest.TestCase):
    def test_capitalized_name(self):
        self.assertEqual(abbreviateName("Sam Harris"), "S.H")

    def test_lowercase_name(self):
        self.assertEqual(abbreviateName("john doe"), "J.D")

    def test_uppercase_name(self):
        self.assertEqual(abbreviateName("MARK SMITH"), "M.S")

    def test_mixed_case(self):
        self.assertEqual(abbreviateName("alice wonder"), "A.W")

    def test_another_name(self):
        self.assertEqual(abbreviateName("Patrick Feenan"), "P.F")

    def test_short_names(self):
        self.assertEqual(abbreviateName("bo li"), "B.L")

    def test_long_names(self):
        self.assertEqual(abbreviateName("Christopher Anderson"), "C.A")


if __name__ == "__main__":
    unittest.main(verbosity=2)
