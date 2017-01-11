# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        # sort intervals by Interval.start
        sorted_intervals = sorted(intervals,key=lambda s: s.start)
        for i in sorted_intervals:
            if res and i.start <= res[-1].end:
                res[-1].end = max(i.end,res[-1].end)
            else:
                res.append(i)
        return res
