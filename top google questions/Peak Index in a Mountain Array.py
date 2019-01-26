class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high)//2
            if mid == low:
                return high if A[low] < A[high] else low
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            if A[mid] > A[mid-1]:
                low = mid
            else:
                high = mid

        if low == high:
            return low