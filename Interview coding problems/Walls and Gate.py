"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Solution:
DFS (from each 0)
BFS()
"""

#  DFS:
class Solution():
	def dfs_solution(self, maps):
		def dfs_recursive(ridx, cidx, maps, dist):
			if ridx < 0 or ridx >= len(maps) or cidx < 0 or cidx >=len(maps[0]) or dist < maps[ridx][cidx]:
				return
			maps[ridx][cidx] = dist
			dfs_recursive(ridx-1, cidx, maps, dist+1)
			dfs_recursive(ridx+1, cidx, maps, dist+1)
			dfs_recursive(ridx, cidx-1, maps, dist+1)
			dfs_recursive(ridx, cidx+1, maps, dist+1)

		for ridx in range(len(maps)):
			for cidx in range(len(maps[0])):
				if maps[ridx][cidx] == 0:
					dfs_recursive(ridx, cidx, maps, 0)

		return maps

	def bfs_solution(self, maps):
		queues = []
		for ridx in range(len(maps)):
			for cidx in range(len(maps[0])):
				if maps[ridx][cidx] == 0:
					queues.append((ridx, cidx))
		dirs  =[[-1, 0], [1, 0], [0, 1], [0, -1]]
		while len(queues) > 0:
			curr = queues.pop()
			for dd in dirs:
				if not (0 <= curr[0] + dd[0] < len(maps)) or not (0 <= curr[1] + dd[1] < len(maps[0])) or \
					maps[curr[0] + dd[0]][curr[1] + dd[1]] < maps[curr[0]][curr[1]] + 1:
					continue
				maps[curr[0] + dd[0]][curr[1] + dd[1]] = maps[curr[0]][curr[1]] + 1
				queues.append([curr[0] + dd[0], curr[1] + dd[1]])

		return maps

