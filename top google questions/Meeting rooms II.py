# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        counts = 0
        si, ei = 0, 0
        while si < len(intervals):
            if starts[si] >= ends[ei]:
                counts -= 1
                ei += 1

            counts += 1
            si += 1

        return counts

