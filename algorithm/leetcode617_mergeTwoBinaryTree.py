# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTwoBinaryTree(self,t1,t2):
        """
        :param t1: TreeNode
        :param t2: TreeNode
        :return: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTwoBinaryTree(t1.left, t2.left)
            root.right = self.mergeTwoBinaryTree(t1.right, t2.right)
            return root
        else:
            return t1 or t2

