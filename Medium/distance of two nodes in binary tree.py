"""
	find distance (edge) between any two nodes p, q in a binary tree

	Solution:
		distance(p, q) = distance(p, root) + distance(q, root) - distance(LCA, root) * 2
"""
def distance_2nodes(root, p, q):
	"""
	:param root: root of tree
	:param p: node 1
	:param q: node 2
	:return: distance (edge)
	"""
	def path2node(node, path, tar):
		if not node:
			return
		path.append(node.val)
		if node.val == tar.val:
			return path
		path2node(node.left, path, tar)
		path2node(node.right, path, tar)
		path.pop()


	path_p, path_q = [], []
	path2node(root, path_p, p)
	path2node(root, path_q, q)

	# find LCA
	i = 0
	while i < len(path_p) and i < len(path_q):
		if path_p[i] == path_q[i]:
			i += 1
		else:
			break
	return len(path_p) + len(path_q) - 2 - 2 * (i-1)
