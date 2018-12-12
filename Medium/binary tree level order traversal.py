# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        to_visit = [root]
        while len (to_visit) > 0:
            curr_res, next_level = [], []
            for curr in to_visit:
                if curr:
                    curr_res.append(curr.val)
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            to_visit = next_level
            res.append(curr_res)
        return res