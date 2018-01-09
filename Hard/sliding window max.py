class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        d = deque()
        out = []
        for i,n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += [i]
            if d[0] == i - k: # if max is out of range
                d.popleft()
            if i >= k-1: # if len(d) == k
                out += [nums[d[0]]]
        return out

