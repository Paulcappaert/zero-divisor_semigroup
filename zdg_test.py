import unittest
from zdg import ZeroDivisorGraph as ZDG

class ZeroDivisorGraphTestCase(unittest.TestCase):

    def test_triangle_two_horns(self):
        g = ZDG((1,2),(2,3),(3,1),(1,4),(2,5))
        s,*_ = g.get_semigroups()
        self.assertEqual(s.get(1, 5), 1)
        self.assertEqual(s.get(2, 4), 2)

    def test_triangle_three_horns(self):
        g = ZDG((1,2),(2,3),(3,1),(1,4),(2,5),(3,6))
        s = g.get_semigroups()
        self.assertEqual(len(s), 1)

    def test_square_one_horns(self):
        g = ZDG((1,2),(2,3),(3,4),(4,1),(1,5))
        s,*_ = g.get_semigroups()
        self.assertEqual(s.get(1, 3), 1)

    def test_square_two_horns(self):
        g = ZDG((1,2),(2,3),(3,4),(4,1),(1,5),(2,6))
        s = g.get_semigroups()
        self.assertEqual(len(s), 0)

    def test_bipartite_one_horn(self):
        g = ZDG((1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(5,6))
        s,*_ = g.get_semigroups()
        self.assertEqual(s.get(3,5),5)
        self.assertEqual(s.get(4,5),5)
        self.assertEqual(s.get(1,5),0)

if __name__ == '__main__':
    unittest.main()
