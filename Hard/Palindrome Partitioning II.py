# class Solution:
"""
TLE solution: backtracking
"""
#     def is_pal(self, s):
#             return s == s[::-1]
#
#     def helper(self, s, curr_list):
#         if len(s) == 0 and self.min_cut >= len(curr_list) - 1:
#             self.min_cut = min(len(curr_list) - 1, self.min_cut)
#             return
#         if len(curr_list) - 1 > self.min_cut:
#             return
#         for i in range(1, len(s) + 1):
#             if self.is_pal(s[:i]):
#                 self.helper(s[i:], curr_list + [s[:i]])
#
#     def minCut(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#
#
#         self.min_cut = len(s) - 1
#         self.helper(s, [])
#         return self.min_cut
"""
DP problem 
"""
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [x for x in range(len(s))]
        pal = [[0 for _ in s] for _ in s]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[j] == s[i] and (i - j < 2 or pal[j+1][i-1]==1):
                    pal[j][i] = 1
                    if j == 0:
                        d[i] = 0
                    else:
                        if d[j-1] + 1 < d[i]:
                            d[i] = d[j-1] + 1

        return d[len(s) - 1]




print(Solution().minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))