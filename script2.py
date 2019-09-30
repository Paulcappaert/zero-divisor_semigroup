import time
from zero_divisor_graph import (graph_from_edges,
                                get_semigroup,
                                possible_mappings)
from groupoid import print_caley_table

graph = graph_from_edges([
    ('a', 'x1'),
    ('a', 'x2'),
    ('b', 'y1'),
    ('b', 'y2'),
    ('a', 'b'),
    ('x1', 'y1'),
    ('x1', 'y2'),
    ('x2', 'y1'),
    ('x2', 'y2'),
    ('x1', 'x2'),
    ('y1', 'y2'),
    ('x1', 'c1'),
    ('x2', 'c2'),
    ('y1', 'd1'),
    ('y2', 'd2'),
])

start = time.time()
s = get_semigroup(graph, 'z', squares_can_be_zero=False)
print_caley_table(s)
end = time.time()
minutes = (end - start) / 60
print(minutes)
