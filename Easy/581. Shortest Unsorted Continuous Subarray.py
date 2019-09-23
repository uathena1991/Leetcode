"""
Stack
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = len(nums)-1, 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                l = min(l, stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums)-1,-1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                r = max(r, stack.pop())
            stack.append(i)

        return r - l + 1 if r > l else 0

"""
Sorting
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for l, (on, sn) in enumerate(zip(nums, sorted_nums)):
            if on != sn:
                break
        for r in range(len(nums)-1, -1, -1):
            if nums[r] != sorted_nums[r]:
                break
        return r - l + 1 if r > l else 0




