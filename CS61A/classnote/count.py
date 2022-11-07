def count(s, value):
    """
    >>> count([1,2,3,5,2,2], 2)
    3
    :param s: 
    :param value:
    :return:
    """
    total = 0
    for i in s:
        if i == value:
            total += 1
    return total