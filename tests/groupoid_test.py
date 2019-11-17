from zdg.groupoid import Groupoid
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

    def test_set_zero(self):
        self.s.set_zero('a')
        self.assertEqual(self.s.get('a','a'), 'a')
        self.assertEqual(self.s.get('a','b'), 'a')
        self.assertEqual(self.s.get('b','a'), 'a')
        self.assertEqual(self.s.get('a','c'), 'a')
        self.assertEqual(self.s.get('c','a'), 'a')

    def test_is_assoc(self):
        pass

    def test_isnt_assoc(self):
        pass


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

    def test_set_zero(self):
        self.s.set_zero('a')
        self.assertEqual(self.s.get('a','a'), 'a')
        self.assertEqual(self.s.get('a','b'), 'a')
        self.assertEqual(self.s.get('b','a'), 'a')
        self.assertEqual(self.s.get('a','c'), 'a')
        self.assertEqual(self.s.get('c','a'), 'a')

    def test_is_assoc(self):
        pass

    def test_isnt_assoc(self):
        pass

if __name__ == '__main__':
    unittest.main()
