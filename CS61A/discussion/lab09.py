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
    if s is []:
        return [[]]
    else:
        subset = subseqs(s[1:])
        return insert_into_all(s[0], subset) + subset
