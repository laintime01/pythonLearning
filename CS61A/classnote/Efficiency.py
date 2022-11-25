def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


# count
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


fib = count(fib)
print(fib(5))
print(fib.call_count)
print(fib(15))
print(fib.call_count)


# Memoization
def memo(f):
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


# Exponentiation
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n - 1)


square = lambda x: x * x


def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)


# Space
def count_frame(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


fib = count_frame(fib)
print(fib(20))
print(fib.open_count)
print(fib.max_count)
