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
