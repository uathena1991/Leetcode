class Solution():
	def find_rect(self, matrix):
		def dfs(matrix, i, j , visited, curr_rect):
			if i < 0 or i >= len(matrix) or j < 0 or j >=len(matrix[0]) or matrix[i][j] != 0:
				return
			visited[i][j] = 1
			curr_rect[0] = min(curr_rect[0], i)
			curr_rect[1] = min(curr_rect[1], j)
			curr_rect[2] = max(curr_rect[2], i)
			curr_rect[3] = max(curr_rect[3], j)
			dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
			for dd in dirs:
				rr = i + dd[0]
				cc = j + dd[1]
				dfs(matrix, rr, cc, visited, curr_rect)


		res = []
		visited = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
		for row in range(len(matrix)):
			for col in range(len(matrix[0])):
				if matrix[row, col] == 0 and visited[row][col] == 0:
					curr_rect = (row, col, row, col)
					dfs(matrix, row, col, visited, curr_rect)
					res.append(curr_rect)
		return res

