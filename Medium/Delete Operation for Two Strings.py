"""
2-D dp
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return m + n - dp[-1][-1] * 2

"""
OPtimized 1-D dp
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            tmp_dp = [0 for _ in range(n+1)]
            for j in range(n):
                if word1[i] == word2[j]:
                    tmp_dp[j+1] = dp[j] + 1
                else:
                    tmp_dp[j+1] = max(tmp_dp[j], dp[j+1])
            dp = tmp_dp

        return m + n - dp[-1] * 2