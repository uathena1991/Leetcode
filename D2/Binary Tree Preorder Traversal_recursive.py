"""Notes:
    Tree traversal
    https://en.wikipedia.org/wiki/Tree_traversal#Pre-order
    
    recursive solution

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
        def Recursion(node):
            """

	        :type node: object
	        """
            if not node:
                return
            Recursion(node.right)
            Recursion(node.left)

            res.append(node.val)

        Recursion(root)
        res.reverse()
        return res
