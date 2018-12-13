class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)  <= 1:
            return 1 if int(s[0]) != 0 else 0
        if s[0] == '0':
            return 0

        dp = [0] * len(s)
        dp[0] = 1 if int(s[0]) != 0 else 0
        if 10 <= int(s[:2]) <= 26:
            dp[1] = 1 if int(s[1]) == 0 else 2
        elif int(s[1]) == 0:
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s)):
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-1] + dp[i-2] if int(s[i]) != 0 else dp[i-2]
            elif int(s[i]) != 0:
                dp[i] = dp[i-1]
            else:
                return 0

        return dp[-1]
