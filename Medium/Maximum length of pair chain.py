class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        len_pairs = len(pairs)
        pairs.sort()
        if len_pairs <= 1:
            return len_pairs
        dp = [1 for _ in range(len_pairs)]
        for i in range(len_pairs):
            tmp = [dp[j] for j in range(i) if pairs[j][1] < pairs[i][0]]
            if tmp:
                dp[i] = max(tmp) + 1

        return max(dp)




"""
    So smart...
"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        max_len, curr_tail = 0, -float('inf')
        for p in pairs:
            if curr_tail < p[0]:
                max_len += 1
                curr_tail = p[1]

        return max_len