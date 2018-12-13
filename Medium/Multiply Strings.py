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


class Solution2:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def sub_multi(a,b):
            res = 0
            for idx,i in enumerate(a[::-1]):
                res += int(i) * int(b) * (10 **idx)
            return res
        short, long = (num1, num2) if len(num1) < len(num2) else (num2,num1)
        sum = 0
        for idx, x in enumerate(short[::-1]):
            sum += sub_multi(long, x) * (10 ** idx)
        return str(sum)


a = Solution()
print a.multiply('12','123')