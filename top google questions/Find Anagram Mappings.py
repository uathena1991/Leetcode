class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        pi = dict()
        for i,b in enumerate(B):
            pi[b] = i
        return [pi[x] for x in A]