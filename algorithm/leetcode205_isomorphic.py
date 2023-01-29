from collections import Counter


def isIsomorphic(s, t):
    """
    :param s: list
    :param t: list
    :return: true or false
    >>> isIsomorphic("egg",'add')
    True
    >>> isIsomorphic("title","paper")
    True
    >>> isIsomorphic("foo","bar")
    False
    """
    m1, m2 = [], []
    for idx in s:
        m1.append(s.index(idx))
    for idx in t:
        m2.append(t.index(idx))
    if m1 == m2:
        return True
    return False