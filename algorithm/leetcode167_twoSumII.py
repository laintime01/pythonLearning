# leetcode 167
# Return the indices of the two numbers, sum is target

class Solution(object):
    def twoSum(self, numbers, target):
        l = 1
        r = len(numbers)
        while l <= r:
            sum = numbers[l - 1] + numbers[r - 1]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                print([l, r])
                return [l, r]


# test
arrays = [1, 3, 5, 8, 11, 15, 18]
target_number = 18

s = Solution()
s.twoSum(arrays, target_number)
