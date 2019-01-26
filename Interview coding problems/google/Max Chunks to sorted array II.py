from collections import Counter
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1:
            return len(arr)

        sorted_arr = sorted(arr)
        cts = 0
        cter_arr, cter_sort = Counter(), Counter()
        for i in range(len(arr)):
            cter_arr[arr[i]] += 1
            cter_sort[sorted_arr[i]] += 1
            if cter_arr == cter_sort:
                cts += 1
                cter_arr, cter_sort = Counter(), Counter()

        return cts