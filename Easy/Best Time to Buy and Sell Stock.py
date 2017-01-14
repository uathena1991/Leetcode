class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices)<=1:
            return 0

        lowest = prices[0]
        for p in prices:
            curr_profit = p - lowest
            if curr_profit < 0:
                lowest = p
            max_profit = max(max_profit,curr_profit)
        return max_profit