class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        divide and conquer
        """
        # print(matrix)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m,n = len(matrix) - 1, len(matrix[0]) - 1
        if (m+1)*(n+1) == 1:
            return True if matrix[m][n] == target else False

        # print(matrix)
        # print(lr, lc, matrix[lr][lc])
        # print(hr, hc, matrix[hr][hc])
        # print(mr, mc, matrix[mr][mc])
        # print("\n")
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        mr, mc = m//2, n//2
        if matrix[mr][mc] == target:
            return True
        elif matrix[mr][mc] < target: # righttop, same row but to the right, same column but to the bottom, rightbottom, leftbottom
            return self.searchMatrix([[matrix[x][y] for y in range(mc+1, n+1)] for x in range(mr)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc+1, n+1)] for x in range(mr, mr+1)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc, mc+1)] for x in range(mr+1, m+1)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc+1, n+1)] for x in range(mr+1, m+1)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc)] for x in range(mr+1, m+1)], target)
        else: # lefttop, right top, same row but to the left, same column but to the top, leftbottom
            return self.searchMatrix([[matrix[x][y] for y in range(mc)] for x in range(mr)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc+1, n+1)] for x in range(mr)], target) or  \
        self.searchMatrix([[matrix[x][y] for y in range(mc)] for x in range(mr, mr+1)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc, mc+1)] for x in range(mr)], target) or \
        self.searchMatrix([[matrix[x][y] for y in range(mc)] for x in range(mr+1, m+1)], target)

        return False



"""
binary search
"""
class Solution:
    def binary_search(self, matrix, target, start, direction):
        low = start
        hi = len(matrix) - 1 if direction == 1 else len(matrix[0]) - 1
        while hi >= low:
            mid = (hi + low) // 2
            if direction == 1: # vertical search
                if matrix[mid][start] == target:
                    return True
                elif matrix[mid][start] < target:
                    low = mid + 1
                else:
                    hi = mid - 1
            else: # horizontal search
                # print(start, mid, low, hi)
                if matrix[start][mid] == target:
                    return True
                elif matrix[start][mid] < target:
                    low = mid + 1
                else:
                    hi = mid - 1

        return False

"""
Smart!!!
if the currently-pointed-to value is larger than target we can move one row "up". Otherwise, if the currently-pointed-to value is smaller than target, we can move one column "right".

"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        for i in range(min(len(matrix[0]), len(matrix))):
            if self.binary_search(matrix, target, i, 1) or self.binary_search(matrix, target, i, 0):
                return True

        return False


