class Solution:
	def maxProfit(self, k, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		"""
		dp problem:
		dp[k][d]: max profit on day d for <= K of transactions, k <= 2
		dp[0][d] = 0: d = 0, 1, .... len(prices) - 1
		dp[k][0] = 0
		
		dp[k][d] = max(dp[k][d-1], price[d] + dp[k-1][j] - price[j])        j < d (buy on day j, sell on day d)
											  pre_max
		"""

		if len(prices) <= 1:
			return 0
		max_prof = 0
		pre_dp = [0] * len(prices)
		curr_dp = [0] * len(prices)
		for i in range(1, k+1):
			curr_dp = [0] * len(prices)
			tmp_max = pre_dp[0] - prices[0]
			for d in range(1, len(prices)):
				curr_dp[d] = max(curr_dp[d-1], tmp_max + prices[d])
				tmp_max = max(tmp_max, pre_dp[d] - prices[d])
				max_prof = max(max_prof, curr_dp)
			pre_dp = curr_dp


		return max_prof
