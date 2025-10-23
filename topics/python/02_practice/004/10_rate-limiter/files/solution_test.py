import unittest
from solution import RateLimiter


class TestRateLimiter(unittest.TestCase):
    def test_basic_requests(self):
        limiter = RateLimiter(3, 60)
        self.assertTrue(limiter.allow_request("user1", 0))
        self.assertTrue(limiter.allow_request("user1", 10))
        self.assertTrue(limiter.allow_request("user1", 20))

    def test_exceed_limit(self):
        limiter = RateLimiter(3, 60)
        limiter.allow_request("user1", 0)
        limiter.allow_request("user1", 10)
        limiter.allow_request("user1", 20)
        self.assertFalse(limiter.allow_request("user1", 30))

    def test_window_expiry(self):
        limiter = RateLimiter(3, 60)
        limiter.allow_request("user1", 0)
        limiter.allow_request("user1", 10)
        limiter.allow_request("user1", 20)
        self.assertTrue(limiter.allow_request("user1", 70))

    def test_multiple_users(self):
        limiter = RateLimiter(2, 60)
        self.assertTrue(limiter.allow_request("user1", 0))
        self.assertTrue(limiter.allow_request("user2", 5))
        self.assertTrue(limiter.allow_request("user1", 10))
        self.assertTrue(limiter.allow_request("user2", 15))
        self.assertFalse(limiter.allow_request("user1", 20))
        self.assertFalse(limiter.allow_request("user2", 25))

    def test_sliding_window(self):
        limiter = RateLimiter(2, 10)
        self.assertTrue(limiter.allow_request("user1", 0))
        self.assertTrue(limiter.allow_request("user1", 5))
        self.assertFalse(limiter.allow_request("user1", 9))
        self.assertTrue(limiter.allow_request("user1", 11))


if __name__ == "__main__":
    unittest.main(verbosity=2)
