class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for cd in candidates:
            for t in range(target + 1):
                if t >= cd:
                    dp[t] += [x+[cd] for x in dp[t - cd]]
        return dp[target]





    """
    With no repetition
    """
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        dp[0] = [[]]
        for ca in candidates:
            for t in range(target, -1, -1):
                if t >= ca:
                    dp[t] += [sorted(x + [ca]) for x in dp[t-ca]]
            # print(ca, dp)
        res = []
        for dd in dp[-1]:
            if dd not in res:
                res.append(dd)
        return res