class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        numbers = [1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(numbers)):
            if num < numbers[i]:
                continue
            while num >= numbers[i]:
                num -= numbers[i]
                res += strings[i]

        return res
	