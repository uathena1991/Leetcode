class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_list = []
        carry = 1
        while digits:
            d = digits.pop()
            if carry == 1:
                d+=1
            if d == 10:
                carry = 1
                new_list.append(0)
            else:
                carry = 0
                new_list.append(d)
        if new_list[-1] == 0:
            new_list.append(1)
        new_list.reverse()
        return new_list

            