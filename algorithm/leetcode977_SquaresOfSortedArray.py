# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# leetcode 977

class Solution(object):
    def sortedSquares(self, nums):
        return sorted([i * i for i in nums])


# test
numbers = [-4, -1, 0, 3, 10]
s = Solution()
print(s.sortedSquares(numbers))
