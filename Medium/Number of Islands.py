"""
Test cases:
[["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
[["1","1","0","1","1"],["1","0","1","0","1"],["1","1","0","0","1"]]

"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        # add 0 to the four edges
        new_grid = [["0" for x in range(len(grid[0])+2)]]
        for i in range(len(grid)):
            new_grid.append(["0"]+grid[i]+["0"])
        new_grid.append(["0" for x in range(len(grid[0])+2)])
        # labeling
        counts = 0
        visited = [[0 for x in range(len(new_grid[0]))] for y in range(len(new_grid))] # visited or not 0 is no, 1 is yes
        for row in range(1, len(new_grid)-1):
            for col in range(1,len(new_grid[0])-1):
                if new_grid[row][col] == "1": # land
                    if visited[row][col] + visited[row-1][col] + visited[row+1][col] + visited[row][col-1] + visited[row][col+1] == 0:
                        counts += 1
                        visited[row][col] = counts
                        # dfs
                        new_neighbours = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                        while len(new_neighbours) != 0:
                            # print new_neighbours
                            curr_row, curr_col = new_neighbours.pop()
                            # check curr location
                            if visited[curr_row][curr_col] == 0 and new_grid[curr_row][curr_col] == "1":
                                visited[curr_row][curr_col] = counts
                                # add new neighbours into the sets
                                if visited[curr_row - 1][curr_col] == 0 and new_grid[curr_row - 1][curr_col] == "1": # up
                                    new_neighbours.append((curr_row - 1, curr_col))
                                if visited[curr_row + 1][curr_col] == 0 and new_grid[curr_row + 1][curr_col] == "1": # down
                                    new_neighbours.append((curr_row + 1, curr_col))
                                if visited[curr_row][curr_col - 1] == 0 and new_grid[curr_row][curr_col - 1] == "1": # left
                                    new_neighbours.append((curr_row, curr_col - 1))
                                if visited[curr_row][curr_col + 1] == 0 and new_grid[curr_row][curr_col + 1] == "1": # right
                                    new_neighbours.append((curr_row, curr_col + 1))
        return counts




# fantastic!
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))