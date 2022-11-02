def prime_factors(n):
    """ Print the prime factors of n in non-decreasing order """
    while n > 1:
        p = smallest_prime_factor(n)
        n = n // p
        print(p)


def smallest_prime_factor(n):
    """ Return the smallest factor of n"""
    k = 2
    while n % k != 0:
        k += 1
    return k


# test
print(prime_factors(145))
