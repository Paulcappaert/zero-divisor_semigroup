from groupoid import Groupoid as groid
from semigroup import get_semigroups


class ZeroDivisorGraph():

    def __init__(self, *edges, zero=0):
        self.graph = graph_from_edges(edges)
        self.zero = zero

    def is_sufficient(self):
        '''
        returns: true if the graph meets the sufficient conditions to be a zero divisor graph
        but still may not be a zero divisor graph
        '''
        mappings = possible_mappings(self.graph)
        if mappings:
            return True
        return False

    def get_semigroups(self):
        '''
        returns: a list of Groupoid objects that match the zero divisor graph and are associative
        '''
        return get_graph_semigroups(self.graph, zero=self.zero)

    def poss_maps_string(self):
        '''
        returns: a string with the possible mappings of the semigroup implied by the graph
        '''
        poss_maps = possible_mappings(self.graph)
        ret_val = ''
        for key in poss_maps:
            if len(key) == 1:
                a, = key
                ret_val += f'{a}      -> {poss_maps[key].union({self.zero})}\n'
            else:
                a, b = key
                ret_val += f'{a}, {b} -> {poss_maps[key]}\n'
        return ret_val

    def num_poss_maps(self):
        '''
        returns: the number of possible semigroups implied by the graph
        note: includes isomorphic semigroups
        '''
        poss_maps = possible_mappings(self.graph)
        num = 1
        for key in poss_maps:
            num *= len(poss_maps[key])
        return num



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
                product = frozenset({a, b})
                mappings[product] = set()
                hood = graph[a].union(graph[b])
                for z in graph:
                    if hood.issubset(graph[z].union({z})):
                        mappings[product].add(z)
                if len(mappings[product]) == 0:
                    print(product)
                    return None

        redundant.add(a)

    return mappings


def get_graph_semigroups(graph, zero=0):
    # returns a set of all possible semigroups for the given
    # zero divisor graph
    g = groid(set(graph).union({zero}), commutative=True, zero=zero)

    for a, adj_set in graph.items():
        for b in adj_set:
            g.upd(a, b, zero)

    mappings = possible_mappings(graph)

    if mappings:
        for key in mappings:
            if len(key) == 1:
                mappings[key].add(zero)

        return get_semigroups(mappings, g)
    else:
        return None
