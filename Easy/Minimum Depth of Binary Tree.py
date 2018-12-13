# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = map(self.minDepth, [root.left, root.right])
        print(depth)
        return 1 + (min(depth) or max(depth))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if left == 0 and right == 0:
                return 1
            if left * right == 0:
                return 1 + max(left, right)
            return 1 + min(left, right)

        if not root:
            return 0
        return helper(root)
