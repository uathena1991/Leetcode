class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)-1):
            curr_profit = prices[i+1]-prices[i]
            if curr_profit > 0:
                max_profit += curr_profit
        return max_profit


a = Solution()
a.maxProfit([7,3,2,3,8,9])