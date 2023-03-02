class Solution(object):
    def search(self, nums, target):
        """
        :param nums:List[int]
        :param target:int
        :return:int
        """
        if target not in nums:
            return -1
        return nums.index(target)


nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))