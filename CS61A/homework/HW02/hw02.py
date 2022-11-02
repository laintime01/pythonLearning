# CS 61A homework 02
def add(x, y):
    return x + y


def square(x):
    return x * x


def triple(x):
    return 3 * x


def increment(x):
    return x + 1


def mul(x, y):
    return x * y


# Q1 Product
def product(n, term):
    """
    return the product of the first n terms in a sequence
    :param n: positive integer
    :param term: a function that takes one argument to produce the term
    :return:
    """
    # x = map(term, [i for i in range(1, n + 1)])
    # ans = 1
    # for j in list(x):
    #     ans = ans * j
    # return ans
    total, k = 1, 1
    while k <= n:
        total = total * term(k)
        k += 1
    print(total)
    return total


# test
product(5, square)
product(3, increment)
product(3, triple)


# Q2 Accumulate
def accumulate(combiner, base, n, term):
    """
    return the result of combining the first n terms in a sequence and base.
    the terms to be combined are term(1)..term(n), combiner is a two-argument
    commutative function.
    :param combiner:
    :param base:
    :param n:
    :param term:
    :return:
    """
    ans, k = base, 1
    while k <= n:
        ans = combiner(ans, term(k))
        k += 1
    return ans


def summation_using_accumulate(n, term):
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    return accumulate(mul, 0, n, term)


print(f"Q2 answer-> {accumulate(lambda x, y: x + y + 1, 2, 3, square)}")
print(accumulate(add, 11, 3, square))


# Q3 Make Repeater
def make_repeater(func, n):
    """
    return the function that computes the nth application of
    :param func:
    :param n:
    :return:
    """

    def repeat(x):
        k = 0
        while k < n:
            x = func(x)
            k += 1
        return x

    return repeat


def compose1(func1, func2):
    """
    return a function f such that f(x) = func1(func2(x))
    :param func1:
    :param func2:
    :return:
    """

    def f(x):
        return func1(func2(x))

    return f


# challenge
def make_c_repeater(n, func):
    """
    defining make_repeater using compose1 and accumulate function i a
    single one-line return statement
    :param n:
    :param func:
    :return:
    """
    return accumulate(compose1, lambda x: x, n, lambda k: func)


add_three = make_repeater(increment, 3)
triple_five = make_repeater(triple, 5)
print(add_three(5))
print(triple_five(1))


# Q4 Church numerals
def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """ church numeral 1: same as successor(zero)
    def successor(zero):
        return lambda f: lambda x: f(zero(f)(x))
    not matter what argument in zero is, it return a func like f(x) = x
    so zero(f)(x) ->f(x)
    def successor(zero):
        return lambda f:lambda x: f(x)
    change name
    def one(f):
        return lambda x: f(x)
    """
    return lambda x: f(x)


def two(f):
    """ church numeral 1: same as successor(successor(zero))
    successor(successor(zero)) = successor(one)   so
    def successor(one):
        return lambda f: lambda x: f(one(f)(x))
    from one(f) we can figure that one(f)(x) = f(x) so
    def successor(one):
        return lambda f: lambda x: f(f(x))
    change name
    def two(f):
        return lambda x: f(f(x))
    """
    return lambda x: f(f(x))


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    # church is using high order function 's argument recombination time to show int
    # lambda x: x+1 -> f(x) = x +1  0 is the init num of x
    return n(lambda x: x + 1)(0)


three = successor(two)
s = one(square)
print(s(2))

print(church_to_int(one))
print(church_to_int(two))
print(church_to_int(three))


def add_church(m, n):
    """ Return the church numeral for m+ n, for church numerals m and n
    >>> church_to_int(add_church(two, three))
    5
    """
    # m,n = one
    # return lambda f: lambda x: m(f)(x) + n(f)(x) means m+n f(f(...f(x)))
    # m +n = m(f)(n(f)(x)) = f(f(f..(f(n(f)(x)))))
    # so ->
    return lambda f: lambda x: m(f)(n(f)(x))


print(church_to_int(add_church(two, three)))


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.
        >>> four = successor(three)
        >>> church_to_int(mul_church(two, three))
        6
        >>> church_to_int(mul_church(three, four))
        12
        """
    # or return lambda f: lambda x: n(f)(x) * m(f)(x)
    # n * m = n(m(f))(x) = m(f)+m(f)+..n in total..m(f) = n(m(f))
    return lambda f: n(m(f))


print(church_to_int(mul_church(two, three)))


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.
        >>> church_to_int(pow_church(two, three))
        8
        >>> church_to_int(pow_church(three, two))
        9
        """
    # or m(f)(x) ** n(f)(x)
    # we need m ** n means n ge m ge m
    # n(m) ->n(m(m(f)))
    return n(m)


print(church_to_int(pow_church(three, two)))
