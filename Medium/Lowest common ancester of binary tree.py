# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recursive(node):
            if self.res:
                return False
            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                mid = True
            else:
                mid = False
            left = recursive(node.left)
            right = recursive(node.right)
            # print(left, right, mid)
            if mid + left + right >= 2:
                self.res = node
            return left or right or mid

        self.res =  []
        recursive(root)
        return self.res


"""
This is fantastic!!! Try to go through the example, the idea is simple but so smart: 
return the ancester if it contains p/q, otherwise, return None, and eventually, the one with both sides as True will be the final results!
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_anc = self.lowestCommonAncestor(root.left, p, q)
        right_anc = self.lowestCommonAncestor(root.right, p, q)
        if left_anc and right_anc:
            return root
        elif left_anc:
            return left_anc
        else:
            return right_anc

