"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            child_depth = []
            for child in node.children:
                child_depth.append(helper(child))
            if len(child_depth) == 0:
                return 1
            return 1 + max(child_depth)

        if not root:
            return 0
        return helper(root)