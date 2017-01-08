"""
Simple recursion or loop will run out of time/memory
learn: bitwise operation <<
reference: http://lifexplorer.me/leetcode-pow-x-n/
"""
# class Solution(object):
#     def myPow(self, x, n):
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
#         res = 1.0
#         if x == 0:
#             return 0
#         if n == 1:
#             return x
#         if n == 0:
#             return 1
#         if n<0:
#             x = 1/x
#             n = -n
#         for i in range(n):
#             res*=x
#         return res

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        if n == 0:
            return 1
        if n == -1:
            return 1/x
        if n%2 == 0:
            t = self.myPow(x,n>>1)
            return t*t
        else:
            return x*self.myPow(x,n-1)

a=Solution()
t = a.myPow(0.0001,2147483647)
print t