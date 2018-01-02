class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1] ## f(0) == 1
        if n <= 2:
            return n
        for k in range(1,n+1):
            tmp = 0
            for j in range(k):
                tmp+=res[j]*res[k-1-j]
            res.append(tmp)

        return res


a = Solution()
t = a.numTrees(6)
print t