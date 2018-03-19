class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # use tuple to record appearance of each number (and corresponding idx for row/column/square)
        counts = []
        for r_idx, row in enumerate(board):
            for c_idx, char in enumerate(row):
                if char != '.':
                    counts.append((r_idx, char))
                    counts.append((char, c_idx))
                    counts.append((r_idx/3, c_idx/3, char))
        return len(counts) == len(set(counts))

sodu = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
print Solution().isValidSudoku(sodu)