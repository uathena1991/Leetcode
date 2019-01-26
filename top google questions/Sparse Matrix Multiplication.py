class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(r, c):
            ss = 0
            for i in range(len(A[0])):
                ss += A[r][i]*B[i][c]
            return ss


        row, col = len(A), len(B[0])
        if len(A[0]) != len(B):
            return -1
        res = [[float('inf')] * col for _ in range(row)]
        # print(res)
        for r in range(row):
            for c in range(col):
                res[r][c] = helper(r,c)
                # print(r,c, res[r][c], res)

        return res