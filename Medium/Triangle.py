"""
<<<<<<< HEAD
DP problem
Note: equal cases
test case:
[[-1],[2,3],[1,-1,-3]]
[[2],[3,4],[6,5,7],[4,1,8,3]]
[[1],[-2,-5],[3,6,9],[-1,2,4,-3]]
[[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]
[[-1],[9,-2],[0,4,5],[7,4,-4,-5],[9,6,0,5,7],[9,2,-9,-4,5,-2],[-4,-9,-5,-7,-5,-5,-2],[-9,5,-6,-4,4,1,6,-4],[-4,3,9,-2,8,6,-9,-2,-2],[7,-6,9,8,-4,2,-4,-2,-1,-2],[0,3,2,4,0,-6,7,6,7,-5,2],[9,0,-8,6,4,6,2,5,-9,9,-1,-6],[6,-3,-4,-5,0,3,3,4,-6,-4,-7,7,3]]
=======
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
        res = []
        loc = [] # best prev row location
        idx = 0
        for i in triangle[-1]:
            res.append(i)
            loc.append(idx)
            idx+=1
        for row_idx in range(len(triangle)-2,-1,-1):
            curr_triangle = triangle[row_idx]
            for r in range(len(res)):
                if loc[r] == len(curr_triangle):
                    loc[r] = len(curr_triangle)-1
                else:
                    loc[r] = loc[r] if curr_triangle[loc[r]-1]>=curr_triangle[loc[r]] else loc[r]-1
                res[r] += curr_triangle[loc[r]]
        return res

a = Solution()
print(a.minimumTotal([[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]))


class Solution:
    def minimumTotal(self, triangle):
        """
        O(N) dp problem
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        dp_prev = triangle[0]
        for r in range(1, len(triangle)):
            dp_curr = [0 for _ in range(len(triangle[r]))]
            dp_curr[0] = dp_prev[0] + triangle[r][0]
            for c in range(1, len(triangle[r])-1):
                dp_curr[c] = min(dp_prev[c], dp_prev[c-1]) + triangle[r][c]
            dp_curr[len(triangle[r]) - 1] = dp_prev[-1] + triangle[r][len(triangle[r]) - 1]
            dp_prev = dp_curr

        return min(dp_curr)




