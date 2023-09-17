'''one solutiong:
    def cycle1(n):
        if n == 0:
            return lambda x: x
        elif n == 1:
            return lambda x: f1(x)
        elif n == 2:
            return lambda x: f2(f1(x))
        elif n == 3:
            return lambda x: f3(f2(f1(x)))
        else:
            return lambda x: cycle1(n-3)(f3(f2(f1(x))))
    return cycle1
'''  