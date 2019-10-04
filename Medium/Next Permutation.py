class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenn = len(nums)
        i = lenn - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        if i > 0:
            turn = i-1
            while i < lenn:
                if nums[i] <= nums[turn]:
                    i-=1
                    break
                i += 1
            if i == lenn:
                i -= 1
            nums[i], nums[turn] = nums[turn], nums[i]
        else:
            turn = -1

        s, e = turn+1, lenn-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
