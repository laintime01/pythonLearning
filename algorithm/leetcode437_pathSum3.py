# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.numOfPath = 0

    def pathSum(self, root, targetSum):
        """
        :param root: TreeNode
        :param targetSum:int
        :return:int
        """
        self.dfs(root, targetSum)
        return self.numOfPath

    # traverse the tree
    def dfs(self, node, target):
        if not node:
            return
        self.test(node, target)

        self.dfs(node.left, target)
        self.dfs(node.right, target)

    # define: for a given node, DFS to find any path that sum == target,
    # if find self.numOfPaths += 1
    def test(self, node, target):
        if node is None:
            return

        if node.val is target:
            self.numOfPath += 1

        # test break down
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)
