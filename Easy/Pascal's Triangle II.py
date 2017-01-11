class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            t = self.getRow(rowIndex-1)
            return [x+y for x,y in zip([0]+t,t+[0])]

a = Solution()
print a.getRow(15)
