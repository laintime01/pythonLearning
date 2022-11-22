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
