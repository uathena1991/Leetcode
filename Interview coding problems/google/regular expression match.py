class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def recursion(i, j):
            if (i, j) not in memo:
                if j == lp + 1:
                    memo[(i, j)] = i == ls + 1
                    return memo[(i, j)]
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    memo[(i,j)] = recursion(i-1, j - 1)
                else:
                    if p[j-1] == '*':
                        if p[j-2] != s[i-1] and p[j-2] != '.':
                            memo[(i,j)] = recursion(i, j-2)
                        else:
                             # repeat once, multiple times, zero
                            memo[(i, j)] = recursion(i, j-1) or recursion(i - 1, j) or recursion(i, j-2)
                    else:
                        memo[(i,j)] = False
            # print(i,j, s[:i], p[:j], memo[(i,j)])
            return memo[(i, j)]

        ls, lp = len(s), len(p)
        if lp == ls == 0:
            return True
        if lp == 0 and ls != 0:
            return False
        memo = {}
        memo[(0, 0)] = True
        for i in range(1, ls+1):
            memo[(i, 0)] = False
        for i in range(1, lp+1):
            if p[i-1] == '*':
                memo[(0, i)] = memo[(0, i-2)]
            else:
                memo[(0, i)] = False
        if ls == 0:
            return memo[(0, lp)]
        recursion(ls, lp)
        # print(memo)
        return memo[(ls, lp)]






    class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        if ls == 0 == lp:
            return True
        if ls != 0 and lp == 0:
            return False
        dp = [[False for _ in range(lp+1)] for _ in range(ls+1)]
        dp[0][0] = True
        dp[0][1] = True if p[0] == '*' else False
        # s = ''
        for i in range(2, lp+1):
            dp[0][i] = (p[i-1] == '*' and dp[0][i-2])

        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] != '.' and p[j-2] != s[i-1]:
                        dp[i][j] = dp[i][j-2] # repeat 0 times
                    else:
                        # repeat 0, 1, > 1 times
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]

        return dp[ls][lp]