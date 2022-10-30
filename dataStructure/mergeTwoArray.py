class Solution(object):
    # first way to do this
    def mergeTwo(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
        print(nums1)
        return nums1

    def mergeTwo_easy(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        return nums1.sort()


# test
nums_zero, m1, nums_one, n1 = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
expected = [1, 2, 2, 3, 5, 6]

solution = Solution()
solution.mergeTwo(nums_zero, m1, nums_one, n1)
solution.mergeTwo_easy(nums_zero, m1, nums_one, n1)