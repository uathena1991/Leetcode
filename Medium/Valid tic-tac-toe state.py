class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def iswin(player):
            triple = player*3
            if triple in board or triple in transp_b or board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
                return True
            else:
                return False
        num_x = sum([sum([y == 'X' for y in x]) for x in board])
        num_o = sum([sum([y == 'O' for y in x]) for x in board])
        if num_o > num_x or num_x - num_o > 1:
            return False
        transp_b = [''.join([x[i] for x in board]) for i in range(3)]
        if (iswin('X') and num_x == num_o) or (iswin('O') and num_x > num_o):
            return False

        return True