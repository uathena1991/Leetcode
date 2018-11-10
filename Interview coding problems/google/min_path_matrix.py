"""
0和1的grid，1是墙，0是路，从左上角走到右下角，最少多少步。 -- bfs
Follow-up: 现在说能把grid中的一个1变成0，问新的最小步数是多少步。


Google foobar:
You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod.
The map is represented as a matrix of 0sand 1s, where 0s are passable space and 1s are impassable walls.
The door out of the prison is at the top left (0,0) and the door into an escape pod is att he bottom right (w-1,h-1).

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod,
where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through,
counting both the entrance and exit nodes. The starting and ending positions are always passable (0).
 The map will always be solvable,though you may or may not need to remove a wall.
 The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed..
"""
"""
Understanding:
1) it doesn't make sense to revisited a node twice, since we are looking for minimum path
2) first solve the original one -- bfs
3) then with rebuild one wall -- it's like segment the matrix into two parts: start -- wall + wall -- end, and go over all walls, find the min path, 
and since you record min_path （from start point) at each location, can do two bfs, one from start, one from end, and iterate over all walls. 
"""
def min_path(matrix, sr, sc, er, ec):
	if len(matrix) == 0:
		return 0
	dirs = [(0, 1), (0, -1), (-1,0), (1, 0)]
	visited = [[0 if matrix[r][c] == 0 else 1 for c in range(len(matrix[0]))] for r in range(len(matrix))]
	min_path = [[len(matrix)*len(matrix[0]) for _ in matrix[0]] for _ in matrix]
	min_path[sr][sc] = 1
	curr_queue = [(sr,sc)]
	while len(curr_queue) > 0:
		cr, cc = curr_queue.pop(0)
		if cr == er and cc == ec:
			return min_path, min_path[cr][cc]
		# if matrix[cr][cc] == 0 and visited[cr][cc] == 0:
		visited[cr][cc] = 1
		for dr,dc in dirs:
			nr, nc = cr + dr, cc + dc
			if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and visited[nr][nc] == 0:
				curr_queue.append((nr, nc))
				min_path[nr][nc] = min_path[cr][cc] + 1
	# print(min_path)
	return min_path, -1 # can't be reached

def min_path_reconstruct(matrix):
	min_path_start, _ = min_path(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1)
	min_path_end, _ = min_path(matrix, len(matrix)-1, len(matrix[0])-1, 0, 0)
	min_res = len(matrix)*len(matrix[0])
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			if matrix[r][c] == 1:







matrix = [[0, 0, 0, 0, 0, 0],
   [1,1, 1, 1, 1, 0],
   [0, 0, 0, 0, 0, 0],
   [0, 1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1, 1],
   [0,0, 0, 0, 0, 0]]
router = min_path( matrix, 0, 0, len(matrix)-1, len(matrix[0])-1)
print(router)



