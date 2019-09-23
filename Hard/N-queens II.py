"""
dfs: use set to record col, row, diag (row - col), antidiag (row + col)
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        col, diag, antidiag = set(), set(), set()
        self.res = 0
        def dfs(row):
            if row == n:
                self.res += 1
            for c in range(n):
                if c in col or c + row in antidiag or c - row in diag:
                    continue
                col.add(c)
                antidiag.add(c+row)
                diag.add(c-row)
                dfs(row+1)
                col.remove(c)
                antidiag.remove(c+row)
                diag.remove(c-row)
        dfs(0)
        return self.res



"""
normal dfs recording path
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(path, curr_setc):
            if not curr_setc:
                if len(path) == n:
                    self.res += 1
                return
            for c in curr_setc:
                ## choose c
                # cal next row's possible cols
                next_c = set(range(n)) - set(path) - {c}
                nr = len(path) + 1
                for ri, ci in enumerate(path + [c]):
                    next_c -= {ci + nr - ri}
                    next_c -= {ci - nr + ri}
                dfs(path + [c], next_c)

                ## not choose c, continue

        self.res = 0
        dfs([], set(range(n)))
        return self.res

