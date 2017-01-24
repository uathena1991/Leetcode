"""
1. sort the list
2. Add another variable to keep track of length of result list res.
3. if next elements == prev, only append the new res; otherwise, append from the scratch
"""
class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = [[],[nums[0]]]
        pre = nums[0]
        curr_len = [1,2] # track current res length
        for idx in range(1,len(nums)):
            curr = nums[idx]
            if pre != curr:
                for i in range(curr_len[-1]):
                    res.append(res[i]+[curr])
            else:
                for i in range(curr_len[-2],curr_len[-1]):
                    res.append(res[i]+[curr])
            curr_len.append(len(res))
            pre = nums[idx]
        res.sort()
        return res

a = Solution()
print a.subsetsWithDup([1,2,2])