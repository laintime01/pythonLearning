# hw04
# Q1 Arms-length recurion
from CS61A.classnote.treeAbstraction import *


def min_depth(t):
    """A simple function to return the distance between t's root and its cloest leaf"""
    if is_leaf(t):
        return 0
    else:
        h = float('inf')
        for b in branches(t):
            h = min(h, 1 + min_depth(b))
    return h
