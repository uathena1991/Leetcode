class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        0: 0 -- > 0
        1: 1 -- > 1
        2: 1 -- > 0
        3: 0 -- > 1
        """
        def counts(r, c):
            dirs = [[1, 0], [0, 1], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            res = 0
            for dx, dy in dirs:
                nx, ny = r + dx, c + dy
                if (0 <= nx < len(board) and 0 <= ny < len(board[0])) and (board[nx][ny] == 1 or board[nx][ny] == 2):
                    res += 1
            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 1 and not (2 <= counts(r,c) <= 3):
                    board[r][c] = 2 # 1 -- > 0
                elif board[r][c] == 0 and counts(r,c) == 3:
                    board[r][c] = 3 # 0 -- > 1

        # print(board)
        # code back to 0, 1
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] %= 2