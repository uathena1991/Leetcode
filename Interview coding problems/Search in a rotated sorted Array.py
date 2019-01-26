class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l <= h:
            m = (l+h)//2
            if target == nums[m]:
                return m
            if target < nums[m]:
                if target < nums[l] and nums[l] <= nums[m]:
                    l = m + 1
                else:
                    h = m - 1
            else:
                if nums[m] < nums[l] and target > nums[h]:
                    h = m - 1
                else:
                    l = m + 1
        return -1