class Solution(object):
    def runningSum(self, nums):
        """
        :param nums:
        :return:
        """
        length = len(nums)
        return [sum(nums[0:i+1]) for i in range(length)]


s = Solution()
lists = [1,2,3,4]
print(s.runningSum(lists))
print(s.runningSum([1,1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))
