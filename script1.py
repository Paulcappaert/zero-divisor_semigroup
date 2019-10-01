import time
from zero_divisor_graph import ZeroDivisorGraph as ZDG

graph = ZDG(
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'e'),
    ('b', 'd'),
    ('c', 'e'),
    ('c', 'd'),
    ('f', 'e'),
    ('g', 'd'),
    ('d', 'e'),
)

start = time.time()
semigroups = graph.get_semigroups()
print(len(semigroups))
end = time.time()
seconds = (end - start)
print(seconds)
