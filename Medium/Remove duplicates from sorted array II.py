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
    			if idx<=1:
    				nums[idx] = n
    				idx+=1
    			elif n > nums[idx-2]:
    				nums[idx] = n
    				idx+=1
    		return idx

a = Solution()
nums = [1,1,1,2,2,2,3,3,3,3]
lens = a.removeDuplicates(nums)
print nums[:lens]
print lens