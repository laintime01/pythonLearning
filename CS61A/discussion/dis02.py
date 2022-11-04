b = lambda x: lambda: x
c = b(100)
print(c)

d = lambda f: f(4)


def square(x):
    return x * x


print(d(square))


def xz(x):
    def z(z):
        return x + z

    return z


b = xz(10)
print(b(1))


