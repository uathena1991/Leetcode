"""
O(NlogN), sort
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        if ln <= 1:
            return
        nums.sort(reverse = True)
        nums[1:ln:2], nums[0:ln:2] = nums[:ln//2], nums[ln//2:]

"""
O(N) and in place
"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        if ln <= 1:
            return
        for i in range(ln - 1):
            if (i % 2 == 0 and nums[i] > nums[i+1]) or (i % 2 != 0 and nums[i] < nums[i+1]): # curr should be smaller than next
                nums[i], nums[i+1] = nums[i+1], nums[i]

                