# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def sum_postorder(head):
            if not head:
                return 0
            left, right = sum_postorder(head.left), sum_postorder(head.right)
            self.res = max(left + right + head.val, head.val, head.val + left, head.val + right, self.res)
            return max(left, right, 0) + head.val


        if not root:
            return 0
        self.res = -float('inf')
        sum_postorder(root)
        return self.res