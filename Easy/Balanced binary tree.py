# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Test cases:
[1,2,2,3,null,null,3,4,null,null,4]
"""
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # find deepest node
        if root.left:
            if not self.isBalanced(root.left):
                return False
        if root.right:
             if not self.isBalanced(root.right):
                return False

        # save left, right subtree depth
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = root.left.val
        if root.right:
            right_depth = root.right.val
        # update root's depth
        if not root.left and not root.right:
            root.val = 1
        else:
            root.val = max(left_depth, right_depth) + 1

        # check current subtree
        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return True
