class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = dict()
        for i in range(len(strs)):
            sorted_i = ''.join(sorted(strs[i]))
            if sorted_i not in res:
                res[sorted_i] = [strs[i]]
            else:
                res[sorted_i].append(strs[i])
        return res.values()

a = Solution()
print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])