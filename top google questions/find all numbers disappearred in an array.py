"""
O(n), O(n) solution
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set([x+1 for x in range(len(nums))])
        for n in nums:
            if n in res:
                res.remove(n)
        return list(res)

    """
    O(n) without extra space!!! So brilliant!
    """
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i,n in enumerate(nums):
            idx = abs(n) - 1
            nums[idx] = - abs(nums[idx])

        return [x+1 for x in range(len(nums)) if nums[x] > 0]