"""Notes:
    Tree traversal
    https://en.wikipedia.org/wiki/Tree_traversal#Pre-order

    iterative solution

    special test case: [3,null,1,2,4,null,5]

    """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
            :type root: TreeNode
            :rtype: List[int]
        """
        res = []
        search_list = [root]
        while search_list:
            curr_node = search_list.pop()
            if curr_node:
                res.append(curr_node.val)
                search_list.append(curr_node.right)
                search_list.append(curr_node.left)
        return res
