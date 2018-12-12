class Solution():
	def generatePalindromes(self, s):
		self.result = []
		from collections import Counter
		elements = dict(Counter(s))
		candidates = ''.join([x for x in elements if elements[x] == 2])
		self.single = ''.join([x for x in elements if elements[x] == 1])
		self.length = len(candidates)
		for i in range(len(candidates)):
			if i > 0 and i < len(candidates) and candidates[i] == candidates[i-1]:
				i += 1
			self.helper(candidates[i], candidates[:i] + candidates[i+1:])
		return self.result



	def helper(self, left, candidates):
		if len(left) == self.length:
			self.result.append([left + self.single + left[::-1]])
		for i in range(len(candidates)):
			if i > 0 and i < len(candidates) and candidates[i] == candidates[i-1]:
				i += 1
			self.helper(left+candidates[i], candidates[:i] + candidates[i+1:])

print(Solution().generatePalindromes('acabbc'))