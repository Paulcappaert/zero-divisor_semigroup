import time
from zdg import ZeroDivisorGraph as ZDG

graph = ZDG(
    (1, 2),
    (2, 3),
    (3, 1),
    (1, 4),
    (2, 5),
    (3, 6),
    (1, 7),
    (2, 7),
    (3, 8),
    (7, 8)
)

start = time.time()
semigroups = graph.get_semigroups()
print(len(semigroups))
end = time.time()
seconds = (end - start)
print(seconds)
