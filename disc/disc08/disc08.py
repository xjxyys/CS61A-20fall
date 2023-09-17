class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
            return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'   

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    sum = 0
    while lnk is not Link.empty:
        sum += lnk.first
        lnk = lnk.rest
    return sum
    # if lnk == Link.empty:
    #     return 0
    # return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_rest_lnks = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_rest_lnks))

def multiply_lnks_literation(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code

def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 != 0:
        t.label += 1
    for b in t.branches:
        make_even(b)

def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label = t.label ** 2
    for b in t.branches:
        square_tree(b)

def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    # another solution
    # for b in t.branches:
    #     branch_path = [[t.label] + path for path in find_paths(b, entry)]
    #     paths.extend(branch_path)
    return paths

def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    combined_branches = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined_branches)

def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    if t == Tree.empty:
        return t
    branches = []
    for b in t.branches:
        next_braches = [alt_tree_map(b, map_fn) for b in t.branches]
        branches.append(Tree(b.label, next_braches))
    return Tree(map_fn(t.label), branches)

def alt_tree_maop(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_maop(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t, depth):
        if depth % 2 == 0:
            label = map_fn(t.label)
        else:
            label = t.label
        branches = [helper(b, depth + 1) for b in t.branches]
        return Tree(label, branches)
    return helper(t, 0)