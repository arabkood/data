import unittest
from solution import CacheWithExpiry


class TestCacheWithExpiry(unittest.TestCase):
    def test_set_and_get(self):
        cache = CacheWithExpiry()
        cache.set("key1", "value1", 10, 0)
        self.assertEqual(cache.get("key1", 5), "value1")

    def test_expiry(self):
        cache = CacheWithExpiry()
        cache.set("key1", "value1", 10, 0)
        self.assertIsNone(cache.get("key1", 11))

    def test_multiple_keys(self):
        cache = CacheWithExpiry()
        cache.set("key1", "value1", 10, 0)
        cache.set("key2", "value2", 20, 0)
        self.assertEqual(cache.get("key1", 5), "value1")
        self.assertEqual(cache.get("key2", 5), "value2")
        self.assertIsNone(cache.get("key1", 11))
        self.assertEqual(cache.get("key2", 15), "value2")

    def test_delete(self):
        cache = CacheWithExpiry()
        cache.set("key1", "value1", 10, 0)
        cache.delete("key1")
        self.assertIsNone(cache.get("key1", 5))

    def test_cleanup(self):
        cache = CacheWithExpiry()
        cache.set("key1", "value1", 10, 0)
        cache.set("key2", "value2", 20, 0)
        cache.cleanup(15)
        self.assertIsNone(cache.get("key1", 5))
        self.assertEqual(cache.get("key2", 15), "value2")

    def test_update_existing_key(self):
        cache = CacheWithExpiry()
        cache.set("key1", "value1", 10, 0)
        cache.set("key1", "value2", 20, 10)
        self.assertEqual(cache.get("key1", 15), "value2")


if __name__ == "__main__":
    unittest.main(verbosity=2)
