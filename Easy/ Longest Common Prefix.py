class Solution(object):
    def longestCommonPrefix(self, strs):
        """
            :type strs: List[str]
            :rtype: str
            """
        if strs:
            res = strs[0]
        else:
            return ""
        flag = 0
        while flag == 0:
            flag = 1
            for s in strs:
                if res != s[0:len(res)]:
                    res = res[:-1]
                    flag = 0
                    break
        return res



