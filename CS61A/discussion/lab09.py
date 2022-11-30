# Q1 Subsequences
def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list
    >>> n1 = [[], [1,2], [3]]
    >>> insert_into_all(0, n1)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + lst[:] for lst in nested_list]


def subseqs(s):
    """Return a nested list of all subsequences of S
    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if not s:
        return [[]]
    else:
        subset = subseqs(s[1:])
        return insert_into_all(s[0], subset) + subset


# Q2 Non-Decreasing subsequences
def non_sub(s):
    """Return a nested list of all subsequences of S that
    elements are non-decreasing
    >>> seqs = non_sub([1,3,2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_sub([])
    [[]]
    """

    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])
            b = subseq_helper(s[1:], prev)
            return insert_into_all(s[0], a) + b

    return subseq_helper(s, 0)


# Q3 number of trees
def num_trees(n):
    """return number of trees
    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429
    """
    if n == 1:
        return 1
    return sum(num_trees(k) * num_trees(n - k) for k in range(1, n))
