class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check *
        if len(s) == 0:
            return True
        high = low = 0
        for i in s:
            if i == '(':
                high += 1
                low += 1
            elif i == ')':
                high -= 1
                low = max(low - 1, 0)
            else:
                low = max(low - 1, 0)
                high += 1
            if high < 0:
                return False
        return low == 0







a = Solution()
print a.checkValidString('((((*))********)')