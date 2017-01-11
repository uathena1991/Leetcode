""" optimal path, dynamic programming"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = grid # initialize
        for j  in range(1,n):
            res[0][j]+=res[0][j-1]
        for i in range(1,m):
            res[i][0]+=res[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] += min(res[i][j-1],res[i-1][j])
        return res[m-1][n-1]
