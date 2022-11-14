# generators
def double_numbers(ite):
    for i in ite:
        # yield like return but return a generator
        yield i + i


# generator only compute next value if needed
# use _ for a name of build in function
range_ = range(1, 9000000)
# double_numbers will not generate numbers bigger than 30
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break

# decorators
# beg decorate say
# beg will can say first, if return say_please is True, beg will change return stings
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :D")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = 'Can you buy me a beer ?'
    return msg, say_please


print(say())
print(say(say_please=True))
