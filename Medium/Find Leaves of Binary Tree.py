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
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right: # leaf
                self.path[-1].append(node.val)
                return None
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node

        self.path = []
        while root:
            self.path.append([])
            root = dfs(root)
        return self.path


"""
DFS with dictionary
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def cal_depth(node):
            if not node:
                return 0
            max_depth = max(cal_depth(node.left), cal_depth(node.right))
            self.path[max_depth].append(node.val)
            return max_depth + 1

        self.path = defaultdict(list)
        cal_depth(root)
        return self.path.values()

