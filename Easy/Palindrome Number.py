class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x!=0 and x%10 == 0):
            return False
        reverse = 0
        while x>reverse:
            reverse = reverse*10 + x%10
            x /= 10
        if x == reverse or x == reverse/10:
            return True
        else:
            return False


a = Solution()
print a.isPalindrome(12321)