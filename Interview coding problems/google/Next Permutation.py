class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        if m <= 1:
            return
        # from right to left, find the first peak
        i = m - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        # print(i, nums[i])
        if i == 0 and nums[0] >= nums[1]:
            i, j = 0, m - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return
        else:
            # find the first element that's smaller than nums[i-1]
            j = i
            while j < m and nums[j] > nums[i-1]:
                j += 1
            # print(j-1, nums[j-1])
            nums[j-1], nums[i-1] = nums[i-1], nums[j-1]
            nums[i:] = sorted(nums[i:])
            # print(nums)
        return