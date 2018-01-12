class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        N = len(s)
        for c in range(2*N - 1):
            left = c/2
            right = left + c%2
            while left >= 0 and right < N and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

        return result
