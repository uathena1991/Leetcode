# Count numbers of 5 (since there are more 2s)
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            return n/5 + self.trailingZeroes(n/5)