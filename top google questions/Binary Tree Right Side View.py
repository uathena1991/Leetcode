# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
BFS
"""
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        curr_level = [root]
        res = []
        while curr_level:
            next_level = []
            for cn in curr_level:
                if cn.left:
                    next_level.append(cn.left)
                if cn.right:
                    next_level.append(cn.right)
            res.append(cn.val)
            curr_level = next_level

        return res

"""
DFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = dict()
        stack = [(root,0)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node:
                res[depth] = node.val
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))

        return [res[d] for d in range(max_depth)]