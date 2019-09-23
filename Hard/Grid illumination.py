from collections import defaultdict
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows, cols, diags, antidiags = defaultdict(int),  defaultdict(int), defaultdict(int), defaultdict(int)
        lamp_set = set([(x,y) for x, y in lamps])
        dirs = [[0,0], [1,1], [1,-1], [-1,-1], [-1, 1], [1,0], [-1,0], [0, 1], [0, -1]]
        for r, c in lamp_set:
            rows[r] += 1
            cols[c] += 1
            diags[r-c] += 1
            antidiags[r+c] += 1
        ans = []
        for r,c in queries:
            if rows[r] > 0 or cols[c] > 0 or diags[r-c] > 0 or antidiags[r+c] > 0:
                ans.append(1)
            else:
                ans.append(0)
            # update dicts
            for dr, dc in dirs:
                if (r + dr, c + dc) in lamp_set:
                    lamp_set.remove((r+dr, c+dc))
                    rows[r+dr] -= 1
                    cols[c+dc] -= 1
                    diags[r+dr - c - dc] -= 1
                    antidiags[r+dr + c + dc] -= 1
        return ans


