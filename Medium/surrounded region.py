class Solution:
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		# dfs
		def dfs(r,c, board):
			if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or board[r][c] != 'O':
				return
			board[r][c] = 'V'
			dfs(r+1, c, board)
			dfs(r-1, c, board)
			dfs(r, c+1, board)
			dfs(r, c-1, board)

		if len(board) <= 2 or len(board[0]) <= 2:
			return
		for r in range(len(board)):
			dfs(r, 0, board)
			dfs(r, len(board[0])-1, board)
		for c in range(len(board[0])):
			dfs(0, c, board)
			dfs(len(board)-1, c, board)

		for r in range(len(board)):
			for j in range(len(board[0])):
				if board[r][j] == 'O':
					board[r][j] = 'X'
		for r in range(len(board)):
			for j in range(len(board[0])):
				if board[r][j] == 'V':
					board[r][j] = 'O'

	def solve_bfs(self, board):
		"""
		bfs solution
		:param board:
		:return:
		"""
		if len(board) <= 2 or len(board[0]) <= 2:
			return
		queues = []
		dirs = [(0,1), (0,-1), (1, 0), (-1, 0)]
		for i in range(len(board)):
			if board[i][0] == 'O':
				board[i][0] = 'V'
				queues.append((i, 0))
			if board[i][-1] == 'O':
				board[i][-1] = 'V'
				queues.append((i, len(board)-1))
		for j in range(len(board[0])):
			if board[0][j] == 'O':
				board[0][j] = 'V'
				queues.append((0, j))
			if board[-1][j] == 'O':
				board[-1][j] = 'V'
				queues.append((len(board)-1, j))

		while len(queues) > 0:
			cx,cy = queues.pop()
			for dx,dy in dirs:
				if 0 <= cx+dx < len(board) and 0 <= cy+dy < len(board[0]) and board[cx+dx][cy+dy] == 'O':
					board[cx+dx][cy+dy] = 'V'
					queues.append((cx+dx, cy+dy))
		for x in range(len(board)):
			for y in range(len(board[0])):
				if board[x][y] == 'O':
					board[x][y] = 'X'
		for x in range(len(board)):
			for y in range(len(board[0])):
				if board[x][y] == 'V':
					board[x][y] = 'O'



