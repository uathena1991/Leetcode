"""
avoid using sum += ******, it's faster to just use string
"""
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = '0'*max((len(num2) - len(num1)), 0) + '0' + num1
        num2 = '0'*max((len(num1) - len(num2)), 0) + '0' + num2
        carry = 0
        res = ''
        idx = 0
        for d1,d2 in zip(num1[::-1], num2[::-1]):
            tmp = int(d1) + int(d2) + carry
            res = str(tmp % 10) + res
            carry = int(tmp/10)
            idx += 1
        return res if (len(res)>1 and res[0]!='0') else res[1:]