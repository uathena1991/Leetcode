class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1
        low, high = 0, len(nums) - 1
        while low <=high:
            mid = (low + high)//2
            if nums[mid] > nums[mid + 1]:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    high = mid
            else:
                low = mid

