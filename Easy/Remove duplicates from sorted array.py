class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            idx = 0
            for n in nums:
                if n != nums[idx]:
                    idx+=1
                    nums[idx] = n
		    print idx+1
            return idx+1
nums = [1,1,1,2,2,2,3,3,3,3]
a=Solution()
a.removeDuplicates(nums)
print nums[:3]