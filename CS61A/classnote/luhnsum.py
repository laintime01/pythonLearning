def split(n):
    return n // 100, n % 100, n % 10


def sum_digit(n):
    if n < 10:
        return n
    else:
        k, l = n // 10, n % 10
        return sum_digit(k) + l


def luhn_sum(n):
    last, ten, single = split(n)
    if ten * 2 > 9:
        ten = sum_digit(ten * 2)
    else:
        ten = ten * 2
    if last == 0:
        return ten + single
    return luhn_sum(last) + ten + single