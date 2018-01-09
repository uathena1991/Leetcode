class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) < len(v2):
            v1 += [0 for _ in range(len(v2)-len(v1))]
        elif len(v1) > len(v2):
            v2 += [0 for _ in range(len(v1)-len(v2))]

        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                continue
        return 0


a = Solution()
print a.compareVersion('03.2', '10.2.1')