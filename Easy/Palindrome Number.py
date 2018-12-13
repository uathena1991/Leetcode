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

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= x < 10:
            return True
        if x < 0 or x % 10 == 0:
            return False
        new_num = 0
        curr = x
        while curr > 0:
            new_num =  new_num*10 + curr%10
            curr //= 10
            if new_num == curr or new_num == curr // 10:
                return True
            if new_num > curr*10:
                break
        return False


a = Solution()
print(a.isPalindrome(12321))


