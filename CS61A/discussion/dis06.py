# Q1 mutability
def muted_y():
    """
    >>> muted_y()
    [1, 2, 3, 4]
    """
    x = [1, 2, 3]
    y = x
    x += [4]
    print(y)


def not_muted():
    """
    >>> not_muted()
    [1, 2, 3]
    """
    x = [1, 2, 3]
    y = x
    x = x + [4]
    print(y)


# Q2
def add_this_many(x, el, s):
    """Adds el to the end of s the number of times x occurs in s
    >>> s = [1, 2,4,2,1]
    >>> add_this_many(1,5,s)
    [1, 2, 4, 2, 1, 5, 5]
    """
    s.extend([el] * s.count(x))
    return s
