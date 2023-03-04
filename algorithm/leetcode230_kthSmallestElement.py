class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kth_smallest(self, root, k):
        remain, ans = k, 0
        def dfs(root):
            if not root:
                return False
            if dfs(root.left):
                return True

            nonlocal remain
            remain -= 1

            if remain == 0:
                nonlocal ans
                ans = root.val
                return True

            return dfs(root.right)
        dfs(root)
        return ans
