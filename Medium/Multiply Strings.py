class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                res += int(num1[i])*10**(len(num1)-i-1)*int(num2[j])*10**(len(num2)-j-1)
        return str(res)

a = Solution()
print a.multiply('12','123')