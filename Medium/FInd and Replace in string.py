class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        pre_end = 0
        sources = [x for _, x in sorted(zip(indexes, sources))]
        targets = [x for _, x in sorted(zip(indexes, targets))]
        indexes.sort()
        # print(indexes, sources, targets)
        new_str = ''
        for i in range(len(indexes)):
            # print(indexes[i], sources[i], targets[i])
            # print(S[indexes[i]:len(sources[i])+indexes[i]])
            if len(sources[i]) <= len(S) - indexes[i] and S[indexes[i]:len(sources[i])+indexes[i]] == sources[i]:
                new_str += S[pre_end:indexes[i]]
                new_str += targets[i]
                pre_end = len(sources[i]) + indexes[i]
            # print(pre_end, new_str)
        # if pre_end != len(S) - 1:
        new_str += S[pre_end:len(S)]
        return new_str




S = 'abcd'
indexes = [1, 2]
sources = ['b', 'c']
targets = ['eee', 'ffff']
print(Solution().findReplaceString(S, indexes, sources, targets))