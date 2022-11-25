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
    >>> t = tree()
    """
    if t.branches is None:
        return t
    else:
        for b in t.branches:
            cumulative_mul(b)
            t.label *= b.label
