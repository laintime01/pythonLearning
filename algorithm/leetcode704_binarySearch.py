# binary search python

def binarySearch(target, array):
    low = 0
    high = len(array) - 1
    counts = 0
    while low <= high:
        mid = (low + high) // 2
        counts += 1
        if array[mid] == target:
            print(f"search times -> {counts}")
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1


# test
new_array = list(range(1, 20))
tar_num = 18
result = binarySearch(tar_num, new_array)
if result:
    print(f"index of target in array is {result}")
else:
    print("target not found!")
