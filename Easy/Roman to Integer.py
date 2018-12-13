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


    class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        lastvalue= 4000
        romanToInt={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        lastborrow = 4000
        for c in s:
            if lastborrow < romanToInt[c]:
                res -= 2*lastborrow
            res += romanToInt[c]
            lastborrow = romanToInt[c]
        return res


        