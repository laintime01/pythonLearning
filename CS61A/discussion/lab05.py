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
