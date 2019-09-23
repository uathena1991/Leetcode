"""
1D DP
dp[j] 1*(n+1): for current s1[i], the results up to s2[:j]
prev[j] 1*(n+1): for previous s1[i-1], the results up to s2[:j]
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        prev = [0 for _ in range(n+1)]
        for j in range(n):
            prev[j+1] = prev[j] + ord(s2[j])

        for i in range(m):
            # prev = [0 for _ in range(n+1)]
            dp = [0 for _ in range(n+1)]
            dp[0] = prev[0] + ord(s1[i])
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[j+1] = prev[j]
                else:
                    dp[j+1] = min(prev[j+1] + ord(s1[i]), dp[j] + ord(s2[j]))
            prev = dp
        return dp[-1]

"""
2D DP
dp[i][j]: results for s1[:i], s2[:j]
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(n):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        for i in range(m):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1] + ord(s1[i]), dp[i+1][j] + ord(s2[j]))
        # print(dp)
        return dp[-1][-1]