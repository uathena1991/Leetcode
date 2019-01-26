class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount in coins:
            return 1
        if amount <= 0:
            return 0
        coins.sort()
        if amount < coins[0]:
            return -1
        if len(coins) == 1:
            return -1 if amount%coins[0] != 0 else amount//coins[0]
        dp = [float('inf') for _ in range(amount+1)]
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                pre = [dp[i-c] for c in coins if i >= c]
                if pre:
                    dp[i] = min(pre) + 1
        # print(dp)
        return dp[amount] if dp[amount] < float('inf') else -1