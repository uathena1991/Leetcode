class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def counts_le(matrix, val):
            r, c = 0, len(matrix[0]) - 1
            ct = 0
            while r < len(matrix) and c >= 0:
                if matrix[r][c] <= val:
                    r += 1
                    ct += c+1
                else:
                    c -= 1
            return ct

        if k == 1:
            return matrix[0][0]
        if k == len(matrix) * len(matrix[0]):
            return matrix[-1][-1]
        low, high = matrix[0][0], matrix[-1][-1]
        count = 0
        while low <= high:
            mid = low + (high-low)//2
            count = counts_le(matrix, mid)
            # print(low, high, mid, count)
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        return low
