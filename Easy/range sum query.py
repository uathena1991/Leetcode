class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_start = nums
        for n in range(1, len(nums)):
            self.sum_start[n] += self.sum_start[n-1]



    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.sum_start[j] - self.sum_start[i-1]
        else:
            return self.sum_start[j]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)