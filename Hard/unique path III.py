class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(r, c, board, numstep):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1 or board[r][c] == 1:
                return
            if grid[r][c] == 2:
                # print(numstep)
                if numstep == num0 + 1:
                    self.res += 1
                return
            board[r][c] = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, board, numstep + 1)
            board[r][c] = 0

        m, n = len(grid), len(grid[0])
        board = [[0 for _ in range(n)] for _ in range(m)]
        num0 = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    sr, sc = r, c
                elif grid[r][c] == -1:
                    board[r][c] = 1
                elif grid[r][c] == 0:
                    num0 += 1
        self.res = 0
        dfs(sr, sc, board, 0)
        return self.res






