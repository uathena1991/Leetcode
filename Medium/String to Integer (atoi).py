class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        signs = "+-"
        digits = "0123456789"
        i = 0
        while i <len(str):
            if str[i] == " ":
                i += 1
            else:
                break
        if i >= len(str) or (str[i] not in signs and str[i] not in digits):
            return 0
        cand = ''
        if str[i] in signs:
            cand += str[i]
            i += 1
        while i < len(str) and str[i] in digits :
            cand += str[i]
            i += 1
        if cand == '+' or cand == '-' or cand == '':
            return 0
        if -2**31 <= int(cand) <= 2**31 - 1:
            return int(cand)
        elif int(cand) > 2**31 - 1:
            return 2**31 - 1
        else:
            return -2**31
