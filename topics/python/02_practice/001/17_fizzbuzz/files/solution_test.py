import unittest
from solution import fizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_3(self):
        self.assertEqual(fizzBuzz(3), "Fizz")

    def test_divisible_by_5(self):
        self.assertEqual(fizzBuzz(5), "Buzz")

    def test_divisible_by_both(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")

    def test_not_divisible(self):
        self.assertEqual(fizzBuzz(7), "7")

    def test_another_fizzbuzz(self):
        self.assertEqual(fizzBuzz(30), "FizzBuzz")

    def test_another_fizz(self):
        self.assertEqual(fizzBuzz(9), "Fizz")

    def test_another_buzz(self):
        self.assertEqual(fizzBuzz(10), "Buzz")

    def test_one(self):
        self.assertEqual(fizzBuzz(1), "1")

    def test_large_fizzbuzz(self):
        self.assertEqual(fizzBuzz(45), "FizzBuzz")

    def test_large_number(self):
        self.assertEqual(fizzBuzz(98), "98")


if __name__ == "__main__":
    unittest.main(verbosity=2)
