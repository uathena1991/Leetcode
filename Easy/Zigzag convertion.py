class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []
        if s =="" or numRows == 1:
            return s
        for i in range(numRows):
            if i == 0:
                [res.append(t) for t in s[::(2*numRows-2)]]
            elif i == numRows-1:
                [res.append(t) for t in s[numRows-1::(2*numRows-2)]]
            else:
                idx = 0
                idx1 = i
                idx2 = 2*numRows-2-i
                while idx1 <=len(s)-1 or idx2 <=len(s)-1:
	                if idx1 <=len(s)-1:
	                    res.append(s[idx1])
	                if idx2<=len(s)-1:
		                res.append(s[idx2])
	                idx+=1
	                idx1 = i+(2*numRows-2)*idx
	                idx2 = 2*numRows-2-i+(2*numRows-2)*idx
	return ''.join(res)

a = Solution()
s = "0123456789"
s1 = a.convert(s,4)
print s1