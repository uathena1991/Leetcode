"""
Bottom up DP
space: O(n)
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        minpath = triangle[-1] # last row
        len_tri = len(triangle)
        for row in range(len_tri-2,-1,-1):
            for n in range(row+1):
                minpath[n] = min(minpath[n],minpath[n+1])+triangle[row][n]
        return minpath[0]

