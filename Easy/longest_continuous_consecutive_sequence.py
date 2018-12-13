class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = min(1, len(nums))
        left, right = 0, 1
        while left < len(nums) and right < len(nums):
            while right < len(nums) and nums[right - 1] < nums[right]:
                right += 1
            longest = max(longest, right - left)
            # print(left, right, longest)

            left, right = right, right + 1
        return longest