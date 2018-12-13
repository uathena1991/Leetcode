"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.


"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        longest = min(1, len(nums))
        for idx, nn in enumerate(nums):
            top, down = nums[idx]+1, nums[idx]-1
            while top in set_nums or down in set_nums:
                if top in set_nums:
                    set_nums.remove(top)
                    top += 1
                if down in set_nums:
                    set_nums.remove(down)
                    down -= 1
            longest = max(longest, top-down-1)
        return longest


            