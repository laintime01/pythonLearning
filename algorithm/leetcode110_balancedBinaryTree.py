class TreeNode(object):
    def __init__(self,val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        max_l = self.maxDepth(root.left)
        max_r = self.maxDepth(root.right)

        max_d = max(max_l, max_r) + 1
        return max_d

    def isBalanced(self, root):
        if not root:
            return True

        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)

        if abs(max_left - max_right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)



