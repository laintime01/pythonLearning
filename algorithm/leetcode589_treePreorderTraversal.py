class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        output = []
        self.traverse(output, root)
        return output
    def traverse(self, output, root):
        if root is None:
            return
        output.append(root.val)
        for child in root.children:
            self.traverse(output, child)

