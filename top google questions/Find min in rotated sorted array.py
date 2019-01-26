class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid

        if low == high:
            return nums[low]
