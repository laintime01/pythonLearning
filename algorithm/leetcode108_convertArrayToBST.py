class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sort_array_to_BTS(self, nums):
        """
        :param nums: List[int]
        :return: TreeNode
        """
        return self.dsf(nums, 0, len(nums)-1)

    @staticmethod
    def dsf(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        return TreeNode(
            nums[mid],
            self.dfs(nums, start, mid-1),
            self.dfs(nums, mid+1, end)
        )
