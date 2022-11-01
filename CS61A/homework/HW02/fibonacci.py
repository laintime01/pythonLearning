# compute the nth fibonacci number
def fib(n):
    prev, cur = 1, 0
    k = 0
    while k < n:
        prev, cur = cur, prev+cur
        k += 1
    return cur


# test
print(fib(4))