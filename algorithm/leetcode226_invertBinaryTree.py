# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertBinaryTree(self, root):
        """
        :param root:TreeNode
        :return:TreeNode
        """
        if not root:
            return
        else:
            root.left,root.right = root.right,root.left
            root.left = self.invertBinaryTree(root.left)
            root.right = self.invertBinaryTree(root.right)
        return root
