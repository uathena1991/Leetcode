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
		m = len(prices)
		if m <= 1:
			return 0
		if k >= m//2:
			return sum([prices[i] - prices[i-1] for i in range(1, m)  if prices[i] > prices[i-1]])
		max_prof = 0
		pre_dp = [0] * m
		curr_dp = [0] * m
		for i in range(1, k+1):
			curr_dp = [0] * m
			tmp_max1 = [pre_dp[d] - prices[d] for d in range(m)]
			tmp_max2 = [max(tmp_max1[:d+1]) for d in range(m)]
			for d in range(1, m):
				curr_dp[d] = max(curr_dp[d-1], tmp_max2[d-1] + prices[d])
				# tmp_max[d] = max(tmp_max[:d+1])
			max_prof = max(max_prof, max(curr_dp))
			# print(sum([pre_dp[i] ==  curr_dp[i] for i in range(m)]))
			pre_dp = curr_dp


		return max_prof
