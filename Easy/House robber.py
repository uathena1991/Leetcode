class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_rob = [0 for _ in range(len(nums))]
        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_rob[i] = max(max_rob[i-2] + nums[i], max_rob[i-1])
        
        return max_rob[-1]