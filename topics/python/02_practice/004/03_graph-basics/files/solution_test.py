import unittest
from solution import Graph


class TestGraph(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.add_vertex("A")
        self.assertEqual(g.get_neighbors("A"), [])

    def test_add_edge_undirected(self):
        g = Graph()
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        self.assertEqual(sorted(g.get_neighbors("A")), ["B"])
        self.assertEqual(sorted(g.get_neighbors("B")), ["A"])

    def test_add_edge_directed(self):
        g = Graph(directed=True)
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        self.assertEqual(g.get_neighbors("A"), ["B"])
        self.assertEqual(g.get_neighbors("B"), [])

    def test_has_path_direct(self):
        g = Graph()
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_edge("A", "B")
        self.assertTrue(g.has_path("A", "B"))

    def test_has_path_indirect(self):
        g = Graph()
        g.add_vertex("A")
        g.add_vertex("B")
        g.add_vertex("C")
        g.add_edge("A", "B")
        g.add_edge("B", "C")
        self.assertTrue(g.has_path("A", "C"))

    def test_has_path_no_path(self):
        g = Graph()
        g.add_vertex("A")
        g.add_vertex("B")
        self.assertFalse(g.has_path("A", "B"))

    def test_has_path_nonexistent_vertex(self):
        g = Graph()
        g.add_vertex("A")
        self.assertFalse(g.has_path("A", "D"))

    def test_complex_graph(self):
        g = Graph()
        for v in ["A", "B", "C", "D", "E"]:
            g.add_vertex(v)
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("B", "D")
        g.add_edge("C", "E")
        self.assertTrue(g.has_path("A", "D"))
        self.assertTrue(g.has_path("A", "E"))
        self.assertFalse(g.has_path("D", "E"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
