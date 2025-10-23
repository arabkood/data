import unittest
from solution import isBalanced


class TestIsBalanced(unittest.TestCase):
    def test_simple_balanced(self):
        self.assertEqual(isBalanced("()"), True)

    def test_nested_balanced(self):
        self.assertEqual(isBalanced("([{}])"), True)

    def test_wrong_order(self):
        self.assertEqual(isBalanced("([)]"), False)

    def test_unmatched_open(self):
        self.assertEqual(isBalanced("(("), False)

    def test_unmatched_close(self):
        self.assertEqual(isBalanced("())"), False)

    def test_empty_string(self):
        self.assertEqual(isBalanced(""), True)

    def test_complex_balanced(self):
        self.assertEqual(isBalanced("{[()]}"), True)

    def test_with_text(self):
        self.assertEqual(isBalanced("hello(world)"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
