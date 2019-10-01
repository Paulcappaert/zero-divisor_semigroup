from groupoid import Groupoid
import unittest


class TestGroupoid(unittest.TestCase):

    def setUp(self):
        self.s = Groupoid({'a', 'b', 'c'})

    def test_correctMap(self):
        self.s.upd('a', 'b', 'c')
        self.assertEqual(self.s.get('a', 'b'), 'c')

    def test_correctMap_square(self):
        self.s.upd('a', 'a', 'c')
        self.assertEqual(self.s.get('a', 'a'), 'c')

    def test_correctMap_und(self):
        self.s.upd('a', 'b', 'c')
        with self.assertRaises(ValueError):
            self.s.get('b', 'a')


class TestCommutativeGroupoid(unittest.TestCase):

    def setUp(self):
        self.s = Groupoid({'a', 'b', 'c'}, commutative=True)

    def test_correctProduct(self):
        self.s.upd('a', 'b', 'c')
        self.assertEqual(self.s.get('a', 'b'), 'c')
        self.assertEqual(self.s.get('b', 'a'), 'c')

    def test_correctProduct_square(self):
        self.s.upd('a', 'a', 'c')
        self.assertEqual(self.s.get('a', 'a'), 'c')

    def test_correctProduct_und(self):
        self.s.upd('a', 'a', 'c')
        with self.assertRaises(ValueError):
            self.assertEqual(self.s.get('a', 'b'), 'c')


if __name__ == '__main__':
    unittest.main()
