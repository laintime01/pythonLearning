def inverse_cascade(n):
    def grow(n):
        if n <= 10:
            print(n)
        else:
            grow(n // 10)
            print(n)

    def shrink(n):
        if n <= 10:
            print(n)
        else:
            print(n)
            shrink(n // 10)

    grow(n)
    print(n)
    shrink(n)


# inverse_cascade(1234)

# another way of inverse cascade


def inverse(n, digits=1):
    n = str(n)
    print(n[:digits])
    if digits < len(n):
        inverse(n, digits+1)
        print(n[:digits])


inverse(1234)