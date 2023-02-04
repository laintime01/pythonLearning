import queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def order(self, root):
        """
        :param root: TreeNode
        :return: List[List[int]]
        """
        res = []
        self.dfs(root, 1, res)
        return res

    def dfs(self, now, level, res):
        if now is None:
            return
        if len(res) < level:
            res.append([])
        res[level - 1].append(now.val)
        if now.left:
            self.dfs(now.left, level+1,res)
        if now.right:
            self.dfs(now.right, level+1, res)