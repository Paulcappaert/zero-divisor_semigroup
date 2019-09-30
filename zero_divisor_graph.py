from groupoid import CommutativeGroupoid as groupoid
from groupoid import is_assoc


class MixedCounter():

    def __init__(self, mods):
        self.mods = tuple(mods)
        self.nums = [0] * len(self.mods)

    def tick(self):
        carry = 1
        i = 0
        while carry > 0:
            self.nums[i] += 1
            if self.nums[i] % self.mods[i] == 0:
                self.nums[i] = 0
                carry = 1
            else:
                carry = 0
            i += 1
            if i == len(self.mods):
                i = 0
                carry = 0

    def get_val(self, i):
        return self.nums[i]


def graph_from_edges(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = {b}
        if b in graph:
            graph[b].add(a)
        else:
            graph[b] = {a}

    return graph


def possible_mappings(graph):
    mappings = {}
    redundant = set()
    for a in graph:
        for b in graph:
            if b not in redundant and b not in graph[a]:
                edge = frozenset({a, b})
                mappings[edge] = set()
                hood = graph[a].union(graph[b])
                for z in graph:
                    if hood.issubset(graph[z].union({z})):
                        mappings[edge].add(z)
                if len(mappings[edge]) == 0:
                    print(edge)
                    return None

        redundant.add(a)

    return mappings


def get_semigroup(graph, zero, squares_can_be_zero=True):
    elements = list(graph)
    elements.append(zero)
    grpd = groupoid(elements)
    grpd.set_zero(zero)

    for node1, adj_set in graph.items():
        for node2 in adj_set:
            grpd.upd(node1, node2, zero)

    mappings = possible_mappings(graph)

    if squares_can_be_zero:
        for key in mappings:
            if len(key) == 1:
                mappings[key].add(zero)

    num_possibilites = 1
    keys = tuple(mappings)
    mods = []
    ordered_mappings = {}
    for key in keys:
        ordered_mappings[key] = tuple(mappings[key])
        n = len(mappings[key])
        mods.append(n)
        num_possibilites *= n
    counter = MixedCounter(mods)

    print(num_possibilites)

    for i in range(num_possibilites):
        for i, key in enumerate(keys):
            if len(key) == 2:
                a, b = key
            else:
                [a] = key
                b = a
            c = ordered_mappings[key][counter.get_val(i)]
            grpd.upd(a, b, c)

        if is_assoc(grpd):
            return grpd

        counter.tick()

    return None
