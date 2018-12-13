class Solution(object):
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        n = len(s)
        res = s[0]
        # possible improvement (haven't been done): record current max_len, and start from that, not from 1 or 0 for each location
        for i in range(n):
            tmp1 = self.helper(s, i, i)
            tmp2 = self.helper(s, i, i+1)
            # print tmp1, tmp2
            res = max(res, tmp1, tmp2, key = len)
        return  res

 def longestPalindrome_dp(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s


        dp = [[0 for _ in s] for _ in s]
        for i in range(len(s)):
            dp[i][i] = 1

        res = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if (j - i < 2 or dp[i+1][j-1] == 1) and s[j] == s[i]:
                    dp[i][j] = 1
                    if j - i + 1 > len(res):
                        res = s[i:j+1]
                else:
                    continue
        return res



a = Solution()
s = 'aaabbbccccdfdf'
print a.longestPalindrome(s)