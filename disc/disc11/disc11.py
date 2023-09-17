class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, rest):
        self.first = first
        if not scheme_valid_cdrp(rest):
            raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(rest))
        self.rest = rest
    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.
        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
        "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))
    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)
    
class nil:
    """Represents the special empty pair nil in Scheme."""
    def map(self, fn):
        return nil
    def __getitem__(self, i):
        raise IndexError('Index out of range')
    def __repr__(self):
        return 'nil'
    
nil = nil() # this hides the nil class *forever*

Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))

def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and':
            return eval_and(exp.rest)
        else:
            return calc_apply(calc_eval(exp.first), list(exp.rest.map(calc_eval)))
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else:
        return exp
    
def eval_and(operands):
    """Evaluates a sequence of operands using short-circuiting semantics."""
    if operands is nil:
        return True
    while operands is not nil:
        val = calc_eval(operands.first)
        if val is False:
            return False
        operands = operands.rest
    return val