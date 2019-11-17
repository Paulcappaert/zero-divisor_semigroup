import unittest



from zero_divisor_graph import (possible_mappings,
                                graph_from_edges,
                                get_graph_semigroups)


class TestPossibleMappings(unittest.TestCase):

    def setUp(self):
        pass

    def test_squareGraph(self):
        graph = graph_from_edges({(1, 2), (2, 3), (3, 4), (4, 1)})
        sufficient, pm = possible_mappings(graph)
        self.assertTrue(sufficient)
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
        sufficient, pm = possible_mappings(graph)
        self.assertTrue(sufficient)
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


if __name__ == '__main__':
    unittest.main()
