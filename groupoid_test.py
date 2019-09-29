from groupoid import Groupoid as grpd
from groupoid import assign_mapping
import unittest


class TestGroupoid(unittest.TestCase):

    def setUp(self):
        self.s = grpd({'a', 'b', 'c'})

    def test_correctMap(self):
        self.s.upd_map(('a', 'b'), 'c')
        self.assertEqual(self.s.get_map(('a', 'b')), 'c')

    def test_correctMap_square(self):
        self.s.upd_map(('a', 'a'), 'c')
        self.assertEqual(self.s.get_map(('a', 'a')), 'c')

    def test_correctMap_und(self):
        self.s.upd_map(('a', 'b'), 'c')
        with self.assertRaises(ValueError):
            self.s.get_map(('b', 'a'))

    def test_getNecessary_zeroRels(self):
        self.assertEqual(len(self.s.get_needed_maps()), 9)

    def test_getNecessary_oneRel(self):
        self.s.upd_map(('a', 'a'), 'c')
        self.assertEqual(len(self.s.get_needed_maps()), 8)

    def test_getNecessary_square(self):
        g = grpd({0, 1, 2, 3, 4}, com=True)
        g.set_zero(0)
        g.upd_map((1, 2), 0)
        g.upd_map((2, 3), 0)
        g.upd_map((3, 4), 0)
        g.upd_map((4, 1), 0)
        needed = g.get_needed_maps()
        self.assertEqual(len(needed), 6)
        self.assertTrue((1, 1) in needed)

    def test_getNecessary_allRels(self):
        self.s.upd_map(('a', 'a'), 'c')
        self.s.upd_map(('a', 'b'), 'c')
        self.s.upd_map(('a', 'c'), 'c')
        self.s.upd_map(('b', 'a'), 'c')
        self.s.upd_map(('b', 'b'), 'c')
        self.s.upd_map(('b', 'c'), 'c')
        self.s.upd_map(('c', 'a'), 'c')
        self.s.upd_map(('c', 'b'), 'c')
        self.assertTrue(('c', 'c') in self.s.get_needed_maps())

    def test_copy(self):
        self.s.upd_map(('a', 'b'), 'c')
        self.s.upd_map(('b', 'c'), 'c')
        s1 = self.s.copy()
        s1.upd_map(('b', 'c'), 'a')
        self.assertEqual(self.s.get_map(('b', 'c')), 'c')
        self.assertEqual(s1.get_map(('b', 'c')), 'a')


class TestCommutativeGroupoid(unittest.TestCase):

    def setUp(self):
        self.s = grpd({'a', 'b', 'c'}, com=True)

    def test_correctProduct(self):
        self.s.upd_map(('a', 'b'), 'c')
        self.assertEqual(self.s.get_map(('a', 'b')), 'c')
        self.assertEqual(self.s.get_map(('b', 'a')), 'c')

    def test_correctProduct_square(self):
        self.s.upd_map(('a', 'a'), 'c')
        self.assertEqual(self.s.get_map(('a', 'a')), 'c')

    def test_correctProduct_und(self):
        self.s.upd_map(('a', 'a'), 'c')
        with self.assertRaises(ValueError):
            self.assertEqual(self.s.get_map(('a', 'b')), 'c')

    def test_getNecessary_zeroRels(self):
        self.assertEqual(len(self.s.get_needed_maps()), 6)

    def test_getNecessary_oneRel(self):
        self.s.upd_map(('a', 'a'), 'c')
        self.assertEqual(len(self.s.get_needed_maps()), 5)

    def test_getNecessary_allRels(self):
        self.s.upd_map(('a', 'a'), 'c')
        self.s.upd_map(('a', 'b'), 'c')
        self.s.upd_map(('a', 'c'), 'c')
        self.s.upd_map(('b', 'b'), 'c')
        self.s.upd_map(('b', 'c'), 'c')
        self.assertTrue(('c', 'c') in self.s.get_needed_maps())


class TestAssignMapping(unittest.TestCase):

    def setUp(self):
        self.X = (1, 2, 3, 4, 5)
        self.Y = (1, 2, 3)
        self.n = (len(self.Y)) ** len(self.X)

    def test_getFirstSeed(self):
        mapping = assign_mapping(self.X, self.Y, 0)
        self.assertEqual(len(mapping), 5)
        self.assertEqual(mapping.get(1), 1)
        self.assertEqual(mapping.get(2), 1)
        self.assertEqual(mapping.get(3), 1)
        self.assertEqual(mapping.get(4), 1)
        self.assertEqual(mapping.get(5), 1)

    def test_getLastSeed(self):
        mapping = assign_mapping(self.X, self.Y, self.n - 1)
        self.assertEqual(len(mapping), 5)
        self.assertEqual(mapping.get(1), 3)
        self.assertEqual(mapping.get(2), 3)
        self.assertEqual(mapping.get(3), 3)
        self.assertEqual(mapping.get(4), 3)
        self.assertEqual(mapping.get(5), 3)

    def test_wrapMappingSeed(self):
        mapping = assign_mapping(self.X, self.Y, self.n)
        self.assertEqual(len(mapping), 5)
        self.assertEqual(mapping.get(1), 1)
        self.assertEqual(mapping.get(2), 1)
        self.assertEqual(mapping.get(3), 1)
        self.assertEqual(mapping.get(4), 1)
        self.assertEqual(mapping.get(5), 1)


if __name__ == '__main__':
    unittest.main()
