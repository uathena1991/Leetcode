from collections import defaultdict
class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        if len(wall) == 0:
            return 0
        if len(wall) == 1:
            return 1 if len(wall[0]) == 1 else 0
        sum_counts = defaultdict(int)
        for ww in wall:
            curr_sum  = 0
            for bc in ww[:-1]:
                curr_sum += bc
                sum_counts[curr_sum] += 1

        return len(wall) - sum_counts[max(sum_counts, key = lambda x: sum_counts[x])] if sum_counts else len(wall)
