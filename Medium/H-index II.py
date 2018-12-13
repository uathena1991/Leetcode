class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # O(nlogn + n)
        # print(citations)
        # n = len(citations)
        # for i in range(n):
        #     if citations[i] >= n-i:
        #         return n - i
        # return 0

        n = len(citations)
        low, high = 0, n-1
        while low <= high:
            mid = (low+high)//2
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                high = mid - 1
            else:
                low = mid + 1
        return n - high - 1


                