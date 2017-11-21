class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        st1_sell = [0]
        st1_nothing = [-prices[0]]
        st0_buy = [-prices[0]]
        st0_nothing = [0]
        for i in range(1,len(prices)):
            st0_buy.append(st0_nothing[-1] - prices[i])
            st0_nothing.append(max(st1_sell[-1], st0_nothing[-1]))
            st1_sell.append(max(st1_nothing[-1], st0_buy[-1]) + prices[i])
            st1_nothing.append(max(st1_nothing[-1], st0_buy[-1]))

        return max(st1_sell[-1], st0_nothing[-1])