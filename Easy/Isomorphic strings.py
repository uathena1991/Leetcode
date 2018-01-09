class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = [0 for i in range(256)]
        map2 = [0 for i in range(256)]
        for i in range(len(s)):
            if map1[ord(s[i])] != map2[ord(t[i])]:
                return False
            map1[ord(s[i])] = i+1
            map2[ord(t[i])] = i+1
        return True

a = Solution()
print a.isIsomorphic('ab','ba')