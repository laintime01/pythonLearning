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