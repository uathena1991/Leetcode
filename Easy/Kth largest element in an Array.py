class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq as hq
        if len(nums) < 1:
            return
        # # # max heap # # #
        # neg_nums = [-x for x in nums]
        # hq.heapify(neg_nums)
        # res = 0
        # for i in range(k):
        #     res = hq.heappop(neg_nums
        # return -res

        # # # #min heap:  # # #
        min_heap = [-2**32+1 for _ in range(k)]
        hq.heapify(min_heap)
        for n in nums:
            if n > min_heap[0]:
                hq.heappop(min_heap)
                hq.heappush(min_heap, n)
        return min_heap[0]
