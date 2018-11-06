"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""

"""
Idea: from each building (1) calculate min_distance of all '0's from it (BFS)... Then find the smallest number
"""
class Solution():
	def shortest(self, grid):
		import numpy as np
		dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		dist_map = []
		for r in range(len(grid)):
			for c in range(len(grid[0])):
				if grid[r][c] == 1:
					# update the grid
					queues = []
					dist_map.append(np.copy(grid))
					for dr, dc in dirs:
						if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]) and dist_map[-1][dr+r][dc+c] <= 0:
							queues.append((dr+r, dc+c))
							dist_map[-1][dr+r][dc+c] -= 1
					while len(queues) > 0:
						cr, cc = queues.pop(0)
						for dr, dc in dirs:
							nr, nc = dr + cr, dc + cc
							if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] <= 0 and (-dist_map[-1][nr][nc]> -(dist_map[-1][cr][cc] - 1) or dist_map[-1][nr][nc] == 0):
								queues.append((nr, nc))
								dist_map[-1][nr][nc] = dist_map[-1][cr][cc] - 1

		sum_dis = np.sum([[[-x if x < 0 else np.inf for x in y] for y in z] for z in dist_map], 0)
		print(dist_map)
		print(sum_dis)
		best_idx = np.unravel_index(np.argmin(sum_dis), sum_dis.shape)
		return best_idx



grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]
A = Solution()
print(A.shortest(grid))
