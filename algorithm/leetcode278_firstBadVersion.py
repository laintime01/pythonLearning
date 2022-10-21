# First Bad Version
#   make a test isBadVersion api
def isBadVersion(x):
    if x > 15:
        return True
    else:
        return False


def firstBadVersion(n):
    left, right = 1, n
    while right > left:
        middle = (left + (right - left) / 2)
        print(middle)
        if isBadVersion(middle):
            print("False")
            right = middle
        else:
            left = middle + 1
    return left


version = 50
print(firstBadVersion(version))