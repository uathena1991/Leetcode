'''
2D dp
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dp = [[int(x) for x in y] for y in matrix]
        m,n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # print(dp)
        return max([max(x) for x in dp])**2



"""
1D dp

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        prev, curr = [int(matrix[x][0]) for x in range(m)], [int(matrix[x][0]) for x in range(m)],
        res = max(prev)
        for c in range(1, n):
            curr[0] = int(matrix[0][c])
            for r in range(1, m):
                if matrix[r][c] == '1':
                    curr[r] = min(curr[r-1], prev[r], prev[r-1]) + 1
                else:
                    curr[r] = 0
            prev = [x for x in curr]
            res = max(res, max(curr))
        return res**2
