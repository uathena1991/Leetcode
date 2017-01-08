
""" Notes:
    1) if x  vs. if x is None
    They are different... the first one tests trueness, the latter one tests identity with None...
    2)BST: all the elements in the left subtrees are smaller than the root; all the elements in the right subtrees are larger than the root.
    3) Don't have to check root.right, because the last root has been updated before check it...
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
            :type root: TreeNode
            :rtype: bool
            """
        self.lastroot = None
        self.isBST = True
        self.checkvalid(root)
        return self.isBST
    
    def checkvalid(self,root):
        if root is None:
            return
        self.checkvalid(root.left)
        if self.lastroot is not None and self.lastroot >= root.val:
            self.isBST = False
            return
        self.lastroot = root.val
        self.checkvalid(root.right)



