import unittest
from solution import SearchEngine


class TestSearchEngine(unittest.TestCase):
    def test_add_and_search(self):
        engine = SearchEngine()
        engine.add_document(1, "Python is great")
        result = engine.search("Python")
        self.assertEqual(result, [1])

    def test_search_multiple_docs(self):
        engine = SearchEngine()
        engine.add_document(1, "Python programming")
        engine.add_document(2, "Java programming")
        result = engine.search("programming")
        self.assertEqual(sorted(result), [1, 2])

    def test_search_multiple_words(self):
        engine = SearchEngine()
        engine.add_document(1, "Python is a programming language")
        engine.add_document(2, "Java is also a programming language")
        engine.add_document(3, "Python is popular")
        result = engine.search("Python programming")
        self.assertEqual(result[0], 1)

    def test_remove_document(self):
        engine = SearchEngine()
        engine.add_document(1, "Python programming")
        engine.add_document(2, "Java programming")
        engine.remove_document(1)
        result = engine.search("Python")
        self.assertEqual(result, [])

    def test_no_results(self):
        engine = SearchEngine()
        engine.add_document(1, "Python programming")
        result = engine.search("JavaScript")
        self.assertEqual(result, [])

    def test_case_insensitive(self):
        engine = SearchEngine()
        engine.add_document(1, "Python Is Great")
        result = engine.search("python")
        self.assertEqual(result, [1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
