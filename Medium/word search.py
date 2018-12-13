class Solution:
    def dfs(self, word, cr, cc, board):
        # print(word, (curr_r, curr_c), neibor_locs)
        # print(path)
        if len(word) == 0:
            return True
        if cr < 0 or cr > self.max_row or cc < 0 or cc > self.max_col or board[cr][cc] != word[0]:
            return False
        board[cr][cc] = "!"
        res = self.dfs(word[1:], cr+1, cc, board) or self.dfs(word[1:], cr-1, cc, board) or self.dfs(word[1:], cr, cc+1, board) or self.dfs(word[1:], cr, cc-1, board)
        board[cr][cc] = word[0]
        return res


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.max_row = len(board) - 1
        self.max_col = len(board[0]) - 1
        for r in range(self.max_row + 1):
            for c in range(self.max_col + 1):
                if self.dfs(word, r, c, board):
                    return True

        return False


