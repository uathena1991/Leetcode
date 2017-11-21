class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c**.5)+1):
            if int((c - a**2)**.5)**2 == (c - a**2):
                    return True
        return False
