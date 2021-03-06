class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i != 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                dfs(nums, path + [nums[i]])
                visited[i] = False



        nums.sort()
        visited = [False for _ in nums]
        res = []
        dfs(nums, [])
        return res