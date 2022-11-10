# discussion 5
# Q1 Map, filter, reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list
    >>> my_map(lambda x:x*x, [1,2,3])
    [1, 4, 9]
    """
    return [fn(s) for s in seq]


def my_filter(prod, seq):
    """Keeps elements in seq only if they satisfy pred
    >>> my_filter(lambda x:x % 2 == 0, [1,2,3,4])
    [2, 4]
    """
    return [s for s in seq if prod(s)]


def my_reduce(combiner, seq):
    """ Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x+y, [1,2,3,4])
    10
    >>> my_reduce(lambda x, y: x*y, [1,2,3,4])
    24
    >>> my_reduce(lambda x,y:x+2*y, [1,2,3])
    11
    """
    total = seq[0]
    for s in seq[1:]:
        total = combiner(total, s)
    return total


# Q2 count palindromes
def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings
    L(ignoring case).
    >>> count_palindromes(("Acme", "madam", "Pivot", "pip"))
    2
    >>> count_palindromes(["101", "rAcecar", "much", "wow"])
    3
    """
    pred = lambda x: x.lower() == x[::-1].lower()
    return len(my_filter(pred, L))


# Data Abstraction
from CS61A.classnote.treeAbstraction import *


# Q4
def height(t):
    """Return the height of a tree
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    if not branches(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])


# Q5 Maximum Path sum
def max_path_sum(t):
    """Return the maximum path sum of the tree
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]),tree(10)])
    >>> max_path_sum(t)
    11
    """
    so_far = label(t)
    if is_leaf(t):
        return so_far
    else:
        return label(t) + max(max_path_sum(b) for b in branches(t))


# Q6 Find Path
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
