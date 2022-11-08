# discussion 4 CS61A
# Q1  Count stair ways
def count_stair_ways(n):
    """Return the number of ways to climb up a flight of n stairs,
    moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


# Q2 count K
def count_k(n, k):
    """Count the number of paths up a flight n stairs
    when taking up to and including k steps at a step
    >>> count_k(3,3)
    4
    >>> count_k(10,3)
    274
    >>> count_k(4,4)
    8
    >>> count_k(300,1)
    1
    """
    # one way
    # if k == 1 or n == 1:
    #     return 1
    # elif n ==0:
    #     return 1
    # else:
    #     with_k = count_k(n-k, k)
    #     without_k = count_k(n, k-1)
    #     return with_k + without_k
    # another way
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n == 1 or k == 1:
        return 1
    else:
        i, total = 1, 0
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total


# Q3 WWWPD Lists
# Q4 Even weighted
def even_weighted(s):
    """Return a new list that keeps only the even-indexed elements of s and
    multiplies them by their corresponding index
    >>> x = [1,2,3,4,5,6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

# Q5 Max Product
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s
    >>> max_product([10,3,1,9,2])
    90
    >>> max_product([5,10,5,10,5])
    123
    >>> max_product([])
    1
    """
    if s is None:
        return 1
    else:
        return max(max_product(s[:1]), s[0]*max_product(s[2:]))
