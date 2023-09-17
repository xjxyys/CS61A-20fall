def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif x > y:
        return [[]]
    else:
        # a = [lst.insert(0, x) for lst in paths(x + 1, y)]
        # b = [lst.insert(0, x) for lst in paths(x * 2, y)]
        # return a + b
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + subpath for subpath in a + b]
    
def merge(s1, s2):
    """ Merges two sorted lists """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

def mergesort(seq):
    """ Mergesort algorithm """
    if len(seq) < 2:
        return seq
    else:
        mid = len(seq) // 2
        left = mergesort(seq[:mid])
        right = mergesort(seq[mid:])
        return merge(left, right)

def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    if n <= 0 and tree.is_leaf():
        return [Link(tree.label)]
    else:
        paths = []
        for b in tree.branches:
            for path in long_paths(b, n - 1):
                paths.append(Link(tree.label, path))
        return paths

def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...             Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    # levels represents the nodes at each level
    levels = []
    x = [t]
    while x:
        levels.append([t.label for t in x])
        # sum is used to make sure we get a list of trees not a list of branches
        x = sum([t.branches for t in x], [])
    return max(levels, key=len)

def bake(banana, bread):
    banana.append(bread.append(1)) # This line is Multiple Choice
    # Select all correct answers for the blank above
    # A. banana.append(bread.append(1))
    # B. bread.append(banana.append(1))
    # C. banana.extend([bread.extend([1])])
    # D. bread.extend([banana.extend([1])])
    bread += banana[: (len(banana) - 1)]
    banana.append(bread[bread[1]])
    return banana, bread

s = [1]
banana, bread = bake(s, [7, 2, s])


def amon(g):
    n = 0
    def u(s):
        nonlocal n
        f = lambda x: x + g.pop() + n
        n += 1
        return f(s)
    return u
g = [1, 2, 3]
skeld = amon(g)
pink = skeld(1)
purple = skeld(2)

class Emotion(object):
    num = 0
    def __init__(self):
        Emotion.num += 1
        self.power = 5
    def feeling(self, other):
        if self.power > other.power:
            self.catchphrase()
            other.catchphrase()
        elif self.power < other.power:
            other.catchphrase()
            self.catchphrase()
        else:
            print("Together")
class Joy(Emotion):
    def catchphrase(self):
        print("Think positive thoughts")

class Sadness(Emotion):
    def __init__(self, name, level):
        self.level = level
        Emotion.__init__(self, name)

    def catchphrase(self):
        print("I'm positive you will get lost")

def remove_duplicates(lnk):
    # the lnk is sorted
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    elif lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
    else:
        remove_duplicates(lnk.rest)

# Another version
def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    while lnk is not Link.empty and lnk.rest is not Link.empty:
        if lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
        else:
            lnk = lnk.rest


# 6 Generators
def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in
    ... zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        yield g
        # g = lambda x: f(g(x))是错误的，因为lambda表达式是在运行时才会去捕获g的值，但是g的值被定义成了自己，所以会陷入死循环
        # 下面的函数在定义时就会捕获g的值，所以不会陷入死循环
        g = (lambda g: lambda x: f(g(x)))(g)

from operator import add, mul
def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    total = next(it)
    yield total
    for ele in it:
        total = f(total, ele)
        yield total