dict1 = {'name': 'jack'}
dict2 = {'age': 20}


# one way
def merge_dict(d1, d2):
    d_temp = d1.copy()
    d_temp.update(d2)
    return d_temp


print(merge_dict(dict1, dict2))

# second way
print({**dict1, **dict2})

# ** -> for dict  * for iterable object
print([1,2,3, *range(5)])
l1 = [1,2,3,5]
l2 = [6,8,9,0]
print([*l1,*l2])
