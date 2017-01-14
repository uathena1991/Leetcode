"""
Recursion
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = 0
        def sum_f(root,sum):
            if not root:
                return 0
            sum = 10*sum+root.val
            if not root.left and not root.right:
                return sum
            lsum = sum_f(root.left,sum)
            rsum = sum_f(root.right,sum)
            return lsum+rsum
        return sum_f(root,sum)
