from graph.zero_divisor_graph import (
    graph_from_edges,
    possible_mappings,
    get_graph_semigroups
)


class ZeroDivisorGraph():

    def __init__(self, *edges, zero=0):
        self.graph = graph_from_edges(edges)
        self.zero = zero

    def get_semigroups(self):
        '''
        returns: a list of Groupoid objects that match the zero divisor graph and are associative
        '''
        return get_graph_semigroups(self.graph, zero=self.zero)

    def poss_maps_string(self):
        '''
        returns: a string with the possible mappings of the semigroup implied by the graph
        '''
        sufficient, poss_maps = possible_mappings(self.graph)
        ret_val = ''
        if sufficient:
            for key in poss_maps:
                if len(key) == 1:
                    a, = key
                    ret_val += f'{a}    -> {poss_maps[key].union({self.zero})}\n'
                else:
                    a, b = key
                    ret_val += f'{a}, {b} -> {poss_maps[key]}\n'
        else:
            a, b = poss_maps
            ret_val = f'bad product: {a}, {b}'

        return ret_val

    def num_poss_maps(self):
        '''
        returns: the number of possible semigroups implied by the graph
        note: includes isomorphic semigroups
        '''
        sufficient, poss_maps = possible_mappings(self.graph)
        if sufficient:
            num = 1
            for key in poss_maps:
                num *= len(poss_maps[key])
            return num
        else:
            return 0
