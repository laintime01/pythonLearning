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


# Q5 Filter-Iter
def filter_iter(iterable, f):
    """yield elements of iterable for which f returns true
    >>> is_even = lambda x: x % 2 ==0
    >>> iterable = range(5)
    >>> list(filter_iter(iterable, is_even))
    [0, 2, 4]
    """
    yield from [element for element in iterable if f(element)]


# Q6
def is_prime(n):
    """Returns True if n is a prime number and False otherwise
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def checker(m):
        if m == n:
            return True
        elif n % m == 0:
            return False
        else:
            return checker(m + 1)

    return checker(2)


def primes_gen(n):
    """Generate primes in decreasing order
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)


from CS61A.classnote.treeAbstraction import *


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    if not branches(t):
        return label(t)
    flattened_branches = []
    for branch in branches(t):
        flattened_branches += preorder(branch)
    return [label(t)] + flattened_branches


from functools import reduce


def add(x, y):
    return x + y


def pre_order_alt(t):
    return reduce(add, [pre_order_alt(branch) for branch in branches(t)], [label(t)])
