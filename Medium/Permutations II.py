class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res  = []
        self.len = len(nums)
        for i in range(len(nums)):
            if 0 < i < self.len and nums[i] == nums[i-1]:
                i += 1
                continue
            self.helper([nums[i]], nums[:i] + nums[i+1:])

        return self.res





    def helper(self, left, elements):
        if len(left) == self.len:
            self.res.append(left)
        for i in range(len(elements)):
            if  0 < i < len(elements) and elements[i] == elements[i-1]:
                i += 1
                continue
            self.helper(left + [elements[i]], elements[:i] + elements[i+1:])