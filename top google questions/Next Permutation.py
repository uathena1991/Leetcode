class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
             return
        idx = len(nums) - 1

        # find the first none-decreasing element
        while idx >= 1 and nums[idx-1] >= nums[idx]:
                idx -= 1
        if idx == 0 and nums[0] >= nums[1]:
            l,r = 0, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return

        tochange = idx-1
        # find the smallest larger elements in nums[idx:] > nums[tochange]
        for i in range(len(nums)-1, idx-1, -1):
            if nums[tochange] < nums[i]:
                break
        nums[tochange], nums[i] = nums[i], nums[tochange]
        nums[tochange+1:] = nums[tochange+1:][::-1]
        return




class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        self.res = []
        def dfs(i, nums):
            if i ==  len(nums) - 1:
                self.res.append([x for x in nums])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, nums)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0, nums)
        return self.res







"""
DFS
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path, nums, visited):
            if len(path) == len(nums):
                self.res.append([x for x in path])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(path, nums, visited)
                    path.pop()
                    visited[i] = False


        if len(nums) <= 1:
            return [nums]
        self.res = []
        visited = [False for _ in nums]
        dfs([], nums, visited)
        return self.res


