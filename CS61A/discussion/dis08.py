# Q1
from functools import reduce


class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2


class B:
    def __init__(self):
        print('Boo')
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ''
        for a in self.a:
            ret += str(a)
        return ret


# Q3
from CS61A.classnote.linkedList import *


def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if s is Link.empty:
        return 0
    return s.first + sum_nums(s.rest)


# Q4
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2,Link(3,Link(5)))
    >>> b = Link(6,Link(4,Link(2)))
    >>> c = Link(4,Link(1,Link(0, Link(2))))
    >>> p =multiply_lnks([a,b,c])
    >>> p.first
    48
    """
    first = 1
    for x in lst_of_lnks:
        if x is Link.empty:
            return Link.empty
        first = first * x.first
    lst_of_lnks_rest = [l.rest for l in lst_of_lnks]
    return Link(first, multiply_lnks(lst_of_lnks_rest))


# Q5 Flip Two
def flip_two(s):
    """
    >>> one_link = Link(1,Link(2,Link(3,Link(4,Link(5)))))
    >>> flip_two(one_link)
    >>> one_link
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if s is Link.empty or s.rest is Link.empty:
        return s
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)

# Q6 Make Even
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """