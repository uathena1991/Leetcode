class Node(object):
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None
class Solution():
	def longest_cs(self, root):
		def helper(length, last_value, curr_node):
			if not curr_node:
				return length
			if curr_node == last_value + 1:
				length += 1
			else:
				length = 1
			return max(length, helper(length, curr_node.val, curr_node.left), helper(length, curr_node.val, curr_node.right))

		if not root:
			return 0
		return helper(0, root.val - 1, root)



