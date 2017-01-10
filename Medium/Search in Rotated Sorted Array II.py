class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        for n in nums:
            if n == target:
                return True
        return False




a = Solution()
idx = a.search([1,3,1,1,1],3)
print idx