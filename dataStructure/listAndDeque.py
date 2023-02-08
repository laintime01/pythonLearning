import timeit


def list_append():
    l = []
    for i in range(5000):
        l.append(i)


def list_insert():
    l = []
    for i in range(5000):
        l.insert(0, i)


append_spend = timeit.timeit(
    setup='from __main__ import list_append',
    stmt='list_append()',
    number=10000,
)
print("list_append: ", append_spend)

append_insert = timeit.timeit(
    setup='from __main__ import list_insert',
    stmt='list_insert()',
    number=10000,
)
print("list_append: ", append_insert)

# Use deque when you need to insert data into top of list
from collections import deque


def deque_append():
    l = deque()
    for i in range(5000):
        l.append(i)


def deque_appendleft():
    l = deque()
    for i in range(5000):
        l.appendleft(i)


append_deque = timeit.timeit(
    setup='from __main__ import deque_append',
    stmt='deque_append()',
    number=10000,
)

appendleft_deque = timeit.timeit(
    setup='from __main__ import deque_appendleft',
    stmt='deque_appendleft()',
    number=10000,
)

print("deque_append: ", append_deque)
print("deque_appendleft: ", appendleft_deque)