# delete and append
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        idx = 0
        counts = 0
        while idx + counts < (len(nums)):
            if nums[idx] != 0:
                idx += 1
            else:
                del(nums[idx])
                nums.append(0)
                counts += 1
            # print nums


# slow and fast points
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1


A = Solution()
nums = [0,0,1, 0 , 2]
A.moveZeroes(nums)
print nums