class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if (summ != 0 and summ % k != 0) or not nums:
            return False
        tar = summ // k
        nums.sort()
        if nums[-1] > tar:
            return False
        
        def dfs(groups):
            if not nums:
                return True
            v = nums.pop()
            for i, g in enumerate(groups):
                if v + g <= tar:
                    groups[i] += v
                    if dfs(groups):
                        return True
                    groups[i] -= v
                if not g:
                    break

            nums.append(v)
            return False
        
        groups = [0 for _ in range(k)]
        return dfs(groups)