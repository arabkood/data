import unittest
from solution import chunkList


class TestChunkList(unittest.TestCase):
    def test_uneven_chunks(self):
        self.assertEqual(chunkList([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_even_chunks(self):
        self.assertEqual(chunkList([1, 2, 3, 4, 5, 6], 3), [[1, 2, 3], [4, 5, 6]])

    def test_size_larger_than_list(self):
        self.assertEqual(chunkList([1, 2, 3], 5), [[1, 2, 3]])

    def test_empty_list(self):
        self.assertEqual(chunkList([], 2), [])

    def test_chunk_size_one(self):
        self.assertEqual(chunkList([1, 2, 3], 1), [[1], [2], [3]])

    def test_exact_division(self):
        self.assertEqual(chunkList([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_large_chunk(self):
        self.assertEqual(chunkList([1, 2, 3, 4, 5, 6, 7], 4), [[1, 2, 3, 4], [5, 6, 7]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
