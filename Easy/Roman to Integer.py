class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        elements = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        if len(s) < 1:
            return res
        if len(s) == 1:
            return elements[s]
        curr = s[0]
        nxt = s[1]
        for i in range(len(s)):
            curr = s[i]
            if i == len(s)-1:
                nxt = s[i]
            else:
                nxt = s[i+1]
            if elements[curr] < elements[nxt]:
                res += elements[curr]*(-1)
            else:
                res += elements[curr]
        return res


        