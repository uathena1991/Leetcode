class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        cts = 0
        memi = len(nums) - 1
        # maxci = 2
        for ai in range(len(nums) - 2):
            a  = nums[ai]
            if a == 0:
                continue
            maxci  = ai + 2
            for bi in range(ai+1, len(nums) - 1):
                b = nums[bi]
                if b == 0:
                    continue
                curr_max = a + b
                while maxci < len(nums) and nums[maxci] < curr_max:
                    maxci += 1
                cts += maxci - bi - 1

        return cts

                
