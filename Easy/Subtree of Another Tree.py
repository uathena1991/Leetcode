"""
test case:
[3,4,5,1,2]
[4,1,2]

[3,4,5,1,2,null,null,0]
[4,1,2]

[1,1]
[1]

[3,4,5,1,null,2]
[3,1,2]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # check if the two Trees are the same
        def isSame(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)

        if s and t:
            if isSame(s,t):
                return (self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right))
            else:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        elif not s and not t:
            return True
        else:
            return False