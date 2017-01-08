# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        roots = [root]
        res = []
        order_idx = True # 0: left to right;  1:right to left
        while roots:
            tmp_roots = []
            tmp_new = []
            if order_idx:# left to right
                for r in roots[::-1]:
                    if r:
                        tmp_new.append(r.val)
                        if r.left:
                            tmp_roots.append(r.left)
                        if r.right:
                            tmp_roots.append(r.right)

            else: # right to left
                for r in roots[::-1]:
                    if r:
                        tmp_new.append(r.val)
                        if r.right:
                            tmp_roots.append(r.right)
                        if r.left:
                            tmp_roots.append(r.left)
            order_idx= not order_idx
            res.append(tmp_new)
            roots = tmp_roots
        return res