class Solution(object):
	def isgray(self,x,y):
		"""
		judge if two values are gray numbers or not.
		:param x: in binary format
		:param y: in binary format
		:return: True or False
		"""
		res1 = x ^ y
		count = 0
		while res1 != 0:
			res1,remain = divmod(res1,2)
			if remain == 1:
				count += 1
		return count == 1

a = Solution()