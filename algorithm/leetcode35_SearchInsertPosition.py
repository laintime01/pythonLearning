# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# leetcode 35

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while r >= l:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                r = middle + 1
            else:
                l = middle - 1
        return l