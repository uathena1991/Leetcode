from collections import defaultdict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        res = 0
        for n in counts:
            if n + 1 in counts:
                res = max(res, counts[n] + counts[n+1])

        return res

            