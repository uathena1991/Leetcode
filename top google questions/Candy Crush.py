class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        def check_line(lidx, mask, cond = True):
            if cond: # check rows
                start, end = 0, 0
                while end < self.col:
                    if board[lidx][start] == 0:
                        start += 1
                        end = start
                        continue
                    while end < self.col and board[lidx][start] == board[lidx][end]:
                        end += 1
                    if end - start >= 3:
                        # print(board[lidx][start], start, end)
                        for i in range(start, end):
                            mask.add((lidx, i))
                    start, end = end, end + 1

            else: # check columns
                start, end = 0, 0
                while end < self.row:
                    if board[start][lidx] == 0:
                        start += 1
                        end = start
                        continue
                    while end < self.row and board[start][lidx] == board[end][lidx]:
                        end += 1
                    if end - start >= 3:
                        for i in range(start, end):
                            mask.add((i, lidx))
                    start, end = end, end + 1
            # if change:
            #     print("change", lidx, change)
            #     print(mask)
            return mask


        def modify(ridx, board):
            nonzeros = [x for x in board[ridx] if x != 0]
            return [0] * (len(board[ridx]) - len(nonzeros)) + nonzeros


        # main function
        if not board or not board[0]:
            return board
        # transpose board
        board = [[board[r][c] for r in range(len(board))] for c in range(len(board[0]))]
        # print(board)
        self.row, self.col = len(board), len(board[0])
        mask = {3}
        while len(mask) > 0:
            # mark rows/columns that need to be changed as -1
            # row
            mask = set()

            for r in range(self.row):
                mask = check_line(r, mask, True)
            # column
            for c in range(self.col):
                mask = check_line(c, mask, False)
            # print(change, mask)
            # Modify
            for (i,j) in mask:
                board[i][j] = 0
            for r in range(self.row):
                board[r][:] = modify(r, board)
            # print("modify", board)
            # print("\n")

        # transpose board back
        board = [[board[r][c] for r in range(len(board))] for c in range(len(board[0]))]

        return board


