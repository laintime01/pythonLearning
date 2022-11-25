# Q1 Mint
class Mint:
    """A mint creates coins by stamping on years
    >>> mint = Mint()
    >>> mint.year
    2022
    >>> dime = mint.create(Dime)
    >>> dime.year
    2022
    """
    present_year = 2022

    def __init__(self):
        self.update()

    def create(self, coin):
        return coin(self.year)

    def update(self):
        self.year = Mint.present_year


class Coin:
    cents = None

    def __init__(self, year):
        self.year = year

    def worth(self):
        return self.cents + max(0, Mint.present_year - self.year - 50)


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


# Q2 Store Digits
from CS61A.classnote.linkedList import *


def store_digits(n):
    """Store the digits of a positive number n in a linked list.
    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    """
    ans = Link.empty
    while n > 0:
        ans = Link(n % 10, ans)
        n //= 10
    return ans


# Q3 Mutable Mapping
def deep_map_mut(func, lnk):
    """Mutates a deep link lnk by replacing each item with calling
    func on it.
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x:x*x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    if lnk is Link.empty:
        return lnk
    elif isinstance(lnk.first, Link):
        deep_map_mut(func, lnk.first)
    else:
        lnk.first = func(lnk.first)
    deep_map_mut(func, lnk.rest)


# Q4 Two List

def two_list(vals, counts):
    """Return a linked list according to the two lists
    >>> a = [1,3,2]
    >>> b = [1,1,1]
    >>> c = two_list(a,b)
    >>> c
    Link(1,Link(3,Link(2)))
    """
    ans = Link(None)
    p = ans
    for j in range(len(vals)):
        item = vals[j]
        for _ in range(counts[item]):
            p.rest = Link(item)
            p = p.rest
    return ans.rest


# Q5 Next Virahanka Fibonacci Object
class VirFib():
    """A Virahanka Fibonacci number.
    >>> start = VirFib()
    >>> start
    VirFib object, value 0
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value ==0:
            result = VirFib(1)
        else:
            result = VirFib(self.value + self.previous)
        result.previous = self.value
        return result

    def __repr__(self):
        return "VirFib object, value " + str(self.value)
