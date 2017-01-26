class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        while matrix:
            # using list.pop(idx) to add those to res and delete row_1 row_last 1st and last node in row_rest
            row_1 = matrix.pop(0)
            row_last = matrix.pop(-1) if matrix else []
            row_rest = matrix if matrix else []
            [res.append(x) for x in row_1]
            if row_rest and row_rest[0]:
                [res.append(x.pop(-1)) for x in row_rest]
            [res.append(x) for x in row_last[::-1]]
            if row_rest and row_rest[0]:
                [res.append(x.pop(0)) for x in row_rest[::-1]]
        return res









a = Solution()
m = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
m = [[1],[2],[3],[4],[5],[6],[7]]
print a.spiralOrder(m)