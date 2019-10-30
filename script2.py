from zdg import ZeroDivisorGraph

g = ZeroDivisorGraph(
('a', 'b'),
('a', 'x1'),
('a', 'x2'),
('b', 'y1'),
('b', 'y2'),
('x2', 'x1'),
('y1', 'x1'),
('y2', 'x1'),
('y1', 'x2'),
('y2', 'x2'),
('y1', 'y2'),
('c1', 'x1'),
('c2', 'x2'),
('d1', 'y1'),
('d2', 'y2')
)

print(g.poss_maps_string())
print(g.num_poss_maps())

semigroups = g.get_semigroups()
print(len(semigroups))
