class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                dfs(nums, path + [nums[i]])
                visited[i] = False

		if not nums:
			return [[]]
        res = []
        visited = [False for _ in nums]
        dfs(nums, [])
        return res