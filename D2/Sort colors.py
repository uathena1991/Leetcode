class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		idx0 = 0
		idx1 = 0
		for i in range(len(nums)):
			k = nums[i]
			nums[i] = 2
			if k <= 1:
				nums[idx1] = 1
				idx1+=1
			if k == 0:
				nums[idx0] = 0
				idx0+=1


a = Solution()
nums = [0,2,1,2,1,2,0,2]
a.sortColors(nums)
print nums