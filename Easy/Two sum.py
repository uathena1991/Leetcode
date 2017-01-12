"""
O(n^2) Solution
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sorted_list = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


# O(n) solution: use dict, and nums[i] as key, and i as value, check if target-nums[i] already in the list
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for i in range(len(nums)):
            if target-nums[i] in res:
                return [i,res[target-nums[i]]]
            else:
                res[nums[i]] = i


# for sorted list: two pointers
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        while l < r:
            s = nums[l]+nums[r]
            if s == target:
                return [l+1,r+1]
            elif s < target:
                l+=1
            else:
                r-=1
			    
a = Solution()
print a.twoSum([3,2,4],6)