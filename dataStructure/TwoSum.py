class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,j in enumerate(nums):
            hashmap[j] = i
        for x, y in enumerate(nums):
            d = hashmap.get(target - y)
            if d and x != d:
                return [d,x]


# test
nums1, target1 = [2,7,11,15], 9
nums2, target2 = [3,3], 6
expect_r1 = [0,1]
expect_r2 = [0,1]
solution = Solution()
print(solution.twoSum(nums1, target1))
print(solution.twoSum(nums2, target2))
