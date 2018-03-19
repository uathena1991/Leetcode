class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        t_sum = sum([x for x in nums])
        res = n * (n + 1) /2 - t_sum
        # print res

        return res


print Solution().missingNumber([1,2])