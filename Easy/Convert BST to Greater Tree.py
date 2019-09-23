# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def convertBST(self, root: TreeNode) -> TreeNode:
		def in_order(root, csum):
			if not root:
				return csum
			root.val += in_order(root.right, csum)
			return in_order(root.left, root.val)

		in_order(root, 0)
		return root