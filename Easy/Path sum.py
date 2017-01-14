# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        lsum = self.hasPathSum(root.left,sum - root.val)
        rsum = self.hasPathSum(root.right,sum - root.val)
        return lsum or rsum