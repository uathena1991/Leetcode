class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        min_c = min(set(s), key = s.count)
        max_c = max(set(s), key = s.count)
        if s.count(min_c) + s.count(max_c) >= k:
            return len(s)
        else:
            return max([self.characterReplacement(t, k) for t in s.split(min_c)])

a = Solution()
s = 'aaabbbccccdfdf'
print a.characterReplacement(s,3)