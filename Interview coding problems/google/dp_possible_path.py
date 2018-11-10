"""
第一题：矩阵从左上角到右下角有多少种走法
给定一个矩形的长宽，用多少种方法可以从左上角走到右上角 （每一步，只能向正右、右上 或 右下走）
Follow up 1：如果给矩形里的三个点，要求解决上述问题的同时，经过这三个点
Follow up 2：如何判断这三个点一定是合理的，即存在路径
Follow up 3：如果给你一个H，要求你的路径必须向下越过H这个界，怎么做 --- (All - those without H)
Follow up 4：要经过某些特定row怎么走？要先经过一个row再经过另一个row怎么走？ -- (SAME as asking Follow up 3, H = max(row_i)
"""
"""
The idea is: segment the matrix"""

def dp_path(num_rows, num_columns):
	if num_rows * num_columns == 0:
		return 0
	if num_rows == 1 or num_columns == 1:
		return 1
	dp = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
	dp[0][0] = 1
	for c in range(1, num_columns):
		dp[0][c] = dp[0][c-1] + dp[1][c-1]
		for r in range(1, num_rows-1):
			dp[r][c] = dp[r-1][c-1] + dp[r][c-1] + dp[r+1][c-1]
		dp[num_rows-1][c] = dp[num_rows-1][c-1] + dp[num_rows-2][c-1]
	print(dp)
	return dp[0][-1]
print(dp_path(4,6))
