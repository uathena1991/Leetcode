class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days:
            return 0
        dp = [0 for _ in range(366)] # dp[0], sudo first day; dp[1]: first day, dp[365]: last day,
        durations = [1, 7, 30]
        dayset = set(days)
        for i in range(1, 366): # from last to first day
            if i in dayset:
                # buy: 1, 7 or 30
                dp[i] = min(dp[i - d] + c for c,d in zip(costs, durations))
            else:
                # do not buy, like previous day
                dp[i] = dp[i - 1] if i <= 365 else dp[i]
        return dp[-1]

