class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in range(len(nums))]
        curr_prod = 1
        for i in range(1, len(nums)):
            curr_prod *= nums[i-1]
            res[i] = curr_prod
        curr_prod = 1
        for i in range(len(nums)-2, -1, -1):
            curr_prod *= nums[i+1]
            res[i] *= curr_prod
        return res