def inverse_cascade(n):
    def grow(n):
        if n <= 10:
            print(n)
        else:
            grow(n // 10)
            print(n)

    def shrink(n):
        if n <= 10:
            print(n)
        else:
            print(n)
            shrink(n // 10)

    grow(n)
    print(n)
    shrink(n)


inverse_cascade(1234)

# another way of inverse cascade


def inverse(n, digits=1):
    n = str(n)
    print(n[:digits])
    if digits < len(n):
        inverse(n, digits+1)
        print(n[:digits])


inverse(1234)


# fib in tree recursion way
from ucb import trace

@trace
def fib(n):
    """the computational process of fib evolves into a tree structure"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(3))