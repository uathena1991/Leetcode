"""
recursion -- too slow
"""
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n<=2:
# 	        return n
#         else:
# 	        return  self.climbStairs(n-1) + self.climbStairs(n-2)

"""
loop
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
	        return n
        res = [1,2]
        for i in range(2,n):
			res.append(res[-1]+res[-2])
		return res[-1]


a = Solution()
nsteps = 35
t = a.climbStairs(nsteps)
print t