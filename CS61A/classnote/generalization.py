""" Generalization """


def summation(n, term):
    """ Sum the n natural numbers in way of term """
    k, total = 1, 0
    while k <= n:
        k, total = k + 1, total + term(k)
    return total


def cube(n):
    return pow(n, 3)

print(cube(3))
print(summation(3, cube))
