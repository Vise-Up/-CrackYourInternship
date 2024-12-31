# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left-right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, root):
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
        