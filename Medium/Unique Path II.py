"""
with obstacle
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        # if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1 :
        #     return 1
        dp = [[0 for _ in obstacleGrid[0]] for _ in obstacleGrid]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for c in range(1, len(obstacleGrid[0])): # first row
            dp[0][c] = dp[0][c-1] if obstacleGrid[0][c] == 0 else 0

        for r in range(1, len(obstacleGrid)):
            dp[r][0] = dp[r-1][0] if obstacleGrid[r][0] == 0 else 0 # first column
            for c in range(1, len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                else:
                    dp[r][c] = 0
        return dp[-1][-1]