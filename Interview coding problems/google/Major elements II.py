class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1, cand2 = None, None
        c1,c2 = 0, 0
        for i in nums:
            if i == cand1:
                c1 += 1
            elif i == cand2:
                c2 += 1
            elif c1 == 0:
                cand1, c1 = i, 1
            elif c2 == 0:
                cand2, c2 = i, 1
            else:
                c1 -= 1
                c2 -= 1
        # check
        c1, c2, res = 0, 0, []
        for i in nums:
            if i == cand1:
                c1 += 1
            if i == cand2:
                c2 += 1
        if c1 > len(nums) // 3:
            res.append(cand1)
        if c2 > len(nums)//3:
            res.append(cand2)
        return res