# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        self.str = ''
        if not t:
            return ""
        if not t.left and not t.right:
            self.str += "(" + str(t.val) + ")"
            return self.str
        if t.right:
            self.str += str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"
            return self.str
        else:
            self.str += str(t.val) + "(" + self.tree2str(t.left) + ")"
            return self.str

