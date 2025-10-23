import unittest
from solution import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_basic_get_put(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_evict_least_recently_used(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)

    def test_get_nonexistent_key(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1)

    def test_complex_scenario(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_single_capacity(self):
        cache = LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)

    def test_put_makes_recent(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
