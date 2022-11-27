def raise_exp(x):
    if isinstance(x, str):
        raise TypeError('Only take numbers')
    else:
        return x * x


def try_statement():
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        print('handling a ', type(e))


try_statement()


def reduce_alt(f, s, n):
    """
    >>> reduce_alt(lambda x,y: x*y, [2,4,8], 1)
    64
    """
    for i in s:
        n = f(i, n)
    return n


def reduce_alt_again(fa, sa, na):
    """
    >>> reduce_alt(lambda x,y: x*y, [2,4,8], 1)
    64
    """
    if not sa:
        return na
    else:
        first, rest = sa[0], sa[1:]
        return reduce_alt_again(fa, rest, fa(first, na))
