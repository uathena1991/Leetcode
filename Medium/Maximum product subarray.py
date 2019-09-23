class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        global_max, local_max, local_min = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            local_max, local_min = max(local_min*n, local_max*n, n), min(local_max*n, local_min*n, n)
            global_max = max(local_max, local_min, global_max)
        return global_max