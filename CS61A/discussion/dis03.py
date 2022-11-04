# Q1 recursive multiplication
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion"""
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


# Q4 Is Prime
def is_prime(n):
    """ Returns True if n is a prime number and False otherwise"""

    def f(x):
        if x == n:
            return True
        elif n % x == 0:
            return False
        return f(x + 1)

    return f(2)


# test
print(is_prime(2))
print(is_prime(12))
print(is_prime(51))


# Q5 Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements"""
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)


print("------Q5--------")
hailstone(10)


# Q6 Merge Numbers


def merge(n1, n2):
    """ Merge two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
