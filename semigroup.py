from mod_math import ModularCounter

def get_assoc_products(groupoid):
    '''
    parameter: groupoid with incomplete mapping
    returns: dict of possible mappings that are implied if the groupoid is a semigroup
    '''
    pass


def get_semigroups(possible_mappings, groupoid):
    '''
    parameters:
        groupoid with an incomplete mappings
        dictionary of elements of the groupoid to sets of possible mappings for those elements
    returns: a list of groupoids copied from the passed groupoid and completed with
        mappings from the possible_mappings parameter
    '''
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
