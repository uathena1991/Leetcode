# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursion_flatten(self,root,prev):
        if not root:
            return
        if prev.val:
            prev.right = root
            prev.left = None
        prev = root
        self.recursion_flatten(root.left,prev)
        self.recursion_flatten(root.right,prev)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(None)
        self.recursion_flatten(root,prev)

            