class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        max_rob = [0 for _ in range(len(nums))]
        max_rob2 = [0 for _ in range(len(nums))]
        # if the robber robs the first house in the list
        max_rob[0] = nums[0]
        max_rob[1] = max_rob[0]
        for i in range(2, len(nums)-1):
            max_rob[i] = max(max_rob[i-2] + nums[i], max_rob[i-1])
        # last house couldn't be robbed
        max_rob[-1] = max_rob[-2]

        # if the robber doesn't robs the first house in the list
        max_rob2[0] = 0
        max_rob2[1] = nums[1]
        for i in range(2, len(nums)):
            max_rob2[i] = max(max_rob2[i-2] + nums[i], max_rob2[i-1])
        # last house could be robbed
        max_rob2[-1] = max(max_rob2[-3] + nums[-1], max_rob2[-2])
        # print max_rob
        # print max_rob2
        return max(max_rob[-1], max_rob2[-1])