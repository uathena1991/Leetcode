class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pre = float('-inf')
        res = []
        for i,s in enumerate(S):
            if s == C:
                pre = i
            res.append(abs(i - pre))


        pre = float('inf')
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                pre = i
            res[i] = min(res[i], abs(pre-i))

        return res
