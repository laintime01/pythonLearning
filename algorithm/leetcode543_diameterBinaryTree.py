class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        self.res = 1
        self.maxDepth(root)

        return self.res-1

    def maxDepth(self, now):
        if not now:
            return 0
        maxL = self.maxDepth(now.left)
        maxR = self.maxDepth(now.right)
        self.res = max(self.res, (maxR+maxL+1))
        maxD = max(maxL, maxR) + 1
        return maxD