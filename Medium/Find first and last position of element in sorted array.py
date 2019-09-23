class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find first
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h)//2
            if nums[m] == target:
                if (m > 0 and nums[m-1] < target) or m == 0:
                    break
                else:
                    h = m
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1
        if l > h:
            return [-1, -1]

        first = m
        # find last
        l, h = m, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                if (m < len(nums)-1 and nums[m+1] > target) or m == len(nums)-1:
                    break
                else:
                    l = m + 1
            else:
                h = m

        return [first, m]


