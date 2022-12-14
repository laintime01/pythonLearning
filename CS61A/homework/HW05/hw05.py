# homework 05
# Q1 Merge
def merge(a, b):
    """
        >>> def sequence(start, step):
        ...     while True:
        ...         yield start
        ...         start += step
        >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
        >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
        >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
        >>> [next(result) for _ in range(10)]
        [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
        """
    i, j = next(a), next(b)
    while True:
        if i == j:
            yield i
            i, j = next(a), next(b)
        elif i > j:
            yield j
            j = next(b)
        else:
            yield i
            i = next(a)


# Q2 Generate Permutations
def gen_perms(seq):
    """Generates all permutations of the given sequence.
    Each permutation is a list of the elements
    >>> sorted(gen_perms([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(gen_perms('ab'))
    [['a', 'b'], ['b', 'a']]
    """
    if not seq:
        yield []
    else:
        for p in gen_perms(seq[1:]):
            for i in range(len(seq)):
                yield p[:i] + [seq[0]] + p[i:]


# Q3 Yield Paths
from CS61A.classnote.treeAbstraction import *


def yield_paths(t, value):
    """Yield all possible paths from the root of t to  a node with the label
    value as a list.
    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> t2 = tree(0, [tree(2, [t1])])
    >>> path_to_2 = yield_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if label(t) == value:
        yield [label(t)]
    for b in branches(t):
        for path in yield_paths(b, value):
            yield [label(t)] + path
