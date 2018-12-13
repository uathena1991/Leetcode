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


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)
        s0, s1 = 0, 0
        for n in range(len(nums)):
            if n % 2 == 0:
                s0 = max(s0 + nums[n], s1)
            else:
                s1 = max(s1 + nums[n], s0)
            # print(n, s0, s1)

        return max(s0, s1)

