# CS 61A homework 02
def add(x,y):
    return x+y


def square(x):
    return x * x


def triple(x):
    return 3 * x


def increment(x):
    return x + 1

def mul(x,y):
    return x*y


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
    return accumulate(add,0,n,term)
def product_using_accumulate(n, term):
    return accumulate(mul,0,n,term)

print(f"Q2 answer-> {accumulate(lambda x, y: x + y + 1, 2, 3, square)}")
print(accumulate(add,11,3,square))

# Q3 Make Repeater

