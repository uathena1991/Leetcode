"""
Define a few objects and functions that are commonly used in leetcode
"""
import pdb
import math


# create singly-linked ListCode
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	def create_listnode(self, list):
		if not list:
			return None
		head = ListNode(list[0])
		curr = head
		for i in list[1:]:
			post = ListNode(i)
			curr.next = post
			curr = post
		return head

	def printout_listnode(self, head):
		curr = head
		res = []
		while curr:
			res.append(curr.val)
			curr = curr.next
		print res
		return res


class TreeNode(object):
	"""
	binary tree with children, and next pointer
	"""

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None


#
class List2Tree(object):
	"""
	Build binary tree from  list
	TBD: from other traversal lists
	"""
	def list2node(self, list):
		"""
		convert list of values to TreeNode list
		:param list:  must be complete (with [] representing empty nodes), e.g. [1,2,3,[],5,6,7]
		:return:  list with TreeNodes
		TBD: check correctness of input list
		"""
		tree_list = []
		for i in list:
			tree_list.append(TreeNode(i))
		return tree_list

	def from_level_list(self, treelist):
		"""
		:param treelist: list with TreeNodes -- from list2node
		:return: root
		"""
		if not treelist:
			return None
		d_total = int(math.ceil(math.log(len(treelist) + 1, 2)))
		for d in range(d_total - 1): # d: [0, log(N+1) - 2]
			for i in range(2**d):
				curr = treelist[2**d - 1 + i]
				if curr and d < d_total - 1:
					if 2**(d + 1) - 1 + 2*i < len(treelist):
						curr.left = treelist[2**(d + 1) - 1 + 2*i]
					if 2**(d + 1) - 1 + 2*i + 1 < len(treelist):
						curr.right = treelist[2**(d + 1) - 1 + 2*i + 1]
		return treelist[0]


## print trees (with different traversals)
class PrintTree(object):
	def level_traversal(self, root): # print tree as level-traversal list (check)
		if not root:
			return
		curr = [root]
		next = []
		res_list = []
		while curr:
			for x in curr:
				if x:
					res_list.append(x.val)
					if x.left:
						next.append(x.left)
					if x.right:
						next.append(x.right)
			curr = next
			next = []
		return res_list
	### TBD ### other traversals


################# TEST ##################
# TreeNode and so
# list = List2Tree().list2node([0,1,2,[],4,5,6,[],[],9])
# a_tree = List2Tree().from_level_list(list)
# print PrintTree().level_traversal(a_tree)

