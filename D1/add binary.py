""" Notes:
    A little tricky here... just know a few built-in function: int(a,2), bin(a)[2,:]
    If time permitted, try the real transformation...http://lifexplorer.me/leetcode-add-binary/
    """

class Solution(object):
    def addBinary(self, a, b):
        """
            :type a: str
            :type b: str
            :rtype: str
            """
        inta = int(a,2)
        intb = int(b,2)
        intsum = inta + intb
        return bin(intsum)[2:]
