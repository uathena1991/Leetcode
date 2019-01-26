# from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False
        ln_map = {x:i for i, x in enumerate('abcdefghijklmnopqrstuvwxyz')}
        cts_s1 = [0 for _ in range(26)]
        cts_s2 = [0 for _ in range(26)]
        for i in range(len_s1):
            cts_s1[ln_map[s1[i]]] += 1
            cts_s2[ln_map[s2[i]]] += 1
        while i < len_s2 :
            i += 1
            if cts_s1 == cts_s2:
                return True
            if i < len_s2:
                cts_s2[ln_map[s2[i]]] += 1
                cts_s2[ln_map[s2[i-len_s1]]] -= 1
        return False