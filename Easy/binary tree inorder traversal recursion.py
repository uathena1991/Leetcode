def inorder(root):
	if not root:
		return root.val
	inorder(root.left)
	print root.val
	inorder(root.right)


# recursive
class BT_inorder():
	def __init__(self, root):
		self.stack = []
		self.stack.append(root)

	def pushAllleft(self, node):
		while node:
			self.stack.append(node)
			node = node.left

	def inorder_recursive(self):
		while len(self.stack) > 0:
			curr = self.stack.pop()
			self.pushAllleft(curr.left)
			print curr.val
			if curr.right:
				self.pushAllleft(curr.right)




