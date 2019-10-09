from semigroup import get_semigroups
from groupoid import Groupoid as groid
import unittest


class TestGetSemigroups(unittest.TestCase):

    def test_Three(self):
        g = groid({1, 2, 3}, commutative=True, zero=1)
        mappings = {
            frozenset({2, 3}): {2, 3},
            frozenset({2}): {2, 3},
            frozenset({3}): {2, 3}
        }
        semigroups = get_semigroups(mappings, g)
        self.assertIsNotNone(semigroups)
        for s in semigroups:
            self.assertIn(s.get(2, 3), {2, 3})

    def test_Four(self):
        g = groid({0, 1, 2, 3}, commutative=True, zero=0)
        g.upd(1, 2, 0)
        g.upd(2, 3, 0)
        mappings = {
            frozenset({1, 3}): {1, 2, 3},
            frozenset({1}): {1, 2, 3, 0},
            frozenset({2}): {1, 2, 3, 0},
            frozenset({3}): {1, 2, 3, 0},
        }

        semigroups = get_semigroups(mappings, g)
        self.assertIsNotNone(semigroups)
        for s in semigroups:
            self.assertIn(s.get(1, 3), {1, 2, 3})


if __name__ == '__main__':
    unittest.main()
