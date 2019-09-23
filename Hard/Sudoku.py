from collections import defaultdict
import heapq as hq
class Solution:
	def solveSudoku(self, board) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		def dfs(num_undefined):
			if num_undefined == 0:
				return True
			r,c = prio_cands[-1]
			for i in set([str(i+1) for i in range(9)]) - rows[r] - cols[c] - squs[r//3*3 + c//3]:
				rows[r].add(i)
				cols[c].add(i)
				squs[r//3*3+c//3].add(i)
				board[r][c] = i
				prio_cands.pop()
				if dfs(num_undefined-1):
					return True
				rows[r].remove(i)
				cols[c].remove(i)
				squs[r//3*3+c//3].remove(i)
				board[r][c] = '.'
				prio_cands.append((r,c))
			return False


		rows, cols, squs = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
		# pre-processing
		for r in range(9):
			for c in range(9):
				if board[r][c] != '.':
					rows[r].add(board[r][c])
					cols[c].add(board[r][c])
					squs[r//3*3 + c//3].add(board[r][c])
		# create priority queue
		cands_dict = {}
		for r in range(9):
			for c in range(9):
				if board[r][c] == '.':
					cands_dict[(r,c)] = len(rows[r]) + len(cols[c]) + len(squs[r//3*3 + c//3])
		prio_cands = sorted(cands_dict, key = lambda x: cands_dict[x])
		# dfs and backtracking
		dfs(len(prio_cands))