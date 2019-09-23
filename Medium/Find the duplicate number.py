"""
solve as a find circle in a chain problem.
Second half loop, 妙哉~~
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        slow, fast = nums[0], nums[0]
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2= nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow2