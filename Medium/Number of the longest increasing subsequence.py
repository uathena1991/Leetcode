"""
DP
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums
        # dp[i] = [length, # of subseqs with that length] fors nums[:i+1] -- including i
        dp = [[1, 1] for _ in range(len_nums)]
        for i in range(len_nums):
            tmp = (1,1)
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] <= dp[j][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
        max_len = max(dp)[0]

        return sum([dp[x][1] for x in range(len_nums) if dp[x][0] == max_len])
                    