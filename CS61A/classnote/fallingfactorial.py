""" Falling Factorial """


def falling(n, k):
    """ Compute the falling factorial of n to depth k"""
    ans = 1
    while k > 0:
        n, ans, k = n-1, ans * n, k-1
