class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.diameter = 0

    def depth(self, node):
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0

        if left + right > self.diameter:
            self.diameter = left + right
        # make sure the parent nodes get the correct depth from this node
        return 1 + (left if left > right else right)

    def diameterBinaryTree(self, root):
        self.depth(root)
        return self.diameter
