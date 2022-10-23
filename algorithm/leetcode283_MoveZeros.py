# leetcode 283 move zeros
class Solutions(object):
    def moveZero(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        print(nums)


# test
arrays = [0,0,2,0,1]
s = Solutions()
s.moveZero(arrays)