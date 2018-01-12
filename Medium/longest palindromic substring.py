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


a = Solution()
s = 'aaabbbccccdfdf'
print a.longestPalindrome(s)