class Solution(object):
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        :param nums:List
        :param target:int
        :return:List[int]
        """
        dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            else:
                dic[value] = index


print(Solution().twoSum([3, 3], 6))
