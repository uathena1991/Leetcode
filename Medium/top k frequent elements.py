class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import heappush, heappop
        from collections import defaultdict
        dict_map = defaultdict(int)
        for nn in nums:
            dict_map[nn] += 1
        heap = []
        for nn in dict_map:
            heappush(heap, (dict_map[nn], nn))
        while len(heap) > k:
            heappop(heap)
        return [x[1] for x in heap[::-1]]
