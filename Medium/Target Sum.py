from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        prev, curr = defaultdict(int), defaultdict(int)
        prev[0] = 1
        for n in nums:
            curr = defaultdict(int)
            for ii in prev:
                curr[ii+n] += prev[ii]
                curr[ii-n] += prev[ii]
            prev = curr
        return curr[S]