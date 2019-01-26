# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recursion(self, node):
        if not node:
            return False, None
        if not node.left and not node.right:
            self.res += 1
            return True, node.val
        left, right = self.recursion(node.left), self.recursion(node.right)
        if (left[0] and right[0] and left[1] == right[1] == node.val) or (right[0] and not left[0] and right[1] == node.val and not left[1]) or (left[0] and not right[0] and left[1] == node.val and not right[1]):
            self.res += 1
            return True, node.val
        return False, node.val

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.recursion(root)
        return self.res