class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq as hq
        cts = Counter(nums)
        items = list(cts.keys())
        min_heap = [(cts[i], i) for i in items[:k]]
        hq.heapify(min_heap)
        print(cts)
        print(min_heap)
        for i in items[k:]:
            if cts[i] > min_heap[0][0]:
                hq.heappop(min_heap)
                hq.heappush(min_heap, (cts[i], i))
        print(min_heap)

        return [x[1] for x in min_heap[::-1]]


