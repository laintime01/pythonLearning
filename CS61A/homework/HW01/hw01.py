# Q1 syllabus Quiz pass
# Q2 A plus Abs B
from operator import add, sub


def a_plus_abs_b(a, b):
    """
    return a+abs(b) without calling abs
    a_plus_abs_b(2,3) -> 5
    a_plus_abs_b(2,-3) -> 5
    :param a:
    :param b:
    :return:
    """
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)


# test
print(a_plus_abs_b(1, -3))


# Q3 Two of Three

def two_of_three(x, y, z):
    """
    return a*a + b*b where a and b are the two smallest members of the x,y,z
    :param x:
    :param y:
    :param z:
    :return:
    """
    return x ** 2 + y ** 2 + z ** 2 - max(x, y, z) ** 2


# test
print(two_of_three(1, 2, 3))


# Q4 Largest Factor
def largest_factor(x):
    """
    return the largest factor of x that is smaller than x
    :param x:
    :return:
    """
    for y in range(x - 1, 1, -1):
        if x % y == 0:
            return y


# test
print(largest_factor(20))


# Q5 if Function vs Statement
def if_function(condition, true_result, false_result):
    """
    return return true_result if is true and false_result if is false
    if_function(True,2,3)->2
    :param condition:
    :param true_result:
    :param false_result:
    :return:
    """
    if condition:
        return true_result
    else:
        return false_result


def cond():
    return False


def true_func():
    print(42)


def false_func():
    print(47)


def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():
    # interpreter will calculate these three first then use them as call expression
    # so 42,47 will be printed which means true_func and false_func are called
    return if_function(cond(), true_func(), false_func())


with_if_statement()
with_if_function()

# Q6 Hailstone

def hailstone(x):
    """
    print the hailstone sequence starting at x and return its length
    :param x:
    :return:
    """
    count = 1
    if x == 1:
        return 1
    if x < 0:
        print("x must above 0")
        return
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x*3 + 1
        count += 1
    return count

print(hailstone(27))
print(hailstone(-10))

