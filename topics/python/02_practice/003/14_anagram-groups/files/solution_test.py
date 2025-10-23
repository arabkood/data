import unittest
from solution import groupAnagrams


class TestGroupAnagrams(unittest.TestCase):
    def test_example_case(self):
        result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        result = [sorted(group) for group in result]
        result = sorted(result)
        expected = [["bat"], ["ate", "eat", "tea"], ["nat", "tan"]]
        expected = sorted(expected)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        self.assertEqual(groupAnagrams([""]), [[""]])

    def test_single_char(self):
        self.assertEqual(groupAnagrams(["a"]), [["a"]])

    def test_two_groups(self):
        result = groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"])
        result = [sorted(group) for group in result]
        result = sorted(result)
        expected = [["abc", "bca", "cab"], ["xyz", "zyx"]]
        expected = sorted(expected)
        self.assertEqual(result, expected)

    def test_no_anagrams(self):
        result = groupAnagrams(["a", "b", "c"])
        result = [sorted(group) for group in result]
        result = sorted(result)
        self.assertEqual(result, [["a"], ["b"], ["c"]])

    def test_all_same(self):
        result = groupAnagrams(["abc", "bca", "cab"])
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), ["abc", "bca", "cab"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
