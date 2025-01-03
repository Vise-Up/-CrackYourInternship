# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        if not subRoot:
            return True
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self,root,subtree):
        if not root and not subtree:
            return True
        if root and subtree and root.val==subtree.val:
            return self.sameTree(root.left,subtree.left) and self.sameTree(root.right,subtree.right)
        return False        