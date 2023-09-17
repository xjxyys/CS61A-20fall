def range_link(start, end):
    """Return a linked list of integers from start to end
    >>> range_link(1, 3)
    Link(1, Link(2, Link(3)))
    """

def map_link(f, s):
    """Return a Link that contains f(x) for each element x in s.
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
def filter_link(f, s):
    """Return a Link contains only elements x in s for which f(x) is a true value.
    >>> s = fliter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """