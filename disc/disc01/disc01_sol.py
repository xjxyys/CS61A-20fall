def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if (temp < 60) or raining:
        return True
    else:
        return False
#   return temp < 60 or raining

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    else:
        k = 2
        while k < n:
            if n % k == 0:
                return False
            k += 1
        return True
