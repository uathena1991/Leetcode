# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def recursive_in_order(node):
            if not node:
                return
            recursive_in_order(node.left)
            res.append(node.val)
            # print(node.val, res)
            if len(res) >= k:
                return
            recursive_in_order(node.right)

        res = []
        if not root:
            return
        recursive_in_order(root)
        return res[k-1]


