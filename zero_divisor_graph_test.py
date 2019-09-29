from zero_divisor_graph import (possible_mappings,
                                graph_from_edges,
                                get_semigroup)
from zero_divisor_graph import MixedCounter as counter
import unittest


class TestMixedCounter(unittest.TestCase):

    def setUp(self):
        self.c1 = counter((3, 3, 2, 5))

    def test_counter1(self):
        self.c1.tick()
        self.assertEqual(self.c1.get_val(0), 1)
        self.assertEqual(self.c1.get_val(1), 0)
        self.assertEqual(self.c1.get_val(2), 0)

    def test_counter3(self):
        for _ in range(3):
            self.c1.tick()
        self.assertEqual(self.c1.get_val(0), 0)
        self.assertEqual(self.c1.get_val(1), 1)
        self.assertEqual(self.c1.get_val(2), 0)

    def test_counter12(self):
        for _ in range(12):
            self.c1.tick()
        self.assertEqual(self.c1.get_val(0), 0)
        self.assertEqual(self.c1.get_val(1), 1)
        self.assertEqual(self.c1.get_val(2), 1)

    def test_counterEnd(self):
        for _ in range(89):
            self.c1.tick()
        self.assertEqual(self.c1.get_val(0), 2)
        self.assertEqual(self.c1.get_val(1), 2)
        self.assertEqual(self.c1.get_val(2), 1)
        self.assertEqual(self.c1.get_val(3), 4)

    def test_counterWrap(self):
        for _ in range(90):
            self.c1.tick()
        self.assertEqual(self.c1.get_val(0), 0)
        self.assertEqual(self.c1.get_val(1), 0)
        self.assertEqual(self.c1.get_val(2), 0)
        self.assertEqual(self.c1.get_val(3), 0)


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
        s = get_semigroup(graph, 0)
        self.assertIsNotNone(s)

    def test_triangle(self):
        graph = graph_from_edges({(1, 2), (2, 3), (3, 1)})
        s = get_semigroup(graph, 0)
        self.assertIsNotNone(s)
        self.assertIn(s.get(1, 1), {0, 1})
        self.assertIn(s.get(2, 2), {0, 2})
        self.assertIn(s.get(3, 3), {0, 3})

    def test_squareWithOneEnd(self):
        graph = graph_from_edges(
            {(1, 2), (2, 3), (3, 4), (4, 1), (3, 5)})
        s = get_semigroup(graph, 0)
        self.assertIsNotNone(s)
        self.assertEqual(s.get(1, 3), 3)
        self.assertEqual(s.get(1, 5), 3)


if __name__ == '__main__':
    unittest.main()
