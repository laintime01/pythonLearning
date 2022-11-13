# function
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y


# call the add function
add(5, 6)  # => 11
# key value
add(y=6, x=5)


# *args
def varargs(*args):
    return args


varargs(1, 2, 3)  # =>(1,2,3)


# **kwargs
def keyword_args(**kwargs):
    return kwargs


keyword_args(big="foot", loch="ness")  # => {"big":"foot", "loch":"ness"}


# mix *args and **kwargs
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


all_the_args(1, 2, a=3, b=4)

# the other way
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(args)
all_the_args(kwargs)
all_the_args(args, kwargs)

# scope of function
x = 5


def setX(num):
    x = num  # 43
    print(x)  # 43


def setGlobalX(num):
    global x
    print(x)  # 5
    x = num  # 6
    print(x)  # 6


setX(43)
setGlobalX(6)


# function in function
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
add_10(3)  # 13

# lambda
(lambda x: x > 2)(3)  # True
(lambda x,y: x**2 + y **2)(2,1) # 5

# build in function
list(map(add_10, [1,2,3,4])) # [11,12,13,14]
list(map(max, [1,2,3], [4,2,1])) # [4,2,3]
list(filter(lambda x:x>5, [4,6,7,8,9]))  # [6,7,8,9]

# return list using list
[add_10(i) for i in [1,2,3]] # [11,12,13]
print([x for x in [1,2,3,6] if x >2]) # [3,6]
# create set and dict using it
print([x for x in 'abshdi' if x not in 'abc']) # ['s','h','d','i']
print({x:x**2 for x in range(5)}) # {0:0,1:1,2:4,3:9,4:16}


