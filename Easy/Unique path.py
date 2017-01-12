class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1]*n]*m # initialize --
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i-1][j]+res[i][j-1]
        return res[m-1][n-1]