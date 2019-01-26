# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        sort_intervals = sorted(intervals, key = lambda x: x.start)
        cts = 0
        pre, curr = sort_intervals[0], sort_intervals[1]
        idx = 1
        while idx < len(intervals):
            curr = sort_intervals[idx]
            if pre.end <= curr.start:
                pre = curr
            else:
                if pre.end >= curr.end: # delete current
                    pre = curr
                cts += 1
            idx += 1
        return cts

            