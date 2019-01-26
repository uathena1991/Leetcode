class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cts = Counter(s)
        scts = sorted(cts, key = lambda x: cts[x], reverse = True)
        res = ''
        for cc in scts:
            res +=  cc*cts[cc]
        return res


        