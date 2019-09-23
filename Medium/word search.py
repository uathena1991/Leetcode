class Solution:
    def dfs(self, r, c, word, board):
        if not word:
            return True
        if r < 0 or r >= self.lenx or c < 0 or c >= self.leny or board[r][c] != word[0]:
            return False
        board[r][c] = '-!'
        res  = self.dfs(r+1, c, word[1:],board) or self.dfs(r-1, c, word[1:],board) or self.dfs(r, c + 1, word[1:], board) or self.dfs(r, c - 1, word[1:], board)
        board[r][c] = word[0]
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.lenx, self.leny = len(board), len(board[0])
        if self.lenx * self.leny < len(word):
            return False

        return any([self.dfs(x, y, word, board) for x in range(self.lenx) for y in range(self.leny)])