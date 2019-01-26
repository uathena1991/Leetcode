from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_cts = defaultdict(int)
        l, r, res = 0, 0, 0
        while r < len(s):
            curr_cts[s[r]] += 1
            if len(curr_cts) < 3:
                res = max(res, r - l + 1)
                # print(l, r, curr_cts, res, s[l:r+1])
            else:
                while len(curr_cts) > 2:
                    curr_cts[s[l]] -= 1
                    if curr_cts[s[l]] == 0:
                        del curr_cts[s[l]]
                    l += 1
                # print('del',s[l:r+1])
            r += 1
        return res