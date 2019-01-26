class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = len(arr)
        if m <= 1:
            return m
        curr_max, cts = 0, 0
        for i in range(m):
            curr_max = max(curr_max, arr[i])
            if curr_max == i:
                cts += 1
        return cts

"""
Let's try to find the smallest left-most chunk. 
If the first k elements are [0, 1, ..., k-1], then it can be broken into a chunk, and we have a smaller instance of the same problem.

We can check whether k+1 elements chosen from [0, 1, ..., n-1] are [0, 1, ..., k] by checking whether the maximum of that choice is k.
"""