class Solution:
	"""
	backtracking
	"""
	def helper(self, s, curr_path, res):
		if len(s) == 0:
			res.append(curr_path)
			return
		for i in range(1, len(s) + 1):
			if self.is_pal(s[:i]):
				# curr_path.append(s[:i])
				self.helper(s[i:], curr_path + [s[:i]], res)

	def is_pal(self, s):
		return s == s[::-1]


	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		res = []
		self.helper(s, [], res)
		return res