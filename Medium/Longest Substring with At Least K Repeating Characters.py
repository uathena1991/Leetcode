class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        least_freq = min(set(s), key = s.count)
        if s.count(least_freq) >= k:
            return len(s)
        else:
            return max([self.longestSubstring(subs, k) for subs in s.split(least_freq)])



a = Solution()
s = 'aaabbbccccdfdf'
print a.longestSubstring(s,3)