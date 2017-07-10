"""
test case
[10,5,-3,3,2,null,11,3,-2,null,1]
8
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # find number of path start from curr_root
        def haspathsum(curr_root, curr_sum):
            if not curr_root:
                return 0
            return int(curr_root.val == curr_sum) + haspathsum(curr_root.left, curr_sum - curr_root.val) + haspathsum(curr_root.right, curr_sum - curr_root.val)

        # traverse the whole tree...
        def traverse_tree(curr_root):
            if curr_root:
                return haspathsum(curr_root, sum) + traverse_tree(curr_root.left) + traverse_tree(curr_root.right)
            else:
                return 0

        return traverse_tree(root)
