import unittest
import sys
import os


class TestTextProcessorLibrary(unittest.TestCase):
    """Test suite for Text Processor Library Challenge."""

    @classmethod
    def setUpClass(cls):
        """Check if solution.py exists and import it."""
        if not os.path.exists("solution.py"):
            raise FileNotFoundError(
                "solution.py not found. Please create your solution file."
            )

        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        try:
            import solution

            cls.solution = solution
        except Exception as e:
            raise ImportError(f"Could not import solution.py: {e}")

    # reverse_string tests
    def test_reverse_string_exists(self):
        """Test: reverse_string function exists"""
        self.assertTrue(
            hasattr(self.solution, "reverse_string"),
            "Function 'reverse_string' not found",
        )

    def test_reverse_string_basic(self):
        """Test: reverse_string('hello') returns 'olleh'"""
        result = self.solution.reverse_string("hello")
        self.assertEqual(
            result, "olleh", "reverse_string('hello') should return 'olleh'"
        )

    def test_reverse_string_palindrome(self):
        """Test: reverse_string with palindrome"""
        result = self.solution.reverse_string("racecar")
        self.assertEqual(
            result, "racecar", "reverse_string('racecar') should return 'racecar'"
        )

    # count_vowels tests
    def test_count_vowels_exists(self):
        """Test: count_vowels function exists"""
        self.assertTrue(
            hasattr(self.solution, "count_vowels"), "Function 'count_vowels' not found"
        )

    def test_count_vowels_basic(self):
        """Test: count_vowels('hello') returns 2"""
        result = self.solution.count_vowels("hello")
        self.assertEqual(result, 2, "count_vowels('hello') should return 2")

    def test_count_vowels_mixed_case(self):
        """Test: count_vowels with mixed case"""
        result = self.solution.count_vowels("AEIOU")
        self.assertEqual(result, 5, "count_vowels('AEIOU') should return 5")

    def test_count_vowels_no_vowels(self):
        """Test: count_vowels with no vowels"""
        result = self.solution.count_vowels("xyz")
        self.assertEqual(result, 0, "count_vowels('xyz') should return 0")

    # capitalize_words tests
    def test_capitalize_words_exists(self):
        """Test: capitalize_words function exists"""
        self.assertTrue(
            hasattr(self.solution, "capitalize_words"),
            "Function 'capitalize_words' not found",
        )

    def test_capitalize_words_basic(self):
        """Test: capitalize_words('hello world') returns 'Hello World'"""
        result = self.solution.capitalize_words("hello world")
        self.assertEqual(
            result,
            "Hello World",
            "capitalize_words('hello world') should return 'Hello World'",
        )

    def test_capitalize_words_single(self):
        """Test: capitalize_words with single word"""
        result = self.solution.capitalize_words("python")
        self.assertEqual(
            result, "Python", "capitalize_words('python') should return 'Python'"
        )

    # remove_spaces tests
    def test_remove_spaces_exists(self):
        """Test: remove_spaces function exists"""
        self.assertTrue(
            hasattr(self.solution, "remove_spaces"),
            "Function 'remove_spaces' not found",
        )

    def test_remove_spaces_basic(self):
        """Test: remove_spaces('hello world') returns 'helloworld'"""
        result = self.solution.remove_spaces("hello world")
        self.assertEqual(
            result,
            "helloworld",
            "remove_spaces('hello world') should return 'helloworld'",
        )

    def test_remove_spaces_multiple(self):
        """Test: remove_spaces with multiple spaces"""
        result = self.solution.remove_spaces("a b c d")
        self.assertEqual(
            result, "abcd", "remove_spaces('a b c d') should return 'abcd'"
        )

    def test_remove_spaces_no_spaces(self):
        """Test: remove_spaces with no spaces"""
        result = self.solution.remove_spaces("hello")
        self.assertEqual(
            result, "hello", "remove_spaces('hello') should return 'hello'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
