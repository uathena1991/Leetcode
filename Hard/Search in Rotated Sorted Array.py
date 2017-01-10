class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low_idx = 0
        high_idx = len(nums)-1
        while low_idx <= high_idx:
            mid_idx = (low_idx+high_idx)/2
            if nums[mid_idx] == target:
                return mid_idx
            if nums[low_idx] <= target < nums[mid_idx] or (nums[low_idx]>nums[mid_idx] and not(nums[mid_idx] <= target <= nums[high_idx])):
                high_idx = mid_idx-1
            else:
                low_idx = mid_idx+1
        return -1



a = Solution()
idx = a.search([1,3,5],1)
print idx