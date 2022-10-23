# leetcode rotate array by k

class Solution(object):
    def rotateArray(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


# test
nums = [1,2,3,4,5,6,7,8]
k =3
s = Solution()
s.rotateArray(nums, k)