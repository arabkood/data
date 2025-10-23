import unittest
from solution import Trie


class TestTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))

    def test_search_nonexistent(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.search("app"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with("app"))

    def test_starts_with_full_word(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with("apple"))

    def test_starts_with_nonexistent(self):
        trie = Trie()
        trie.insert("apple")
        self.assertFalse(trie.starts_with("ban"))

    def test_insert_prefix_then_word(self):
        trie = Trie()
        trie.insert("app")
        trie.insert("apple")
        self.assertTrue(trie.search("app"))
        self.assertTrue(trie.search("apple"))

    def test_multiple_words(self):
        trie = Trie()
        words = ["apple", "app", "apricot", "banana"]
        for word in words:
            trie.insert(word)
        for word in words:
            self.assertTrue(trie.search(word))

    def test_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("apple"))
        self.assertFalse(trie.starts_with("app"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
