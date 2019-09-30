import time
from zero_divisor_graph import graph_from_edges, get_semigroup
from groupoid import print_caley_table

graph = graph_from_edges([
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'e'),
    ('b', 'd'),
    ('c', 'e'),
    ('c', 'd'),
    ('f', 'e'),
    ('g', 'd'),
    ('d', 'e'),
])

start = time.time()
s = get_semigroup(graph, 'z')
print_caley_table(s)
end = time.time()
seconds = (end - start)
print(seconds)
