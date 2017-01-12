"""
Consider empty list or list where there's no letters/digits (or only one letter)
test case:
',.'
'3a'
'.a'
"A man, a plan, a canal: Panama"
"race a car"
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        l = 0
        r = len(s)-1
        while l<r:
            a = s[l]
            b = s[r]
            while not s[l].isalpha() and not s[l].isdigit() and l<len(s)-1:
                l += 1
            while not s[r].isalpha() and not s[r].isdigit() and r>0:
                r -= 1
            if 0<=l<r<=len(s)-1 and s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True

a = Solution()
print a.isPalindrome(",.")