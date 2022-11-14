# Q2 Insert items
def insert_items(lst, entry, elem):
    """Insert elem into lst after each occurrence of entry and then returns lst
    >>> test_lst = [1,5,8,5,2,3]
    >>> new_list = insert_items(test_lst, 5, 7)
    [1, 5, 7, 8, 5, 7, 2, 3]
    """
    ln = len(lst)
    for i in range(0, ln):
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            i += 2
    print(lst)
    return lst


# Q4
def count_occurrences(t, n, x):
    """Return the number of times that x appears in
    the first n elements of iterator t.
    >>> s = iter([10,9,10,9,9,10,8,8,8,7])
    >>> count_occurrences(s,10,9)
    3
    """
    ans = 0
    for _ in range(n):
        if next(t) == x:
            ans += 1
    return ans


# Q5
def repeated(t, k):
    """Return the first value in iter t that appears k times
    >>> s = iter([10,9,10,9,9,10,8,8,8,7])
    >>> repeated(s, 3)
    8
    """
    assert k > 1, 'k must grt than 1'
    s,se = list(t), []
    for i in range(len(s)):
        if s[i] == s[i+1]:
            se.append(s[i])
            if len(se) == k-1:
                return se[0]
        else:
            se = []



