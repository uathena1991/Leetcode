class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev = [0,0,0]
        for i, c in enumerate(costs):
            curr = [0,0,0]
            curr[0] = min(prev[1], prev[2]) + c[0]
            curr[1] = min(prev[0], prev[2]) + c[1]
            curr[2] = min(prev[1], prev[0]) + c[2]
            prev = curr
        return min(prev)