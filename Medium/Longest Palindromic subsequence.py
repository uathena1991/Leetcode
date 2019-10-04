class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ls = len(s)
        if s == s[::-1]:
            return ls
        dp = [[0 for _ in s] for _ in s]
        for i in range(ls-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, ls):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][ls-1]

