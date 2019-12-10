class Groupoid():
    '''
    An objec to represent a Groupoid
    A set of elements with a mapping from the cross product to the elements
    '''

    def __init__(self, elements, commutative=False, zero=None):
        self.elements = frozenset(elements)
        self.map = {}
        self.commutative = commutative
        if zero is not None:
            self.set_zero(zero)

    def caley_table(self):
        '''
        returns: stirng of the caley table representation of the groupoid
        raises: ValueError if groupoid mapping is incomplete
        '''
        ordered_elements = list(self.elements)
        ordered_elements.sort()
        ret_val = '*|\t'
        for a in ordered_elements:
            ret_val += f'{a}|\t'
        ret_val += '\n'
        for a in ordered_elements:
            ret_val += str(a) + '|\t'
            for b in ordered_elements:
                product = self.get(a, b)
                ret_val += f'{product},\t'
            ret_val += '\n'
        return ret_val

    def upd(self, a, b, result):
        '''
        paramters: elements a, b and result such that a * b = result
        raises: ValueError if a, b or result is not an element of the groupoid
        '''
        if {a, b, result}.issubset(self.elements):
            if self.commutative:
                self.map[frozenset({a, b})] = result
            else:
                self.map[(a, b)] = result
        else:
            raise ValueError(f"invalid elements {a}, {b}, {result}")

    def has_map(self, a, b):
        '''
        parameters: a, b
        returns: true if a * b is defined in the map
        '''
        if self.commutative:
            return frozenset({a, b}) in self.map
        else:
            return (a, b) in self.map

    def get(self, a, b):
        '''
        parameters: a, b
        returns: the mapping of a * b
        raises: ValueError if a * b is not a defined mapping
        '''
        if self.commutative and frozenset({a, b}) in self.map:
            return self.map[frozenset({a, b})]
        elif not self.commutative and (a, b) in self.map:
            return self.map[(a, b)]
        else:
            raise ValueError(f'invalid product {a}, {b}')

    def set_zero(self, zero):
        '''
        parameters: zero, updates the mapping to make this the zero of the groupoid
        raises: ValueError if zero is not in the groupoid
        '''
        if self.commutative:
            for x in self.elements:
                self.map[frozenset({zero, x})] = zero
        else:
            for x in self.elements:
                self.map[(zero, x)] = zero
                self.map[(x, zero)] = zero

    def copy(self):
        '''
        returns: a copy of the semigroup with the same, elements and mapping
        '''
        g = Groupoid(self.elements, commutative=self.commutative)
        g.map = self.map.copy()
        return g


    def is_assoc(self):
        '''
        returns: true if the groupoid is associative
        raises: ValueError if the mapping is incomplete
        '''
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    val1 = self.get(self.get(a, b), c)
                    val2 = self.get(a, self.get(b, c))
                    if not val1 == val2:
                        return False
        return True
