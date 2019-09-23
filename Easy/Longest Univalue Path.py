# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            left_l, right_l = 0, 0
            if node.left and node.left.val == node.val:
                left_l = left + 1
            if node.right and node.right.val == node.val:
                right_l = right + 1
            self.res = max(self.res, left_l + right_l)
            return max(left_l, right_l)

        
        self.res = 0
        helper(root)
        return self.res
