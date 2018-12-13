class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        ## worst: O(n)
        while low <= high:
            while low < high and nums[low] == nums[high]:
                low += 1
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[low]: # rotation on the left of mid
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] > nums[high]: # rotation is on the right of mid
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # low to high, ascending order
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False


