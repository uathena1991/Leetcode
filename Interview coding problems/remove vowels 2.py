class Solution(object):
	def remove_vowels(self,l):
		vowels = 'aeiouAEIOU'
		res = []
		for i in l:
			if i in vowels:
				continue
			else:
				res.append(i)

		return ''.join(str(e) for e in res)
a = Solution()
print (a.remove_vowels('EE'))