# leetcode rotate array by k

class Solution(object):
    def rotateArray(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


def otherSolution(array, n):
    def reverse(array, l, h):
        while l <= h:
            array[l], array[h] = array[h], array[l]
            l += 1
            h -= 1

    ln = len(array)
    n = n % ln
    # reverse array[:ln-n]
    reverse(array, 0, ln - n - 1)
    # reverse array[ln-n:]
    reverse(array, ln - n, ln - 1)
    # reverse whole array
    reverse(array, 0, ln - 1)


# test
nums = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
s = Solution()
s.rotateArray(nums, k)
