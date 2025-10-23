import unittest
from solution import checkPassword


class TestCheckPassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertEqual(checkPassword("Password1"), True)

    def test_no_uppercase(self):
        self.assertEqual(checkPassword("password123"), False)

    def test_no_lowercase(self):
        self.assertEqual(checkPassword("PASSWORD123"), False)

    def test_no_digit(self):
        self.assertEqual(checkPassword("Password"), False)

    def test_too_short(self):
        self.assertEqual(checkPassword("Pass1"), False)

    def test_another_valid(self):
        self.assertEqual(checkPassword("SecurePass123"), True)

    def test_minimal_valid(self):
        self.assertEqual(checkPassword("Abcdef12"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
