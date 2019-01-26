from collections import Counter
import heapq as hq
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)
        heap = [(-counts[x], x) for x in counts]
        hq.heapify(heap)
        res, i = [], 0
        while i < k:
            res.append(hq.heappop(heap)[1])
            i += 1
        return res
        