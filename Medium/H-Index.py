class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # O(nlogn + n)
        # citations.sort()
        # n = len(citations)
        # for i in range(n):
        #     print(citations[i], )
        #     if citations[i] >= n-i:
        #         return n - i
        

        # bucket sort
        n = len(citations)
        bucket = [0 for _ in range(n+1)]
        for i in citations:
            if i < n:
                bucket[i] += 1
            else:
                bucket[n] += 1
        
        curr_sum = 0
        for bb in range(len(bucket)-1, -1, -1):
            curr_sum += bucket[bb]
            if curr_sum>= bb:
                return bb
        
        return 0
        