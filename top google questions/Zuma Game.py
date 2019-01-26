from collections import Counter
class Solution:
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        def preprocessing(board):
            if not board:
                return
            res = [[board[0], 1]]
            for x in board[1:]:
                if res and x == res[-1][0]:
                    res[-1][1] += 1
                    if res[-1][1] >= 3:
                        res.pop()
                else:
                    res.append([x, 1])
            return res

        def list2string(lboard):
            return ''.join([x[0]*x[1] for x in lboard])

        def shorten(cboard):
            res = [[x[0], x[1]] for x in cboard]
            stat = True
            while stat:
                curr,x = 0, 1
                stat = False
                while x < len(res):
                    if res[x][0] == res[curr][0]:
                        res[curr][1] += res[x][1]
                        stat = True
                        del res[x]
                    else:
                        curr = x
                        x += 1
                x = 0
                while x < len(res):
                    if res[x][1] >= 3:
                        del res[x]
                    else:
                        x += 1
            return res

        def dfs(curr_board, curr_hand, step):
            # print("\n", curr_hand)
            # print(curr_board)
            # print(''.join([x[0]*x[1] for x in curr_board]))
            if not curr_hand:
                if curr_board:
                    # print('failed: no hand')
                    return False
            if not curr_board:
                # print('succ', step)
                self.min = min(self.min, step)
                return True
            # stat = True
            for idx, [ball, ct] in enumerate(curr_board):
                if ct == 2 and ball in curr_hand:
                    # stat = False
                    curr_hand[ball] -= 1
                    if curr_hand[ball] == 0:
                        del curr_hand[ball]
                    # print('before dfs', curr_board, idx, [ball,ct])
                    # print('before shorten', curr_board[:idx] + curr_board[idx+1:])
                    # print('aftre shorten', curr_board[:idx] + curr_board[idx+1:])
                    strboard = list2string(curr_board[:idx] + curr_board[idx+1:])
                    if strboard not in self.memo:
                        self.memo[strboard] = shorten(curr_board[:idx] + curr_board[idx+1:])
                    dfs(self.memo[strboard], curr_hand, step + 1)
                    # print("after dfs", curr_board, idx, [ball,ct])
                    curr_hand[ball] += 1

            # if there's no 2 consecutive balls
            # if stat: # singles
            for idx, [ball, ct] in enumerate(curr_board):
                if ct == 1 and ball in curr_hand:
                    # stat = False
                    curr_board[idx][1] += 1
                    curr_hand[ball] -= 1
                    if curr_hand[ball] == 0:
                        del curr_hand[ball]
                    # print('before shorten', curr_board)
                    strboard = list2string(curr_board)
                    if strboard not in self.memo:
                        self.memo[strboard] = shorten(curr_board)
                    dfs(self.memo[strboard], curr_hand, step + 1)
                    curr_hand[ball] += 1
                    curr_board[idx][1] -= 1
            # print('failed, after all')
            return False

        redunt = set(hand) - set(board)
        hand = [x for x in hand if x not in redunt]
        # print(hand)
        self.lenhand, self.min = len(hand), len(hand) + 2
        self.memo = dict() # memorize shorten of current combinations
        hand_cts = Counter(hand)
        board_cts = preprocessing(board)
        dfs(board_cts, hand_cts, 0)
        return self.min if self.min < len(hand) + 1 else -1

