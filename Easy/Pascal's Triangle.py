class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        for n in range(1,numRows):
            res.append([1]*(n+1))
            for j in range(1,n):
                res[n][j] = res[n-1][j] + res[n-1][j-1]
        return res

a = Solution()
print a.generate(7)