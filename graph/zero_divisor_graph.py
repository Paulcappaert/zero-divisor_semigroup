from groupoid.semigroup import get_semigroups
from groupoid.groupoid import Groupoid as groid

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
    '''
    returns:
        1. True if the graph is sufficient to be a zero divisor graph, false otherwise
        2. Dict: The possible mappings if the graph is sufficient, otherwise,
        a single key 'bad' with the insufficient product its item
    '''
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
                    return False, product

        redundant.add(a)

    return True, mappings

def get_graph_semigroups(graph, zero=0):
    # returns a set of all possible semigroups for the given
    # zero divisor graph
    g = groid(set(graph).union({zero}), commutative=True, zero=zero)

    sufficient, mappings = possible_mappings(graph)

    for a, adj_set in graph.items():
        for b in adj_set:
            g.upd(a, b, zero)
            mappings[frozenset({a, b})] = {zero}

    for a in g.elements:
        mappings[frozenset({a, zero})] = {zero}

    if sufficient:
        for key in mappings:
            if len(key) == 1:
                mappings[key].add(zero)

        return get_semigroups(mappings, g)
    else:
        return None
