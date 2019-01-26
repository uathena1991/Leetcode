class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        if len(nums) == 1 or nums[1] < nums[0]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # print(nums[mid], nums[low], nums[high])
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                low = mid
            else:
                high = mid


