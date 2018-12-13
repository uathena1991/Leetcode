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


###### dict method ###
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a = '0'*(max(len_a, len_b) - min(len_a, len_b)) + a
        else:
            b = '0'*(max(len_a, len_b) - min(len_a, len_b)) + b
        a = '0' + a
        b = '0' + b
        carry = '0'
        res = ''
        idx = len(a)-1
        cond_dict = {('0','0', '0'): ('0', '0'), ('0', '1', '0'): ('1','0'), ('1', '0', '0') :('1', '0'), ('1', '1', '0'): ('0', '1'),
                     ('0','0', '1'): ('1', '0'), ('0', '1', '1'): ('0', '1'), ('1', '0', '1') :('0', '1'), ('1', '1', '1'): ('1', '1')}
        while idx >= 0:
            tmp, carry = cond_dict[(a[idx], b[idx], carry)]
            res = tmp + res
            idx -= 1
        return res if res[0] != '0' else res[1:]

