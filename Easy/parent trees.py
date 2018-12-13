from collections import defaultdict
class Solution():
	def __init__(self, list):
		self.parent = defaultdict(list)
		for curr in list:
			p, c = tuple(curr)
			self.parent[c].append(p)
			if p not in self.parent:
				self.parent[p] = []

	def find_01_parent(self):
		res = []
		for c, p in self.parent:
			if len(p) <= 1:
				res.append(c)
		return res

	def get_anc(self, c):
		stack = self.parent[c]
		res = []
		while stack:
			curr_p = stack.pop()
			if curr_p not in res:
				res.append(curr_p)
			stack = stack + self.parent[curr_p]
		return res


	def iscommon(self, c1, c2):
		anc1 = self.get_anc(c1)
		anc2 = self.get_anc(c2)
		for ac in anc2:
			if ac in anc1:
				return True
		return False

	def highest_parent(self, c1):
		def helper(c1, ):
			if len(self.pair[c1]) == 0:
				return 0
			return 
		curr_par = self.parent(c1)
		for cur in curr_par:








