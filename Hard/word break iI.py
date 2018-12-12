class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def dfs(s, wordDict, memo):
            if len(s) == 0:
                return []
            if s in memo:
                return memo[s]
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(s) == len(word):
                    res.append(word)
                else:
                    tmp = dfs(s[len(word):], wordDict, memo)
                    for tt in tmp:
                        res.append(word + " " + tt)

            memo[s] = res
            return res

        self.res = []
        memo = dict()
        return dfs(s, wordDict, memo)
