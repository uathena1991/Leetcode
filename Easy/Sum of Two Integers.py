class Solution(object):
	def getSum(self, a, b):
		"""
		:return:
		:type a: int
		:type b: int
		:rtype: int
		no operator +/- (bit manipulation)
		key: negative numbers
		ref: https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
		"""
		mask = 0xFFFFFFFF # assume python integer is 32-bit -- with first bits of sign????
		MIN = 0x80000000
		MAX = 0x7FFFFFFF
		while b != 0:
			# carry
			carry = a & b
			a = (a ^ b) & mask  # add mask to get the last 32 bits
			b = (carry << 1) & mask
			# print a,b, carry
		# if a is negative, get a's 32 bits complement positive first
		# then get 32-bit positive's Python complement negative
		return a if a <= MAX else ~(a ^ mask)

A = Solution()
print A.getSum(3, -2147483648)