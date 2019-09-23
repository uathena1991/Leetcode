"""
use set to record: cols, diags, antidiags
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, diag, antidiag = set(), set(), set()
        self.res = []
        def dfs(path, row):
            if row == n:
                self.res.append(['.'*x + 'Q'+'.'*(n-x-1) for x in path])
                return
            for c in range(n):
                if c in col or c + row in antidiag or c - row in diag:
                    continue
                col.add(c)
                antidiag.add(c + row)
                diag.add(c-row)
                dfs(path + [c], row + 1)
                col.remove(c)
                antidiag.remove(c+ row)
                diag.remove(c - row)

        dfs([], 0)
        return self.res
                
"""
method of record queens' row, col in a set.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(path, curr_setc):
            if not curr_setc:
                if len(path) == n:
                    self.res.append(['.'*x+'Q' + '.'*(n-x-1) for x in path])
                return
            for c in curr_setc:
                ## choose c
                # cal diagonal constraints:
                nr = len(path) + 1
                next_setc = set(range(n)) - set(path) - {c}
                for ri, ci in enumerate(path + [c]):
                    next_setc -= {ci + nr - ri}
                    next_setc -= {ci - nr + ri}

                dfs(path + [c], next_setc)

        self.res = []
        dfs([], set(range(n)))
        # print(self.res)
        return self.res

"""
method of record each cell's status
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def print_puzzle(puzzle):
            for t in puzzle:
                    print(t)
            print('\n')
        
        def update_puzzle(puzzle, r, c):
            """update puzzle if (r, c) is 'Queen',
            (scan from top to bottom row, so only consider puzzle[r:n][:])
            """
            for ci in range(n):
                puzzle[r][ci] = '.'
            for ri in range(n):
                puzzle[ri][c] = '.'   
            puzzle[r][c] = 'Q'
            step = 1
            for s in range(1, n - r):
                if c - s >= 0:
                    puzzle[r+s][c-s] = '.'
                if c + s < n:
                    puzzle[r+s][c+s] = '.'
            return puzzle
        

        def backtracking(r, puzzle, set_c):
            if r == n-1 and len(set_c) == 1:
                tmp = set_c.pop()
                if puzzle[r][tmp] == 'u':
                    puzzle[r][tmp] = 'Q'
                    self.res.append([''.join(x) for x in puzzle])
                return
            if not set_c or not any([x == 'u' for x in puzzle[r]]):
                return
            for c in set_c:
                if puzzle[r][c] == 'u':
                    ## choose r,c, next row        
                    old_puzzle = [[x for x in y] for y in puzzle]
                    backtracking(r + 1, update_puzzle(puzzle, r, c), set_c - {c})
                    puzzle = [[x for x in y] for y in old_puzzle]
                ## not choose r,c
                puzzle[r][c] = '.'

        self.res = []
        backtracking(0,  [['u'] * n for _ in range(n)], set(range(n)))
        return self.res
                    
            


            