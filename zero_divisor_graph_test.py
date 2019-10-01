from zero_divisor_graph import (possible_mappings,
                                graph_from_edges,
                                get_graph_semigroups)
import unittest


class TestPossibleMappings(unittest.TestCase):

    def test_squareGraph(self):
        graph = graph_from_edges({(1, 2), (2, 3), (3, 4), (4, 1)})
        pm = possible_mappings(graph)
        self.assertIsNotNone(pm)
        self.assertEqual(pm[frozenset({1, 3})], {1, 3})
        self.assertEqual(pm[frozenset({2, 4})], {2, 4})
        self.assertEqual(pm[frozenset({1})], {1, 3})
        self.assertEqual(pm[frozenset({3})], {1, 3})
        self.assertEqual(pm[frozenset({2})], {2, 4})
        self.assertEqual(pm[frozenset({4})], {2, 4})
        self.assertEqual(len(pm), 6)

    def test_squareWithOneEnd(self):
        graph = graph_from_edges(
            {(1, 2), (2, 3), (3, 4), (4, 1), (4, 5)})
        pm = possible_mappings(graph)
        self.assertEqual(pm[frozenset({1, 3})], {1, 3})
        self.assertEqual(pm[frozenset({2, 4})], {4})
        self.assertEqual(pm[frozenset({2, 5})], {4})
        self.assertEqual(pm[frozenset({1, 5})], {1, 3})
        self.assertEqual(pm[frozenset({3, 5})], {1, 3})
        self.assertEqual(pm[frozenset({1})], {1, 3})
        self.assertEqual(pm[frozenset({3})], {1, 3})
        self.assertEqual(pm[frozenset({2})], {2, 4})
        self.assertEqual(pm[frozenset({4})], {4})
        self.assertEqual(len(pm), 10)


class TestPossibleSemigroups(unittest.TestCase):

    def test_squareGraph(self):
        graph = graph_from_edges({(1, 2), (2, 3), (3, 4), (4, 1)})
        semigroups = get_graph_semigroups(graph, 0)
        self.assertNotEqual(len(semigroups), 0)

    def test_triangle(self):
        graph = graph_from_edges({(1, 2), (2, 3), (3, 1)})
        semigroups = get_graph_semigroups(graph, 0)
        self.assertNotEqual(len(semigroups), 0)
        for s in semigroups:
            self.assertIn(s.get(1, 1), {0, 1, 2, 3})
            self.assertIn(s.get(2, 2), {0, 1, 2, 3})
            self.assertIn(s.get(3, 3), {0, 1, 2, 3})

    def test_squareWithOneEnd(self):
        graph = graph_from_edges(
            {(1, 2), (2, 3), (3, 4), (4, 1), (3, 5)})
        semigroups = get_graph_semigroups(graph, 0)
        self.assertNotEqual(len(semigroups), 0)
        for s in semigroups:
            self.assertEqual(s.get(1, 3), 3)
            self.assertEqual(s.get(1, 5), 3)

    def test_squareWithTwoEnds(self):
        graph = graph_from_edges(
            {(1, 2), (2, 3), (3, 4), (4, 1), (3, 5), (4, 6)})
        s = get_graph_semigroups(graph, 0)
        self.assertEqual(len(s), 0)

    def test_sixBipartiteGraph(self):
        pass


if __name__ == '__main__':
    unittest.main()
