# Q1 Linked list
from CS61A.classnote.linkedList import *

link = Link(1000)
print(link.first)
print(link.rest is Link.empty)
link = Link(1000, 2000)
print(link.rest)


# Q2 Convert Link
def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements
    >>> link = Link(1,Link(2,Link(3,Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    else:
        return [link.first] + convert_link(link.rest)


# Q3 Duplicate Link
def duplicate_link(lnk, val):
    if lnk is Link.empty:
        return
    elif lnk.first == val:
        r = lnk.rest
        lnk.rest = Link(val, r)
        duplicate_link(r, val)
    else:
        duplicate_link(lnk.reset, val)


# Q4 Tree
from CS61A.classnote.treeAbstraction import *


# Q5 Cumulative Mul
def cumulative_mul(t):
    """
    >>> t = tree(1,[tree(3, [tree(5)]), tree(7)])
    >>> cumulative_mul(t)
    >>> t
    tree(105,[tree(15, [tree(5)]), tree(7)])
    """
    for b in t.branches:
        cumulative_mul(b)
        t.label *= b.label


# Q6 every other
def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    >>> link = Link(1,Link(2,Link(3, Link(4))))
    >>> every_other(link)
    >>> link.rest.first
    3
    >>> link.first
    1
    """
    if s is Link.empty or s.rest is Link.empty:
        return
    else:
        s.rest = s.rest.rest
        every_other(s.rest)
