def findPivotIndex(lists):
    """
    :param lists:
    :return:
    >>> findPivotIndex([1,7,3,6,5,6])
    3
    >>> findPivotIndex([1,2,3])
    -1
    """
    for i in range(len(lists)):
        if sum(lists[:i]) == sum(lists[i+1:]):
            return i
    return -1


