import unittest
from solution import sayHello


class TestSayHello(unittest.TestCase):
    def test_simple_name(self):
        self.assertEqual(sayHello("Alice"), "Hello, Alice!")

    def test_arabic_name(self):
        self.assertEqual(sayHello("أحمد"), "Hello, أحمد!")

    def test_name_with_spaces(self):
        self.assertEqual(sayHello("John Smith"), "Hello, John Smith!")

    def test_short_name(self):
        self.assertEqual(sayHello("Li"), "Hello, Li!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
