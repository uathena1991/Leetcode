class Solution(object):
    def reverse(self, x):
        """
            :type x: int
            :rtype: int
            """
        abs_x = abs(x)
        if x == 0:
            return 0
        str_x = str(abs_x)
        str_x = str_x [::-1]
        if int(str_x) > 2147483647:
            return 0
        else:
            return int(str_x)*(x/abs_x)
