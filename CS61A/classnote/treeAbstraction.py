def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branch!'
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


# fib tree
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])


# count leaves of tree T
def count_leaves(t):
    """
    >>> count_leaves(fib_tree(4))
    5
    """
    if is_leaf(t):
        return 1
    else:
        return sum(count_leaves(b) for b in branches(t))


def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])


# another way
def increment(t):
    """Return a tree like t but with all labels incremented"""
    return tree(label(t) + 1, [increment_leaves(b) for b in branches(t)])


# print a tree
def print_tree(t, indent=0):
    print('  ' * indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)


# print summing paths
def print_sums(t, so_far):
    """Return the sum of tree paths"""
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


# count paths that have a total label sum
def count_paths(t, total):
    """Return the number of paths from the root to any
    node in tree t for which the labels along the path sum
    to total
    >>> t=tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum(count_paths(b, total- label(t)) for b in branches(t))


t = tree(1, [tree(5, [tree(7)]), tree(6)])
print(t)
print(label(t))
print(branches(t))
print(fib_tree(4))
print(increment_leaves(t))
print(increment(t))
print_tree(t)
numbers = tree(3, [tree(4), tree(5, [tree(6)])])
print_sums(numbers, 0)
