class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pools = {'6':'9', '9':'6', '1':'1', '8':'8', '0':'0'}
        rev = num[::-1]
        for i in range(len(num)):
            if num[i] not in pools or pools[num[i]] != rev[i]:
                return False

        return True
    