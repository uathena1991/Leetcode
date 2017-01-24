class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        else:
            return [prev + [i] for i in range(1,n+1) for prev in self.combine(i-1,k-1)]

a = Solution()
print a.combine(4,1)