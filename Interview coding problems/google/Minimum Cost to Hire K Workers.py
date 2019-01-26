import heapq as hq
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        sorted_wq = sorted([(w/q, q, w) for q,w in zip(quality, wage)])
        best, sum_q =  float('inf'), 0
        heap = []
        for r, q, w in sorted_wq:
            hq.heappush(heap, -q)
            sum_q += q
            if len(heap) > K:
                sum_q += hq.heappop(heap)
            if len(heap) == K:
                best = min(best, r * sum_q)

        return best