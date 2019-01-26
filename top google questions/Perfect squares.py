"""TLE
"""
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        i = 0
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        for a in range(n+1):
            b = 1
            while  a + b*b <= n:
                dp[a + b*b] = min(dp[a] + 1, dp[a+b*b])
                b += 1
        print(dp)
        return dp[n]

"""BFS
"""

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        spools = []
        while i*i <= n:
            spools.append(i*i)
            i += 1

        cts = 1
        curr_levels = [0]
        while True:
            next_levels = []
            for a in curr_levels:
                for b in spools:
                    if a + b == n:
                        return cts
                    if a + b < n:
                        next_levels.append(a + b)
            cts += 1
            curr_levels = set(next_levels)


