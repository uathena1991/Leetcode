class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        len_a = len(A)
        len_b = len(B)
        rep = len_b/len_a + (not len_b/len_a == len_b*1.0/len_a)
        for i in range(2):
            if B in A*(rep + i):
                return rep + i
        return -1
        