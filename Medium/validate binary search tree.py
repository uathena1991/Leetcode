# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, low = float('-inf'), high = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if low < root.val < high:
            return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right,  root.val, high)
        return False

