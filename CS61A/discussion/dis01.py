def special_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x


print(special_case())


# Q2 jacket weather
def wears_jacket_with_if(temp, raining):
    return True if temp < 60 or raining else False


print(wears_jacket_with_if(80, False))


# Q4 prime
def is_prime(n):
    i = 2
    while i < n:
        print(i)

        if n % i == 0:
            return False
        i += 1
        print(i)
    return True


print(is_prime(7))


# Q5 fizzbuzz in oneline
def fizzbuzz(n):
    print(["fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) or i for i in range(1, n + 1)])


fizzbuzz(16)


# Q6 Unique Digits
def unique_digits(n):
    """Return the number of unique digits in positive integer n."""
    # d_list = []
    # while n > 0:
    #     d_list.append(n % 10)
    #     n = n // 10
    # return len(set(d_list))
    print(len(set(" ".join(str(n)).split(" "))))


def has_digit(n, k):
    """Return whether k is a digit in N"""
    digit_list = []
    while n > 0:
        digit_list.append(n % 10)
        n = n // 10
    if k in digit_list:
        return True
    else:
        return False


print(has_digit(10, 1))
print(has_digit(12, 7))
unique_digits(1313131)


# sum of digits in number
def sumDigits(n):
    """ return sum of digits in number"""
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n // 10))


no = 12345
print(sumDigits(no))


# double eight
def double_eight(n):
    """return true if n has two eights in a row"""
    list_n = " ".join(str(n)).split(" ")
    i = 0
    while i < len(list_n)-1:
        if list_n[i] == "8" and list_n[i+1] == "8":
            return True
        i += 1
    return False




print(double_eight(28313188))
