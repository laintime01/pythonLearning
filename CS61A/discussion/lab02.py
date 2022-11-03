# Q2 wwpd high order function
def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)

    return odd


steven = lambda x: x
stewart = even(steven)
print(stewart(61))
print(stewart(-4))


def cake():
    print("beets")

    def pie():
        print('sweet')
        return 'cake'

    return pie


chocolate = cake()
chocolate
chocolate()
more_chocolate = chocolate()
more_chocolate
more_cake = cake
more_cake
print('--------')


def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y


print(snake(10, 20))
print(snake(10, 20)())
cake = 'cake'
print(snake(10, 20))

print("-----------Q3-------------")
# Q3 lambdas and currying
from operator import add, mul, mod


def lambda_curry2(func):
    """ Return a curried version of a two-argument function FUNC"""
    return lambda y: lambda x: func(x, y)


curried_add = lambda_curry2(add)
add_three = curried_add(3)
print(add_three(6))


# Q4 count van count
def count_coud(condition):
    """Return a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function condition
    >>> coun_factors = count_coud(lambda n,i: n%i ==0)
    >>> coun_factors(4) # 1,2,4
    3
    >>> coun_factors(12) # 1,2,3,4,6,12
    6
    """

    def func(x):
        i = 1
        count = 0
        while i <= x:
            if condition(x, i):
                count += 1
            i += 1
        return count

    return func


print("----------Q4----------")
coun = count_coud(lambda n, i: n % i == 0)
print(coun(4))
is_prime = lambda n, i: count_factor(i) == 2


def count_factor(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


count_primes = count_coud(is_prime)
print(count_primes(20))

# Q6 composite identity function
def composer(f, g):
    """return the composition function which given x, computes f(g(x))"""
    return lambda x:f(g(x))

def composite_identity(f, g):
    """Return a function with one parameter x that returns True if f(g(x))
    is equal to g(f(x))."""

    # basic solution
    # def identity(x):
    #     return composer(f, g)(x) == composer(g, f)(x)
    # return identity

    # one line solution
    return lambda x: f(g(x)) == g(f(x))

# test
print("------------Q6------------")
add_one = lambda x: x + 1
square = lambda x: x**2
c1= composite_identity(add_one,square)
print(c1(0))  # true
print(c1(4))  # false

# Q7 I heard you liked functions
def cycle(f1, f2, f3):
    """Return a function that is itself a higher-order function"""
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn
