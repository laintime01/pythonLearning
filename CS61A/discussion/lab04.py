# lab4
# Recursion/Tree recursion
# Q1 squared virahanka fibonacci
def virfib_sq(n):
    print(n)
    if n <= 1:
        return n
    return (virfib_sq(n - 2) + virfib_sq(n - 1)) ** 2


def virfib_sq_while(n):
    if n <= 1:
        return n
    i, l = 2, [0, 1]
    while i <= n:
        l.append((l[i - 1] + l[i - 2]) ** 2)
        i += 1
    return l[n]


# Q2 summation
def summation(n, term):
    """Return the sum of numbers 1 through n(including n)
    with term applied to each number
    Implement using recursion
    >>> summation(5,lambda x:x*x*x)
    225
    >>> summation(9, lambda x:x+1)
    54
    >>> # Do not use while/for loops!
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
        return summation(n - 1, term) + term(n)


# Q3 Pascal's Triangle
def pascal(row, column):
    """Return the value of the item in Pascal's Triangle
    whose position is specified by row and column
    >>> pascal(0,0)
    1
    >>> pascal(3,2)
    3
    >>> pascal(4,2)
    6
    """
    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        top = pascal(row - 1, column)
        top_left = pascal(row - 1, column - 1)
    return top + top_left


# Q4 Insect Combinatorics
def paths(m, n):
    """Return the number of paths from one corner of an M by N grid to
    the opposite corner
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


# List Comprehensions
# Couple
def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i],t[i]]
    >>> a=[1,2,3]
    >>> b=[4,5,6]
    >>> couple(a,b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c=['c',6]
    >>> d=['s','1']
    >>> couple(c,d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    return list([s[i],t[i]] for i in range(len(s)))


# optional questions
# recursion
def double_eights(n):
    """Return whether or not n has two digits in row that
    are number 8
    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    """
    if n % 100 == 88:
        return True
    elif n < 100:
        return False
    else:
        return double_eights(n//10)


# List Comprehensions
# Q7 Coordinates