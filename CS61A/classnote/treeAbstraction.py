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


t = tree(1, [tree(5, [tree(7)]), tree(6)])
print(t)
print(label(t))
print(branches(t))