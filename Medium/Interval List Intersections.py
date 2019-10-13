class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        sA = sorted(A, key = lambda x:x[0])
        sB = sorted(B, key = lambda x:x[0])
        i, j, res = 0, 0, []
        while i < len(sA) and j < len(sB):
            s1,e1 = sA[i]
            s2,e2 = sB[j]
            if e1 < s2:
                i += 1
            elif e2 < s1:
                j += 1
            else: # overlap
                res.append([max(s1,s2), min(e1, e2)])
                if e1 < e2:
                    i += 1
                else:
                    j += 1
        return res
