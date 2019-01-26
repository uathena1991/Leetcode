class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n - 1
        while low <= high:
            mid = (high + low) // 2
            mr, mc = mid // n, mid % n
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False