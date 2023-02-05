class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self,root,p,q):
        """Given a binary search tree (BST), find the
        lowest common ancestor (LCA) node of two given
        nodes in the BST.
        :param root: TreeNode
        :param p: TreeNode
        :param q:TreeNode
        :return:TreeNode
        """
        while root:
            if root.val<p.val and root.val<q.val:
                root = root.right
            elif root.val>p.val and root.val>q.val:
                root = root.left
            else:
                return root
