# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, r1, r2):
        if not r1 and not r2:
            return True
        if (not r1 or not r2):
            return False
        return r1.val == r2.val and self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
