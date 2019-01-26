class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        self.res = []
        def backtracking(curr, rest):
            if not rest:
                self.res.append(curr)
                return
            for cr in rest:
                backtracking(curr + [cr], rest - {cr})


        backtracking([], set(nums))
        # print(self.res)
        return self.res
    