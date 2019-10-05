from zero_divisor_graph import ZeroDivisorGraph

g = ZeroDivisorGraph(
('a1','x1'),
('a1','y1'),
('a2','x2'),
('a2','y2'),
('a3','x3'),
('a3','y3'),
('a4','x4'),
('a4','y4'),
('x1','x2'),
('x1','x3'),
('x1','x4'),
('x2','x3'),
('x2','x4'),
('x3','x4'),
('x1','y2'),
('x1','y3'),
('x1','y4'),
('x2','y1'),
('x2','y3'),
('x2','y4'),
('x3','y1'),
('x3','y2'),
('x3','y4'),
('x4','y1'),
('x4','y2'),
('x4','y3'),
('y1','y2'),
('y1','y3'),
('y1','y4'),
('y2','y3'),
('y2','y4'),
('y3','y4')
)

print(g.poss_maps_string())
print(g.num_poss_maps())
