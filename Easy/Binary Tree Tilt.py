# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = 0
        # cal sum of subtrees
        def sum_subtree(node):
            global res
            if not node:
                return 0
            left_sum = sum_subtree(node.left)
            right_sum = sum_subtree(node.right)
            res += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        sum_subtree(root)
        return res

