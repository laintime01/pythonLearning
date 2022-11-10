# lab05
# Q1 Flatten
def flatten(s):
    """Return a flattened version of list s."""
    if not s:
        return []
    elif s[0] == list:
        return flatten(s[0]) + flatten(s[1:])
    else:
        return s[0] + flatten(s[1:])


# Data Abstraction
# Q2 Distance
from math import sqrt


def make_city(name, lat, lon):
    return [name] + [lat, lon]


def get_name(city):
    return city[0]


def get_lat(city):
    return city[1]


def get_lon(city):
    return city[2]


def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    x1, x2 = get_lat(city_a), get_lat(city_b)
    y1, y2 = get_lon(city_a), get_lon(city_b)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def closer_city(lat, lon, city_a, city_b):
    """Return the name of either city_a or city_b, whichever is closest to
    coordinate(lat, lon). If the two cities are the same distance away from
    the coordinate, consider city_b to be the one

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('SVienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    city = make_city('spot', lat, lon)
    return city_a[0] if distance(city, city_a) < distance(city, city_b) else city_b[0]


# Q4 Dont violate the abstraction barrier

# Q5 Finding berries!
from CS61A.classnote.treeAbstraction import *


def berry_finder(t):
    """Return True if t contains a node with the value 'berry
    and False otherwise
    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> t = tree(1, [tree('berry', [tree('not berry')])])
    >>> berry_finder(t)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> berry_finder(numbers)
    False
    """
    if label(t) == 'berry':
        return True
    return True in [berry_finder(b) for b in branches(t)]


# Q6 Sprout leaves
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
     1
       2
       3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
     1
       2
         4
         5
       3
         4
         5
    """
    if is_leaf(t):
        return tree(label(t), [tree(leaf) for leaf in leaves])
    return tree(label(t), [sprout_leaves(s, leaves) for s in branches(t)])


# Q8 Preorder
def preorder(t):
    """Return a list of the entries in this tree in the order
    that they would be visited by a preorder traversal
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """

    if not branches(t):
        return [label(t)]
    flattened = []
    for branch in branches(t):
        flattened += preorder(branch)
    return [label(t)] + flattened
