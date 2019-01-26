class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(cpath, num_l, num_r):
            if len(cpath)  == n * 2:
                self.res.append(cpath)
                return
            if num_l > 0:
                dfs(cpath + '(', num_l - 1, num_r)
            if num_r > num_l:
                dfs(cpath + ")", num_l, num_r - 1)

        if n  == 0:
            return []
        self.res = []
        dfs('', n, n)
        return self.res
