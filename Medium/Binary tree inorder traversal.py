# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        roots_q = []
        curr_root = root
        while True:
            while curr_root:
                roots_q.append(curr_root)
                curr_root = curr_root.left
            if not roots_q:
                return res
            curr_root = roots_q.pop()
            res.append(curr_root.val)
            curr_root = curr_root.right
        return res