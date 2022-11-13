# module
import math

print(math.sqrt(16))  # 4

# specific function
from math import ceil, floor

print(ceil(3.7))  # 4.0
print(floor(3.7))  # 3.0

# simple
import math as m
print(math.sqrt(16) == m.sqrt(16)) # True

# dir
print(dir(math))
