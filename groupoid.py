class Groupoid():
    # a set of elements over which there is a mapping from
    # the cross product of the elements to the elements
    def __init__(self, elements):
        self.elements = frozenset(elements)
        self.map = {}

    def upd(self, a, b, result):
        self.map[(a, b)] = result

    def get(self, a, b):
        return self.map[(a, b)]

    def set_zero(self, zero):
        for x in self.elements:
            self.map[(zero, x)] = zero
            self.map[(x, zero)] = zero


class CommutativeGroupoid():

    def __init__(self, elements):
        self.elements = frozenset(elements)
        self.map = {}

    def upd(self, a, b, result):
        self.map[frozenset({a, b})] = result

    def get(self, a, b):
        return self.map[frozenset({a, b})]

    def set_zero(self, zero):
        for x in self.elements:
            self.map[frozenset({zero, x})] = zero


def is_assoc(groupoid):
    for a in groupoid.elements:
        for b in groupoid.elements:
            for c in groupoid.elements:
                val1 = groupoid.get(groupoid.get(a, b), c)
                val2 = groupoid.get(a, groupoid.get(b, c))
                if not val1 == val2:
                    return False
    return True


def print_caley_table(groupoid):
    ordered_elements = list(groupoid.elements)
    ordered_elements.sort()
    for a in ordered_elements:
        print(f'{a}|\t', end='')
    print()
    for a in ordered_elements:
        for b in ordered_elements:
            product = groupoid.get(a, b)
            print(f'{product},\t', end='')
        print()
