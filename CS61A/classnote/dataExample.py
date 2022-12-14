t = [1, 2, 3]
print(t[1:3])
t[1:3] = [t]
print(t)
t.extend(t)


class Worker:
    greeting = "Sir"

    def __init__(self):
        self.elf = Worker

    def work(self):
        return self.greeting + ', I work'

    def __repr__(self):
        return Bourgeoisie.greeting


class Bourgeoisie(Worker):
    greeting = 'Peon'

    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'


jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

print(Worker().work())
print(jack)
print(jack.work())
print(john.work())


def smallest_abs(l):
    return min(map(abs, l))


print(smallest_abs([1, 2, 3, 4, 5]))


def largest_adj_sum(l):
    return max([l[i] + l[i + 1] for i in range(len(l) - 1)])


def digit_dict(l):
    last = [x % 10 for x in l]
    return {d: [x for x in l if x % 10 == d] for d in last}


print(digit_dict([5, 8, 13, 21, 34, 55, 89]))


def all_have_equals(l):
    """Does every elements equal some other element in l?"""
    return all([l[i] in l[:i] + l[i + 1:] for i in range(len(l))])


print(all_have_equals([4, 3, 2, 3, 2, 4, 5, 5]))

s = 'Beginning'
print(s.replace('n', 'N', -1))

from CS61A.classnote.linkedList import *


# Example Linked lists
def ordered(s):
    """Check if the linked list is ordered"""
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif s.first > s.rest.first:
        return False
    else:
        return ordered(s.rest)


def merge(s, t):
    """Return a sorted Link with the elements of sorted s&t"""
    if s is Link.empty:
        return t
    if t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_without_calling_link(s, t):
    if s is Link.empty:
        return t
    if t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_without_calling_link(s.rest, t)
        return s
    else:
        t.rest = merge_without_calling_link(t.rest, s)
        return t