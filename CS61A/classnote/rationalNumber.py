# Constructor and selectors
def rational(n, d):
    """Construct a rational number x that represents n/d."""
    return [n ,d]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def mul_rational(x, y):
    """Multiply rational numbers x and y"""
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def print_rational(x):
    """print rational x"""
    print(numer(x), "/", denom(x))


x, y = rational(1, 2), rational(3, 8)
print(x)
print_rational(mul_rational(x, y))
