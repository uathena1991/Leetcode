'''
test case
[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
'''
# Definition for a binary tree node.
# class TreeNode(object):

#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        # choose the longest left/right subtree
        def curr_depth(node):
            if not node:
                return 0
            left_depth, right_depth = curr_depth(node.left), curr_depth(node.right)
            tmp = left_depth + right_depth
            self.diameter = tmp if self.diameter < tmp else self.diameter
            return 1 + max(left_depth, right_depth)
        curr_depth(root)
        return self.diameter



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.res = max(self.res, L + R + 1)
            return 1 + max(L, R)


        self.res = 1
        dfs(root)
        return self.res - 1

