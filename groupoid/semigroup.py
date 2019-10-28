from groupoid.util.mod_math import ModularCounter

def inverse_set(a, b, pm, elements):
    '''
    returns: set of values z such that az = b is a possible mapping
    '''
    inv = set()
    for z in elements:
        if b in pm[frozenset({a, z})]:
            inv.add(z)
    return inv

def get_assoc_maps(pm, elements):
    '''
    parameter: dict of possible mappings for a groupoid
    returns: dict of possible associative mappings
             None if there is no associative mappings
    '''
    for _ in range(len(pm)):
        for a in elements:
            for b in elements:
                for c in elements:
                    ab = pm[frozenset({a, b})]
                    bc = pm[frozenset({b, c})]
                    prod1 = set()
                    for p in ab:
                        prod1.update(pm[frozenset({p, c})])
                    prod2 = set()
                    for p in bc:
                        prod2.update(pm[frozenset({p, a})])
                    products = prod1.intersection(prod2)

                    ab_vals = set()
                    for p in products:
                        ab_vals.update(inverse_set(c, p, pm, elements))

                    bc_vals = set()
                    for p in products:
                        bc_vals.update(inverse_set(a, p, pm, elements))

                    pm[frozenset({a, b})].intersection_update(ab_vals)
                    pm[frozenset({b, c})].intersection_update(bc_vals)



def get_semigroups(possible_mappings, groupoid):
    '''
    parameters:
        groupoid with an incomplete mappings
        dictionary of elements of the groupoid to sets of possible mappings for those elements
    returns: a list of groupoids copied from the passed groupoid and completed with
        mappings from the possible_mappings parameter
    '''
    get_assoc_maps(possible_mappings, groupoid.elements)

    num_possibilites = 1
    mods = []
    ordered_mappings = {}
    ordered_keys = tuple(possible_mappings.keys())

    for key in ordered_keys:
        ordered_mappings[key] = tuple(possible_mappings[key])
        n = len(possible_mappings[key])
        mods.append(n)
        num_possibilites *= n

    counter = ModularCounter(mods, ordered_keys)

    print(num_possibilites)

    semigroups = set()
    for i in range(num_possibilites):

        for key in ordered_mappings:
            c = ordered_mappings[key][counter.get_count(key)]
            if len(key) == 2:
                a, b = key
                groupoid.upd(a, b, c)
            else:
                a, = key
                groupoid.upd(a, a, c)

        if groupoid.is_assoc():
            semigroups.add(groupoid.copy())

        counter.tick()

    return semigroups
