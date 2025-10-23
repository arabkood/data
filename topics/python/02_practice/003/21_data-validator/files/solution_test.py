import unittest
from solution import validateUser


class TestValidateUser(unittest.TestCase):
    def test_valid_user(self):
        result = validateUser({"name": "Ali", "age": 25, "email": "ali@test.com"})
        self.assertTrue(result["valid"])
        self.assertEqual(result["errors"], [])

    def test_empty_name(self):
        result = validateUser({"name": "", "age": 25, "email": "ali@test.com"})
        self.assertFalse(result["valid"])
        self.assertIn("name is empty", result["errors"])

    def test_age_too_young(self):
        result = validateUser({"name": "Ali", "age": 15, "email": "ali@test.com"})
        self.assertFalse(result["valid"])
        self.assertIn("age must be between 18 and 100", result["errors"])

    def test_age_too_old(self):
        result = validateUser({"name": "Ali", "age": 150, "email": "ali@test.com"})
        self.assertFalse(result["valid"])
        self.assertIn("age must be between 18 and 100", result["errors"])

    def test_invalid_email(self):
        result = validateUser({"name": "Ali", "age": 25, "email": "invalid"})
        self.assertFalse(result["valid"])
        self.assertIn("email must contain @ and .", result["errors"])

    def test_multiple_errors(self):
        result = validateUser({"name": "", "age": 15, "email": "invalid"})
        self.assertFalse(result["valid"])
        self.assertEqual(len(result["errors"]), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
