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


# Q2 Weights
# mobile
def mobile(left, right):
    """Construct a mobile from a left arm and a right arm"""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether is a mobile"""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile"""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m):
    """Select the right arm of a mobile"""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


# arm
def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm"""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm"""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


# planet
def planet(mass):
    """Construct a planet of some mass"""
    assert mass > 0
    return ['planet', mass]


def mass(w):
    """select the mass of a planet."""
    assert is_planet(w), 'must call mass on a planet'
    return w[1]


def is_planet(w):
    """Whether w is a planet"""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'


def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a planet or mobile
    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return mass(m)
    else:
        return total_weight(end(left(m))) + total_weight(end(right(m)))


# Q3 Balanced
def balanced(m):
    """Return whether m is balanced
    >>> t,v,u = examples()
    >>> balanced(t)
    True
    """
    if is_planet(m):
        return True
    else:
        t_left = length(left(m)) * total_weight(end(left(m)))
        t_right = length(right(m)) * total_weight(end(right(m)))
        return t_left == t_right and balanced(end(left(m))) and balanced(end(right(m)))


# Totals
from CS61A.classnote.treeAbstraction import *


def total_tree(m):
    """Return a tree representing
    """
    if is_planet(m):
        return tree(mass(m))
    else:
        branches = [total_tree(end(f(m))) for f in [left, right]]
        return tree(sum([label(b) for b in branches]), branches)


# more trees
# Q5 Replace Loki at Leaf
def replace_loki_at_leaf(t, lokis_replacement):
    """Return a new tree where every leaf value equal to "loki" has
     been replaced with loki_replacement"""
    if is_leaf(t) and label(t) == "loki":
        return tree(lokis_replacement)
    else:
        bs = [replace_loki_at_leaf(b, lokis_replacement) for b in branches(t)]
        return tree(label(t), bs)


# Q6 has path
def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word
    """
    assert len(word) > 0, 'no path for empty word'
    if label(t) != word[0]:
        return False
    elif len(word) == 1:
        return True
    else:
        for b in branches(t):
            if has_path(b, word[1:]):
                return True
    return False


# Q7
def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def add_interval(x, y):
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)


def interval(a, b):
    """Construct an interval from a to b."""
    assert a <= b, 'Lower bound cannot be greater than upper bound'
    return [a, b]


def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]


def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]


# Q8 Interval Arithmetic
def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * upper_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# interval subtraction
def sub_interval(x, y):
    """Return the interval that contains the difference any value in x
    and any value in y"""
    neg_y = interval(-upper_bound(y), -lower_bound(y))
    return add_interval(x, neg_y)


# interval division
def div_interval(x, y):
    """Return division of interval"""
    assert not (lower_bound(y)) <= 0 <= upper_bound(y), 'Divide by zero'
    reciprocal_y = interval(1 / upper_bound(y), 1 / lower_bound(y))
    return mul_interval(x, reciprocal_y)
